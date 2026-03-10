class employee:
    def __init__(self):
        print('started excuting data/atribute')
        self.id = 123
        self.salary = 50000
        self.disagnation = "SDE"
        print('atribute/data have been initiated')
    
    def travel(self,destination):
        print('this travel method called manutally')
        print(f"employee is travelling to {destination}")

# create an obj/instance of the class
sam = employee()
#print(sam.id)


#calling a method
sam.travel("Indore")