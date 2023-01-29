# class and object concept

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.getEligibility())

    def getStudent(self):
        template = "Hi,{} you are {} years old."
        print(template.format(self.name, self.age))

    def setStudent(self, name, age):
        self.age = age
        self.name = name

    def sample():
        pass

    def getEligibility(self):
        if (self.age >= 18):
            return "Eligible for voting."
        else:
            return "Not eligible for voting."


studentObj = Student("Anin Arafath", 18)
# studentObj.setStudent(name="Anin Arafath", age=18)
studentObj.getStudent()
