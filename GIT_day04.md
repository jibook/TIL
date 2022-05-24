## git add 취소하기(파일 상태를 Unstage로 변경)

```bash
// 모든 파일이 Staged 상태로 바뀐다.
$ git add *
// 파일들의 상태를 확인한다.
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)
  renamed:    README.md -> README
  modified:   CONTRIBUTING.md
```



```bash
// CONTRIBUTING.md 파일을 Unstage로 변경한다.
$ git reset HEAD CONTRIBUTING.md
Unstaged changes after reset:
M	CONTRIBUTING.md
```



```bash
// 파일들의 상태를 확인한다.
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)
  renamed:    README.md -> README
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)
  modified:   CONTRIBUTING.md
```





## git commit 취소하기

```bash
// [방법 1] commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
$ git reset --soft HEAD^
// [방법 2] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존
$ git reset --mixed HEAD^ // 기본 옵션
$ git reset HEAD^ // 위와 동일
$ git reset HEAD~2 // 마지막 2개의 commit을 취소
// [방법 3] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
$ git reset --hard HEAD^
```



## git push 취소하기

```bash
// 가장 최근의 commit을 취소 (기본 옵션: --mixed)
$ git reset HEAD^
```

```bash
// Reflog(브랜치와 HEAD가 지난 몇 달 동안에 가리켰었던 커밋) 목록 확인
$ git reflog 또는 $ git log -g
// 원하는 시점으로 워킹 디렉터리를 되돌린다.
$ git reset HEAD@{number} 또는 $ git reset [commit id]
```



## git push 강제로 푸쉬하기 

```bash
$ git push origin [branch name] -f

$ git push origin +[branch name]

// ex) master branch를 원격 저장소(origin)에 강제로 push
$ git push origin +master
```



