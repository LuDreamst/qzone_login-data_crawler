# qzone_login-data_crawler
## 程序用于在实现qq空间的数据爬取  
## 前期准备  
1.配备有selenium模块的python3环境  
2.将chromedriver.exe分别置于python.exe和chrome.exe同目录，chromedriver的[下载连接](https://registry.npmmirror.com/binary.html?path=chromedriver/104.0.5112.79/)
### 注：chrome和chromedriver的版本号应当一致
3.添加Path变量  
（不论是否按照以上步骤设置，只要确保selenium能调用chrome即可）
## 正式开始  
1.终端指令启动chrome：  
`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Workspace\Code\selenium\ChromeProfile"`  
--user-data-dir=后的路径自行选择，自行创建  
2.手动登录qq空间，并点击进入“个人主页”  
（解释：selenium直接调用chrome，无法保留cookie等数据，每次运行需要输入账号密码，可能还需要滑块验证，短信验证。如此一来，前置任务过于繁琐，且效率太低，故采用另一种方案：连接已打开的浏览器）  
3.运行程序即自动获取qq说说发布日期、文本、浏览量、赞数、点赞的人  
4.浏览器界面鼠标下滑刷新并重新运行可爬取更多内容
