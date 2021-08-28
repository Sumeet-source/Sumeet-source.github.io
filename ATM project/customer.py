from tkinter import *
from pymysql import *
import pymysql.cursors
from tkinter import messagebox
from datetime import *

win=Tk()
win.config(bg="blue")
win.geometry("500x330")
win.title("Welcome to the main page")
win.resizable(0,0)
def deposit():
    upwin=Tk()
    upwin.geometry("380x250")
    upwin.title("Welcome to the deposit")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    nwlb=Label(upwin,text="Enter ammount",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=230,y=140)

    def depo():
       
        acc=asktb.get()
        pi=valtb.get()
        am=nwtb.get()
       
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount+'"+am+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,dep,time) values ('"+acc+"','"+pi+"','"+am+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","deposited  successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    updatebtn=Button(upwin,text="deposit",font="Times 10",relief=RAISED,bd=8,command=depo).place(x=26,y=200)
       
def withdraw():
    upwin=Tk()
    upwin.geometry("380x260")
    upwin.title("Welcome to the withdraw")
    upwin.resizable(0,0)
  

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    nwlb=Label(upwin,text="Enter ammount",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=230,y=140)

    def minus():
       
        acc=asktb.get()
        pi=valtb.get()
        am=nwtb.get()
       
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount-'"+am+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+am+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")
            
    updatebtn=Button(upwin,text="withdrwal",font="Times 10",relief=RAISED,bd=8,command=minus).place(x=26,y=200)
      

