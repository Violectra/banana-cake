import requests
import json
from langdetect import detect

headers = {'X-Auth-Token': '<enter_your_token>'}
response = requests.get('https://api.gotinder.com/v2/recs/core?locale=ru', headers=headers)

json_data = json.loads(response.content)
results = json_data['data']['results']
counter = 0
for i in range(len(results)):
    dude = results[i]['user']
    bio = dude['bio']
    if (bio != '' and len(bio) > 90 and len(dude['photos']) > 1):
        lang = detect(bio)
        if (lang == 'ru'):
            print('name=' + dude['name'] + ', lang=' + lang + ', bio=' + bio)
            # like him
            likeRes = requests.get('https://api.gotinder.com/like/' + dude['_id'], headers=headers)
            print(likeRes.json())
            counter = counter + 1
print("Liked: " + counter)
