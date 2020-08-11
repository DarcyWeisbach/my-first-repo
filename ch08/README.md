8章のまとめです．

必要な知識はtraining.pyに保存してあります．

cwdとはcurrent working directoryのこと
簡単にカレントディレクトリともいう．]

復習として
./　は現在のディレクトリ
../　は親ディレクトリ

os.path.abspath(path)　相対パスを絶対パスを得る．
os.path.relpath()　相対パス

osモジュールはなければエラーが出て終了してしまうため
os.path.exists()
os.path.isfile(path)　pathが存在してそれがファイルであればtrue
os.path.isdir(path)　pathが存在してそれがディレクトリであればtrue

shelveで変数を保存しておくために
.bak .dat .dir　が作成される．

{}.format(number)みたいな入力方法も覚えておく