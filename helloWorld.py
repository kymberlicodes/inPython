## First Python Program
print("Hello world!")

def feedTheDogs(breakfast, dinner):
	if breakfast or dinner:
		return True
	else:
		return False

test1 = feedTheDogs(True, True)
test2 = feedTheDogs(True, False)
test3 = feedTheDogs(False, True)
test4 = feedTheDogs(False, False)

print(f'Is it time to feed the dogs? {test1}')
print(f'Is it time to feed the dogs? {test2}')
print(f'Is it time to feed the dogs? {test3}')
print(f'Is it time to feed the dogs? {test4}')
