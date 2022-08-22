import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="student")
if mydb.is_connected():
    print("Database Connection : Successful")
else:
    print("Database Connection : Unsuccessful")
cur = mydb.cursor()
useme=['VEGPIZZA','NONVEGPIZZA','DESSERTS','BEVERAGES','SNACKS','SIDES']
cur.execute("create database if not exists tower_of_pizza;")
cur.execute("use tower_of_pizza;")
cur.execute("create table if not exists Personal(OrderNo int primary key, CustomerName char(50) not null, PhoneNo bigint, Delivery char(1) Not null, Address char(200) default 'None given', BillAmount int, Delivery_Boy char(50));")
cur.execute("create table if not exists VegPizza(OrderNo int primary key, Margherita int default 0,CheeseandCorn int default 0,FreshVeggie int default 0, PaneerMakhani int default 0,CheeseandTomato int default 0,PeppyPaneer int default 0);")
cur.execute("create table if not exists Beverages(OrderNo int primary key,Coke int default 0,Fanta int default 0 ,Sprite int default 0,ThumbsUp int default 0, ChocolateShake int default 0,Strawberryshake int default 0);")
cur.execute("create table if not exists Sides(OrderNo int primary key,Cheesydip int default 0,CheesyJalapenodips int default 0,GarlicBreadSticks int default 0);")
cur.execute("create table if not exists NonvegPizza(OrderNo int primary key,PepperBarbecueChicken int default 0,ChickenSausage int default 0,PeriPeriChicken int default 0,ChickenGoldenDelight int default 0);")
cur.execute("create table if not exists Desserts(OrderNo int primary key, BsflurryChocoCrunch int default 0, BlackForestFlurry int default 0,RedVelvetCake int default 0,SoftServeStrawberry int default 0);")
cur.execute("create table if not exists Snacks(OrderNo int primary key, AlooVegPatty int default 0,VegSpringRoll int default 0,CornSpinachRoll int default 0,ChilliPaneerRoll int default 0,PlainSandwich int default 0);")       
value=[(27871,'Vikrant Sethi',8390828999,'P','None',782,'NULL'),
       (27872,'Tanya Aggarwal',8298398383,'H','E-132 Paschim Vihar',3780,'Mr. Prakash'),
       (27873,'Meena Gupta',3772893898,'H','AD Block Rohini',510,'Mr. Rahim'),
       (27874,'Sakshi Arora',7382738888,'H','W Apartments Rajouri Garden',2789,'Mr. Raju'),
       (27875,'Reema Sharma',3279873277,'P','None',235,'NULL'),
       (27876,'Arunima Rawat',7239837899,'P','None',120,'NULL')]
b="insert into Personal values(%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(b,value)
vp=[(27871,0,0,0,0,3,1),
    (27873,9,0,0,0,4,8),
    (27874,0,1,2,4,0,0)]
np=[(27871,0,4,0,0),
    (27875,1,0,3,0),
    (27876,3,0,2,6)]
bev=[(27873,0,0,3,0,2,1),
     (27872,2,4,0,1,1,0),
     (27874,5,0,2,0,0,2)]
sid=[(27872,1,3,0),
     (27873,0,0,4),
     (27875,5,1,0)]
des=[(27872,0,0,2,0),
     (27875,0,0,0,0),
     (27876,3,1,0,0)]
sna=[(27875,0,0,2,0,1),
     (27872,3,0,0,2,1),
     (27871,0,1,1,0,0)]
li=[vp,np,des,bev,sna,sid]
for i in useme:
    l=li[useme.index(i)]
    a=len(li[useme.index(i)][0])
    b="insert into "
    d=" values("
    e='%s,'*(a-1)+'%s)'
    c=b+i+d+e
    cur.executemany(c,l)

mydb.commit()
mydb.close()


