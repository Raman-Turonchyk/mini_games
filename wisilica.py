import random


word_list = ['печенье', 'глобус', 'ракета', 'мотоцикл', 'диверсия', 'атом', 'статуя']
tries = 6


def get_word():
    slovo = random.choice(word_list)
    slovo = slovo.upper()
    play(slovo, tries)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                ''',
                # голова, торс, обе руки, одна нога
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                r'''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                r'''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word, tries):
    print('Давайте играть в угадайку слов!')
    print('Слово содержит буквы', random.sample(word, 2))
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    while True:
        print(display_hangman(tries))
        print(word_completion)
        print('Количество допустимых промахов =', tries)
        print('Буквы которые вы вводили:', guessed_letters)
        print('Слова которые вы вводили:', guessed_words)
        polzovatel = input('Введите букву или слово целиком ')
        if polzovatel.isalpha():
            if len(polzovatel) == 1 and polzovatel:
                if polzovatel in word:
                    for i in range(len(word)):
                        if word[i] == polzovatel:
                            word_completion = word_completion[:i] + polzovatel + word_completion[i + 1:]
                elif polzovatel in guessed_letters:
                    print('Вы вводили данную букву!')
                    continue
                else:
                    tries -= 1
                    guessed_letters += polzovatel
            elif len(polzovatel) == len(word):
                if polzovatel == word:
                    print('Вы победили, поздравляем!')
                    break
                elif polzovatel in guessed_words:
                    print('Вы вводили данное слово!')
                    continue
                else:
                    tries -= 1
                    guessed_words += polzovatel.split()
            elif len(polzovatel) != len(word) and len(polzovatel) > 1:
                print(f'Введите слово целиком, оно состоит из {len(word)} букв или одну букву!')
                continue
            if word_completion == word:
                print('Вы победили, поздравляем!')
                break
            if tries == 0:
                print(display_hangman(tries))
                print('Вы проиграли...')
                break


while True:
    game = input('Вы хотите сыграть в игру? Ответьте ДА или НЕТ ').upper()
    if game == 'ДА':
        get_word()
    else:
        break
