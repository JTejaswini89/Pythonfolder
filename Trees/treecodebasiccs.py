class Management:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self,property_type="both",level=0):
        if property_type=="name":
            spaces=" "*self.get_level()*2
            prefix=spaces+"|--"
            print(prefix+self.name)
        elif property_type=="designation":
            spaces=" "*self.get_level()*2
            prefix=spaces+"|--"
            print(prefix+self.designation)
        else:
            spaces=" "*self.get_level()*2
            prefix=spaces+"|--"
            print(prefix+self.name+self.designation)
        for child in self.children:
            child.print_tree(property_type, level + 1)

    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def management_file():
    root=Management("Nilupul","(CEO)")

    chinmay=Management("Chinmay","(CTO)")
    vishwa=Management("Vishwa","(INFRASTRUCUTRE HEAD)")
    dhaval=Management("Dhaval","(Cloud Manager)")
    abhijith=Management("Abhijit","(App manager)")
    aamir=Management("Aamir","(Application Head)")
    gels=Management("Gels","(HR Head)")
    peter=Management("Peter","(Recuritment Manager)")
    waqas=Management("Waqas","(Policy Manager)")


    chinmay.add_child(vishwa)
    vishwa.add_child(dhaval)
    vishwa.add_child(abhijith)
    gels.add_child(peter)
    gels.add_child(waqas)

    root.add_child(chinmay)
    root.add_child(gels)
    print("This the tree with only names")
    root.print_tree("name")
    print()
    print("This the tree with only their desgination")
    root.print_tree("designation")
    print()
    print("This the tree with their name and respective designation.")
    root.print_tree("both")


if __name__=="__main__":
    management_file()




    
