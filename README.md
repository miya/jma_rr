# rainfall
気象庁の一日の降水データをスクレイピングしてgifを生成するやつ。  
データ元: https://www.jma.go.jp/jp/radnowc/  
## Usage
```git clone https://github.com/0x0u/rainfall```   
```cd rainfall```  
```pip3 install -r requiremenets.txt```  
```python3 rainfall.py```  
## Description
プログラムを実行すると前日の一日分の降水データ（5分毎に画像がアップロードされるので、12x24=288枚の画像）をダウンロードし、画像処理ライブラリpillowを使ってgifを作成します。  
qiita: https://qiita.com/0x0/items/f14bfa90d102af8f0e74
