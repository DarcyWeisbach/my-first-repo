def spam():
    #ローカルスコープからグローバル変数を変更したければgrobalを使う必要がある．
    global eggs   # ❶
    eggs = 'spam' # ❷

eggs = 'global'
spam()
print(eggs)
