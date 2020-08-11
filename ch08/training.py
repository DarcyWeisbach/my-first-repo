import os
import shelve
import pprint
"""
directory_now = os.getcwd()
print(directory_now)
os.chdir("C:\\users")
directory_now = os.getcwd()
print(directory_now)
"""
#os.makedirs(".\\documents\\taikutu")

a=os.path.abspath("..")#相対パスを絶対パスに変換
print(a)
#os.path.isabs()は絶対パスならtrue，相対パスならfalse
b=os.path.dirname(".\\documents")
print(b)

path=os.path.abspath("./documents")#相対パスを絶対パスに
c = os.path.basename(path)#絶対パスの最下層
d = os.path.dirname(path)#絶対パスの最下層以外
print(c)
print(d)
e = os.path.split(path)
print(e)
print(os.path.getsize(path))
print(os.listdir(".."))
hello_file = open('.\\documents\\char.txt')
hello_content = hello_file.read()
print(hello_content)
bacon_file=open('.\\documents\\gh.txt',"w")
bacon_file.write("hello,world!")
shelf_file = shelve.open("mydata")
cats = ["jk","jd","jc"]
shelf_file["cats"]=cats
shelf_file.close()
shelf_file2=shelve.open("mydata")
type(shelf_file2)
print(shelf_file2["cats"])
shelf_file2.close()

dogs = [{"name":"dada","desc":"chubby"},{"name":"pokka","desc":"fluffy"}]
pprint.pformat(dogs)
file_obj=open("mydogs.py","w")
file_obj.write("dogs="+pprint.pformat(dogs)+"\n")
file_obj.close()
you = {"name": "dada", "desc": "chubby"}
t=you.keys()
print(type(t))
