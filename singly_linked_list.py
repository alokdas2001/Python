class node:
    def __init__(self , data):
        self.data = data
        self.next = None;

class Linkedlist:
    def __init__(self):
        self.start = None;



    def insert_last(self , value):
        new_node = node(value)
        if(self.start == None):
            self.start = new_node;
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node


    def insert_first(self , value):
        new_node = node(value)

        new_node.next = self.start
        self.start = new_node

    def insert_specific_pos(self, prev_node , value):

        if not prev_node:
            print("prev node not in list")
            return
  
            new_node = node(value)

            new_node.next = prev_node.next
            prev_node.next = new_node
        

        


    def delete_first(self):
        if self.start == None:
            print("Linked List is empty")
        else:
            self.start = self.start.next

    def delete_last(self):
        
      
        if(self.start == None):
            print("List Is Empty")

        else:
            temp = self.start
            while (temp.next != None):
                prev = temp
                temp= temp.next
            
            prev.next = None

    def delete_specific_pos(self ,start ,  position):
   
        pass




    def view_list(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while(temp!= None):
                print(temp.data , end = ' ')
                temp = temp.next




obj = Linkedlist()


obj.insert_last(10)
obj.insert_last(20)
obj.insert_last(30)
obj.insert_last(40)
obj.view_list()
print()
obj.delete_first()
obj.view_list()
print()
obj.insert_first(5)
obj.view_list()
print()


obj.insert_specific_pos(2 , 25)   # problem ... pass like linkedlist.self.start .....
obj.view_list()
print()

obj.delete_last()
obj.view_list()
           
       
