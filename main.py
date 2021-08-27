import datetime
from typing import List
now = datetime.datetime.now()
while True:
    log: str = input("logを記載してください：")
    log = now.strftime(r"%m月%d日-%H:%M　") + log + "\n"
    x: str = input("「"+log+"」で登録しますか？[y/N]:")
    if x == "y" or x == "ｙ":
        break
    elif x == "N" or x == "Ｎ":
        continue
    elif x == "q" or x == "ｑ":
        quit()
    else:
        print("正しく入力してください。抜けたい場合はqを入力してください。")
with open("log.txt",mode="r", encoding="utf-8") as f:
    l: List[str] = f.readlines()
with open("log.txt",mode="a",encoding="utf-8") as f:
    f.write(log)
print("最近の記録")
if len(l) == 0:
    print("no content")
elif len(l) <= 5:
    for i in l:
        print(i[:-2])
else:
    for i in l[-5:]:
        print(i[:-2])