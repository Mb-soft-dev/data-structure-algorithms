# Linked List

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data): 
        node = Node(data)
        self.size += 1
        if self.isEmpty():
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

    def search(self, data): 
        head = self.head
        while head: 
            if head.data == data: 
                return data
            head = head.next
        return -1

    def isEmpty(self):
        return self.head is None
    
    def delete(self, data):
        if self.isEmpty():
            return False
        if self.head.data == data: 
            self.__deleteHead()
            self.size -= 1
            return True
        else:
            isDeleted = self.__deleteTraversal(data)
            if isDeleted: 
                self.size -= 1
            return isDeleted
            
    def __deleteHead(self):
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    
    def __deleteTraversal(self, data):
        head = self.head
        prevNode = None
        while head:
            if head.data == data:
                if prevNode is None: raise Exception("Error")
                prevNode.next = head.next
                return True
            else:
                prevNode = head
                head = head.next
        return False

    def print_list(self): 
        if self.isEmpty(): print('linked list is empty')
        head = self.head
        while head: 
            print(head.data, head.next)
            head = head.next

    def length(self): 
        return self.size

    def reverse(self):
        if self.isEmpty(): return 'The linked list is empty'
        if self.head.next is None: return "One element in the linked list"
        prev = None
        curr = self.head

        self.tail = self.head

        while curr != None:
            next_node = curr.next
            curr.next = prev

            prev = curr 
            curr = next_node

        
        self.head = prev