import requests
   import os

   # 抓取目标 URL
   url = "https://api.wcc.best/sub?target=clash&url=http://8.149.134.37:12585/vmess/sub&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini"
   response = requests.get(url)
   content = response.text

   # 保存到文件
   with open("sub.txt", "w") as f:
       f.write(content)

   print("文件已更新！")
