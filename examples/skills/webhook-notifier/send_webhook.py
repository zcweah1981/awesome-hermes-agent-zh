import requests
import os
import sys

def send_to_webhook(content, platform="feishu"):
    webhook_url = os.environ.get("WEBHOOK_URL")
    if not webhook_url:
        print("[Error] 环境变量 WEBHOOK_URL 未设置")
        sys.exit(1)

    payload = {
        "msg_type": "text",
        "content": {
            "text": content
        }
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print(f"[Success] 消息已成功发送到 {platform}")
        else:
            print(f"[Error] 发送失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"[Error] 请求异常: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_webhook.py <content>")
        sys.exit(1)
    
    msg_content = sys.argv[1]
    send_to_webhook(msg_content)