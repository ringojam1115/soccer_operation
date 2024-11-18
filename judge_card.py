import json

# JSONファイルのパスを指定して読み込む
with open('/Users/satourintarou/programming/python/soccerNet_download/path/to/Users/satourintarou/research/england_epl/2014-2015/2015-04-11 - 19-30 Burnley 0 - 1 Arsenal/Labels-v3.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# 検索したい文字列
search_string = "Foul"
results = []

# "actions"の中のkeyとvalueをループで回していく
for key, value in data.get("actions", {}).items():
    if value.get("imageMetadata", {}).get("label") == search_string:
        results.append(key)

print(results)