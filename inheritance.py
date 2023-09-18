class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter ur name")
        self.mark=input(("enter your name"))
    def putd(self):
        print(self.name,self.mark)


class teacher(student):
    def display(self):
        print("am derived class")

obj=teacher('','')
obj.getdetails()
obj.putd()
obj.display()
