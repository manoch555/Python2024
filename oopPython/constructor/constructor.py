#การสร้าง constructor
class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary 
        self.department = department
        
    #การสร้าง method
    def show_data(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))  
         
    # Destructor   
    def __del__(self):
        print("Call Destructor") 
         
#การสร้าง object
obj1 = Employee("Manoch",50000,"โปรแกรมเมอร์")
obj2 = Employee("Ploy",40000,"บัญชี")
obj3 = Employee("Kung",30000,"ขาย")
#การเรียกใช้งาน method
obj1.show_data()
obj2.show_data()
obj3.show_data()

#การหา Object อยู่ใน Class อะไร
print(isinstance(obj1,Employee))
print(dir(obj1))
print(obj1.__class__)