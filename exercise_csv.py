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
LIGHT_PIN  = 0
THERMO_PIN = 1
VOLUME_PIN = 2
MOTION_PIN = 26

wiringPiSetupGpio()


# メインループ
# =============================================================================
with open('sensor.csv', mode='w') as f:
    while True:
        # これ以降を自分で作成
        pass