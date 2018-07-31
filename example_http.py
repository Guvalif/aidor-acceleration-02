# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


# 外部プログラムの読み込み
# =============================================================================
from bottle import (Bottle, response)
import cv2
from wiringpi import *

from adc import analogRead


# 定数定義・初期化処理
# =============================================================================
LIGHT_PIN  = 0
THERMO_PIN = 1
VOLUME_PIN = 2
MOTION_PIN = 26
SERVO_PIN  = 18

CAMERA_INDEX = 0

capture_device = cv2.VideoCapture(CAMERA_INDEX)
router         = Bottle()

wiringPiSetupGpio()

pinMode(SERVO_PIN, PWM_OUTPUT)
pwmSetMode(PWM_MODE_MS)
pwmSetRange(1024) # 1024 => 2^10 => 10[bit]に精度を設定
pwmSetClock(375)  # 基本周波数が50[Hz]となるように、基準周波数21.6[MHz]を分周 { (21.6 * 10^6) / (1024 x 375) => 50[Hz] }


# URIの定義・HTTPサーバの起動
# =============================================================================
@router.route('/v1/image', method=['GET'])
def image_get():
    map(lambda _: capture_device.read(), range(5))

    result, frame = capture_device.read()
    result, image = cv2.imencode('.jpg', frame)

    response.headers['Cache-Control'] = 'no-cache'
    response.content_type = 'image/jpg'

    return image.tobytes()


@router.route('/v1/sensor', method=['GET'])
def sensor_get():
    response_json = {
        'resource': 'sensor',
        'data': {
            'light': analogRead(LIGHT_PIN),
            'thermo': analogRead(THERMO_PIN),
            'volume': analogRead(VOLUME_PIN),
            'motion': bool(digitalRead(MOTION_PIN))
        }
    }

    response.headers['Cache-Control'] = 'no-cache'
    response.content_type = 'application/json'

    return response_json


@router.route('/v1/servo/<value:int>', method=['GET']) # 本来は'PUT'にすべきです
def servo_put(value):
    response_json = {
        'resource': 'servo',
        'data': {
            'command': 'pwm_write',
            'result': pwmWrite(SERVO_PIN, max(min(value, 123), 26))
        }
    }

    response.headers['Cache-Control'] = 'no-cache'
    response.content_type = 'application/json'

    return response_json


router.run(host='0.0.0.0', port=80)