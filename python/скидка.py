price=float(input('какова стоимость вашего товара?'))
if price <=10:
    sale=float(price*0.10)
if price>10:
    sale=float(price*0.20)
final_price=float(price-sale)
print('Ваша скидка составила',sale,'$,','итоговая цена',final_price,'$')
    
