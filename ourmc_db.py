import requests
import json
import datetime
import os

# 우마공 api GET
OurMcSpaceApi = 'https://userdb.ourmc.space/api/v1/report/all?limit=1000' #API 주소.
print("API에 데이터 요청중...")
print("상황에 따라 1분까지 걸릴 수 있습니다...")
ApiData = requests.get(OurMcSpaceApi).json()
print("로드 완료..!")

# HTTP 상태 코드 확인
print("데이터 정상 수신여부 확인...")
if ApiData["code"] == 200 :
    print("정상 수신됨.")
elif ApiData["code"] == 500 :
    print(".")
    print("정상 수신되지 않음.")
    print("API 서버 에러")
    print("상태 코드 : %d" %(ApiData["code"]))
    print("이유 : %s" %(ApiData)["reason"]["message"])
    print(".")
    os.system("pause")

# 버킷 폴더 내 banned_player.json 로드.
print(".")
print("버킷 폴더 내 banned-players.json 로드중...")
with open('./banned-players.json', 'r', encoding='UTF-8') as f:
    BukkitBanlist = json.load(f)
print("로드 완료..!")
print(".")

# 밴 적용 날짜 계산을 위한...
Date = datetime.datetime.now()

# 중복 확인용 Boolean 값 선언.
IsExist = False

# List에 추가를 위한 본체..?
if ApiData["code"] == 200 :                                                                 # api 수신 확인.
    print("데이터 동기화를 시작합니다...")
    for i in (range(ApiData["value"]["count"]-1)):                                          # 신고된 유저 개수만큼 반복.
        UUID = ApiData["value"]["list"][i]["user"]["uuid"]                                  # UUID 불러오기.
        DashUUID = UUID[0:8]+'-'+UUID[8:12]+'-'+UUID[12:16]+'-'+UUID[16:20]+'-'+UUID[20:33] # Dash 포함된 UUID로 변환.
        NAME = ApiData["value"]["list"][i]["user"]["userName"]                              # 마인크래프트 ID 불러오기.
        
        for j in range (0,len(BukkitBanlist)):
            if BukkitBanlist[j]["uuid"] == DashUUID:
                IsExist = True # 이미 밴 리스트에 같은 UUID를 가진 유저가 있을시 True로 변경후 반복문 탈출.
                break
            else :
                continue # j번째와 불 일치시 그 다음 UUID 확인.
        

        # 기존 밴 되어있던 리스트에서 현재 밴 하려는 UUID 미 발견시 리스트에 추가 및 알림.
        if IsExist == False :
            BukkitBanlist.append({
            "uuid": f"{DashUUID}",
            "name": f"{NAME}",
            "created": f"{Date.year}-{Date.month}-{Date.day} {Date.hour}:{Date.minute}:{Date.second} +0900",
            "source": "console",
            "expires": "forever",
            "reason": "우마공 악성이용자DB 에서 신고된 사용자입니다."
            })
            print("(%d/%d) 밴 리스트에 추가되었습니다. ID : %s" %(i+1,ApiData["value"]["count"]-1,NAME))


        # 이미 존재 하는경우.    
        elif IsExist == True :
            print("(%d/%d) 이미 밴 되어있습니다. ID : %s" %(i+1,ApiData["value"]["count"]-1,NAME))
        
        IsExist = False # 중복확인용 Boolean 값 초기화.
    
    # BukkitBanlist 에 쓰여진 데이터를 다시 banned_player.json 에 저장.
    with open("./banned-players.json", "w" ,encoding='UTF-8') as f:
        json.dump(BukkitBanlist, f, indent='  ', ensure_ascii=False)
    print(".")
    print("banned-players.json 에 정상 저장되었습니다.")
    print("종료하셔도 됩니다.")
    print("개발자 : me@doeon.net")
    print(".")

os.system('pause')