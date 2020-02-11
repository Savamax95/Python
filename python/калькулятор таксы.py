def calculatetax(price, tax_rate):
	total = price + (price * tax_rate)
	return total
my_price = float(input ('Введите цену: '))	
totalprice = calculatetax(my_price, 0.06)
print('Цена = ', my_price, 'Итоговая цена = ', totalprice)
