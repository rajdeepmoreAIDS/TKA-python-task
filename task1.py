
def electronicGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


def fashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


def foodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalbill(a, b, c, d, e):
    electronics = electronicGST(a, b)
    fashion = fashionGST(c, d)
    food = foodGST(e)
    return electronics + fashion + food


def discountedbill(a, b, c, d, e):
    total = totalbill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount
    return final_amount

a = 100
b = 100
c = 100
d = 100
e = 100

electronics =electronicGST(a, b)
fashion = fashionGST(c, d)
food = foodGST(e)
total = totalbill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = discountedbill(a, b, c, d, e)

print("Final shop billing ")
print("Electronics with GST: rs. ", electronics);
print("fashion with GST:     rs. ", fashion);
print("food with GST:        rs. ", food);
print(" ")
print("Final payable amount")
print("Total amount with GST: rs. ", total);
print("Discount of 20% :      rs. ", discount);
print("Final payable amount:  rs. ", final_amount);
