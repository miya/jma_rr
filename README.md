# rainfall
[![Build Status](https://travis-ci.org/0x0u/rainfall.svg?branch=master)](https://travis-ci.org/0x0u/rainfall)

https://qiita.com/0x0/items/f14bfa90d102af8f0e74

## What is this?
気象庁の一日の[降水データ]( https://www.jma.go.jp/jp/radnowc)をスクレイピングしてgifを生成するやつ。  

## Usage
```
git clone https://github.com/0x0u/rainfall
cd rainfall
pip3 install -r requiremenets.txt
python3 rainfall.py
```

## Description
プログラムを実行すると前日の一日分の降水データ（5分毎に画像がアップロードされるので、12x24=288枚の画像）をダウンロードし、画像処理ライブラリpillowを使ってgifを作成、Dropboxに送信します。 これらの処理をTravis CIのCron Jobsを使いCI上で実行します。
