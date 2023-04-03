import json

import requests
def tik_tok(urll):
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":urll}

	headers = {
		"X-RapidAPI-Key": "fcfecc6db4mshf2eda4d0a842c22p1c0432jsn0ff1c84c6f35",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	natija=response.text
	rest=json.loads(natija)
	# print(rest)
	return ({"Video":rest['video'][0]})
# tik_tok('https://vm.tiktok.com/ZMFnohMVX/')