class stack:
    def __init__(self):
        self.items = []
    
    def push(self , items):
        self.items.append(items)

    def pop(self):
        self.items.pop()

    def show_stack(self):
        return self.items

obj = stack()
obj.push("A")
obj.push("B")
obj.push("C")
obj.push("D")
obj.pop()
print(obj.show_stack())