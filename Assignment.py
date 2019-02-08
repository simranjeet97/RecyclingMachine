class RecycleMachine:
    def __init__(self,item,option,bal,can,bott, paper,n_item,money):
        self.item = item
        self.option = option
        self.bal = bal
        self.can = can
        self.bott = bott
        self.paper = paper
        self.n_item = n_item
        self.money = money
        
    def stop(self):
        print("-------Reciept-------")
        l = self.item.split(" ")
        print(l[1]," ",l[0],"  --- > ",l[2])
        print(l[4]," ",l[3]," --- > ",l[5])
        print(l[7]," ",l[6]," --- > ",l[8])
        print("Total Balance is -", self.bal)
        print("Thank You for using ItsExceptional Machine")
		self.item = " "
        
    def accept_product(self):
        print("Balance $",self.bal,"\n"
              "Please Select a Prodcut : \n"
              "1. Can \n"
              "2. Bottle \n"
              "3. Paper \n"
              "4. STOP \n")
        self.option = input("Enter Product - ")
       
        
    def select_product(self):

        if self.option == "stop":
            self.stop()
        
        elif self.option == "can" or "bottle" or "paper":
            self.item += self.option
            self.n_item = int(input("How Many {0} do you have ? : ".format(self.option)))
            
            print("Please Place {0},{1} into Machine.".format(self.n_item,self.option))
            for i in range(self.n_item):
                print("{0} Accepted".format(self.option))

            if self.option == "can":
                print("You Added {0} {1}(s) for ".format(self.n_item,self.option),"$",2)
                self.money=2*self.n_item
                self.item +=" "+str(self.n_item)+" "+str(self.money)+" "
                
            elif self.option == "bottle":
                print("You Added {0} {1}(s) for ".format(self.n_item,self.option),"$",3)
                self.money=3*self.n_item
                self.item +=" "+str(self.n_item)+" "+str(self.money)+" " 
                
            elif self.option == "paper":
                print("You Added {0} {1}(s) for ".format(self.n_item,self.option),"$",5)
                self.money=5*self.n_item
                self.item +=" "+str(self.n_item)+" "+str(self.money)+" "
                
            print("You Have ${0}.".format(self.money))

            self.bal += self.money
            print("Total Balance is - ",self.bal)
                

obj2 = RecycleMachine("","",0,0,0,0,0,0)

while True:

    obj2.accept_product()
    obj2.select_product()
