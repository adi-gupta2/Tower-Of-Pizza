import math
import random
import sys
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="hello",database="tower_of_pizza")
cur = mydb.cursor()

p='''    __________					        __________
   (__________)		        		       (__________)
    \:< & (;)/					    	\:< & (;)/
     \^? - +/		    VEG PIZZA    	         \^? - +/
      \=! ;/		                	          \=! ;/
       \+=/					    	   \+=/
        \/				    		    \/'''

np='''     __________						 __________
    (__________)	       		                (__________)
     \:< & (;)/					    	 \:< & (;)/
      \^? - +/		NON-VEG PIZZA	    		  \^? - +/
       \=! ;/		        	        	   \=! ;/
	\+=/				    		    \+=/
         \/			    			     \/'''


d='''       @  						        @
      ( )  /						       ( )  /
     (   )/                     DESERTS                       (   )/
    (____0)						     (____0)
    |_____| 						     |_____|
      | |						       | |
     [___]					    	      [___]'''


b='''           _                                                   _
          /	                                              /
     |___/_|                                             |___/_|
     | []  |                BEVERAGES                    | []  |
     |   []|                                             |   []|
     |_____|                                             |_____| '''

sid='''            /                                                   /
     ______/                                             ______/
    |CHEESY|	            SIDES                       |CHEESY|           
    | DIPS |                                            | DIPS |
    |______|                                            |______|   '''

sna='''        _____                                            _____
       |    /                                            \    |
       |   /}              SNACKS                        {\   |
       |  /}                                              {\  |
       | /)                                                {\ |
       |/                                                    \|   '''

vegpizza=[['Margherita',200,0],['Cheese and Corn',305,0],['Fresh veggie',335,0],['Paneer makhani',395,0],['Cheese and Tomato',305,0],['Peppy Paneer',300,0]]
nonvegpizza=[['Pepper Barbecue Chicken',335,0],['Chicken Sausage',350,0],['PeriPeri Chicken',400,0],['Chicken Golden Delight',430,0]]
beverages = [['Coke', 77, 0], ['Fanta', 77, 0], ['Sprite', 77, 0], ['Thumbs up', 77, 0], ['Chocolate shake', 148, 0],['Strawberry shake', 148, 0]]
sides = [['Garlic Bread Sticks', 99, 0], ['Cheesy Jalapeno dips', 25, 0], ['Cheesy dip', 25, 0]]
desserts= [['Bsflurry Choco Crunch', 79, 0], ['Black Forest Flurry', 134, 0],['Red Velvet Cake',60,0],['Soft Serve Strawberry', 85, 0]]
snacks=[['Aloo Veg Patty',30,0],['Veg Spring Roll',60,0],['Corn spinach roll',70,0],['Chilli Paneer roll',50,0],['Plain Sandwich',80,0]]

size=[['Small',30,0],['Regular',55,0],['Large',60,0]]
crusts=[['Cheese Burst','Oodles of yummy liquid cheese filled inside.',0],['Classic Hand Tossed','Crisp on outside, soft & light inside.',0],['Wheat Thin Crust','The healthier and delicious light wheat thin crust ',0],['New Hand Tossed','Fresh. Hand Stretched. Classic.',0],['Stuffed Crust','Stuffed with the best mozzarella fingerlicking cheese',0]] 
cheese=[['Single layer',60,0],['Double layer',75,0],['Molten Mozzarella Delight',80,0]]
toppings=[['Green Capsicum',15,0],['Onion',17,0],['Tomato',13,0],['Paneer',20,0],['Corn',20,0],['Chicken Sausage',30,0],['Mushroom',15,0],['Mozzarella',35,0],['Pepper Barbeque Chicken',40,0],['Red Paprika',7,0],['Jalapeno',15,0],['Olives',8,0],['Smoked Chicken',40,0],['Red Capsicum',15,0]]

