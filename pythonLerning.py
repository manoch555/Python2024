




#match
'''
service = input("กรุณาป้อน(1-3)")
match service:  
    case "1":print("ser1")
    case "2":print("ser2")
    case "3":print("ser3")
    case "":print("not ser")
'''
    
    
#while Loop
'''
counter  = 0
while counter<10:
    counter+=1  
   
print("--------------------------------")   
    
#for Loop 1
for counter1 in range(4): #0-3
    print(counter1)
   
print("--------------------------------")     
     
#for Loop 2
for counter2 in range(2,6): #2-5
    print(counter2)  
   
print("--------------------------------")     
    
#for Loop 3
for counter3 in range(1,11,2):
    print(counter3)   
 
print("--------------------------------")  

#break
for counter1 in range(1,11): #0-3
    if counter1==6:
        break
    print(counter1)
   
print("-------------------------------") 

#continue 
for counter1 in range(1,11): #0-3
    if counter1==6:
        continue
    print(counter1)
   
print("-------------------------------") 

#แม่สูตรคูณ
number = int(input("ป้อนแม่สูตรคูณ:"))                    
for i in range(1,13):
    print(number,"x",i,"=",number*i)
    
print("-------------------------------")    
 
# หาผลรวมตัวเลข 5 จำนวน
total = 0
for i in range(1,6):
    number1 = int(input("ลำดับที่ "+str(i)+" :"))
    total+=number1
print("ผลรวม = ",total)

print("-------------------------------")  

# หาผลรวมตัวเลข ไม่จำกัดจำนวน
total=0
while True:
    number2 = int(input("ป้อนตัวเลข:"))
    if number2 <=0:
        break
    total+=number2
print("ผลรวม = ",total)

print("-------------------------------")

# Nested Loop
for i in range(2):
    print("รอบที่ ",i)
    for j in range(3):
        print(j)
print("-------------------------------")  

'''


                  
'''
# แม่สูตรคูณ แบบกำหนดช่วง
start =int(input("ป้อนแม่สูตรคูณเริ่มต้น "))
end =int(input("ป้อนแม่สูตรคูณสุดท้าย "))

for number4 in range(start,end+1):
    print("---------------------")
    print("  สูตรคูณแม่",number4)
    
    for i in range(1,13):
        print(number4,"x",i,"=",number4*i)
print("------------------------------------") 

'''


#การสร้าง string หลายบรรทัด
address = """
ที่อยู่ : 36 ซอย จุฬาฯ 14 
แขวงวังใหม่ เขตปทุมวัน กรุงเทพฯ
ร้านเปิดบริการ : 16.00 - 21.00 น. (หยุดวันจันทร์)
"""
print(address) 

# f string
year = 2513
message = f"เกิดเมื่อปี พ.ศ. {year}"  
age = f"อายุ {2567-year} ปี"
salary = 50000
mySalary = f"เงินเดือน = {salary:.2f} บาท"
print(message) 
print(age)  
print(mySalary) 

#ดึงตัวอักษรมาใช้
text = "ManochPongpitakkul"
'''for c in text: 
    print(c)'''

'''
#function การจัดการสตริง                                                     
text1 = "ManochPongpitakkul"
print(text1.upper())

text2 = "MANOCHPONGPITAKKUL" 
print(text2.lower())


#function การตรวจสอบคำขึ้นต้น-ลงท้าย ของข้อความ
text3 = "นาย มาโนช พงษ์พิทักษ์กุล"
print(text3.startswith("นาย"))
print(text3.endswith("กุล"))

#function การค้นหาคำ
text4 = "ManochPongpitakkul"
print(text4.find("Pong"))

#function การค้นหาคำซ้ำ
text5= "ManochPongpitakkul"
print(text5.count("o"))

#function การแทนที่คำ
text6= "ManochPongpitakkul"
print(text6.replace("Manoch","Ploy"))

#function การลบช่องว่างซ้าย-ขวา
text7= "  ManochPongpitakkul  "
print(len(text7))
text7= "  ManochPongpitakkul  ".strip()
print(len(text7))

#function การจัดรูปแบบ string
text8 = "ฉันชื่อ {0} อายุ {1} ปี".format("Noch",54)
print(text8)


#function list ()
num2 =[1,2,3,4,5,6,6]
num2.append(0)  #เพิ่มสมาชิก1ตัวต่อท้าย
num2.extend([7,8,9]) #เพิ่มสมาชิกหลายตัวต่อท้าย
num2.insert(1,11) #แทรกสมาชิกตามตำแหน่ง
num2.sort() #เรียงน้อย=>มาก
num2.reverse() #เรียงมาก=>น้อย
num2.count(6) #นับที่ซ้ำ
num2.remove(1) #ลบทีละตัว
num2.clear() #ลบหมด
print(num2)


# tuple
num3 = (1,2,3)
(name,price,stock) = num3
print(name)
print(price)
print(stock)
print(num3)
print(type(num3))
print(len(num3))

# Dictionary
colors = {
    "red":"แดง",
    "green":"เขียว",
    "blue":"น้ำเงิน"
}
print(colors["red"])



         ###  Part 2  ###
 #Literal Pattern
service = None
match service:
    case 1: 
        print("ฝากเงิน")
    case 2: 
        print("ถอนเงิน")
    case 3: 
        print("เช็คยอดคงเหลือ")     
    case None: 
        print("ไม่ถูกต้อง")
        
  #Wildcard Pattern 
service = 5
match service:
    case 1: 
        print("ฝากเงิน")
    case 2: 
        print("ถอนเงิน")
    case 3: 
        print("เช็คยอดคงเหลือ")     
    case _: 
        print("ป้อนข้อมูลไม่ถูกต้อง")   


 #Capture Pattern
service = 10
match service:
    case 1: 
        print("ฝากเงิน")
    case 2: 
        print("ถอนเงิน")
    case 3: 
        print("เช็คยอดคงเหลือ")     
    case service: 
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง")   

  # Guard Filter
# 100 = สอบได้คะแนนเต็ม , 50-99 = ผ่านเกณฑ์การสอบวัดผล , <50 = ไม่ผ่านเกณฑ์
score = int(input("ป้อนคะแนนสอบของคุณ 0-100 :"))
print("คะแนนสอบของคุณคือ ", score) 
match score:
    case score if score<0 or score>100:
        print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนคะแนนสอบของคุณอีกครั้ง")
    case 100:
        print("สอบได้คะแนนเต็ม ")
    case score if score >=50 and score < 100 :
        print("ผ่านเกณฑ์การสอบวัดผล ")  
    case _ :
        print("ไม่ผ่านเกณฑ์")  
        
  #  #Or Pattern     
data = input("ป้อนคำนำหน้าชื่อของคุณ")   
match data:
    case "เด็กชาย" | "นาย":       
        print("เพศชาย")
    case "เด็กหญิง" | "นาง" | "นางสาว":       
        print("เพศหญิง")   
    case _ :
        print("ไม่พบข้อมูล")     
        
  #Sequence Pattern   
data = [1,2] 
match data:
    case []:
        print("ไม่มีข้อมูล")     
    case [1,2]:
        print("มีข้อมูล2ตัว")     
    case [1,2,3]:
        print("มีข้อมูล3ตัว") 
  
  '''
           
  #Mapping Pattern  
