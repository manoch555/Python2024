#Setter Getter Method
class Employee:
    def __init__(self,name,salary,department):
        #Private Attribute 
        self.__name = name  
        self.__salary = salary  
        self.__department = department 
       
    #การสร้าง method
    #Protected method
    def _show_data(self):
        print("ชื่อพนักงาน = "+self.getname())  
        print("เงินเดือน =",format(self.getsalary())) 
        print("ตำแหน่ง = "+self.getdepartment()) 
        
    #Setter Method   
    def setname(self,newname):
        self.__name = newname
    def setsalary(self,newsalary):
        self.__salary = newsalary 
    def setdepartment(self,newdepartment):
        self.__department = newdepartment    
        
    #Getter Method  
    def getname(self):
        return self.__name      
    def getsalary(self):
        return self.__salary  
    def getdepartment(self):
        return self.__department   
#การสร้าง object
obj1 = Employee("Ploy",40000,"บัญชี")

"""obj1.setname("Manoch")
obj1.setsalary(800000)
obj1.setdepartment("ขาย")"""

obj1._show_data()




