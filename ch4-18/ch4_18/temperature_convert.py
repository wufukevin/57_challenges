from enum import Enum


class Temperature(Enum):
    Kelvin = 'K'
    Fahrenheit = 'F'
    Celsius = 'C'

    def convert_to(self):
        if self.value == 'K':
            return self.Celsius
        elif self.value == 'F':
            return self.Celsius
        else:
            return self.Fahrenheit


def ask_question():
    def float_convertor(f):
        return float(f)

    def temperature_convertor(t):
        return Temperature(t.upper())

    for mode in Temperature:
        print(f"Press {mode.value} to convert from {mode.name} to {mode.convert_to()}")

    input_mode = temperature_convertor(input('Your choice: '))
    input_temperature = float_convertor(input(f'Please enter the temperature in {input_mode.name}: '))
    return input_mode, input_temperature


class TemperatureConvertor:
    def convert(self, mode, temperature):
        if mode == Temperature.Kelvin:
            result = temperature - 273.15
        elif mode == Temperature.Fahrenheit:
            result = (temperature - 32) * 5 / 9
        else:
            result = (temperature * 9 / 5) + 32
        print(f'The temperature in {mode.convert_to().name} is {result:.2f}.')


if __name__ == '__main__':
    convertor = TemperatureConvertor()
    convertor.convert(*ask_question())
