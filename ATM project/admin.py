from tkinter import *
from pymysql import *
import pymysql.cursors
from tkinter import messagebox
win=Tk()
win.config(bg="blue")
win.geometry("500x400")
win.title("Account creation for Customers")
win.resizable(0,0)
mainlabel=Label(win,text="Enter the following customer details below ",font="Arial 15").place(x=50,y=15)

def show():
    if True:
        conn = connect(host="localhost",user="root",password="",db='atm')
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
    conn = connect(host="localhost",user="root",password="",db="atm")
    try:
        var = conn.cursor()
        var.execute("insert into pnb(account, name, amount, address,contact,pin) values ('"+acc.get()+"','"+nm.get()+"','"+amnt.get()+"','"+addr.get()+"','"+cont.get()+"','"+pi.get()+"')")
        conn.commit()
        messagebox.showinfo("Information","Data Sent Successfully") 
    except:
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

def delete():
    dele=Tk()
    dele.title("Delete with ID")
    dele.geometry("300x100")
    dele.resizable(False,False)

    def delet():
        conn = connect(host="localhost",user="root",password="",db="atm")
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

    lb1=Label(dele,text="Enter account number")
    lb1.place(x=15,y=20)

    tb1 = Entry(dele)
    tb1.place(x=95,y=20)

    delbtn = Button(dele,text="Delete",command=delet).place(x=120,y=50)

def update():
    upwin = Tk()
    upwin.title("Update here!")
    upwin.geometry("300x300")
    upwin.resizable(False,False)
    
    def update_fun():
        conn = connect(host="localhost",user="root",password="",db="atm")
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

 #designing

lb1=Label(win,text="Enter account no").place(x=80,y=60)
acc=StringVar()
tb1=Entry(win,textvariable=acc).place(x=230,y=60)

lb2=Label(win,text="Enter name.").place(x=80,y=100)
nm=StringVar()
tb2=Entry(win,textvariable=nm).place(x=230,y=100)

lb3=Label(win,text="Enter amount").place(x=80,y=140)
amnt=StringVar()
tb3=Entry(win,textvariable=amnt).place(x=230,y=140)

lb4=Label(win,text="Enter address").place(x=80,y=180)
addr=StringVar()
tb4=Entry(win,textvariable=addr).place(x=230,y=180)

lb5=Label(win,text="Enter contact").place(x=80,y=220)
cont=StringVar()
tb5=Entry(win,textvariable=cont).place(x=230,y=220)

lb6=Label(win,text="Enter pin").place(x=80,y=260)
pi=StringVar()
tb6=Entry(win,textvariable=pi).place(x=230,y=260)

submitbtn = Button(win,text="Submit",command=submit,width=10,height=1,font="Times 10",relief=RAISED,bd=10).place(x=50,y=300)

deletebtn = Button(win,text="Delete",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=delete).place(x=200,y=300)

updatebtn = Button(win,text="Update",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=update).place(x=350,y=300)

showbtn = Button(win,text="Show All Data",width=10,height=1,font="Times 10",relief=RAISED,bd=10,command=show).place(x=200,y=350)

win.mainloop()
