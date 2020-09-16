def user_info(**info):
    for i, el in enumerate(info):
        if i == len(info) - 1:
            print(info[el], end='')
        else:
            print(info[el], end=', ')


user_info(name=input('Имя: '),
          secondname=input('Фамилия: '),
          year_of_birth=input('Год рождения: '),
          city_of_residence=input('Город проживания: '),
          email=input('email: '),
          phone=input('Номер телефона: '))
