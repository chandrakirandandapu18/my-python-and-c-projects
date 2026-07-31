class muthatha:
    def lands():
        print("i have lands...")

class thatha(muthatha):
    def houses():
        print("i have houses...")

class nanna(thatha):
    def govt_job():
        print('i have govt job and land...')
class atha(thatha):
    def gold():
        print("i have gold... ")

class me(nanna):
    def study():
        print("i will earn billions..")

class cousin(atha):
    def studying():
        print("i am still studying...")

obj=me()
obj.study()
obj.govt_job()
obj.houses()
obj.lands()

o=cousin()
o.gold()
o.houses()
o.lands()
o.studying()    