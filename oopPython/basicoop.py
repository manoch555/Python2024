#การสร้าง class
class Employee:
    
    #การสร้าง method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary 
        self.department = department
       
    def show_data(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))    
#การสร้าง object
obj1 = Employee()
obj2 = Employee()
#การเรียกใช้งาน method
obj1.detail("Manoch",50000,"โปรแกรมเมอร์")
obj2.detail("Ploy",40000,"บัญชี")  
obj1.show_data() 
obj2.show_data() 