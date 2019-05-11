menuList = []
priceList = []
def showBill():
    print("----- My Food -----")
    price = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        price += int(priceList[number])
    print("Total Price : ",price)

while True:
    menuName = input("Enter the  menu : ")
    if(menuName.lower() == "exit" ):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
