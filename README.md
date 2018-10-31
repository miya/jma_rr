# rainfall
気象庁の一日の降水データをスクレイピングしてgifを生成するやつ。
<br>データ元: https://www.jma.go.jp/jp/radnowc/

## Usage
```git clone https://github.com/0x0u/rainfall```
<br>```cd rainfall```<br>```pip3 install -r requiremenets.txt```<br>```python3 rainfall.py```

## Description
プログラムを実行すると前日の一日分の降水データ（5分毎に画像がアップロードされるので、12x24=288枚の画像）をダウンロードし、画像処理ライブラリpillowを使ってgifを作成します。
