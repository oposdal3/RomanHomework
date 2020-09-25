from time import sleep
from termcolor import colored


class TrafficLight:
    def __init__(self):
        self.__color = 'Красный'

    def running(self):
        while True:
            color = self.__color
            print(colored(color, 'red'))
            for i in range(6, -1, -1):
                if i >= 3:
                    print(colored(i, 'red'))
                    sleep(1)
                else:
                    print('None')
                    sleep(0.5)
                    print(colored(color, 'red'))
                    print(colored(i, 'red'))
                    sleep(0.5)
            color = 'Жёлтый'
            print(colored(color, 'yellow'))
            for i in range(1, -1, -1):
                print(colored(i, 'yellow'))
                sleep(1)
            color = 'Зелёный'
            print(colored(color, 'green'))
            for i in range(10, -1, -1):
                if i >= 3:
                    print(colored(i, 'green'))
                    sleep(1)
                else:
                    print('None')
                    sleep(0.5)
                    print(colored(color, 'green'))
                    print(colored(i, 'green'))
                    sleep(0.5)
            color = 'Жёлтый'
            print(colored(color, 'yellow'))
            for i in range(1, -1, -1):
                print(colored(i, 'yellow'))
                sleep(1)


traffic = TrafficLight()
traffic.running()
