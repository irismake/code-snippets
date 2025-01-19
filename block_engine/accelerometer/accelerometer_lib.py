from accelerometer import Accelerometer
from micropython import const
import struct
import time


class Qma6100p(Accelerometer):

    QMA6100P_CHIP_ID = const(0x00)
    QMA6100P_INT_STATUS_2 = const(0x0B)
    QMA6100P_REG_RANGE = const(0x0F)
    QMA6100P_REG_BW_ODR = const(0x10)
    QMA6100P_REG_POWER_MANAGE = const(0x11)
    QMA6100P_INT_EN_1 = const(0x17)
    QMA6100P_REG_RESET = const(0x36)
    QMA6100P_REG_NVM = const(0x33)

    QMA6100P_RANGE_2G = const(0x01)
    QMA6100P_RANGE_4G = const(0x02)
    QMA6100P_RANGE_8G = const(0x04)
    QMA6100P_RANGE_16G = const(0x08)
    QMA6100P_RANGE_32G = const(0x0F)

    QMA6100P_BW_100 = const(0)
    QMA6100P_BW_200 = const(1)
    QMA6100P_BW_400 = const(2)
    QMA6100P_BW_800 = const(3)
    QMA6100P_BW_1600 = const(4)
    QMA6100P_BW_50 = const(5)
    QMA6100P_BW_25 = const(6)
    QMA6100P_BW_12_5 = const(7)
    QMA6100P_BW_OTHER = const(8)

    QMA6100P_LPF_OFF = const(0x00 << 5)
    QMA6100P_LPF_1 = const(0x04 << 5)
    QMA6100P_LPF_2 = const(0x01 << 5)
    QMA6100P_LPF_4 = const(0x02 << 5)
    QMA6100P_LPF_8 = const(0x03 << 5)
    QMA6100P_LPF_RESERVED = const(0xFF)

    QMA6100P_MODE_STANDBY = const(0)
    QMA6100P_MODE_ACTIVE = const(1)

    QMA6100P_MCLK_102_4K = const(0x03)
    QMA6100P_MCLK_51_2K = const(0x04)
    QMA6100P_MCLK_25_6K = const(0x05)
    QMA6100P_MCLK_12_8K = const(0x06)
    QMA6100P_MCLK_6_4K = const(0x07)
    QMA6100P_MCLK_RESERVED = const(0xFF)

    QMA6100P_XOUTL = const(0x01)
    QMA6100P_XOUTH = const(0x02)
    QMA6100P_YOUTL = const(0x03)
    QMA6100P_YOUTH = const(0x04)
    QMA6100P_ZOUTL = const(0x05)
    QMA6100P_ZOUTH = const(0x06)

    QMA6100P_INT1_MAP_1 = const(0x1A)
    QMA6100P_DRDY_BIT = const(0x10)

    def __init__(self, i2c, i2c_address=0x12) -> None:
        super().__init__()
        self._i2c_address = i2c_address
        self._i2c = i2c
        self.soft_reset()
        # qma6100p_writereg(0x11, 0x80);
        self._i2c.writeto_mem(self._i2c_address, 0x11, bytes([0x80]))
        # qma6100p_writereg(0x11, 0x84);
        self._i2c.writeto_mem(self._i2c_address, 0x11, bytes([0x84]))
        # qma6100p_writereg(0x4a, 0x20);
        self._i2c.writeto_mem(self._i2c_address, 0x4a, bytes([0x20]))
        # qma6100p_writereg(0x56, 0x01);
        self._i2c.writeto_mem(self._i2c_address, 0x56, bytes([0x01]))
        # qma6100p_writereg(0x5f, 0x80);
        self._i2c.writeto_mem(self._i2c_address, 0x5f, bytes([0x80]))
        time.sleep_ms(2)

        #  qma6100p_writereg(0x5f, 0x00);
        self._i2c.writeto_mem(self._i2c_address, 0x5f, bytes([0x00]))
        time.sleep_ms(10)
        # qma6100p_writereg(QMA6100P_REG_RANGE, reg_data)
        self._i2c.writeto_mem(self._i2c_address, Qma6100p.QMA6100P_REG_RANGE,
                              bytes([Qma6100p.QMA6100P_RANGE_8G]))
        # qma6100p_set_bw(QMA6100P_BW_100);
        self._i2c.writeto_mem(
            self._i2c_address, Qma6100p.QMA6100P_REG_BW_ODR,
            bytes([Qma6100p.QMA6100P_LPF_8 | Qma6100p.QMA6100P_BW_100]))

        # qma6100p_set_mode(QMA6100P_MODE_ACTIVE);
        self._i2c.writeto_mem(self._i2c_address,
                              Qma6100p.QMA6100P_REG_POWER_MANAGE,
                              bytes([Qma6100p.QMA6100P_MCLK_51_2K | 0x80]))

        self._i2c.writeto_mem(self._i2c_address, 0x21, bytes([0x03]))

    @property
    def chip_id(self):
        return self._i2c.readfrom_mem(self._i2c_address,
                                      Qma6100p.QMA6100P_CHIP_ID, 1)[0] >> 4

    def tick(self):
        data = self._i2c.readfrom_mem(self._i2c_address, 0x21, 1)[0]
        data &= ~(1 << 6)
        self._i2c.writeto_mem(self._i2c_address, 0x21, bytes([data]))
        data = struct.unpack(
            "<hhh",
            self._i2c.readfrom_mem(self._i2c_address, Qma6100p.QMA6100P_XOUTL,
                                   6))
        self.update(data[0] >> 2, data[1] >> 2, data[2] >> 2)

    def soft_reset(self):
        self._i2c.writeto_mem(self._i2c_address, Qma6100p.QMA6100P_REG_RESET,
                              bytes([0xB6]))
        time.sleep_ms(5)
        self._i2c.writeto_mem(self._i2c_address, Qma6100p.QMA6100P_REG_RESET,
                              bytes([0x00]))
        time.sleep_ms(10)

        count = 100
        while count > 0:
            reg_0x33 = self._i2c.readfrom_mem(self._i2c_address,
                                              Qma6100p.QMA6100P_REG_NVM, 1)[0]
            if (reg_0x33 & 0x05) == 0x05:  # bit1:NVM_LOAD_DONE, bit3:NVM_RDY
                break
            count -= 1
            time.sleep_ms(1)
