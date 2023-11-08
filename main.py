from PIL import Image, ImageDraw, ImageFont # from PIL import *

running = True
print('Генератор мемов запущен!')
while running:
    text_type = input('Введите цифру 1, если хотите выбрать только нижний текст. цифру 2, если только верхний текст. 1 и цифру 2, если верхний и нижний текст: ')
    top_text = ''
    bottom_text = ''

    if '2' in text_type:
        top_text = input('Введите верхний текст: ')
    if '1' in text_type:
        bottom_text = input('Введите нижний текст: ')

    katalog = ['Кот в очках.png', 'Кот в ресторане.png' ]
    for i in range(len(katalog)):
        print(i, katalog[i])
    kartinka = int(input('Нужно выбрать картинку: '))

    image = Image.open(katalog[kartinka])
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=70)
    text = draw.textbbox((0, 0), top_text, font)
    draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill='blue')
    draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill='red')
    memename = input('Придумайте имя для картинки: ')
    image.save(memename + '.jpg')

    user = input('Введите 1, если хотите создать ещё один мем, если хотите завершить программу, то 2: ')
    if user == '1':
        pass
    elif user == '2':
        quit(print('Программа завершена'))
    else:
        print('Вы ввели не правильные цифры)')



