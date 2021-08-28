
from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

"""def abc():
    win.destroy()
    os.system('E:\\python\\tkinter\\database\\find.py ')
    """
    

def login():
    #uid=tb.get()
    us=user.get()
    pa=pwd.get()
    print(us)
    print(pa)


    conn=pymysql.connect(host='localhost',user='root',password='',db='pkp')
    a=conn.cursor()

    a.execute("select * from login where username='"+us+"' and pass='"+pa+"'")
    results=a.fetchall()
    count=a.rowcount
    print(results)
    print(count)
    if(count>0):
        def update():
            
    
            def update_fun():
                conn =pymysql.connect(host="localhost",user="root",password="",db='atm')
                try:
                    acc=tb1.get()
                    askval = asktb.get()
                    newval = valtb.get()
                    print(newval)
                    var = conn.cursor()
                    v=var.execute("select * from pnb where account = "+str(acc))
                    if v!=0:
                        dbid=var.fetchall()
                        if(askval=='name' or askval=='NAME' or askval=='address' or askval=='ADDRESS' or askval=='contact' or askval=='CONTACT'  or askval=='ACCOUNT'  or askval=='account'):
                            
                            var.execute("update pnb set "+askval+" = '"+newval+"' where account = "+str(acc))
                            messagebox.showinfo("Information","Data updated Successfully")
                            conn.commit()
                        else:
                            messagebox.showerror("Information","Enter a valid option")
                    else:
                        messagebox.showerror("Information","Data not found")
                except:
                    conn.rollback()
                    messagebox.showinfo("Information","Data Transfer Failed")


            upwin = Tk()
            upwin.title("Update here!")
            upwin.geometry("300x300")
            upwin.resizable(False,False)
            lb1=Label(upwin,text="Enter account").place(x=30,y=30)
    
            acc=StringVar()
            tb1=Entry(upwin,textvariable=acc)
            tb1.place(x=100,y=30)

            asklb=Label(upwin,text="What you want to update?").place(x=60,y=60)

            ask=StringVar()
            asktb = Entry(upwin,textvariable=ask,width=29)
            asktb.place(x=30,y=90)

            vallb=Label(upwin,text="Enter New Values!").place(x=60,y=120)

            val=StringVar()
            valtb = Entry(upwin,textvariable=val,width=29)
            valtb.place(x=30,y=150)

            updatebtn=Button(upwin,text="Update",command=update_fun).place(x=90,y=180)


        def delete():
            
           

            def delet():
                conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
                try:
                    acc=tb1.get()
                    var = conn.cursor()
                    v=var.execute("delete  from pnb where account = "+acc)
                    if v!=0:
                        dbid=var.fetchall()
                        messagebox.showinfo("Information","Data deleted Successfully")
                        conn.commit()
                    else:
                        messagebox.showerror("Information","Data not found")
                except:
                    conn.rollback()
                    messagebox.showinfo("Information","Data Transfer Failed")
            dele=Tk()
            dele.title("Delete with ID")
            dele.geometry("300x100")
            dele.resizable(False,False)
            lb1=Label(dele,text="Enter account number")
            lb1.place(x=15,y=20)

            tb1 = Entry(dele)
            tb1.place(x=95,y=20)

            delbtn = Button(dele,text="Delete",command=delet).place(x=120,y=50)

        def show():
            if True:
                conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
                var = conn.cursor()
                var.execute('select * from pnb ')
                v = var.fetchall()
                show = Tk()
                show.geometry("850x500")
                show.resizable(False,True)
                show.title("Details")
                vary=80
                headlb=Label(show,text="customer details Details",font="Times 25 bold").grid(row=0,column=1,padx=200)
                #-------------------------------Label of the Table---------------------------------#
                lb1 = Label(show,text="Account number",width=20,bg="white",bd=5).place(x=2,y=50)
                lb2 = Label(show,text="Name",width=20,bg="white",bd=5).place(x=175,y=50)
                lb3 = Label(show,text="Amount",width=20,bg="white",bd=5).place(x=348,y=50)
                lb4 = Label(show,text="address",width=20,bg="white",bd=5).place(x=521,y=50)
                lb5 = Label(show,text="contact ",width=20,bg="white",bd=5).place(x=690,y=50)
        
                for i in range(0,var.rowcount):
                    lb1 = Label(show,text=v[i][0],width=20,bg="white",bd=5).place(x=2,y=vary)
                    lb2 = Label(show,text=v[i][1],width=20,bg="white",bd=5).place(x=175,y=vary)
                    b3 = Label(show,text=v[i][2],width=20,bg="white",bd=5).place(x=348,y=vary)
                    lb4 = Label(show,text=v[i][3],width=20,bg="white",bd=5).place(x=521,y=vary)
                    lb5 = Label(show,text=v[i][4],width=20,bg="white",bd=5).place(x=690,y=vary)
                    vary+=30
            
            
                print(vary)
                conn.commit()

            else:
                conn.rollback()
                print("!!!!!!!!!!!!!!!!!!!!!!Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
         
        
        
        def submit():
            acc=tb1.get()
            nm=tb2.get()
            amnt=tb3.get()
            addr=tb4.get()
            cont=tb5.get()
            pi=tb6.get()
            print(acc,nm,amnt,addr,cont,pi)
            conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
            try:
                var = conn.cursor()
                var.execute("insert into pnb(account,name,amount,address,contact,pin) values ('"+acc+"','"+nm+"','"+amnt+"','"+addr+"','"+cont+"','"+pi+"')")
                #var.execute("insert into pnb(account, name, amount, address,contact,pin) values ('"+tb1.get()+"','"+tb2.get()+"','"+tb3.get()+"','"+tb4.get()+"','"+tb5.get()+"','"+tb6.get()+"')")
                
                conn.commit()
                messagebox.showinfo("Information","Data Sent Successfully") 
            except:
                
                messagebox.showinfo("Information","Data Transfer Failed")
            conn.rollback()

        
        winn=Tk()
        win.config(bg="blue")
        winn.geometry("500x400")
        winn.title("Account creation for Customers")
        winn.resizable(0,0)
        mainlabel=Label(winn,text="Enter the following customer details below ",font="Arial 15").place(x=50,y=15)
        lb1=Label(winn,text="Enter account no").place(x=80,y=60)
        acc=StringVar()
        tb1=Entry(winn,textvariable=acc)
        tb1.place(x=230,y=60)
      

        lb2=Label(winn,text="Enter name.").place(x=80,y=100)
        nm=StringVar()
        tb2=Entry(winn,textvariable=nm)
        tb2.place(x=230,y=100)

        lb3=Label(winn,text="Enter amount").place(x=80,y=140)
        amnt=StringVar()
        tb3=Entry(winn,textvariable=amnt)
        tb3.place(x=230,y=140)

        lb4=Label(winn,text="Enter address").place(x=80,y=180)
        addr=StringVar()
        tb4=Entry(winn,textvariable=addr)
        tb4.place(x=230,y=180)

        lb5=Label(winn,text="Enter contact").place(x=80,y=220)
        cont=StringVar()
        tb5=Entry(winn,textvariable=cont)
        tb5.place(x=230,y=220)

        lb6=Label(winn,text="Enter pin").place(x=80,y=260)
        pi=StringVar()
        tb6=Entry(winn,textvariable=pi)
        tb6.place(x=230,y=260)

        submitbtn = Button(winn,text="Submit",command=submit,width=10,height=1,font="Times 10",relief=RAISED,bd=10).place(x=50,y=300)
        deletebtn = Button(winn,text="Delete",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=delete).place(x=200,y=300)
        
        updatebtn = Button(winn,text="Update",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=update).place(x=350,y=300)
        showbtn = Button(winn,text="Show All Data",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=show).place(x=200,y=350)
        

    
        #messagebox.showinfo("message","login")
        
    else:
        messagebox.showinfo("message","not login")
        
        

win=Tk()
win.geometry("500x400")
win.title("Login Emp")
win.configure(bg='gray')
#win.overrideredirect(True)
#win.overrideredirect(False)
win.resizable(False,False)

topframe=Frame(win,width=1500,height=200,bg="yellow",relief='raise',bd=10)
topframe.pack(side=TOP)

lb=Label(topframe,text="Panjab National Bank",font=('italic',20,'bold'),width=20,fg='pink',bd=4)
lb.grid(row=0,column=0)



mframe=Frame(win,width=1000,height=800,bg="orange",relief='raise',bd=10)
mframe.pack(padx=50,pady=20)



lb=Label(mframe,text="Admin Login",font=('italic',15,'bold'),bd=5,width=30,fg='pink',relief='raise')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)


lb2=Label(mframe,text="username",width=8)
lb2.grid(row=1,column=0,padx=10,pady=10)
lb3=Label(mframe,text="password",width=8)
lb3.grid(row=2,column=0,padx=10,pady=10)


user=StringVar()
tb1=Entry(mframe,textvariable=user)
tb1.grid(row=1,column=1)
pwd=StringVar()
tb2=Entry(mframe,textvariable=pwd)
tb2.grid(row=2,column=1)

btn1=Button(mframe,text="Login",font=('italic',15,'bold'),bd=5,width=12,fg='black',relief='raise',command=login)
btn1.grid(row=5,column=0,columnspan=2,padx=10,pady=10)















