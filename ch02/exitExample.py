import sys
 
while True:
    print('終了するにはexitと入力してください。')
    response = input()
    if response == 'exit':
        sys.exit()#need import sys
        #exit()との違いは？
        #終了ステータスの表示
    print(response + 'と入力されました。')
