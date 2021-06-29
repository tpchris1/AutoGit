# AutoGit
A simple script for git automation for report-like repo

[Chinese version](README-zh-TW.md) 


## Introduction
1. While Git commands may be pretty basic for software developers, it could be quite a challenge for non-insiders
2. AutoGit is developed to help other people who is not familiar with Git but need to use it to some degree
3. It is divided into two versions, both versions two batch files:`Download(git pull)`and`Upload(git push)`
4. The scenerios which AutoGit is dedicated to is as following:

```
# The basic Batch version
One intranet Gitlab and one user simply pushing daily reports to the Gitlab

# The advanced Python version
One intranet Gitlab instance which can be accessed through NAT tunneling from internet
Two intranet computers in different location and a outranet one
Sometimes editing a bit through Web IDE of Gitlab
Need to keep the daily reports completely syncronous among all places   
```


## Features
### 1. The basic Batch version
1. This version simply contains two batch files 
2. They simply integrate the `git pull` and `git push` process respectively
3. Neither of them contains any conflict-solving process

### 2. The advanced Python version
1. Built in Python and "compiled" through [pyinstaller](https://pypi.org/project/pyinstaller/)
2. Wrapped in two batch files for convenience
3. The Gitlab instance would have two domain according to intranet or internet. Hence, this version can automatically change the remote url for repo based on the accessibility of current network
4. Solve conflict by keeping both conflicted files and guide users to choose which one to keep through commandline
5. The conflict solving cases is described here: [Case_analysis.md(in Chinese)](不同狀況的記錄.md)
  
## Installation 
1. Both versions are wrapped in batch files which are tested under Win10 x64 2004
2. But python version can be run by your default python installation
3. If you want to compile the code, `pyinstaller` is required
    
## Notice
1. Git process is complex and somehow dangerous, hence
### *!!! Very NOT recommended used on important source code !!!*
 
  