menu=['PIZZA','DESSERTS','BEVERAGES','SNACKS','SIDES']
useme2=['CUSTOMER RECORDS','VEGPIZZA','NONVEGPIZZA','DESSERTS','BEVERAGES','SNACKS','SIDES']
useme=['VEGPIZZA','NONVEGPIZZA','DESSERTS','BEVERAGES','SNACKS','SIDES']
list_menu=[vegpizza,nonvegpizza,desserts,beverages,snacks,sides]
main_list=["PLACE AN ORDER","CUSTOM PIZZA","UPDATE AN ORDER","VIEW STATISTICS","DELETE AN ORDER","ABOUT US","DROP US A SUGGESTION","EXIT"]
orders =[size,crusts,cheese,toppings]
headings =['SIZE','CRUSTS','CHEESE','TOPPINGS']
delimen = ["Mr. Raju","Mr. Suresh","Mr. Ramesh","Mr. Sunil","Mr. Rahim","Mr. Amir"]
shape=[p,d,b,sna,sid]

def select_menu(menu,num):
    for i in menu:
        print(str(menu.index(i)+1)+'.',i)
    print('\n')
    global main
    main = input('Enter your choice :')
    main = correction(main,1,num)

def remove(string): 
    return string.replace(" ", "")

def string(y):
    for r in y:
        if not y:
            y=input("Wrong data type entered, please type again :")
            return string(y) 
        elif r.isalpha() or r.isspace():
            continue
        else:
            y=input("Wrong data type entered, please type again :")
            return string(y) 
    return y

def checking():
    global ing
    ing=0
    for k in list_menu:
        for j in k:
            if j[2] != 0:
                ng=1
                break
            else:
                ng=0
    for i in toppings:
        if i[2]==1:
            g=1
            break
        else:
            g=0
    ing = ng or g
    return ing

def quant():
    global brk
    brk = 0
    c = input('Enter your choice :')
    choice = correction(c,1,len(i))
    i[choice-1][2] = 1
    print('To continue, PRESS any key')
    ext = input('For exiting, PRESS 0 :',)
    print('\n')
    if ext == '0':
        for j in orders:
            for p in j:
                p[2]=0
            brk = 1
            break
        
def correction(cho,start,end):
    cho = cho.strip()
    if cho.isdigit():
        ho = int(cho)
        if ho <= end and ho >= start :
            return ho
        else:
            v=input("Sorry Invalid Input please type again :")
            return correction(v,start,end)
    else:
        v=input("Wrong data type entered, please type again :")
        return correction(v,start,end)

def for_ordering():
    print('PRESS any key to order something else:')
    global opt
    opt = input('PRESS 0 to exit :')
    print('\n')
    

def order(u):
    for i in u:
        j = len(u)
        print(u.index(i)+1,'.',i[0],'(Rs - ',i[1],')',sep='')
    choice = input('Enter your choice :')
    choice = correction(choice,1,j)
    quantity = input("Enter quantity :")
    quantity = correction(quantity,1,50)
    if main == 1:
        if pi == 1:
            list_menu[0][choice-1][2] += quantity
        elif pi == 2:
            list_menu[1][choice-1][2] += quantity
    else:
        list_menu[main][choice-1][2] += quantity
    for_ordering()
    if opt != '0':
        select_menu(menu,5)
        
