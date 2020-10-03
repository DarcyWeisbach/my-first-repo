import shutil,os,send2trash
'''
a=os.getcwd()
#print(a)
#os.chdir("c:\\")
shutil.copy(".\\aaa.txt",".\\delicious")
"""
aaa.txtを右のdeliciouフォルダに移動する．
名前はそのままコピーされる．
"""
shutil.copy("eggs.txt",".\\delicious\\eggs2.txt")

os.chdir(".\\")#いらないかもしれない
b=shutil.copytree("bacon","bacon_backup")
#一回しか実行することはできない．
print(b)

#shutil.move()でファイルの移動が可能

for filename in os.listdir():
    if filename.endwith('.rtx'):
        os.unlink(filename)
        print(filename)
        #we should use filename

'''
baconFile=open("bacon.txt","a")
baconFile.write("bacon is not a vegtable.")
baconFile.close()
send2trash.send2trash("bacon.txt")