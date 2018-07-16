import requests

headers = {'X-Auth-Token': '<enter_your_token>'}
dudeId = '<enter_his_id>'
likeRes = requests.get('https://api.gotinder.com/like/' + dudeId, headers=headers)
print(likeRes.json())