def update():
        order=input("Please Enter your order number (xxxxx):")
        correction(order,27878,99999)
        try:
            cur.execute('select OrderNo,CustomerName,PhoneNo from personal where orderno={}'.format(order))
            f = cur.fetchall()
            if not f:
                print("Order Doesn't Exist\n")                
                return                
        except:
            print("Order Doesn't Exist\n")
            return
        print("USERS DETAILS")
        for i in f :
            print("Order No:",i[0],'\t',"Name:",i[1],'\t',"Phone No:",i[2])
        print('\n')         
        
        while True:
            sno=0
            orders=[]
            print(" FINAL ORDER" )
            for h in range (0,len(list_menu)):
                for i in list_menu[h]:
                    u=remove(i[0])
                    edit='select sum({}) from {} where OrderNo={}'.format(u,useme[h],order)
                    d=cur.execute(edit)
                    s=cur.fetchone()
                    if s!=(0,) and s!=(None,):
                        for x in s:
                            sno+=1                        
                            print(sno,".",i[0],":",x,"*",i[1],"= Rs.",x*i[1])
                            lol=[useme[h],u]
                            orders.append(lol)
            print("\n")        
            print('Please confirm order:')
            print('1. If no changes ')
            print('2. To update quantity of an item')
            print('3. To delete an item')
            edt=input('Please Enter your choice :')
            edt=correction(edt,1,3)
        
            if edt==1:
                print('\n')
                break
            elif edt==2:            
                g=int(input("Enter Serial No. to be updated :"))
                b=int(input("Enter new quantity :"))
                table=orders[g-1][0]
                upp=orders[g-1][1]
                cur.execute("update {} set {}={} where OrderNo={}".format(table,upp,b,order))
                mydb.commit()             
            else:            
                b=int(input("Enter Serial No. to be deleted :"))
                table=orders[b-1][0]
                upp=orders[b-1][1]
                cur.execute("update {} set {}=0 where orderno={}".format(table,upp,order))
                mydb.commit()
                
            a=input('Enter 0 to Exit, Press any key to stay :')
            if a=='0':
                break
    
   
def stats():
    print('\n')
    print('Username : Admin')
    passw= input('Enter Admin Password :')
    if passw.strip()=='Admin':
        None
    else:
        print('Wrong Password, Reverting to Main Menu\n')
        start()
    while True:
        print('\n')
        print('Please choose the category whose statistics you want to view')
        select_menu(useme2,7)
        if main==1:
            cur.execute('select orderno,customername,phoneno,address,billamount from personal;')
            q=cur.fetchall()
            print('+','-~'*35,'+',sep='')
            print('|','OrderNo.'.rjust(7),'Customer Name'.rjust(16),'Phone No.'.rjust(11),'Address'.rjust(21),'Amount'.rjust(8),'|')
            print('+','-~'*35,'+',sep='')            
            for k in q:
                if len(k[3])>20:
                    pop=k[3].split()
                    lsd=pop[len(pop)-1]
                else:
                    lsd=k[3]
                print('|',str(k[0]).rjust(7),k[1].rjust(17),str(k[2]).rjust(11),lsd.rjust(21),str(k[4]).rjust(8),'|')
            print('+','-~'*35,'+',sep='')
        else:
            h=list_menu[main-2]
            qe=useme2[main-1]
            ejd='Sales'
            print('+','-'*28,'+','-'*10,'+',sep='')
            print('|','Item Name'.rjust(26),'|',ejd.rjust(8),'|')
            print('+','-'*28,'+','-'*10,'+',sep='')
            for i in h:
                u=remove(i[0])
                st='select sum({}) from {}'.format(u,qe)
                cur.execute(st)
                f=cur.fetchone()        
                for l in f:
                    ans=str(l)
                    print('|',i[0].rjust(26),'|',str(ans).rjust(8),'|')
                    break
            print('+','-'*28,'+','-'*10,'+',sep='')
        print('\n')
        a=input('Enter 0 to Exit, Press any key to stay :')
        if a=='0':
            break
    print('\n')


def custorder():
    for v in range(4):
        global i
        i = orders[v]
        p = headings[v]
        if v == 1:
            print(p)
            for k in i:
                print(i.index(k)+1,'. ',k[0],sep='')
                print('  ',k[1])
            quant()
            if brk==1:
                break 
        elif v == 3:
            ans=1
            m=0
            print(p)
            for k in i :
                print(i.index(k)+1,'. ',k[0],'(Rs - ',k[1],')',sep='')
            while True:
                m+=1
                choice = input('Enter ingrediant no :')
                choice = correction(choice,1,14)
                i[choice-1][2] = 1
                print('PRESS any key to add more ingrediants:')
                ans=input('PRESS 0 to exit:')
                if ans == '0':
                    break
        else:
            print(p)
            for k in i:
                print((i.index(k))+1,'. ',k[0],'(Rs - ',k[1],')',sep='')
            quant()
            if brk==1:
                break
    if checking():
        last=input('Proceed to pay: PRESS 1, Proceed to MAIN MENU: PRESS 2 :')
        print('\n')
        last=correction(last,1,2)
        if last == 1:
                 bill()
        else:
            start()
            
