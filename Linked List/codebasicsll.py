class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None#initially head points to none 
    def get_length(self):
        count=0
        itr=self.head
        while itr:#traverse through all teh nodes and count them
            count+=1
            itr=itr.next
        return count
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=''
        while itr:#move through all the nodes to create a string representation
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
        node=Node(data,None)## we took none as next value cause if the node have none as it nxt value then it is end 
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:#traverse to last node
            itr=itr.next
        itr.next=Node(data,None)#insert the new node at teh end
    def insert_at(self,data,index):
        node=Node(data)
        if index<0 or index>=self.get_length():
            print("Invalid length")
        if index==0:
            node=self.head
            return
        count=0
        itr=self.head
        while itr:#traverse to teh index to where we need to insert
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def  insert_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def remove_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
    def remove_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        while itr.next.next:#to move to the second last node of linkedlist
            itr=itr.next
        itr.next=None#remove last node
    def remove_at(self,data,index):
        if index<0 or index>self.get_length():
            print("Invalid length")
            return
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:#traverse to the node last before teh index
            if count==index-1:
                itr.next=itr.next.next#remove the node
                break
            itr=itr.next
            count+=1

        
link=LinkedList()
"""link.insert_at_beginning(10)
link.insert_at_beginning(20)
link.insert_at_end(30)
link.insert_at(40,1)
link.insert_at_end(50)
link.insert_at_end(60)
link.print_ll()
link.remove_at_beginning()
link.remove_at_end()
link.remove_at(30,2)
link.print_ll()"""

link.insert_list(["banana","mango","grapes","orange"])
link.print_ll()
link.insert_at("apple",2)
link.print_ll()
link.remove_at("orange",4)
link.print_ll()
link.remove_at("banana",0)
link.print_ll()
link.remove_at("mango",0)
link.print_ll()
link.remove_at("apple",0)
link.print_ll()
link.remove_at("grapes",0)
link.print_ll()

    
            
