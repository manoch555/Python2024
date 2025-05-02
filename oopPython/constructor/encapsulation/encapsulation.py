#Encapsulation
class Employee:
    def __init__(self,name,salary,department):
         
        self._name = name #Protected Attribute 
        self.__salary = salary  #Private Attribute 
        self.__department = department #Private Attribute 
       
    #การสร้าง method
   
    def _show_data(self):
        print("ชื่อพนักงาน = {}".format(self._name))  #Protected method
        print("เงินเดือน = {}".format(self.__salary)) #Private method
        print("ตำแหน่ง = {}".format(self.__department)) #Private method
         
#การสร้าง object
obj1 = Employee("Ploy",40000,"บัญชี")

obj1._name = "Manoch"
#print(obj1._name)
obj1.__salary = 800000
obj1._show_data()



