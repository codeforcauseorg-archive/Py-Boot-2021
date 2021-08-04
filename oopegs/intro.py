class Human:

    def __init__(self):
        self.hands = 2
        self.money = 1000

    def party(self):
        self.money -= 200


class CFCStudent(Human):

    def study(self):
        print("I study so hard")


vinit = Human()
ravi = Human()
deepak = CFCStudent()

deepak.study()
deepak.party()
print(deepak.money)


