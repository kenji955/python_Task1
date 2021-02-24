import csv
import pandas as pd

# 検索ソース
# source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]
path = ('source.csv')
df = pd.read_csv(path)
nameList = list(df["name"])

   # 検索ツール

def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    # ここに検索ロジックを書く
    if word in nameList:
        print("{0}が見つかりました".format(word))
    else:
        print("{0}が見つかりませんでした。リストに追加します".format(word))
        # 検索した対象をリストに追加
        nameList.append(word)
        print('追加後の人数は{0}人です。'.format(str(len(nameList))))
        # 更新したリストで作成したデータフォーマットで対象ファイルを更新する
        df_new = pd.DataFrame({'name':nameList})
        print(df_new)
        df_new.to_csv(path)
        

if __name__ == "__main__":
    search()
