all_guests = {'アリス': {'リンゴ': 5, 'プレッツェル': 12},
              'ボブ': {'ハムサンド': 3, 'リンゴ': 2},
              'キャロル': {'コップ': 3, 'アップルパイ': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():  # ❶
        #itemsでキーとバリューを得る．バリューを得るだけならvalueを使う
        num_brought = num_brought + v.get(item, 0)  # ❷
        #getはキーに存在していればバリューを返して，キーがなければ第2引数を返す．
    return num_brought

print('持ち物の数:')
print(' - リンゴ ' + str(total_brought(all_guests, 'リンゴ')))
print(' - コップ ' + str(total_brought(all_guests, 'コップ')))
print(' - ケーキ ' + str(total_brought(all_guests, 'ケーキ')))
print(' - ハムサンド ' + str(total_brought(all_guests, 'ハムサンド')))
print(' - アップルパイ ' + str(total_brought(all_guests, 'アップルパイ')))
