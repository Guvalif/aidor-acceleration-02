# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


# 外部プログラムの読み込み
# =============================================================================
from time import sleep

from cv2 import VideoCapture, imwrite
from wiringpi import *


# 定数定義・初期化処理
# =============================================================================
CAMERA_INDEX = 0
MOTION_PIN   = 26

camera = VideoCapture(CAMERA_INDEX)

wiringPiSetupGpio()


# メインループ
# =============================================================================
while True:
    # これ以降を自分で作成
    pass