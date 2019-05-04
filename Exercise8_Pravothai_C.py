print("----------------- Login System -----------------")
UserName = input("USERNAME : ")
PASSWORD = input("PASSWORD : ")
if UserName == 'admin' and PASSWORD == '1234' :
    print("----- !!! WELCOME !!! -----")
    print("----------------- Products List -----------------")
    print(" 1.  Apple        : 100 Baht")
    print(" 2.  Orange       : 80 Baht")
    print(" 3.  Chocolate    : 200 Baht")
    print(" 4.  Pepper       : 100 Baht")
    print(" 5.  Cream        : 100 Baht")
    ProductNumber = int(input("Choose Product Number :"))
    if ProductNumber == 1 :
        price = 100
    if ProductNumber == 2:
        price = 80
    if ProductNumber == 3:
        price = 200
    if ProductNumber == 4:
        price = 100
    if ProductNumber == 5:
        price = 100
    if price != 0 :
        amount = int(input("Input Amount : "))
        sum = price * amount
        print("Total Price  :  ",sum)
        print("----------------- THANK YOU -----------------")




