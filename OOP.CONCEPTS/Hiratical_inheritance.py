#one base class is included in two or more child class
class Father:
    def show(self):
        print("Properties of father ..")

class child1(Father):
    def display1(self):

        print("properties of child 1..")

class child2(Father):
    def display2(self):
        print("properties of child 2..")

c1=child1()
c2=child2()

c1.show()
c1.display1()

c2.show()
c2.display2()