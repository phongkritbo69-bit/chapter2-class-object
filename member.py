class Member:
    def __init__(self, name, visits, months):
        self.name = name 
        self.visits = visits
        self.months = months

    def is_at_risk(self):
        return self.visits < 4 and self.months > 6 

m1 = Member("phongkrit boulowpetch", 2, 10)
print("ชื่อสมาชิก :", m1.name)
print("เสี่ยงเลิกใช้บริการ", m1.is_at_risk())

m2 = Member("สมหญิง กิ่งไม้", 5, 10)
print("ชื่อสมาชิก :", m2.name)
print("เสี่ยงเลิกใช้บริการ", m2.is_at_risk())

m3 = Member("อนิทุน ชุนวีระการณ์", 1, 10)
print("ชื่อสมาชิก :", m3.name)
print("เสี่ยงเลิกใช้บริการ", m3.is_at_risk())
