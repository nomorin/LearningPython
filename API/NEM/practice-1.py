import requests
import json
import pprint

# エンドポイント.
url = "http://api-01.us-east-1.096x.symboldev.network:3000/"
get_blocks = "blocks"

# リクエスト.
response = requests.get(url + get_blocks)

# 取得したjsonをlistに格納.
lists = json.loads(response.text)

# jsonが見やすいように整形して表示する.
# pprint.pprint(lists, width=40)

# jsonの要素を表示する.
print(lists['data'][0]['block']['beneficiaryAddress'])