def fastcash():
    win=Tk()
    win.bg='blue'
    win.geometry("380x280")
    win.title("Welcome to fast cash")
    win.resizable(0,0)

    asklb=Label(win,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(win,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(win,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(win,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    def two():
        
        acc=asktb.get()
        pi=valtb.get()
        am=200
        
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount-'"+str(am)+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+str(am)+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def five():
        
        acc=asktb.get()
        pi=valtb.get()
        am=500
        
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount-'"+str(am)+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+str(am)+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def thousand():
        
        acc=asktb.get()
        pi=valtb.get()
        am=1000
        
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount-'"+str(am)+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+str(am)+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def fiveth():
        
        acc=asktb.get()
        pi=valtb.get()
        am=5000
        
        conn = connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update pnb set amount=amount-'"+str(am)+"' where account='"+acc+"' and pin='"+pi+"' ")
            var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+str(am)+"','"+str(datetime.now())+"')")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")
            

    submitbtn = Button(win,text="200",width=15,height=1,font="Times 10",relief=RAISED,bd=10,command=two).place(x=20,y=140)
    deletebtn = Button(win,text="500",width=15,height=1,font="Times 10",relief=RAISED,bd=10,command=five).place(x=180,y=140)
    updatebtn = Button(win,text="1000",width=15,height=1,font="Times 10",relief=RAISED,bd=10,command=thousand).place(x=20,y=200)
    showbtn = Button(win,text="2000",width=15,height=1,font="Times 10",relief=RAISED,bd=10,command=fiveth).place(x=180,y=200)

    
def ministate():
    upwin=Tk()
    upwin.geometry("300x200")
    upwin.title("Welcome to the main page")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=29)
    asktb.place(x=30,y=90)

    def showmini():
        if True:
            acc=asktb.get()
            conn = connect(host="localhost",user="root",password="",db='atm')
            var = conn.cursor()
            var.execute("select * from mini where account='"+acc+"'")
            v = var.fetchall()
            show = Tk()
            show.geometry("850x500")
            show.resizable(False,True)
            show.title("Details")
            vary=80
            headlb=Label(show,text="customer details Details",font="Times 25 bold").grid(row=0,column=1,padx=200)
            #-------------------------------Label of the Table---------------------------------#
            lb1 = Label(show,text="Account ",width=20,bg="white",bd=5).place(x=2,y=50)
            lb2 = Label(show,text="pin",width=20,bg="white",bd=5).place(x=175,y=50)
            lb3 = Label(show,text="withdrawl",width=20,bg="white",bd=5).place(x=348,y=50)
            lb4 = Label(show,text="Time",width=20,bg="white",bd=5).place(x=521,y=50)
            lb5 = Label(show,text="Deposit ",width=20,bg="white",bd=5).place(x=690,y=50)
        
            for i in range(0,var.rowcount):
                lb1 = Label(show,text=v[i][0],width=20,bg="white",bd=5).place(x=2,y=vary)
                lb2 = Label(show,text=v[i][1],width=20,bg="white",bd=5).place(x=175,y=vary)
                lb3 = Label(show,text=v[i][2],width=20,bg="white",bd=5).place(x=348,y=vary)
                lb4 = Label(show,text=v[i][3],width=20,bg="white",bd=5).place(x=521,y=vary)
                lb5 = Label(show,text=v[i][4],width=20,bg="white",bd=5).place(x=690,y=vary)
                vary+=30
            
            
            print(vary)
            conn.commit()
        else:
            conn.rollback()
            print("!!!!!!!!!!!!!!!!!!!!!!Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    updatebtn=Button(upwin,text="show",font="Times 10",relief=RAISED,bd=8,command=showmini).place(x=26,y=140)

def transfer():
    upwin=Tk()
    upwin.geometry("350x230")
    upwin.title("Balance Enquiry")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Select the option",font="Times 20").place(x=70,y=40)

    ask=StringVar()

    def hdfc():
        upwin=Tk()
        upwin.geometry("480x350")
        upwin.title("Welcome to the transfer page")
        upwin.resizable(0,0)

        asklb=Label(upwin,text="Enter account number from",font="Times 15").place(x=26,y=40)

        ask=StringVar()
        asktb = Entry(upwin,textvariable=ask,width=20)
        asktb.place(x=250,y=40)

        vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

        val=StringVar()
        valtb = Entry(upwin,textvariable=val,width=20)
        valtb.place(x=250,y=90)

        nwlb=Label(upwin,text="Enter amount",font="Times 15").place(x=26,y=140)

        nw=StringVar()
        nwtb = Entry(upwin,textvariable=nw,width=20)
        nwtb.place(x=250,y=140)

        relb=Label(upwin,text="Enter account number to",font="Times 15").place(x=26,y=190)

        re=StringVar()
        retb = Entry(upwin,textvariable=re,width=20)
        retb.place(x=250,y=190)

        ifslb=Label(upwin,text="Enter ifsc",font="Times 15").place(x=26,y=240)

        ifs=StringVar()
        ifstb = Entry(upwin,textvariable=ifs,width=20)
        ifstb.place(x=250,y=240)
 
 
        updatebtn=Button(upwin,text="deposited",font="Times 10",relief=RAISED,bd=8).place(x=26,y=290)
        def fund():
            acc=asktb.get()
            pi=valtb.get()
            am=nwtb.get()
            amnt=retb.get()
            ifss=ifstb.get()
            print(acc)
            print(pi)
            print(am)
            print(amnt)
            print(ifss)
        
            conn = connect(host="localhost",user="root",password="",db='atm')
            var = conn.cursor()
            var.execute("select * from pnb where account='"+acc+"' and pin='"+pi+"' ")
            row=var.rowcount
            if(row>0):
                var.execute("update pnb set amount=amount-'"+str(am)+"' where account='"+acc+"' and pin='"+pi+"' ")
                var.execute("insert into mini (account,pin,withd,time) values('"+acc+"','"+pi+"','"+str(am)+"','"+str(datetime.now())+"')")
                # var.execute("select * from hdfc where account='"+acc+"' and ifsc='"+ifss+"' ")
                var.execute("update  hdfc set amount=amount+'"+str(am)+"' where account='"+amnt+"' and ifsc='"+ifss+"' ")
                conn.commit()
                messagebox.showinfo("Information","withdrawl successfully")
            else:
                messagebox.showinfo("Information","not valid")
                conn.rollback()
 
        updatebtn=Button(upwin,text="deposited",font="Times 10",relief=RAISED,bd=8,command=fund).place(x=26,y=290)
        
    submitbtn = Button(upwin,text="HDFC",width=15,height=1,font="Times 10",relief=RAISED,bd=10,command=hdfc).place(x=30,y=90)
    deletebtn = Button(upwin,text="STATE",width=15,height=1,font="Times 10",relief=RAISED,bd=10).place(x=180,y=90)
    updatebtn = Button(upwin,text="PNB",width=15,height=1,font="Times 10",relief=RAISED,bd=10).place(x=30,y=160)
    showbtn = Button(upwin,text="ICICI",width=15,height=1,font="Times 10",relief=RAISED,bd=10).place(x=180,y=160)

def balenq():
    upwin=Tk()
    upwin.geometry("400x200")
    upwin.title("Welcome to the transfer page")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Enter account number ",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=250,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=250,y=90)

    def bal():
        acc=asktb.get()
        blc=valtb.get()
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()

            a.execute("select amount from pnb where account='"+acc+"'and pin='"+blc+"'")
            results=a.fetchall()
            count=a.rowcount
            if(count>0):
                for row in results:
                    for j in range(0,count):
                        messagebox.showinfo("your balance is",row[j])
            else:
                #print("Not Found")
                messagebox.showinfo("message","not found")
        except:
            conn.rollback()
            messagebox.showinfo("message","not change")
            conn.close()  

    updatebtn=Button(upwin,text="show",font="Times 11",relief=RAISED,bd=10,command=bal).place(x=26,y=130)    
       
def pinchange():
    upwin=Tk()
    upwin.geometry("420x300")
    upwin.title("Welcome to the main page")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Enter account ",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=220,y=40)

    vallb=Label(upwin,text="Enter old pin!",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=220,y=90)

    nwlb=Label(upwin,text="Enter new pin!",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=220,y=140)

    relb=Label(upwin,text="Re-Enter the new pin",font="Times 15").place(x=26,y=190)

    re=StringVar()
    retb = Entry(upwin,textvariable=re,width=20)
    retb.place(x=220,y=190)

    def change():
        acc=asktb.get()
        ol=valtb.get()
        np=nwtb.get()
        cn=retb.get()
        try:
            if(np==cn):
                conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
                a=conn.cursor()
                a.execute("update pnb set pin='"+np+"' where account='"+acc+"' and pin='"+ol+"'")
                conn.commit()
                messagebox.showinfo("message","change")
            else:
                messagebox.showinfo("message","pin not match")
        except:
             conn.rollback()
             messagebox.showinfo("message","not change")
             conn.close()

    updatebtn=Button(upwin,text="change",font="Times 10",relief=RAISED,bd=10,command=change).place(x=26,y=240)

def conchange():
    upwin=Tk()
    upwin.geometry("500x340")
    upwin.title("Welcome to contact page details")
    upwin.resizable(0,0)

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=280,y=40)

    pilb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    pi=StringVar()
    pitb = Entry(upwin,textvariable=pi,width=20)
    pitb.place(x=280,y=90)

    oldlb=Label(upwin,text="Enter old contact number!",font="Times 15").place(x=26,y=140)

    old=StringVar()
    oldtb = Entry(upwin,textvariable=old,width=20)
    oldtb.place(x=280,y=140)

    nwlb=Label(upwin,text="Enter new contact number",font="Times 15").place(x=26,y=190)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=280,y=190)

    relb=Label(upwin,text="Re-Enter the new contact number",font="Times 15").place(x=26,y=240)

    re=StringVar()
    retb = Entry(upwin,textvariable=re,width=20)
    retb.place(x=280,y=240)

    def changecon():
        acc=asktb.get()
        pii=pitb.get()
        ol=oldtb.get()
        new=nwtb.get()
        ree=retb.get()
    
        try:
            if(ree==new):
                conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
                a=conn.cursor()
                a.execute("update pnb set contact='"+new+"' where account='"+acc+"' and pin='"+pii+"' and contact='"+ol+"'")
                conn.commit()
                messagebox.showinfo("message","change")
            else:
                messagebox.showinfo("message","contat not match")
        except:
             conn.rollback()
             messagebox.showinfo("message","not change")
             conn.close()

    updatebtn=Button(upwin,text="change",font="Times 10",relief=RAISED,bd=10,command=changecon).place(x=26,y=290)

    



    

submitbtn = Button(win,text="Deposit Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=deposit).place(x=15,y=30)

submitbtn = Button(win,text="Mini Statement",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=ministate).place(x=260,y=30)

deletebtn = Button(win,text="Withdraw Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=withdraw).place(x=15,y=100)
deletebtn = Button(win,text="Fast Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=fastcash).place(x=260,y=100)

updatebtn = Button(win,text="Blanace Enquiry",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=balenq).place(x=15,y=170)
updatebtn = Button(win,text="Change Pin",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=pinchange).place(x=260,y=170)

showbtn = Button(win,text="Transfer fund",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=transfer).place(x=15,y=240)
showbtn = Button(win,text="Update Contact ",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=conchange).place(x=260,y=240)



win.mainloop()
