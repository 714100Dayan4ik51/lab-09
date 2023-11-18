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


def barrel_game(n):
    barrel_numbers = list(range(1, n + 1))
    random.shuffle(barrel_numbers) # перемешиваем порядок бочонков

    print("Нажмите любую клавишу для вытягивания бочонка.")
    pull = []
    while True:
        user_input = input()
        if not barrel_numbers:
            print("Бочонки закончились.")
            logging.warning("Бочонки закончились.")
            break
        random_barrel = barrel_numbers.pop() # берем бочонок
        pull.append(random_barrel) # добовляем бочонок в список вытянутых
        print("Вытянут бочонок под номером:", random_barrel)
        logging.info(f"Выпал бочонок под номером: {random_barrel}")

    print("Последовательность вытянутых бочонков:", pull)


def main():
    n = get_input()
    game = barrel_game(n)

if __name__ == "__main__":
    main()