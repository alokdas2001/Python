a = [2 , 4 , 6 , 9 , 10 , 54 , 98]

key = 54


def binary_search(a, key):
	low = 0
	high = len(a) - 1
	while low < high:
		mid = (low + high) // 2
		if key == a[mid]:
			return True
		elif key < mid:
			high = mid - 1
		else:
			low = mid + 1

	return False


if binary_search(a , key):
    print("found")
else:
    print("not found")
