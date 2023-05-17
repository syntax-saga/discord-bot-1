import requests # pip install requests

channel_id = "YOUR CHANNEL ID" #The channel id should be replaced with your channel id as shown in the video in youtube.
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
authorization = "YOUR AUTHORIZATION" #The authorization token should be replaced with your authorization key, also shown in video.

message = input("Message: ")

payload = {
    "content": message
}

header = {
    "authorization": authorization
}

r = requests.post(url=url, data=payload, headers=header)
