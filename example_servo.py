# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


# 外部プログラムの読み込み
# =============================================================================
from time import sleep

from wiringpi import *


# 定数定義・初期化処理
# =============================================================================
SERVO_PIN = 18

wiringPiSetupGpio()

pinMode(SERVO_PIN, PWM_OUTPUT)
pwmSetMode(PWM_MODE_MS)
pwmSetRange(1024) # 1024 => 2^10 => 10[bit]に精度を設定
pwmSetClock(375)  # 基本周波数が50[Hz]となるように、基準周波数21.6[MHz]を分周 { (21.6 * 10^6) / (1024 x 375) => 50[Hz] }


# メインループ
# =============================================================================
while True:
    pwmWrite(SERVO_PIN, 26)  # -90°相当のパルス幅を出力 (0.5[msec])

    sleep(1)

    pwmWrite(SERVO_PIN, 123) # +90°相当のパルス幅を出力 (2.4[msec])

    sleep(1)
