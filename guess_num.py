# 重複性在程式碼中是不好的

import random
sta = input('請決定隨機數字開始值：')
end = input('請決定隨機數字結束值：')
sta = int(sta)
end = int(end)

r = random.randint(sta, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字:')
	num = int(num)
	if num > end:
		print('超出猜測範圍')
	elif num < sta:
		print('小於猜測範圍')
	elif num == r:
		print('猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')

