from urllib.parse import urlparse
import primp
import time
import os

def join_discord_server(invite, token, session_id=None):
    client = primp.Client(impersonate="chrome_131", impersonate_os="windows")

    if invite.startswith('http'):
        parsed_url = urlparse(invite)
        invite_code = parsed_url.path.split('/')[-1]
    else:
        invite_code = invite
    
    base_url = "https://discord.com/api/v9"
    
    headers = {
        "accept": "*/*",
        "accept-language": "th-TH,th;q=0.9,en;q=0.8",
        "authorization": token,
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "th",
        "x-discord-timezone": "Asia/Bangkok",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRoLVRIIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM3NDQ5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    
    get_url = f"{base_url}/invites/{invite_code}?inputValue=https%3A%2F%2Fdiscord.gg%2F{invite_code}&with_counts=true&with_expiration=true&with_permissions=false"
    response = client.get(get_url, headers=headers)
    if response.status_code != 200:
        pass
    
    post_headers = headers.copy()
    post_headers["content-type"] = "application/json"
    post_headers["x-context-properties"] = "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjEzNDY0MzU2NzE2OTAwNTU3OTMiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTM0NjU5MzQzMDgxNzQ3MjUzMiIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0="
    
    post_url = f"{base_url}/invites/{invite_code}"
    body = {"session_id": session_id} if session_id else {}
    response = client.post(post_url, headers=post_headers, json=body)
    if response.status_code in (200, 204):
        return "Joined"
    elif response.status_code == 400 and "captcha" in response.text.lower():
        return "Captcha"
    else:
        return f"Failed: {response.status_code}"

def read_tokens(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    os.system('cls')
    invite = input("Invite: ")
    tokens = read_tokens('tokens.txt')
        
    for token in tokens:
        token_short = token[:25] + "..."  
        result = join_discord_server(invite, token)
        print(f"[{time.strftime('%H:%M:%S')}] [AXON] [{token_short}] -> {result}")

if __name__ == "__main__":
    main()