def confirm():
    while True:
        global ping
        ping=0
        sno = 0
        conf=[]
        print('FINAL ORDER')
        for k in list_menu:
            for j in k:
                if j[2] != 0:
                    ping=1
                    sno+=1
                    print(str(sno)+'.',j[0], ' : ', j[1], '*', j[2], "=  Rs", j[2] * j[1])
                    lis = [sno,list_menu.index(k),k.index(j)]
                    conf.append(lis)
                else:
                    continue
                
        for i in toppings:
            if i[2]==1:
                ping=1
                sno+=1
                print(sno,'.',' Custom Ordered Pizza',sep='')
                for j in range(4):
                    print('\t',headings[j],':')
                    for u in orders[j]:
                        if u[2] != 0:
                            print('\t','\t',u[0])
                break
        print('Please confirm order')
        print('1. If no changes ')
        print('2. To delete an item')
        print('3. To cancel your entire order')
        edt=input('Please Enter your choice :')
        edt=correction(edt,1,3)
        if edt ==1:
            break 
        if edt == 2 and ping==1:
            dele = input('Enter serial number of order to be deleted :')
            correction(dele,1,sno)
            dele = int(dele)
            print('\n')
            if len(conf)==1 and size[1][2]==0 and size[0][2]==0 and size[2][2]==0:
                    kool=input('Do you want to cancel your order ? Press 1 (YES), Press 2 (NO):')
                    kool=correction(kool,1,2)
                    if kool==1:
                        for k in list_menu:
                            for j in k:
                                j[2] = 0
                        for j in orders:
                            for c in j:
                                c[2]= 0
                        ping=0
                        return
                        
            else:              
                for k in conf:                
                    if k[0]==dele:
                        list_menu[k[1]][k[2]][2]=0
                    elif sno==dele:
                        for p in orders:
                            for q in p:
                                q[2]=0                
                
        elif edt==3:
            kool=input('Do you want to cancel your order ? Press 1 (YES), Press 2 (NO):')
            kool=correction(kool,1,2)
            if kool==1:
                for k in list_menu:
                    for j in k:
                        j[2] = 0
                for j in orders:
                    for c in j:
                        c[2]= 0
                ping=0
                return
            else:
                return
        else:
            ping=0
            return 
                 


