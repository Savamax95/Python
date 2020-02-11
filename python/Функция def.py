
class ball:
	def _init_(self,color,size,direction):
		self.color = color
		self.size = size
		self.direction = direction
	def bounce(self):
		if self.direction == 'вниз':
			self.direction = 'вверх'
myball=ball('зеленый','большой','вверх')
print('Я только создал мяч')
print('Размер моего мяча', maball.size)
print('Цвет моего мяча', myball.color)
print('Мой мяч движется' myball.direction)
print('Сейчас я поменяю направление движения мяча')
print
myball.bounce()
print('Теперь мой мяч движется', myball.direction)


		