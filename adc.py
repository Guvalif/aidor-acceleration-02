# -*- coding: utf-8 -*-

__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License (http://opensource.org/licenses/mit-license.php)'


from struct import pack

import wiringpi as wpi


SPI_CH = 1
SPEED  = 1000000


class ADC(object):
    def __init__(self, spi_ch, speed):
        self.spi_ch = spi_ch
        self.speed  = speed

        wpi.wiringPiSPISetup(self.spi_ch, self.speed)


    def analogRead(self, channel):
        command = 0xC0 | (channel << 3)
        data    = pack('>I', command << 24)

        wpi.wiringPiSPIDataRW(self.spi_ch, data)

        data  = map(ord, data)
        value = (data[0] << 24 | data[1] << 16 | data[2] << 8 | data[3]) >> 13

        return value


adc = ADC(SPI_CH, SPEED)

analogRead = lambda ch: adc.analogRead(ch)