def bill():
    print('\n')
    deli = input('''PRESS 1: Home delivery:  PRESS 2: Pickup :''')
    deli = correction(deli,1,2)
    if deli == 1:
        sdeli = 'H'
        address = input("Enter your address please :")
        for i in address:                                                  
            while i.isalnum() == "False":
                print('Sorry invalid address, type again:')
                address = input('Please enter your address again :')
            else:
                print("THANKS! Your order is getting prepared.")
                break
    
    else:
        sdeli = "P"
        address = 'None'
    coupons=input('Do you want to use your coupon ? (PRESS 1: Yes PRESS 2: No) :')
    coco=correction(coupons,1,2) #USING COUPON
    print('\n')
    confirm()
    if ping==0:
        print('No order placed, Reverting to main menu','\n')
        return
    cur.execute("select * from personal")
    s = cur.fetchall()
    if s:
        prevord = s[-1][0]
        ordno = prevord+1        
    else:
        ordno=27878
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    a=str(dt_string)
    eid='89198BS'  
    for i in range(2):
        print('\n')
        billu='''-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
                                  TOWER OF PIZZA         
                                Serving since 1987
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~'''
        print(billu)
        print(a)
        print("Order number : ",ordno,"Employee ID :".rjust(40), eid.rjust(7))
        print("Name :", name)                        #FINAL BILL FORMAT
        print("Phone Number :", phone)
        total = 0
        time = 5
        prtbill=[]
        print('\n')
        
        for k in list_menu:
            for j in k:
                if j[2] != 0:
                    print(j[0].rjust(23),':'.rjust(2), str(j[1]).rjust(4), ' * ', str(j[2]).rjust(2),'='.rjust(3), "Rs".rjust(4), str(j[2] * j[1]).rjust(5))
                    total += j[2]*j[1]
                    time += j[2]*1
                else:
                    continue
        
        tot = 0
        for v in range(4):
            for j in orders[v]:
                if j[2] != 0:
                    if v == 1:
                        tot += 40
                    else:
                        tot += j[2]*j[1]
                else:
                    continue
                
        if tot!= 0:
            time += 10
            total+=tot
            c='CUSTOM MADE PIZZA :'
            print(c)
            prtbill.append(c)        
            for j in range(4):
                    for u in orders[j]:
                        if u[2] != 0:
                            if j==1:
                                if len(u[0])>11:
                                    pop=u[0].split()
                                    lsd=pop[len(pop)-1]
                                else:
                                    lsd=u[0]
                                print(headings[j].rjust(23),':'.rjust(2),lsd.rjust(11),'='.rjust(3), "Rs".rjust(4), '40'.rjust(5))
                            else:
                                if len(u[0])>11:
                                    pop=u[0].split()
                                    lsd=pop[len(pop)-1]
                                else:
                                    lsd=u[0]
                                print(headings[j].rjust(23),':'.rjust(2),lsd.rjust(11),'='.rjust(3), "Rs".rjust(4), str(u[1]).rjust(5))
            print(' '*8,'-'*45)
        total = total + tot
        if coco==1:
            if x == 1:
                l=total-100
                if l<0:
                    l=0
                print('Coupon Discount'.rjust(23),':'.rjust(2),str(total).rjust(4),' - 100   =   Rs',str(l).rjust(5))        #USING COUPON DISCOUNTS
                total = l 
            elif x == 2:
                l=total-200
                if l<0:
                    l=0
                print('Coupon Discount'.rjust(23),':'.rjust(2),str(total).rjust(4),' - 200   =   Rs',str(l).rjust(5))
                total = l
            elif x == 3:
                print('FREE Large Sprite'.rjust(23),':'.rjust(2),'1'.rjust(4), ' *   0   =   Rs     0')
            elif x == 5:
                print('FREE Chocolate Pudding'.rjust(23),':'.rjust(2), '1'.rjust(4), ' *   0   =   Rs     0')
        gst = math.ceil(total/20)
        if total<0:
            gst = 0
            total = 0
        jlk = random.randint(0,5)
        print('GST(5%)'.rjust(23),':'.rjust(2),'0.05  *',str(total).rjust(4),'='.rjust(2),'Rs'.rjust(4),str(gst).rjust(5))    #GST AND EXTRA TAX COSTS
        print('FINAL AMOUNT'.rjust(23),':'.rjust(2),'=   Rs'.rjust(20),str(gst+total).rjust(5),'\n')
        print('Your order will be served in :',time,'minutes')         #TIME CALCULATION FOR ORDER
        if deli==1: 
            man = delimen[jlk]
            print('Your order will be delivered by',delimen[jlk])
        else:
            man = 'None'
        print('WE HOPE YOU HAVE A GREAT MEAL')
        print('-~'*40)
        print('Toodles. Lots of love till we meet next <3')       
        if i==0:
            print('YOUR BILL HAS BEEN SAVED ON YOUR DEVICE.')
            sys.stdout=open('TowerOfPizzaBill.txt','w')            
    

    sname="insert into personal(orderno,customername,phoneno,delivery,address,billamount,delivery_boy) values (%s,%s,%s,%s,%s,%s,%s)"
    val=(ordno,name,phone,sdeli,address,total+gst,man)
    cur.execute(sname,val)
    mydb.commit()    
    for k in list_menu:
        ind=list_menu.index(k)        
        for i in k:
            oppo=remove(i[0])
            if i[2]!=0:
                cur.execute("insert into {}(orderno) values({})".format(useme[ind],ordno))
                mydb.commit()
                for i in k:
                    if i[2]!=0:	
                        cur.execute("update {} set {}={} where orderno={}".format(useme[ind],oppo,i[2],ordno))
                        mydb.commit()
                break
        for k in list_menu:
            ind=list_menu.index(k)        
        for i in k:
            oppo=remove(i[0])
            if i[2]!=0:
                cur.execute("insert into {}(orderno) values({})".format(useme[ind],ordno))
                mydb.commit()
                for i in k:
                    if i[2]!=0:	
                        cur.execute("update {} set {}={} where orderno={}".format(useme[ind],oppo,i[2],ordno))
                        mydb.commit()
                break      
    sys.stdout.close()                        
    sys.exit()
   

