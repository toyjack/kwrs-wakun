#!/usr/bin/python
# -*- coding: utf-8 -*-
dic={"万":"ま","乃":"の","宇":"う","奴":"ぬ","知":"ち","三":"み","比":"ひ","木":"き","乎":"や","波":"は","於":"お","世":"せ","無":"む","布":"ふ","豆":"つ","爾":"に","岐":"き","伊":"い","為":"ゐ","保":"ほ","之":"し","阿":"あ","米":"め","仁":"に","奈":"な","須":"す","衣":"え","止":"と","曽":"そ","勢":"せ","子":"こ","恵":"ゑ","古":"こ","夜":"や","利":"り","以":"い","由":"ゆ","紀":"き","太":"た","呂":"ろ","毛":"も","左":"さ","加":"か","美":"み","八":"は","都":"つ","久":"く","女":"め","留":"る","良":"ら","礼":"れ","和":"わ","安":"あ","禰":"ね","也":"や","不":"ふ","末":"ま","介":"け","天":"て","牟":"む","千":"ち","多":"た","佐":"さ","倍":"へ","流":"る","路":"ろ","井":"ゑ","与":"よ","閉":"へ"}
results=[]
with open('./wakun.txt', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    results.append(line.translate(str.maketrans(dic)))

with open('./out.txt', encoding='utf-8', mode='w') as f:
    f.write(''.join(results))
