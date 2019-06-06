# jma_rr
[![Build Status](https://travis-ci.org/0x0u/jma_rr.svg?branch=master)](https://travis-ci.org/0x0u/jma_rr)

https://qiita.com/0x0/items/f14bfa90d102af8f0e74

## What is this?
気象庁の5分毎に更新される[降水ナウキャスト]( https://www.jma.go.jp/jp/radnowc)の画像データの１日分（5分毎に画像がアップロードされるので、12x24=288枚の画像）をダウンロードし、画像処理ライブラリpillowを使ってgifを作成、Dropboxに送信します。 これら一連の処理をTravisCIのCronJobsを使いCI上で定期実行します。CI上で処理をすることが前提になっているので、このリポジトリ内のファイルを自分のリポジトリにpushする必要があります。

<img src="https://user-images.githubusercontent.com/34241526/50583477-cabc1b80-0eac-11e9-81f2-5afe2947baa6.gif">

## Usage
1. リポジトリをcloneした後リポジトリ内のjma_rr.pyと.travis.ymlを新たに作成した自分のリポジトリにpush
2. [DropboxAPI](https://www.dropbox.com/developers/apps)にてアクセストークンを取得
3. [TravisCI](https://travis-ci.org/)にてjma_rrリポジトリを登録する
4. Settings > Settings（jma_rrリポジトリの）> EnvironmentVariables（DropBoxの環境変数）を設定  
```name: DROPBOX_ACCESS_TOKEN value: 'Dropboxのアクセストークン'```
5. 同じ画面でCronJobsの設定（Intervalをdailyにした場合は設定した時間を起点に24時間後に実行される）  
```Branch: master, Interval: daily, Options: Always run```
