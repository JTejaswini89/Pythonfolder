class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None#as we have left node in tree we use left
        self.right=None#we have right node from the tree we use
    def add_child(self,data):
        #check if the same value exsist
        if data==self.data:
            return
        if data < self.data:
            #add value to left
            if self.left:
                #if the left of root node have element
                self.left.add_child(data)
            else:
                #if the left child is empty
                self.left=BinaryTreeNode(data)
        else:
            #add value to right
            if self.right:
                #add the element if the left child is not empty
                self.right.add_child(data)
            else:
                self.right=BinaryTreeNode(data)
    #left,root,right
    def in_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.in_order_traversal()
        element.append(self.data)
        if self.right:
            element+=self.right.in_order_traversal()
        return element
    #left,right,root
    def post_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.post_order_traversal()
        if self.right:
            element+=self.right.post_order_traversal()
        element.append(self.data)
        return element
    #root,left,right
    def pre_order_traversal(self):
        element=[]
        element.append(self.data)
        if self.left:
            element+=self.left.pre_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()
        return element
    #to add the elements from teh list
    def calculate_sum(self):
        sum_ele=self.data
        if self.left:
            sum_ele+=self.left.calculate_sum()
        if self.right:
            sum_ele+=self.right.calculate_sum()
        return sum_ele
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()#recursive call to print the left most min value
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()#recursive call to print the ringht most max value

    def delete_value(self,value):
        if value < self.data:
            if self.left:
                self.left=self.left.delete_value(value)
        elif value > self.data:
            if self.right:
                self.right=self.right.delete_value(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            """min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete_value(min_val)"""
            max_val=self.right.find_max()
            self.data=max_val
            self.right=self.right.delete_value(max_val)
        return self
            
def build_tree(element):
    root=BinaryTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__=="__main__":
    numbers=[8, 3, 10, 1, 6, 14, 4, 7, 13]
    numbers_tree=build_tree(numbers)
    print("The in order traversal is done as:",numbers_tree.in_order_traversal())
    print("The post order is done as:",numbers_tree.post_order_traversal())
    print("The pre order is done as:",numbers_tree.pre_order_traversal())
    print("The sum of all teh elements in the tree is:",numbers_tree.calculate_sum())
    print("The minimum value from the tree is:",numbers_tree.find_min())
    print("The maximum value from the tree is:",numbers_tree.find_max())
    numbers_tree.delete_value(10)
    print("After deletion 10:",numbers_tree.in_order_traversal())

















    
