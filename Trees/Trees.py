class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def get_length(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_t(self):
        spaces=" "*self.get_length()*3
        if self.parent is None:  # Explicitly handle the root node
            print(self.data)
        else:
            prefix = spaces + "|--"
            print(prefix + self.data)

        if self.children:  # Checking for children explicitly
            for child in self.children:
                child.print_t()
    
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
def brand_product_tree():
    root=TreeNode("File Manager")
    #Documents Folder(parent for doc1 and doc2
    document=TreeNode("Documents")
    document.add_child(TreeNode("doc.1"))
    document.add_child(TreeNode("doc.2"))
    #videos Folder (parent for video 1 and video2)
    video=TreeNode("Videos")
    video.add_child(TreeNode("Video1"))
    video.add_child(TreeNode("Video2"))
    #Photo folder
    photo=TreeNode("Photos")
    photo.add_child(TreeNode("Photo1"))
    photo.add_child(TreeNode("Photo2"))


    root.add_child(document)
    root.add_child(video)
    root.add_child(photo)
    root.print_t()
if __name__=="__main__":
    brand_product_tree()







    
