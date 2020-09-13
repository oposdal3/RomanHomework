kol = int(input('Введите количество товаров: '))
myProductlist = []
i = 1
nameall = []
priceall = []
kolprudall = []
adall = []
while i < kol + 1:
    product = {}

    name = input('Введите название: ')
    product['название'] = name
    nameall.append(name)

    price = int(input('Введите цену товара: '))
    product['цена'] = price
    priceall.append(price)

    kolprud = int(input('Введите количаство продукта: '))
    product['колличество'] = kolprud
    kolprudall.append(kolprud)

    ad = input('Введите еденицу измерения: ')
    product['ед'] = ad
    if i > 1:
        if ad != adall[0]:
            adall.append(ad)
    else:
        adall.append(ad)

    infProduct = (i, product)
    i += 1
    myProductlist.append(infProduct)

exemp = {'название': nameall, 'цена': priceall, 'колличество': kolprudall, 'ед': adall}
print(exemp)
