import random


def is_valid(num_gip, margin):
    num_gip = int(num_gip) if num_gip.isdigit() else 0
    result = True if num_gip in list(range(1, margin + 1)) else False
    return result


def ugadaika():
    n = int(input('Введите предел праввой границы чисел: '))
    num = random.randint(1, n)
    counter = 0
    while True:
        num_gip = input('Угадайте число загаданное программой: ')
        counter += 1
        if is_valid(num_gip, n) is True:
            num_gip = int(num_gip)
            if num_gip > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            elif num_gip < num:
                print('Ваше число слишком маленькое, попробуйте еще разок')
                continue
            else:
                print('Вы угадали, поздравляем!')
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                print('Число попыток =', counter)
                break
        else:
           print('А может быть все-таки введем целое число от 1 до 100?')
           continue


def main():
    print('Добро пожаловать в числовую угадайку!')
    while True:
        ugadaika()
        answer = input('если хотите сыграть в игру еще раз напишите да ')
        if answer == 'да':
            continue
        else:
            break


if __name__ == '__main__':
    main()

