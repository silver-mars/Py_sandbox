from random import choice

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
            'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
            'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
            'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
            'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет',
            'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет, Мир.\nЯ - магический шар, и я знаю ответ на любой твой вопрос.')
name = input("Как зовут тебя?\n")
print(f"Здравствуй, {name}.")

while True:
    print("Задайте Ваш вопрос...")
    if input():
        print(choice(answers))
    answer = input("Желаете ли узнать что-нибудь ещё?\n")
    if answer.lower() == 'да':
        continue
    else:
        print("Возвращайтесь, если возникнут вопросы.")
        break
