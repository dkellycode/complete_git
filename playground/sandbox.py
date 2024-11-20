import random as rd

class Rollnow:
    def rolld6(self):
        roll1 = rd.randint(1,6)
        roll2 = rd.randint(1,6)
        return roll1, roll2

    def rolld20(self):
        roll1 = rd.randint(1,20)
        roll2 = rd.randint(1,20)
        return roll1, roll2

d6 = Rollnow()
print('d6 result = ' + str(d6.rolld6()))

d20 = Rollnow()
print('d20 result = ' + str(d20.rolld20()))
