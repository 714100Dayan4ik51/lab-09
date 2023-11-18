import random
import logging

logging.basicConfig(filename='barrel_game.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_input():
    while True:
        try:
            n = int(input("Введите количество бочек (целое положительное число): "))
            logging.info(f"Начинаем игру с {n} бочонками.")
            if n > 0:
                return n

            else:
                logging.error('Ввели отрицаетльное число.')
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            logging.error('Ввели не целое число.')
            print("Пожалуйста, введите целое число.")