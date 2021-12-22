## Git 특강 2일차

### 원격 저장소 연결 

```bash
git remote add origin https://github.com/jibook/TIL.git
```



### 원격 저장소 연결 여부 확인

```bash
git remote -v

origin  https://github.com/jibook/TIL.git (fetch)
origin  https://github.com/jibook/TIL.git (push)
```



### 원격 저장소에 보내기

```bash
git push origin master
git push -u origin master #다음부터는 깃푸시만 하면된다
```



### 버전 로그 보여줌(커밋 로그 보여줌)

```bash
git log
git log -p #수정한 항목을 상세하게 보여줌
git log --one line #한줄로 간단하게 해준당
```
