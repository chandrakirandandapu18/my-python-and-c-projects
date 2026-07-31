class GrandParent:
    def display(self):
        print("GP properties..")

class Father(GrandParent):
    def show(self):
        print("Father properties...")

class Son(Father):
    def display_Son(self):
        print("My properties..")
s=Son()
s.display()
s.show()
s.display_Son