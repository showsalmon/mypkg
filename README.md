# mypkg
[![test](https://github.com/showsalmon/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/showsalmon/mypkg/actions/workflows/test.yml)
* このリポジトリは、ロボットシステム学で学んだROS2を使った練習リポジトリです。

# このリポジトリ内のノード
talker.py
* self.nが1の時はmsg.dataに1を代入し、self.nが2以上の時はsel.aとself.bを足し、msg.dataに代入してフィボナッチ数列を計算します.その計算したフィボナッチ数列を1秒ごとメッセージとして送信します.
listener.py
* talker.pyから送信されたメッセージを受信して画面に出力します.

talk_listen.launch.py
* 一つの端末でtalker.pyとlistener.pyを一度に立ち上げます.

## 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 20.04
* ROS2 foxy

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* © 2023 Sho Haneishi
