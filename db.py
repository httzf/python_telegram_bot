file = open('text.txt', 'a', encoding = 'UTF-8')

text = [
        f'<i>Привет!</i>'
        f' '
        f'\nВот что я <u>умею:</u>',
        f'/start'
        f'\n/help'
        f'\n/keyboard - секундомер!'
        f'\n/inline_keyboard - плейлисты с музычкой!'
        f'\n '
        f'\nУдачного пользования!'
]

to_write = '\n' .join(text)

file.write(to_write)
