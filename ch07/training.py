import re

phone_number_regex=re.compile(r"\d{4}-\d{3}-\d{3}")
mo = phone_number_regex.search("私の電話番号は0120-828-828である．")
print("電話番号が見つかりました："+mo.group())

"""
1.re.compile()で正規表現モジュール
2.re.compile()でregexオブジェクト生成
3.regexオブジェクトのsearch()で検索する文字列からmatchオブジェクトを返す
4.matchオブジェクトをgroup()で返す

"""
bat_regex=re.compile(r"Bat(wo)?man")
mo2=bat_regex.search("myname is Batwoman")
print(mo2.group())

"""
woがあってもなくてもいい場合(wo)?である．
"""

batt_regex=re.compile(r'Bat(wo)*man')
mo1=batt_regex.search("myname is Batwowowowowowowowowowoman")
print(mo1.group())

"""
woが任意の数あってもいいのであれば(wo)*を使う．
"""
phone_number_regex2 = re.compile(r"\d{3}-\d{3}-\d{4}")
cha = "cell: 411-555-9999 work: 212-444-5433"
th = phone_number_regex2.search(cha)
print(th.group())
th2 = phone_number_regex2.findall(cha)
print(th2)

"""
search()が最初に見つけたものを返すのに対してfindall()はすべて返す．
しかし，group()ではなく普通にlistを返すことに注意する．
"""
phone_number_regex3 = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
cha = "cell: 411-555-9999 work: 212-444-5433"
th = phone_number_regex3.search(cha)
print(th.group(0))
th2 = phone_number_regex3.findall(cha)
print(th2)

at_regex=re.compile(r".at")
b=at_regex.findall("the cat in the hat sat on the flat mat")
print(b)

"""
ワイルドカード文字
正規表現では.は任意の文字を示す．ただし，.に対して1文字のみ
"""

name_regex = re.compile(r"Agent \w+")
names = name_regex.sub("CENSORED","Agent Alice gave the secret documents to Agent Bob.")
print(names)
"""
sub()で入れ替え
"""

"""
出力結果
電話番号が見つかりました：0120-828-828
Batwoman
Batwowowowowowowowowowoman
411-555-9999
['411-555-9999', '212-444-5433']
411-555-9999
[('411', '555', '9999'), ('212', '444', '5433')]
['cat', 'hat', 'sat', 'lat', 'mat']
CENSORED gave the secret documents to CENSORED.
"""
