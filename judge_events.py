import json
from pathlib import Path

# 検索したいラベル
search_string = "Yellow card"
results = []


#テスト用のファイルパス取得の関数
def get():
    # 対象ディレクトリ
    target_directory = Path("/Users/satourintarou/programming/python/soccerNet_download/path/to/Users/satourintarou/research")

    # ファイルパスを文字列形式で取得
    file_paths = [str(file) for file in target_directory.rglob("*.json") if file.is_file()]

    return file_paths


# 検索したいラベルの画像ファイル名をリストにする関数
def judge_event():
    
    file_paths = get()

    for path in file_paths:
      # JSONファイルのパスを指定して読み込む
      with open(path, 'r', encoding='utf-8') as file:
          data = json.load(file)

      # "actions"の中のkeyとvalueをループで回していく
      for key, value in data.get("actions", {}).items():
          if value.get("imageMetadata", {}).get("label") == search_string:
              
              # 削除したい部分
              remove_part = "/Users/satourintarou/programming/python/soccerNet_download/path/to/Users/satourintarou/research"

              # 置換操作
              modified_path = path.replace(remove_part, "")
              file_name = modified_path + key
              results.append(file_name)
    
    print(results)
    print(len(results))

              

judge_event()
    
