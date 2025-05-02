#Super
class Employee:
    #class variable
    __minsalary = 12000
    maxsalary = 50000
    companyname = "บริษัท XYZ จำกัด"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showdata(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

class Accounting(Employee):
    __departmentname = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)
        super()._showdata()
        
class Programmer(Employee):
    __departmentname = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)
        super()._showdata()
class Sale(Employee):
    __departmentname = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)        
        super()._showdata()
account = Accounting("Noch",50000)

programmer = Programmer("Ploy",40000)

sale = Sale("Kung",30000)

