import requests
import json
def instagramDown(urll):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": urll}

    headers = {
        "X-RapidAPI-Key": "fcfecc6db4mshf2eda4d0a842c22p1c0432jsn0ff1c84c6f35",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest=json.loads(response.text)
    if 'error' in rest:
        return 'Linkda Xatolik bor'
    else:
        dic = {}
        if rest['Type'] == 'Post-Video':
            dic['type'] = 'video'
            dic['media'] = rest['media']
            return dic
