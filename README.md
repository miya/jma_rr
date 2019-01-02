# rainfall
[![Build Status](https://travis-ci.org/0x0u/rainfall.svg?branch=master)](https://travis-ci.org/0x0u/rainfall)

https://qiita.com/0x0/items/f14bfa90d102af8f0e74

## What is this?
気象庁の5分毎に更新される[降水ナウキャスト]( https://www.jma.go.jp/jp/radnowc)の画像データ（5分毎に画像がアップロードされるので、12x24=288枚の画像）をダウンロードし、画像処理ライブラリpillowを使ってgifを作成、Dropboxに送信します。 これらの処理をTravisCIのCronJobsを使いCI上で定期実行します。

<img src="https://user-images.githubusercontent.com/34241526/50583477-cabc1b80-0eac-11e9-81f2-5afe2947baa6.gif">

## Usage

1. このリポジトリをcloneした後、自分のリポジトリにpush
2. [DropboxAPI](https://www.dropbox.com/developers/apps)にてアクセストークンを取得
3. [TravisCI](https://travis-ci.org/)にてrainfallリポジトリを登録する
4. More optionsからSettingに移動して、Environment Variables(環境変数)を設定  
name: DROPBOX_ACCESS_TOKEN value: 'Dropboxのアクセストークン'
5. 同じくSettingからCronJobsの設定(Intervalをdailyにした場合は設定した時間を起点に23時間後)  
Branch: master, Interval: daily, Options: Always run
