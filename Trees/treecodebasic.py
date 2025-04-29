class Global:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_global(self,level):
        if self.get_level()>level:
            return
        spaces=" " *self.get_level()*3
        prefix=spaces+"|--"
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_global(level)
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def global_tree():
    root=Global("Global")#root node

    #Adding all nodes to the root node as they also child of root
    india=Global("India")
    gujarat=Global("Gujarat")
    ahmedabad=Global("Ahmedabad")
    baroda=Global("Baroda")
    karnataka=Global("Karanataka")
    banguluru=Global("Bangaluru")
    mysure=Global("Mysure")
    usa=Global("USA")
    new=Global("New Jersey")
    princ=Global("Princeton")
    trent=Global("Trenton")
    califo=Global("California")
    san=Global("Sanfrancisco")
    mou=Global("Mountain View")
    palo=Global("PaloAlto")


    #Adding the nodes to their respective parent nodes
    india.add_child(gujarat)
    usa.add_child(new)
    usa.add_child(califo)

#Adding children for gujarat
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)

    #adding children for karnataka
    india.add_child(karnataka)
    karnataka.add_child(banguluru)
    karnataka.add_child(mysure)

#adding children for new Jersey
    new.add_child(princ)
    new.add_child(trent)

#adding children for california
    califo.add_child(san)
    califo.add_child(mou)
    califo.add_child(palo)
#addign all teh sub-parent to root node as they are its children
    root.add_child(india)
    root.add_child(usa)
    return root

if __name__=="__main__":
    root=global_tree()
    print("The Global tree with level0:")
    root.print_global(0)
    print()
    print("The Global tree with level1:")
    root.print_global(1)
    print()
    print("The Global tree with level2:")
    root.print_global(2)
    print()
    print("The Global tree with level3:")
    root.print_global(3)














    






    
    

    
