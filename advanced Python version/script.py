import subprocess
import os
import sys

class AutoGit():
    """A simple example class"""
    # 命令們
    status = 'git status'
    fetch = 'git fetch'
    new_branch = 'git checkout -b {}'
    delete_branch = 'git branch -d {}'
    merge = 'git merge'
    merge_abort = 'git merge --abort'
    pull = 'git pull'
    diff = 'git diff --name-only --diff-filter=U'

    add = "git add ."
    commit = "git commit -m \"{}\""
    push = "git push"

    # domain_outside = "327gh77283.qicp.vip"
    # domain_in_office = "gitlab.richdevice.com"
    # domains = ["github.com", "gitlab.com"]    
    domains = ["gitlab.richdevice.com", "327gh77283.qicp.vip"]    

    def parseInput(self, param: int):
        if param == 1:
            self.gitPull()
        elif param == 2:
            self.gitPush()
        elif param == 3:
            self.checkUrl()

        return
    
    def checkUrl(self):
        valid = True
        index = 0
        
        while(valid):
            output = ''
            print("檢查連線狀況...")
            os.system("git remote -v")
            try:
                subprocess.check_output(self.fetch, shell=True, stderr=subprocess.STDOUT) # 吧stderr的輸出換到stdout裡面           
            except subprocess.CalledProcessError as e:
                output = e.output.decode() # decode的目的就是為了把回傳的bytes專橫string
                print(output)

            if 'fatal:' in output:
                old_url = output.split('\'')[1]
                old_domain = old_url.split('/')[2]
                # print(old_domain)
                
                if index < len(self.domains):
                    if self.domains[index] != old_domain:
                        new_url = old_url.replace(old_domain, self.domains[index])
                        os.system("git remote set-url origin " + new_url)
                    index+=1
                else:
                    print('\n\n-------------------！！注意！！----------------------')
                    print("目前連接為：")
                    print(old_url)
                    new_url = input("\n所有已知的Gitlab連結都無法連線，請檢查網絡連線或手動輸入新連結：")
                    os.system("git remote set-url origin " + new_url)
            else:
                print('\n\n-----------------！！連線成功！！--------------------')
                break

        # os.system("git remote -v")
        return

    def gitPull(self):
        output = ''

        self.checkUrl()

        try:
            subprocess.check_output(self.pull, shell=True, stderr=subprocess.STDOUT) # 吧stderr的輸出換到stdout裡面           
        except subprocess.CalledProcessError as e:
            output = e.output.decode() # decode的目的就是為了把回傳的bytes專橫string
            print(output)

        # Gitlab有a.txt，且修改為ver2(committed)，local為ver1(modified)，但not commited
        if 'error: Your local changes to the following files would be overwritten by merge' in output:
            os.system(self.add)
            os.system(self.commit.format("Commit to resolve conflict"))
            self.resolvePullConflict()
        
        # Gitlab有a.txt，且修改為ver2(committed)，local為ver1(committed)
        if 'CONFLICT (content)' in output: 
            self.resolvePullConflict()

        
        # Gitlab有a.txt，且修改為ver2，local本來也有但刪掉了，且commited
        if 'CONFLICT (modify/delete)' in output:
            rawlist = subprocess.check_output("git status -z -u", shell=True).decode().split(' ')
            attrlist = []
            filelist = []

            for idx,val in enumerate(rawlist):
                if idx%2 == 0: attrlist.append(val)
                else: filelist.append(val.replace('\x00',''))
            
            print('\n\n-------------------！！注意！！----------------------')
            print("以下文件在本地端已刪除，請決定是否保留：")
            for attr,f in zip(attrlist,filelist):
                if attr == 'DU':
                    os.rename(f,"！衝突local已刪除 - "+f)
                    print("！衝突local已刪除 - "+f)
            print('\n\n選擇完成後，可以直接提交')
            
        print('\n\n-----------------！！下載完成！！--------------------')
        
        return
    
    def resolvePullConflict(self):
        os.system(self.merge) # 嘗試merge 用來取得有conflict的文件列表

        diff_filelist = subprocess.check_output(self.diff, shell=True).decode().split('\n') # 取得conflict文件列表
        os.system(self.merge_abort) # 回退merge

        # print(diff_filelist)
        for i in diff_filelist:
                if i: # 防止空目錄
                    os.rename(i,"！衝突local - "+i) # 重命名本地文件為

        os.system(self.add)
        os.system(self.commit.format("Rename old filename"))
        os.system(self.merge) # 原本的remote文件會直接被pull下來
        
        
        print('\n\n-------------------！！注意！！----------------------')
        print("請手動選擇以下衝突文件：")
        for i in diff_filelist:
            if i: # 防止空目錄
                os.rename(i,"！衝突remote - "+i)
                print("！衝突remote - "+i," | ","！衝突local - "+i)
                selection = input("選擇remote輸入1，選擇local輸入2:\n")
                if selection == 1:
                    os.rename("！衝突remote - "+i,i)
                    os.remove("！衝突local - "+i)
                else:
                    os.rename("！衝突local - "+i,i)
                    os.remove("！衝突remote - "+i)
        
        print('\n\n-----------！！同步已完成，可以開始編輯！！------------')
        return

    def gitPush(self):
        
        self.checkUrl()

        output = ''
        try:
            output = subprocess.check_output(self.merge, shell=True).decode() # 吧stderr的輸出換到stdout裡面           
        except subprocess.CalledProcessError as e:
            output = e.output.decode() # decode的目的就是為了把回傳的bytes專橫string
        
        # print(output)
        
        if "Already up to date" not in output:
            self.resolvePullConflict()
        
        os.system(self.add)
        os.system(self.commit.format("新增每日報告"))
        os.system(self.push)
        
        print('\n\n-------------------！！上傳完成！！----------------------')
        return
    
    # def try1(self):
    #     rawlist = subprocess.check_output("git status -z -u", shell=True).decode().split(' ')
    #     attrlist = []
    #     filelist = []

    #     for idx,val in enumerate(rawlist):
    #         if idx%2 == 0: attrlist.append(val)
    #         else: filelist.append(val.replace('\x00',''))
    #     for attr,f in zip(attrlist,filelist):
    #         if attr == 'DU':
    #             os.rename(f,"！衝突local已刪除 - "+f)
        
    #     print(attrlist,filelist)
    #     return


autogit = AutoGit()
autogit.parseInput(int(sys.argv[1]))
