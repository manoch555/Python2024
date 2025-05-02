import qrcode

# ข้อความหรือข้อมูลที่ต้องการสร้าง QR Code
data = "https://manochpro-90437.web.app/"

# สร้าง QR Code ด้วยการตั้งค่าพื้นฐาน
qr = qrcode.make(data)

# บันทึก QR Code เป็นไฟล์ภาพ
qr.save("qrcode.png")

print("สร้าง QR Code สำเร็จ! ไฟล์ถูกบันทึกเป็น qrcode.png")
