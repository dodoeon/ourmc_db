# ourmc_db
[우리들의 마인크래프트 공간](https://cafe.naver.com/minecraftgame) 의 [악성이용자 DB](https://userdb.ourmc.space/)
에서 악성이용자 데이터를 받아와\
같은 폴더에 위치한 `banned-players.json` 파일에 추가하는 코드 입니다.

## 의존성 
### `사용된 패키지`
<kbd><samp>requests | 2.26.0</samp></kbd>
<kbd><samp>datetime | 4.3</samp></kbd>
이외 모두 기본 탑재된걸로 알고 있습니다.
( json , os )\
`개발시 Python 3.9.9 사용.`

## 사용법
### `ourmc_db.py` 파일을
`banned-players.json` 파일과 같은 폴더에 위치시킨 뒤\
( 일반적으로 버킷과 같은 폴더 )\
실행시킵니다.\
API에서 정상적인 데이터를 받아올시 바로 추가한 뒤 저장하게 됩니다.

## 실행 파일에 대하여...
### `ourmc_db.exe`
Pyinstaller 으로 실행파일화 해두었으나\
일부 시스템에서 바이러스로 오진 되는 경우가 있습니다.\
민감하신 분들은 소스코드를 직접 다운받으셔서 실행하시길 바라겠습니다.\
[exe 파일 다운로드](https://drive.google.com/file/d/18RwskiYGjO1Ub2pUR8E12JPlDzdVQTiL/view?usp=sharing)

## 책임
이 코드를 사용함에 있어 모든 책임은 사용자에게 있습니다.\
우마공 DB의 내용을 사용함에 있어 모든 책임은 사용자에게 있습니다.
