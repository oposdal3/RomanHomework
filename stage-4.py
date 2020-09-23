from googletrans import Translator
transl = Translator()
with open('text_44.txt', 'a', encoding='utf-8') as file2:
    with open('text_4.txt', 'r', encoding='utf-8') as file1:
        for line in file1:
            result = transl.translate(line, dest='ru')
            print(result.text)
            print(f'{result.text}', file=file2)
