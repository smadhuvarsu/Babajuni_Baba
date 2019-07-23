class House:
    def __init__(self,address,color,squarefeet,lotSize,bedroom,bathroom,price):
        self.address=address
        self.color=color
        self.squarefeet=squarefeet
        self.lotSize=lotSize
        self.bedroom=bedroom
        self.bathroom=bathroom
        self.price=price
        self.extraCosts=0

    def repaint(self,newColor,paintedBy):

        if (paintedBy.lower()=="self"):
            self.color=newColor
            cost=300+self.squarefeet/4.5
            self.extraCosts+=300+self.squarefeet/4.5
            print("Succesfully painted",self.address,newColor,"for $"+ str(cost))
            self.extraCosts+=cost

        elif(paintedBy=="hire"):
            self.color=newColor
            if(self.squarefeet<1500):
                cost=self.squarefeet*2

            elif(self.squarefeet<3000):
                cost=self.squarefeet

            else:
                cost=4500+(self.squarefeet-3000)/2
            print("Succesfully hired a painter to paint",self.address,newColor,"for $"+str(round(cost,2)))
            self.extraCosts+=cost
        else:
            print("Invalid value for 'paintedBy'..")

    def addBedroom(self,squarefeet):
        if (squarefeet+self.squarefeet>self.lotSize):
            print("You are building on other peoples property!You will be sued!")
            return

        if (squarefeet<=0):
            print("Invalid room size.")
            return
        elif(squarefeet>=1440):
            multiplier=80
        else:
            multiplier=200-(squarefeet/12)

        cost=squarefeet*multiplier
        self.extraCosts+=cost
        print("Succesfully added a new bedroom to",self.address,"for $",str(round(cost,2)))
        self.bedroom+=1
        self.squarefeet+=squarefeet

    def addBathroom(self,squarefeet):
        if (squarefeet+self.squarefeet>self.lotSize):
            print("You are building on other peoples property!You will be sued!")
            return

        if (squarefeet<=0):
            print("Invalid room size.")
            return
        elif(squarefeet>=1440):
            multiplier=80
        else:
            multiplier=200-(squarefeet/12)

        cost=squarefeet*multiplier
        self.extraCosts+=cost+1500
        print("Succesfully added a new bathroom to",self.address,"for $",str(round(cost,2)))
        self.bathroom+=1
        self.squarefeet+=squarefeet

    def addToTheLotSize(self,squarefeet):
        if(squarefeet>self.bedroom+self.bathroom):
            print("You are building on other peoples property or in your own house!You will be sued or your family will kick you!")
            return

        if (squarefeet<=0):
            print("Invalid lot size.")
            return
        elif(squarefeet>=1440):
            multiplier=80
        else:
            multiplier=200-(squarefeet/12)

        cost=squarefeet*multiplier
        self.extraCosts+=cost+1500
        print("Succesfully made the lotsize bigger to",self.address,"for $",str(round(cost,2)))
        self.squarefeet+=squarefeet


    def sell(self,price):
        if(price<1):
            print("You can't sell a house for sell than a dollar! It's not fair(especcialy if you house is the mega mansion bigger than earth!")

        elif(price>10000 and price<100000):
            print("Succesfully sold",self.address,"for $",str(round(price,2)))

        elif(price>100000):
            print("Unsuccesfully sold",self.address,"for $",str(round(price,2)))
        

'''house1=House("7342 Briza Loop(a house)","cream",1400,2000,4,3,400000.0)
house2=House("2051 Cedar Bridge(a house),","white",2900,3500,5,6,900000.0)
house3=House("9784 Luis Alvarez(a humoungous mansion-it's 60009000877776567545676707777888888456765888889999999991234567895430436789058097889019888123456789 sq.mi!),","red",60009000877776567545676707777888888456765888889999999991234567895430436789058097889019888123456789,4555555560000000000000,100000,100000,0.01)
print()
house1.repaint("blue","self")
house2.repaint("red","self")
house3.repaint("rainbow","hire")
print()
house1.addBedroom(89)
house2.addBedroom(56)
house3.addBedroom(234567898765437)
print()
house1.addBathroom(89)
house2.addBathroom(36)
house3.addBathroom(2345678)
print()
house1.addToTheLotSize(6)
house2.addToTheLotSize(8)
house3.addToTheLotSize(23450000000000)
print()
house1.sell(70000)
house2.sell(67000)
house3.sell(10000000000000000000000000000000000000000000000000000000000000000000000)
print()'''

class Neighborhood:
    def __init__(self):
        self.house_list=[]

    def Create_House(self):
        address=input("What is the address of your house:")
        color=input("What color is your house:")
        squarefeet=int(input("How many squarefeet is your house:"))
        lotSize=int(input("How many squarefeet is the lot your house is built on:"))
        bedroom=int(input("How many bedrooms are in your house:"))
        bathroom=int(input("How many bathroooms are in your house:"))
        price=int(input("How much does your house cost:"))

        house=House(address,color,squarefeet,lotSize,bedroom,bathroom,price)
        self.house_list.append(house)

        print("Your house has successfully been created.")

    def View_Houses(self):
        for i in self.house_list:
            print(i.address)

        #the_house=input("Which house do you want to view/interact with(give me the address)NOT a dress! Hahahaha! What a hilarious joke!!:")

        
        '''for i in self.house_list:
            if (the_house == i.address):
                print("1.View House Details)
                print("2.Repaint House")
                print("3.Renovate House")
                print("4.DEMOLISH HOUSE!!(Then I won't have to sue it's owners :( !)")
                print("5.")
                print("6.")
                 print("7.")'''

    def Repaint_House(self):
        for i in self.house_list:
            print(i.address)
            repaint()

    def Sell_House(self):
        print(self.house_list)
        sell=input("Which house do you want to sell:")
        money=int(input("How much money do you want to sell this house for:"))
        print("Congratulations! Your house has been sold to someone that I will sue later! ;)")


    def Choice(self):
        choice=()
        while(choice != 4):

            print()
            print("Hello! Today we are in a neighborhood(that I am going to sue in a couple minutes)! ")
            print("    What do you want to do:")
            print("        1.Create a House")
            print("        2.View a House")
            print("        3.Repaint a House")
            print("        4.Renovate a House")
            print("        5.Sell a House")
            print("        6.Quit")        
            choice=int(input("What do you want to do:"))
            print()

            if choice==1:
                self.Create_House()

            elif choice==2:
                self.View_Houses()

            elif choice==3:
                self.Repaint_House()

            elif choice==4:
                pass

            elif choice==5:
                self.Sell_House()

            elif choice==6:
                pass
            

neighborhood=Neighborhood()
neighborhood.Choice()


#I WILL POST THIS ON NEXCLAP!
#ONCE I AM DONE!
