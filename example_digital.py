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
MOTION_PIN = 26

wiringPiSetupGpio()


# メインループ
# =============================================================================
while True:
    print('Motion :', digitalRead(MOTION_PIN))

    sleep(1)