cutomers =[
    {"name":"ก้อง","type":"general"},
    {"name":"โจ้","type":"member"},
    {"name":"แนน","type":"general"}   
]  
id=int(input("ป้อนรหัสลูกค้า :"))
print(f"สวัสดีลูกค้ารหัส {id} :{cutomers[id]["name"]})")

match cutomers[id]:
    case {"type":"member"}:
        print("คุณเป็นสมาชิก ได้รับส่วนลด50%")  
    case _:
         print("ไม่ได้รับส่วนลด")    
  
  
        ######Function#########
  #------1Function แบบปกติ----------
  
    #การสร้าง Function
def say_hello():
    print("สวัสดีครับ")  
    
def show_table():
    print("--------------------")   
    for i in range(1,13):
        print(f"2 x {i} = {2*i}")
        
    #การเรียกใช้ Function
say_hello()    
show_table()

    
  #--------2Function แบบมีพารามิเตอร์---------

     #การสร้าง Function
def say_hello(time,userName,age):
    print("สวัสดี ",time,userName)    
    print("คุณมีอายุ " ,age," ปี") 
    
def saveEmployee(name,department,salary):
    print(f"ชื่อ {name} แผนก {department}")    
    print(f"เงินเดื่อน {salary} บาท")
    
def show_table(num):
    print(f"-------แม่ {num} -------------")   
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")
            
     #การเรียกใช้ Function
myTime= "ตอนเช้า"
say_hello(myTime,"คุณโนช",55) 
saveEmployee("Noch","IT",50000)
show_table(5) 


#--------3Function แบบกำหนดค่าเริ่มต้น --------   

    #การสร้าง Function
def saveEmployee(name,department,salary=30000): #salary กำหนดค่าเริ่มต้น
    print(f"ชื่อ {name} แผนก {department}")    
    print(f"เงินเดื่อน {salary} บาท")
 
    #การเรียกใช้ Function
saveEmployee("Noch","IT")
saveEmployee("Ploy","IT",40000)


#--------การใช้ *args / **kwargs --------
    #การสร้าง Function
def saveEmployee(*args): #*args  tuple
    print(f"ชื่อ {args[0]} แผนก {args[1]}")    
    print(f"เงินเดื่อน {args[2]} บาท")
 
    #การเรียกใช้ Function
saveEmployee("Noch","IT",50000)
saveEmployee("Ploy","IT",40000)

   #การสร้าง Function
def saveEmployee(**kwargs): #**kwargs  dictionary
    print(f"ชื่อ {kwargs["name"]} แผนก {kwargs["department"]}")    
    print(f"เงินเดื่อน {kwargs["salary"]} บาท")
 
    #การเรียกใช้ Function
saveEmployee(name="Noch",department="IT",salary=50000)
saveEmployee(name="Ploy",department="sale",salary=30000)


#--------4Function แบบมีค่าส่งกลับ --------  

    #การสร้าง Function 
def getCapital():
    return "กรุงเทพมหานคร"  
 
myCapital = getCapital() 
print("เมืองหลวงของฉันคือ ",myCapital)
    
    
 #--------5Function แบบรับและส่งค่า --------   
def checkNumber(number):
    if number%2==0:
        return "เลขคู่"
    else: 
        return "เลขคี่"
result = checkNumber(13)        
print (result)        
      
def summation(*data):
    total=0
    for item in data:
        total+=item
    return total
print(summation(10,20,30))


 #--------Lambda Function --> ไม่ต้องกำหนดชื่อ Function  -------- 
result = lambda base,n : base**n 
print("ผลลัพธ์คือของเลขยกกำลัง ",result(2,3))


    










