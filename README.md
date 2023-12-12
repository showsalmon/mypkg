# mypkg
[![test](https://github.com/showsalmon/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/showsalmon/mypkg/actions/workflows/test.yml)
* このリポジトリは、ロボットシステム学で学んだROS2を使った練習リポジトリです。

## このリポジトリ内のノード
### talker.py
* self.nが1の時はmsg.dataに1を代入し、self.nが2以上の時はsel.aとself.bを足し、msg.dataに代入してフィボナッチ数列を計算します.その計算したフィボナッチ数列を1秒ごとメッセージとして送信します.
### listener.py
* talker.pyから送信されたメッセージを受信して画面に出力します.

### talk_listen.launch.py
* 一つの端末でtalker.pyとlistener.pyを一度に立ち上げます.

## 実行方法
### talkerとlistenerで起動する場合
```bash
端末1$ ros2 run mypkg taker
(何も出力されません)

端末2$ ros2 run mypkg listener
[INFO] [1702362508.165740665] [listener]: Listen: 1
[INFO] [1702362509.154592639] [listener]: Listen: 2
[INFO] [1702362510.155604714] [listener]: Listen: 3
[INFO] [1702362511.155570442] [listener]: Listen: 5
[INFO] [1702362512.155917687] [listener]: Listen: 8
・・・
```

### launchで起動する場合
```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/haneishi/.ros/log/2023-12-12-15-38-23-764391-Haneishi-30094
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [30096]
[INFO] [listener-2]: process started with pid [30098]
[listener-2] [INFO] [1702363105.030380962] [listener]: Listen: 1
[listener-2] [INFO] [1702363106.017798907] [listener]: Listen: 1
[listener-2] [INFO] [1702363107.018235797] [listener]: Listen: 2
[listener-2] [INFO] [1702363108.018706936] [listener]: Listen: 3
[listener-2] [INFO] [1702363109.018175437] [listener]: Listen: 5
[listener-2] [INFO] [1702363110.018394139] [listener]: Listen: 8
・・・
```

## 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 20.04
* ROS2 foxy

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* © 2023 Sho Haneishi
