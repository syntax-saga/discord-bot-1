import requests

channel_id = "1107962541407223868"
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
authorization = "MTEwNzk2MTg3MjQxNTcyNzcyNw.GsB4iY.a_O3UE9Y3JLID_w0cvbqeY0FSOlgEx1FGmej3A"

message = input("Message: ")

payload = {
    "content": message
}

header = {
    "authorization": authorization
}

r = requests.post(url=url, data=payload, headers=header)