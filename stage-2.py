try:
    file = open('text_12.txt', 'r', encoding='utf-8')
    content = file.readlines()
    print(f'В файле содержится {len(content)} строк.')
    for i, el in enumerate(content):
        print(f'В {i + 1} строке содержится {el.count(" ") + 1} слов')
    file.close()
except IOError:
    print('Файл не найден создайте файл для его чтения!')
