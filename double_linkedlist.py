class Node:
    def  __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None: # no element is there
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node    
            new_node.prev = cur
            new_node.next = None    

    def prepend(self,data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None



    def add_after_node(self,key , data):
        cur = self.head
        while cur != None:
            if cur.next == None and cur.data == key: #last ele
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            
            cur = cur.next   # to increase value of cur in while loop
 


    def add_before_node(self,key,data):
        cur = self.head
        while cur!= None:
            if cur.prev == None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next


    def delete_node(self,key):
        cur = self.head
        while cur!=None:
            if cur.data == key and cur == self.head:

                #case 1 when only head is there
                if cur.next != None:
                    cur = None
                    self.head = None
                    return
            #case 2 when you want to remove head but there are other ele also
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            #case 3 delete node at specific pos
            elif cur.data == key:
                if cur.next !=None:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            
            #case 4 deleting last node
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next            

    

    
    def print_list(self):
        if self.head == None:
            print("List is Empty")
        else:
            cur = self.head
            c = 0
            while cur != None:
                c += 1 
                print(cur.data )
                
                cur = cur.next
    

          


obj = doubly_linkedlist()
obj.print_list()  #list is empty
print()

obj.append(1) #adding ele after list
obj.append(2)
obj.append(3)
obj.append(4)
obj.print_list()  #prints the list
print()

obj.prepend(0)  # adding ele b4 list
obj.print_list() #print list with prepend
print()

obj.add_after_node(1 , 11)
obj.print_list()
print()

obj.add_before_node(4 , 33)
obj.print_list()
print()

obj.delete_node(1) #delete first node
obj.delete_node(3)
obj.print_list()
print()







       