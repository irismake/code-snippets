import x16k33
import font_5x5
import time


class X16k33MatrixLed5x5(x16k33.X16k33):
    array_5x5 = [[0 for _ in range(5)] for _ in range(5)]

    def show_leds(self, leds: str) -> None:
        """
        Show LED pattern
        
        Parameters:
            leds: LED grid spec as string  
        """

        leds = leds.replace(" ", "").replace("\n", "")
        data = bytearray()
        for column in range(5):
            byte = 0
            for row in range(5):
                byte |= (1 if leds[row * 5 + column] == '#' else 0) << row
            data.append(byte)
        self._write(data)