def delete():
    print("*"*80)
    order=input("Please Enter your order number (xxxxx):")
    correction(order,27878,99999)
    ch = input('Confirm deletion (PRESS 1: (Yes) , PRESS 2: (No)):')
    ch=correction(ch,1,2)
    if ch == 1:
        try:
            cur.execute('select * from personal where orderno={}'.format(order))
            fh = cur.fetchall()
            if not fh:
                print("ERROR, ORDER DOESN'T EXIST")            
            else:
                cur.execute('delete from personal where orderno={}'.format(order))
                mydb.commit()
                print("THANKS, YOUR ORDER HAS BEEN CANCELLED")
            print("*"*80)
            print("\n")
            start()
        except:
            mydb.rollback()
            print('AN UNEXPECTED ERROR OCCURRED, DATA RESTORED TO NORMAL')
            print("*"*80)
            print('\n')
            
    else:
        print('DATA DELETION REVERTED, DATA RESTORED TO NORMAL')
        print("*"*80)
        print('\n')    
    
     
     
def about():
     print("-~"*40)
     aboutus="KNOW MORE ABOUT US "
     print(aboutus.center(80),"\n")
     know='''TOWER OF PIZZA is a HIGH QUALITY PIZZA ORDERING APP that enables its customers
to buy FRESH,CRISPY,CRUNCHY, CHEESY PIZZA at AFFORDABLE RATES.Our Motto is to
\"SHAPE THE FOOD YOU EAT\".We are present in 24 countries and 500+ cities
globally, enabling our vision of better food for more people. We not only
connect people to food in every context but work closely with restaurants to
enable a sustainable ecosystem.'''
     print(know)
     print(" CONTACT US : 884422230","EMAIL: tower_pizza@gmail.com".rjust(50))
     print("-~"*40)
     print("\n")
     start()
     
def suggestion():
     print("-~"*40)
     suggestion="RATE US"
     rev="HOW DID YOU LIKE OUR APP?"
     print(suggestion.center(80))
     print(rev.center(80),"\n")                         
     io=input("LOVED IT!(PRESS 1: (Yes) , PRESS 2: (No):")
     io=correction(io,1,2)
     if io==1:
          sugg=input("SEND FEEDBACK. TELL US WHAT YOU LOVE ABOUT THE APP: ")
     else:
          sugg=input("SEND FEEDBACK. TELL US WHAT WE COULD BE DOING BETTER :")
     print("THANKS FOR SENDING US A FEEDBACK.")
     print("-~"*40)
     print("\n")
     start()

def placingorder():
    global pi
    global opt
    global x
    print("\n")
    print('What would you like to eat?')
    select_menu(menu,5)
    opt = '1'
    while opt != '0':
        if main == 1:
            print('1. Veg pizza')
            print('2. Non-veg pizza')    
            pi = input('Enter your choice :')
            print('\n')
            pi = correction(pi,1,2)
            if pi == 1:
                print(p)
                order(vegpizza)
            elif pi == 2:
                print(np)
                order(nonvegpizza)
        elif main==2:
            print(d)
            order(desserts)
        elif main==3:
            print(b)
            order(beverages)
        elif main==4:
            print(sna)
            order(snacks)
        elif main==5:
            print(sid)
            order(sides)
    if checking():
        last=input('Proceed to pay: PRESS 1, Proceed to MAIN MENU: PRESS 2 :')
        print('\n')
        last=correction(last,1,2)
        if last == 1:
                 bill()
        else:
            start()

