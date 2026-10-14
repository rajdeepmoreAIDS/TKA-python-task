
def calculateconsultation():
    total = a
    services = total * 5/100
    return total + services

def calculatetestcharges():
    total = b 
    tax = total * 12/100
    return total + tax

def calculatemedicinecharges():
    total = c
    tax = total * 5/100
    return total + tax

a = 1000
b = 2000
c = 1000

def calculatetotal_bill():
    total = consultation + testcharges + medicinecharges
    return total 

def calculatefinal_bill():
    total = consultation + testcharges + medicinecharges
    discount = total * 10/100
    return total - discount

def cal_discount():
    discount = totalbill - final_payable_amt
    return discount

consultation = calculateconsultation()
testcharges = calculatetestcharges()
medicinecharges = calculatemedicinecharges()
totalbill = calculatetotal_bill()
final_payable_amt = calculatefinal_bill()
discount = cal_discount()

print("the fees of consultant is ", consultation)
print("the fees of medical tests are ", testcharges)
print("the medicines cost is ", medicinecharges)
print("the total amount is ",totalbill)
print('the discount is', discount)
print("the final payable amount is ",final_payable_amt)