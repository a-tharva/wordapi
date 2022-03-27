import requests

URL = 'http://127.0.0.1:5000/'

ans = requests.get(URL + "define/torch")
print(ans.json())