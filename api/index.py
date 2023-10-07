from googleapiclient.discovery import build
from pprint import pprint
CHANNEL_ID ="UCLj_i7yL-8FZrdQA6eE4iqQ"
def get_youtube():
    DEVELOPER_KEY ='AIzaSyB-i2LYf-EuLskE_iejRoN96Kq7B4V-Y1E'
    YOUTUBE_API_SERVICE_NAME='youtube'
    YOUTUBE_API_VERSION='v3'
    youtube=build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    return youtube
#def search_videos(channel_id):
youtube = get_youtube()
request = youtube.search().list(
    part="snippet",
    type ="video",
    channelId="UCLj_i7yL-8FZrdQA6eE4iqQ",
    maxResults= 500)
response = request.execute()
video_ids=[]
for item in response['items'][:1]:
    title = item['snippet']['title']
    videoId = "VMdCUCBCYDQ"
    video_ids.append(videoId)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId="VMdCUCBCYDQ"
    )
    response=request.execute()
    pprint(response)