# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


from random import randint

class Train:
    
    def __init__(slf, trainNo):
          slf.trainNo = trainNo
    
    def book(self,  fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self):
            print(f" train no : {self.trainNo}  is running on time")


    def getfare(self, fro, to):
            print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12909)
t.book("Rampuria", "Delhi")
t.getstatus()
t.getfare("Rampuria", "Delhi")
