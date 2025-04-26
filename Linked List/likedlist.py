class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty")
            return  
        itr=self.head
        llstr=''
        while itr:#iterates till nodes next value null
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
    def get_length(self):
        count=0
        itr=self.head
        while itr:#iterates to count the nodes
            count+=1
            itr=itr.next
        return count
    """node = Node(data, self.head) already sets node.next = self.head
Then you just make self.head = node ;Works even when self.head is None"""
    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while itr.next:#iterates till it reaches none as next value
            itr=itr.next
        itr.next=Node(data,None)
    def insert_at(self,data,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid length")
        if index==0:
            self.insert_at_begin(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def remove_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
    def remove_at_end(self):
        if self.head is None:
            print("List is empty")
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
    def remove_at(self,data,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid list")
        if index==0:
            self.head==self.head.next.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
        
    

ll=LinkedList()
ll.insert_at_begin(45)
ll.insert_at_begin(55)
ll.insert_at_end(34)
ll.insert_at_begin(10)
ll.insert_at_begin(20)
ll.insert_at(52,2)
print("Linked list:")
ll.print_ll()
print("Linked list after removal of element from position three:")
ll.remove_at(55,3)
ll.print_ll()
print("Linked list after removal of element from beginning:")
ll.remove_at_begin()
ll.print_ll()
print("Linked list after removal of element from end:")
ll.remove_at_end()
ll.print_ll()
print("length of the linkedlist:",ll.get_length())

        
            
