import requests
import simplejson as json

# url = 'http://coalio.metacogni.tv/api/tagged_post/?format=json&username=schart%40gmail.com&api_key=b6c56543a805dca901829d834554e987ab15bdce'
url = 'http://127.0.0.1:8000/api/tagged_post/?format=json&username=faris%40theluckybead.com&api_key=28186263da3e69ba961e38c3d9c19761b698aedf'
headers = {'content-type': 'application/json'}

r = requests.get(url)
print r.json()

payload = {
        "resource_url":"424395433553563648",
        "content": "Yes, <a\
            href=\"/Gary_Burghoff\" class=\"twitter-atreply pretty-link\"\
            dir=\"ltr\"><s>@</s>s><b>Gary_Burghoff</b>b></a>a> is\
            drunk-tweeting his memories of the 1976 <a\
            href=\"/search?q=%23BattleoftheNetworkStars&amp;src=hash\"\
            data-query-source=\"hashtag_click\" class=\"twitter-hashtag\
            pretty-link js-nav\"\
            dir=\"ltr\"><s>#</s>s><b>BattleoftheNetworkStars</b>b></a>a>. This\
            needs to be David O Russell's next movie.",
            "ref_url":"twitter.com"
        }
r = requests.post(url, data=json.dumps(payload), headers=headers)
print r
