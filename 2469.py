from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32.00
        return [round(kelvin,5), round(fahrenheit,5)]

if __name__ == '__main__':
    celsius = 36.5
    print(Solution().convertTemperature(celsius))
