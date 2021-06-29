# AutoGit
自動化Git流程簡單版

## 簡介
1. 雖然Git對於開發者來說使用非常簡單，但是對於需要輕度使用Git的同步功能的普通使用者，Git的命令要去記住以及使用時比較困難的
2. 因此AutoGit被實作出來，以解決這個問題
3. 一共有兩個版本，兩個版本都是通過直接點兩下batch file就可以直接進行`Download(git pull)`和`Upload(git push)`的動作
4. 當然因為Git的多樣性，很難用自動化的標準流程一言以蔽之，因此AutoGit本身是為了針對下面的這個使用場景做了特別的改進
```
# The basic Batch version
基礎的batch版本就是在只有一個遠端Gitlab instance以及本地端只會做git pull和push每天的每日報告

# The advanced Python version
進階的Python版本包括多部電腦和Gitlab端的Web IDE交錯使用時，不會因為需要在不通電腦同步，而造成無法同步的狀況
```

## 功能

### 1. The basic Batch version
1. 只包含兩個文件，每個文件只是寫入了平常需要打的Git指令
2. 兩個文件都沒有包含如何解決文件衝突的狀況

### 2. The advanced Python version
1. 用Python實作，並且用[pyinstaller](https://pypi.org/project/pyinstaller/)打包成`.exe`
2. 再通過兩個batch file包起來
3. 因為考慮到在不同地方下載Gitlab的時候會需要不同的domain，因此可以在幾個domain之間找出可以連線的那個（hard code在腳本裡）
4. 可以做到一定程度的conflict solving，解決的方法就是針對衝突得到文件，直接保留兩份，然後用command line的方式讓用戶選擇需要保留哪一個
5. 針對幾個常見的conflict cases，已經整理在[不同狀況記錄.md](不同狀況的記錄.md)

## 如何安裝
1. 直接在Win10 x64 2004的平台上面可以直接運行batch file
2. Python腳本也可以直接通過Python運行
3. 如果需要編譯本Python腳本，需要安裝`pyinstaller`

## 注意
1. Git流程本身還是複雜且危險的，因此
### *!!! 非常不建議在重要的源碼上直接使用 !!!*