import shutil,os
a=os.getcwd()
#print(a)
#os.chdir("c:\\")
shutil.copy(".\\aaa.txt",".\\delicious")
"""
aaa.txtを右のdeliciouフォルダに移動する．
名前はそのままコピーされる．
"""
shutil.copy("eggs.txt",".\\delicious\\eggs2.txt")