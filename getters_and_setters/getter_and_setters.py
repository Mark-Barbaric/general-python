
class Getters:


    def __init__(self):
        self.__age=0

    
    @property
    def age(self):
        print("getter called")
        return self.__age
    

    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("You're too young")
        
        self.__age = a
    
mark = Getters()
mark.age = 19
print(f"mark's age is {mark.age}")