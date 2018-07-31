# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


# 外部プログラムの読み込み
# =============================================================================
from time import sleep

from cv2 import VideoCapture, imwrite


# 定数定義・初期化処理
# =============================================================================
CAMERA_INDEX = 0

capture_device = VideoCapture(CAMERA_INDEX)


# メインループ
# =============================================================================
while True:
    result, frame = capture_device.read()

    imwrite('frame.jpg', frame)

    sleep(1)
