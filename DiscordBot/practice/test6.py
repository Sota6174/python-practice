import requests

from constants import GOOLAB_APP_ID, GOOLAB_URL, GOOGLE_CGI_URL

data = {
    'app_id': GOOLAB_APP_ID,
    'request_id': 'hiragana0001',
    'sentence': '熟語・漢字が混ざった文章',
    'output_type': 'hiragana'
}
# response = requests.post(GOOLAB_URL, data=data).json()
# print(response)
# {'converted': 'じゅくご・かんじが まざった ぶんしょう', 'output_type': 'hiragana', 'request_id': 'hiragana0001'}
data['sentence'] = '胡坐'
response = requests.post(GOOLAB_URL, data=data).json()
print(response['converted'])
# あぐら

params = {
    'langpair': 'ja-Hira|ja',
    'text': 'かんじがまざったぶんしょう'
}
response = requests.get(GOOGLE_CGI_URL, params=params)
# print(response.url)
responce = response.json()
print(responce)
# [
#   ['かんじが', ['感じが', '漢字が', '幹事が', 'カンジが', '貫地が']],
#   ['まざった', ['混ざった', 'まざった', '交ざった', '雑ざった', '真颯田']],
#   ['ぶんしょう', ['文章', '分掌', '文相', '文翔', '文証']]
# ]
