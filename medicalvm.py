print("Welcome to Medical Vending machine")
print("Products in Medical Vending machine")
def sub_selection1():
    one = int(input("Select the available product:"))
    if(one==1):
        print("Medical first aid kit booklet - Rs.100/-")
        amount2()
    elif(one==2):
        print("Paracetamol - Rs.5/- per tab")
        amount()
    elif(one==3):
        print("Energy drink - Rs.10/-")
        amount1()
    else:
        print("Invalid selection")
def sub_selection2():
    two = int(input("Select the available product:"))
    if(two==1):
        print("Medical first aid kit - Rs.100/-")
        amount2()
    elif(two==2):
        print("Emergency call - Tollfree")
    elif(two==3):
        print("Blood bank call - Tollfree")
    elif(two==4):
        print("Nearest Police station call - Tollfree")
    else:
        print("Invalid selection")
def sub_selection3():
    three = int(input("Select the available product:"))
    if(three==1):
        print("First aid kit booklet - Rs.100/-")
        amount2()
    elif(three==2):
        print("Emergency call - Tollfree")
    elif(three==3):
        print("Antiseptics - Rs.5/- per pack")
        amount()
    elif(three==4):
        print("Cotton - Rs.10/- per pack")
        amount1()
    elif(three==5):
        print("Bandaid - Rs.10/- per pack")
        amount1()
    else:
        print("Invalid selection")
def sub_selection4():
    four = int(input("Select the available product:"))
    if(four==1):
        print("First aid kit - Rs.100/-")
        amount2()
    elif(four==2):
        print("Emergency call - Tollfree")
    elif(four==3):
        print("Vomit Control medicine - Rs.50/-")
        amount3()
    elif(four==4):
        print("Cotton - Rs.10/- per pack")
        amount1()
    else:
        print("Invalid selection")
def sub_selection5():
    five = int(input("Select the available product:"))
    if(five==1):
        print("First aid kit booklet - Rs.100/-")
        amount2()
    elif(five==2):
        print("Emergency call - Tollfree")
    elif(five==3):
        print("Antiseptics - Rs.5/- per pack")
        amount()
    elif(five==4):
        print("Cotton - Rs.10/- per pack")
        amount1()
    else:
        print("Invalid selection")
def amount():
    cost = int(input("Enter the amount Rs.5/-:"))
    if(cost==5):
        print("Payment completed. Please collect your product.")
    else:
        print("Enter Rs.5/-")
        amount()
def amount1():
    cost = int(input("Enter the amount Rs.10/-:"))
    if(cost==10):
        print("Payment completed. Please collect your product.")
    else:
        print("Enter Rs.10/-")
        amount1()
def amount2():
    cost = int(input("Enter the amount Rs.100/-:"))
    if(cost==100):
        print("Payment completed. Please collect your product.")
    else:
        print("Enter Rs.100/-")
        amount2()
def amount3():
    cost = int(input("Enter the amount Rs.50/-:"))
    if(cost==50):
        print("Payment completed. Please collect your product.")
    else:
        print("Enter Rs.50/-")
        amount3()
def products():
    print("List of Symptoms")
    print("1.Fever\n2.Major accident\n3.Minor accident\n4.Vomiting sensation\n5.Insect bites\n")
    option=int(input("Enter your option:"))
    if(option==1):
        print("Available products")
        print("1.Medical first aid kit booklet - Rs.100/-\n2.Paracetamol - Rs.5/-\n3.Energy drink - Rs.10/-\n")
        sub_selection1()
    elif(option==2):
        print("Available products")
        print("1.Medical first aid kit booklet - Rs.100/-\n2.Emergency call - Tollfree\n3.Blood bank call - Tollfree\n4.Nearest Police station call - Tollfree\n")
        sub_selection2()
    elif(option==3):
        print("Available products")
        print("1.Medical first aid kit booklet - Rs.100/-\n2.Emergency call - Tollfree\n3.Antiseptics - Rs.5/-\n4.Cotton - Rs.10/-\n5.Bandaid - Rs.10/-\n")
        sub_selection3()
    elif(option==4):
        print("Available products")
        print("1.Medical first aid kit booklet - Rs.100/-\n2.Emergency call - Tollfree\n3.Vomit control medicine - Rs.50/-\n4.Cotton - Rs.10/-\n")
        sub_selection4()
    elif(option==5):
        print("Available products")
        print("1.Medical first aid kit booklet - Rs.100/-\n2.Emergency call - Tollfree\n3.Antiseptics - Rs.5/-\n4.Cotton - Rs.10/-\n")
        sub_selection5()
    else:
        print("Invalid option")
products()
        
        
        
        
    
    
