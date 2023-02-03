import random
word_list = ['виселица', 'война', 'мир']

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
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

def defense():
    ### The main part of defense
    while True:
        predication = input()
        if not predication.isalpha():
            print("Вводите только содержащиеся в словах глифы!")
            continue
        if len(predication) == 1:
            if predication in guessed_letters:
                print("Вы уже вводили этот глиф.")
                continue
            else:
                guessed_letters.append(predication)
                print(guessed_letters)
        else:
            if predication in guessed_words:
                print("Вы уже вводили это слово.")
                continue
            else:
                guessed_words.append(predication)
                print(guessed_words)
        return(predication)

def revelation(hidden_word, rev_char):
    for char in word:
        if char == rev_char:
            result += rev_char.upper()
        else:
            result += hidden_word
    return result

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте сыграем в игру.')
    print(display_hangman(tries))
    print(word_completion)
    print(f"Глифов в этом слове: {len(word)}")
    print("Прорицайте глиф или слово целиком.")

    predication = defense()
    ### The main part of game
    while True:
        if len(predication) == 1:
            if predication in word:
                revelation(word_completion, predication)
            else:
                tries -= 1
                print(display_hangman(tries))
        else:
            if predication == word:
                print("Congratulations!")
                break
            else:
                guessed_words.append(predication)
                tries -= 1
                print("Неверная попытка")
                print(display_hangman(tries))
        if tries == 0:
            print("It was over try")
            print(display_hangman(tries))
            break

word = get_word()
play(word)
