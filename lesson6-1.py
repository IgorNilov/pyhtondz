import time


class TrafficLight:
    __color = 'red'
    sve = input('Сколько раз повторить светофор :')

    def running(self):
        print('Светофор работает')
        self.sve = 'sve'
        self.__color = 'red'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)

        count = 0
        while count == self.sve:
            break
            count += 1


cvet = TrafficLight()
print(cvet.running())
