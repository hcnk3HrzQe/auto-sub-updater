import requests  # 第1行必须顶格（无缩进）
import os        # 第2行同样顶格

def main():
    url = "https://api.wcc.best/sub?target=clash&url=http://8.149.134.37:12585/vmess/sub&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open("sub.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("✅ 文件更新成功")
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
