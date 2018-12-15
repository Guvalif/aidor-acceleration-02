# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


# 外部プログラムの読み込み
# =============================================================================
from time import sleep

from wiringpi import *

from adc import analogRead


# 定数定義・初期化処理
# =============================================================================
VOLUME_PIN = 2
SERVO_PIN  = 18

wiringPiSetupGpio()
pinMode(SERVO_PIN, PWM_OUTPUT)
pwmSetMode(PWM_MODE_MS)
pwmSetRange(1024)
pwmSetClock(375)


# メインループ
# =============================================================================
while True:
    # これ以降を自分で作成
    pass