def start():
    select_menu(main_list,8)
    if main==1:
        placingorder()
    elif main==2:
        custorder()
    elif main==3:
        update()
    elif main==4:
        stats()
    elif main==5:
        delete()
    elif main==6:
        about()
    elif main==7:
        suggestion()
    elif main == 8:        
        ping=0
        for k in list_menu:
            for j in k:
                if j[2] != 0:
                    ping=1
                    break                
        for i in size:
            if i[2]==1:
                ping=1
                break
        if ping == 0:
            print('Your Happiness, Our pleasure. Toodles. Till next time, lots of love')
            mydb.close()
            sys.exit()
        else:
            print("WAIT! You added some delicious food in your cart yet didn't order")
            last=input('Proceed to pay: PRESS 1, Proceed to order something else: PRESS 2 :')
            last=correction(last,1,2)
            if last == 1:
                     bill()
                     for k in list_menu:
                        for j in k:
                            j[2] = 0
                     for j in orders:
                        for c in j:
                            c[2]= 0
                     start()
            else:
                start()
            


#MAIN PROGRAM STARTS Here
print('\n')
s='''   -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
                         TOWER OF PIZZA                         
                      A FOOD DELIVERING APP                        
                                                                  
    __________					        __________
   (__________)		        		       (__________)
    \:< & (;)/		CREATED BY:             	\:< & (;)/
     \^? - +/		    ADITI GUPTA (04)   	         \^? - +/
      \=! ;/		    KHUSHI VERMA (25)  	          \=! ;/
       \+=/		    CLASS : XIIA 	    	   \+=/
        \/	                                            \/  
                                                        
   -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'''
print(s)
welcome = 'WELCOME TO TOWER OF PIZZA'
print(welcome.center(80))                                       # INTRODUCTORY LINE
honour = 'ITS AN HONOUR FOR US TO SERVE YOU.'
print(honour.center(80), '\n')

if mydb.is_connected():
    print("YOU HAVE SUCCESSFULLY LOGGED IN")
else:
    print("LOGIN FAILED")
    
name = input('Please enter your name :')
name = name.strip()                          #INPUTING NAME
name = string(name)
phone = input('Please enter your phone number :')                 #INPUTING NUMBER
phone = correction(phone,1000000000,9999999999)

print('\n')
print('CONGRATULATIONS YOU ARE OUR LUCKY WINNER AND YOU','\n','JUST WON A CHANCE TO WIN A COUPON','\n',' PRESS a number between 1 to 5 TO AVAIL IT')
x = input('Enter a number between 1 and 5 : ')                                   #LUCKY DRAW
x = correction(x,1,5)
code=['AOFF100','SOFF200','H8FREE','JSORRY','S2PUDD']
off1=['RUPEES 100 OFF','CONGRATULATIONS','You get Rs.100 off on your order','AVAIL IT NOW']
off2=['RUPEES 200 OFF','CONGRATULATIONS','You get Rs.200 off on your order','AVAIL IT NOW']
free=['FREE LARGE SPRITE','CONGRATULATIONS','You get FREE LARGE SPRITE','along with your order' ]
sorry=['Sorry, bad luck,','but dont worry , Next time','Uptill that time try out our new','BLACK FOREST FLURRY..MMM..YUMM']
happy=['FREE CHOCOLATE PUDDING','CONGRATULATIONS','You get A FREE CHOCOLATE PUDDING','along with your order']
coupons=[off1,off2,free,sorry,happy]
print('\n')

ast='*'
print('\t',ast*36)
print('\t','*'+' '*34+'*')
for i in range(4):
    bl = coupons[x-1][i]
    print('\t',ast,bl.center(32),ast)  #PRINTING COUPONS
    
for j in range(2):
    print('\t','*'+' '*34+'*')
print('\t','*',code[x-1].ljust(32),'*')

print('\t',ast*36)
print('\n')     

print("HEY",name,"! WELCOME TO TOWER OF PIZZA. IT'S FOOD O'CLOCK.","\n")
print("What would you like to do first?","\n")

while True:
    start()    

#print ur bill has been saved
    


    
