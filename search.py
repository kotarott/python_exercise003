import pandas as pd
import os
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, path):
    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        eel.add_results("CSVファイルは存在しません。")
        return

    # 検索対象取得
    # df = pd.read_csv("source.csv")
    source = list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.add_results("『{}』はあります".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.add_results("『{}』はありません".format(word))
        eel.add_results("『{}』をリストに追加します。".format(word))
        # 追加
        # add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df = pd.DataFrame(source, columns=["name"])
    df.to_csv(path, encoding="utf_8-sig")
    print(source)