a = 5
b = 0

try:
    print("open")
    print(a/b)
except Exception as e:
    print("error " , e)
finally:
    print("closed")
