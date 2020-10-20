#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from credential import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
from requests_oauthlib import OAuth1Session
from http import HTTPStatus
from datetime import datetime
import os
import yuntaku_bot


def post_tweet(body):
    # 認証処理
    twitter = OAuth1Session(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )
    # ツイート処理
    res = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params={"status": body})
    print(res)

    # エラー処理
    if res.status_code == HTTPStatus.OK:
        print("Successfuly posted")
    else:
            print(f"Failed: {res.status_code}")

def main():
    print("main start")
    # カレントディレクトリを実行ファイルの場所に移動
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())

    # body = "テスト投稿2"

    # tweet生成
    twtext = yuntaku_bot.step3()
    post_tweet(twtext+'。 #yunbot')


if __name__ == '__main__':
    main()
