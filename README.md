# mypkg
* このリポジトリは、ロボットシステム学で学んだROS2を使った練習リポジトリです。

# talker.pyコマンド
[![test](https://github.com/showsalmon/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/showsalmon/mypkg/actions/workflows/test.yml)
* このソフトは、self.nが1の時はmsg.dataに1を代入し、self.nが2以上の時はself.aとself.bを足し,msg.dataに代入してフィボナッチ数列を計算します. その計算したフィボナッチ数列を1秒毎listener.pyに発信します.

# listener.pyコマンド
* このソフトはtalker.pyから発信されたmsgを受信して画面に出力します.

# talk_listen.launch.pyコマンド
* このソフトは、一つの端末でtalker.pyとlistener.pyのコマンドを一度に立ち上げます.

## 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 20.04

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* © 2023 Sho Haneishi
