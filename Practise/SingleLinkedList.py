class Node:
    def __init__(self, v = None, ptr = None):
        self.val = v
        self.next = ptr

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    
    #O(1)
    def add_first(self, e):
        if(self.head == None): #list is empty to start
            self.head = Node(e)
            self.tail = self.head
        else:
            tmp = Node(e)
            tmp.next = self.head
            self.head = tmp
            tmp = None #were done with that pointer
        self.size += 1

    #0(1)
    def add_last(self, e):
        if(self.head == None): #list is empty to start
            self.head = Node(e)
            self.tail = self.head
        else:
            tmp = Node(e)
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1
        
    def remove_first(self):
        if (self.head == None):
            raise Exception("List is empty")
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.size -= 1
#o(n)
    def remove_last(self):
        if (self.head == None):
            raise Exception("List is empty")
        else:
            ptr = self.head
            while (ptr.next != self.tail):
                ptr = ptr.next
            ptr.next = None
            self.tail = ptr

    #O(n)
    def __str__(self):
        output = ""
        ptr = self.head
        while (ptr !=  None):
            output += str(ptr.val) + ","
            ptr = ptr.next
        return output
    
    def __len__(self):
        return self.size

        

#main
linkedList = SinglyLinkedList()
linkedList.add_first(1)
linkedList.add_first(2)
linkedList.add_first(3) #3 -> 2 -> 1 -> None
# linkedList.add_first(10)
# linkedList.remove_first()
linkedList.remove_last()
linkedList.remove_last()
linkedList.remove_last()

print(linkedList)
