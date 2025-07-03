from datetime import datetime

name=input("Entre your name:")
# lists of items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/kg
Paneer  Rs 90/kg
Boost   Rs 45/kg
'''
price=0
pricelist=[]
# declaratin
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
# rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':90,'boost':45}
option=int(input("for lists of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Entre your items:")
        quantity=int(input("entre your quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entred item is not avoilable")
    else:
        print("you entred wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","jeevan super market",25*"=")
            print(28*"=","wanaparthey")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" " ,plist[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',totalprice)
                print("gst amount",40*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'TotalAmount:','Rs',finalamount)
                print(75*"-")
                print(20*" ","thanks for visiting")
                print(75*"-")





