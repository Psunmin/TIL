# CLI 실습
## 경로
### 루트 및 홈 디렉터리
1. 루트 '/'
    - 최상의 폴더
    - 윈도우에서는 c드라이브
2. 홈 디렉토리 '~'
    - 현재 로그인된 사용자의 홈 폴더
    
### 절대경로와 상대 경로
1. 절대 경로: 루트디렉토리로부터 목적 지점까지의 경로
    - ex) c:/Users/SSAFY/Desktop
2. 상대 경로: 현재 작업하고 있는 디렉터리 기준으로 목적 지점까지의 경로
    - ex) ./PythonStudy
    - ./: 현재 작업하고 있는 폴더
    - ../: 현재 폴더의 부모 폴더

## 터미널 명령어
1. touch
    - 파일을 생성하는 명령어
    - 숨김 파일을 만들때는 파일명 앞에 '.'을 붙인다
    - 띄어쓰기를 통해 여러 파일을 동시 생성
    - ex) touch text1.txt text2.txt .hidden.md
2. mkdir
    - 새 폴더를 생성
    - 파일 및 폴더에 공백을 넣고 싶으면 홑따옴표로 묶음
    - ex) mkdir new_folder1 'new forder2'
3. ls
    - 현재 디렉터리의 파일 및 폴더 목록을 보여줌
    - -a 옵션: 숨김 파일까지 모두 표시
    - -l 옵션: 용량, 수정 날짜 등 파일 정보 표시
    - ex) ls, ls -a, (ls -a -l or ls -al)
4. mv
    - 파일 및 폴더를 다른 폴터로 이동
    - 파일 및 폴더 이름 변경
    - 이동 ex) mv text1.txt new_folder1  (text1파일을 new_folder로 이동)
    - 이름 변경 ex) mv text2.txt alter_text2.txt
5. cd
    - 현재 작업 중인 디렉터리를 변경
    - cd 또는 cd ~: 홈 디렉터리로 이동
    - cd .. : 부모 디렉터리로 이동
    - cd - : 이동 전의 디렉터리로 이동
    - 상대 경로 ex) cd ./new_folder1
    -  절대 경로 ex) cd C:/Users
6. rm
    - 폴더 및 파일 지움
    - 휴지통 이동이 아닌 완전 삭제
    - *를 사용하면 전체 파일 삭제됨
    - *.txt는 txt 확장자 파일 모두 삭제
    - -r 옵션 폴더 지울 때 사용
    - ex) rm *.txt
    - ex) rm -r new_folder1

7. start
    - 폴더 및 파일 여는 명령어
    - ex) start 'new folder2'

### 유용한 단축키
1. 위, 아래 방향키: 과거에 작성한 명령어 조회
2. tab: 파일 및 폴더 이름 자동 완성
3. ctrl + a: 커서가 맨 앞으로 이동
4. ctrl + e: 커서가 맨 뒤로 이동
5. ctrl + w: 커서가 앞 단어를 삭제
6. ctrl + l: 터미널 화면 청소
7. ctrl + insert: 복사
8. shift + insert: 붙여넣기  