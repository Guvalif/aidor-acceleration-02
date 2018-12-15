IoTプロトタイピングワークショップ「ハードウェア概論編」| サンプルプログラム
===============================================================================

What's This?
-------------------------------------------------------------------------------

IoTプロトタイピングワークショップ「ハードウェア概論編」で使用したサンプルプログラムです。

### 実施実績

- 2018/08/01: IoT・ロボットビジネス創出プログラム「[AIDOR ACCELERATION](https://teqs.jp/acceleration)」第1ターム 基礎知識講座 第2回
- 2018/10/31: IoT・ロボットビジネス創出プログラム「[AIDOR ACCELERATION](https://teqs.jp/acceleration)」第2ターム 基礎知識講座 第2回
- 2018/11/02: [IoTプロトタイピングワークショップ「ハードウェア概論編」@大阪](https://connpass.com/event/103997/)
- 2018/12/15: [IoTプロトタイピングワークショップ「ハードウェア概論編」@東京](https://connpass.com/event/109698/)


Getting Started
-------------------------------------------------------------------------------

Raspberry Piにログインした後、下記画像 青線部内のアイコンをクリックし**ターミナル**を開きます。

![](.assets/desktop.png)

**ターミナル**上で、以下のコマンドを1行づつ入力します：

```sh
sudo pip install wiringpi
sudo apt-get install python-opencv
```

これにより、

- `cv2`: 画像処理を行うためのライブラリ
- `wiringpi`: Raspberry PiのGPIOを制御するためのライブラリ

以上2点がインストールされます。


How to Use
-------------------------------------------------------------------------------

[ダウンロードリンク](https://github.com/Guvalif/iot-01/archive/master.zip)をクリックすることで、
プログラムを一式ダウンロードできます。

**ターミナル**上で`sudo idle`と入力し、**Python 2 IDLE**を起動します。
その後、メニューから`File -> Open...`とたどることで、それぞれのプログラムを開くことができます。

プログラムを実行するには、メニューから`Run -> Run Module`とたどります。

なお、同梱されるプログラムは以下の通りです：

- `adc.py`: A/DコンバータIC "MCP3208" で、アナログ信号を測定するためのライブラリ
- `example_analog.py`: アナログ信号を閲覧するプログラム
- `example_digital.py`: デジタル信号を閲覧するプログラム
- `example_camera.py`: カメラ画像を撮影するプログラム
- `example_servo.py`: サーボモータを動かすプログラム
- `exercise_robot_controller.py`: システム開発実践「ロボットコントローラの作成」用のひな形
- `exercise_monitoring_camera.py`: システム開発実践「人感センサによる監視カメラの作成」用のひな形


More Details
-------------------------------------------------------------------------------

発展課題の詳細解説に関しては、[ANSWER.md](ANSWER.md)をご参照ください。


Copyright (c) 2018,
-------------------------------------------------------------------------------

- [PLEN Project Company Inc.](https://plen.jp)
- [Kazuyuki TAKASE](https://github.com/Guvalif)

This software is released under [the MIT License](http://opensource.org/licenses/mit-license.php).