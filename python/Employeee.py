class Employee(object):
    def __init__(self,name=None,department=None,salary=0.0):
        self.name = name
        self.department=department  
        self.salary=salary
        print("def __init__(self)")

    #def __copy__(self):
    #   return Employee(self.name,self.department,self.salary)

    def show(self):
        print(f"Employee Name={self.name}")
        print(f"Department={self.department}")
        print(f"Salary={self.salary}")
        print("---------------------------------------")


if __name__ == "__main__":
        e1 = Employee()
        e1.show()

        e2 = Employee("Amit", "HR", 45000.0)
        e2.show()

        e3 = e2
        e3.show()

        e3 = e2.__copy__()

        if e3 == e2:
            print("same")
        else:
            print("different")

        print("e2:", id(e2))
        print("e3:", id(e3))
