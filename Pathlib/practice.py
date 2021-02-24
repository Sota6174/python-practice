import pathlib

# 存在するファイルの確認
path_dir = pathlib.Path('data')
# 存在する場合はTrue, 存在しない場合はFalse
print("'data'ディレクトリ", path_dir.exists())
print(list(path_dir.iterdir()))     # pathオブジェクトの中に存在するfile, dirを取得

path_dir = pathlib.Path('images')
print("\n'images'ディレクトリ", path_dir.exists())

# ディレクトリ作成：mkdir(), exist_ok=True（既にある場合もエラーを出さない）
pathlib.Path('images').mkdir(exist_ok=True)
pathlib.Path('data').mkdir(exist_ok=True)
# 確認
print("\n'images'ディレクトリ: ", pathlib.Path('images').exists())

# ファイル作成：touch(), exist_ok=True（既にある場合もエラーを出さない）
pathlib.Path('data/test.csv').touch(exist_ok=True)
pathlib.Path('images/test.png').touch(exist_ok=True)
# 確認
print("\n'images/test.png'ファイル: ", pathlib.Path('images/test.png').exists())
print(list(pathlib.Path('data').iterdir()))

# 中間ディレクトリ(temp)ごと作成
path_file = pathlib.Path('temp/dir/test1.txt')  # pathオブジェクト作成
path_file.mkdir(parents=True, exist_ok=True)    # 中間ディレクトリ作成
path_file.touch(exist_ok=True)                  # ファイル作成
print("\n'temp/dir/test1.txt'ファイル: ", path_file.exists())
