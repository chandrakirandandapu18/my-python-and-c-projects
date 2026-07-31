class base1:
    def display(self):
        print("Display method activated...")

class base2:
        def show(self):
             print("Show method activated....")

class derivated(base1,base2):
    def derivative(self):
         print("derivated...")

O=derivated()
O.show()
O.derivative()
O.display()

         
     
     
        
    