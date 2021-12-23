from tkinter import *
from tkinter import ttk,messagebox
import datetime,random,sqlite3

root = Tk()
root.geometry("1400x1000+0+0")
root.title("Student Managment System")
root.config(bg="white")

#================= All function =====================
def changecolor():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    hex_code = "#%02x%02x%02x" % (R,G,B)
    menubar.config(bg=hex_code)
    greet.config(bg=hex_code)
    time_.config(bg=hex_code)
    date_.config(bg=hex_code)
    menubar.after(700,changecolor)
    #root.config(bg=hex_code)

def now_datetime():
    d = datetime.datetime.now()
    date_.config(text=f"Date: {(str(d)[0:10])}")
    time_.config(text=f"Time: {(str(d)[11:19])}")
    time_.after(200,now_datetime)

def clear_entry_func():
    roll_var.set('')
    name_var.set('')
    email_var.set('')
    gender_var.set('')
    contact_var.set('')
    dob_var.set('')
    address_ent.delete(1.0,END)
       
def clear_details_func():
    search_var.set('')
    sort_var.set('')

def notify():
    notify_add_data.place(x=1000,y=1200)

#======All Varibles=======
roll_var = StringVar()
name_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
contact_var = StringVar()
dob_var = StringVar()

def add_data():
    global address_ent
    if roll_var.get()=="" or name_var.get()=="" or email_var.get()=="" or contact_var.get()=="" or dob_var.get()=="" :
        messagebox.showerror("Error","Please Fill All Entry")
    else:
        try:
            cunn = sqlite3.connect("stm_database.db")
            cunn.execute('''
                    CREATE TABLE "StudentData" (
                "st_id"	INTEGER,
                "st_roll"	VARCHAR(7),
                "st_name"	VARCHAR(50),
                "st_email"	VARCHAR(35),
                "st_gender"	VARCHAR(15),
                "st_contact"	VARCHAR(12),
                "st_dob"	VARCHAR(10),
                "st_address"	VARCHAR(100),
                PRIMARY KEY("st_id" AUTOINCREMENT))
                ''')
            
        except:
            cunn = sqlite3.connect("stm_database.db")
        ins =("insert into StudentData (st_roll,st_name,st_email,st_gender,st_contact,st_dob,st_address) VALUES (?,?,?,?,?,?,?)")
        data = (roll_var.get(),name_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get(),address_ent.get(1.0,END))
        cunn.execute(ins,data)
        cunn.commit()
        cunn.close()
            
        notify_add_data.place(x=50,y=680)
        notify_add_data.after(3000,notify)
        clear_entry_func()
        fetch_data()

def fetch_data():
    try:
        cunn = sqlite3.connect("stm_database.db")
        sel = cunn.execute("select * from StudentData")
        data = sel.fetchall()
        if len(data)!=0:
            st_table.delete(*st_table.get_children())
            for row in data:
                st_table.insert('',END,values=row)
            cunn.commit()
        cunn.close()
    except:
        return "None"
    
def table_data(ev):
    conn = sqlite3.connect("stm_database.db")
    sel_data = conn.execute("select * from StudentData")
    data_lst = sel_data.fetchall()
    index_is = data_lst[1]
    clear_entry_func()
    roll_var.set(index_is[1])
    name_var.set(index_is[2])
    email_var.set(index_is[3])
    gender_var.set(index_is[4])
    contact_var.set(index_is[5])
    dob_var.set(index_is[6])
    address_ent.delete(1.0,END)
    address_ent.insert(END,index_is[7])
    conn.close()

def update_data():
    global address_ent
    # conn = sqlite3.connect("stm_database.db")
    # conn = sqlite3.connect("stm_database.db")
    # conn.execute("update StudentdData set st_name=%s ,st_email=%s,st_gender=%s,st_contact=%s,st_dob=%s,st_address=%s where st_roll=1",(
    #                                                                                                                 name_var.get(),
    #                                                                                                                 email_var.get(),
    #                                                                                                                 gender_var.get(),
    #                                                                                                                 contact_var.get(),
    #                                                                                                                 dob_var.get(),
    #                                                                                                                 address_ent.get(1.0,END)
    #                                                                                                                 ))

    # conn.commit()
    #conn.close()
    cunn = sqlite3.connect("stm_database.db")
    ins ="""update StudentData set st_roll = ? st_name = ? st_email = ? st_gender = ? st_contact = ? st_dob = ? st_address = ? where st_roll = ?"""
    data = (roll_var.get(), name_var.get(), email_var.get(), gender_var.get(), contact_var.get(), dob_var.get(), address_ent.get(1.0,END), roll_var.get())
    cunn.execute(ins, data)
    cunn.commit()
    cunn.close()


#================= Title and Menubar =====================
title = Label(root,text='Student Managment System',font=("times new roman",'45',"bold"),fg="red",bg="yellow",relief=GROOVE,border=10).pack(fill=X)

menubar = Frame(root,height=33,bg="gray")
menubar.pack(fill="x")

greet = Label(menubar,text="Welcome To Student Managment System",bg="gray",fg="white",font=("times new roman",16,"bold"))
greet.pack(side=LEFT,padx=150)
date_ = Label(menubar,bg="gray",fg="white",font=("times new roman",16,"bold"))
date_.pack(side=LEFT,padx=30)
time_ = Label(menubar,bg="gray",fg="white",font=("times new roman",16,"bold"))
time_.pack(side=LEFT,padx=150)

#=================== Entry Details =======================
eny_frm = Frame(root,bg="crimson",relief=RAISED,bd=4)
eny_frm.place(x=30,y=135,width=470,height=845)

eny_title = Label(eny_frm,text="Manage Student",fg="white",font=("times new roman",30,"bold"),bg="crimson")
eny_title.grid(row=0,columnspan=2,pady=20)

roll_ = Label(eny_frm,bg="crimson",text="Roll No.",fg='white',font=("times new roman",20,"bold"))
roll_.grid(row=1,column=0,sticky=W,padx=25,pady=20)
roll_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=roll_var)
roll_ent.grid(row=1,column=1)

name_lbl = Label(eny_frm,bg="crimson",text="Name",fg='white',font=("times new roman",20,"bold"))
name_lbl.grid(row=2,column=0,sticky=W,padx=25,pady=20)
name_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=name_var)
name_ent.grid(row=2,column=1)

email_id = Label(eny_frm,bg="crimson",text="Email",fg='white',font=("times new roman",20,"bold"))
email_id.grid(row=3,column=0,sticky=W,padx=25,pady=20)
email_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=email_var)
email_ent.grid(row=3,column=1)

gender_lbl = Label(eny_frm,bg="crimson",text="Gender",fg='white',font=("times new roman",20,"bold"))
gender_lbl.grid(row=4,column=0,sticky=W,padx=25,pady=20)
gender = ttk.Combobox(eny_frm,font=("times new roman",19,"bold"),justify=CENTER,state="readonly",textvariable=gender_var)
gender["values"] = ('Select Gender',"Male","Female","Other")
gender.grid(row=4,column=1)
gender.current(0)

cont_no = Label(eny_frm,bg="crimson",text="Contect",fg='white',font=("times new roman",20,"bold"))
cont_no.grid(row=5,column=0,sticky=W,padx=25,pady=20)
cont_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=contact_var)
cont_ent.grid(row=5,column=1)

dob_lbl = Label(eny_frm,bg="crimson",text="D.O.B",fg='white',font=("times new roman",20,"bold"))
dob_lbl.grid(row=6,column=0,sticky=W,padx=25,pady=20)
dob_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=dob_var)
dob_ent.grid(row=6,column=1)

add_lbl = Label(eny_frm,bg="crimson",text="Address",fg='white',font=("times new roman",20,"bold"))
add_lbl.grid(row=7,column=0,sticky=W,padx=25,pady=20)
address_ent = Text(eny_frm,relief=GROOVE,bd=3,height=4,width=28,font=("times new roman",15))
address_ent.grid(row=7,column=1,pady=20)

notify_add_data = Label(eny_frm,text="Data Add Succesful!",font=("times new roman",13),bg='crimson',fg="yellow")

#==== Buttom ====
btn_frm = Frame(eny_frm,bg="crimson",relief=RAISED,bd=2)
btn_frm.place(x=30,y=700,width=407,height=120)

add_btn = Button(btn_frm,text="Add",fg="black",bg="white",bd=4,cursor="hand2",command=add_data,relief=RAISED,width=14,font=("times new roman",15,"bold"))
add_btn.grid(row=0,column=0,pady=8,padx=13)

update_btn = Button(btn_frm,text="Update",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=13,font=("times new roman",15,"bold"),command=update_data)
update_btn.grid(row=0,column=2,pady=8,padx=10)

delete_btn = Button(btn_frm,text="Delete",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=14,font=("times new roman",15,"bold"))
delete_btn.grid(row=1,column=0,padx=13)

clr_btn = Button(btn_frm,text="Clear",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=13,font=("times new roman",15,"bold"),command=clear_entry_func)
clr_btn.grid(row=1,column=2,padx=10)

#================== View Deitels ==================== 
search_var = StringVar()
sort_var = StringVar()
dtl_frm = Frame(root,bg="crimson",relief=RAISED,bd=4)
dtl_frm.place(x=530,y=135,width=820,height=845)

d_title = Label(dtl_frm,text="Search By",fg="white",font=("times new roman",19,"bold"),bg="crimson")
d_title.grid(row=0,columnspan=1,pady=20,padx=30)

sort = ttk.Combobox(dtl_frm,font=("times new roman",13,"bold"),state="readonly",width=15,textvariable=sort_var)
sort["values"]= ('Sl No.','Roll No.',"Name","Email","Gender","Contect","D.O.B","Address")
sort.grid(row=0,column=2)

search_ent = Entry(dtl_frm,font=("times new roman",13,"bold"),textvariable=search_var,relief=GROOVE,bd=3,width=15)
search_ent.grid(row=0,column=3,padx=22)

search_btn = Button(dtl_frm,text="Search",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=10,font=("times new roman",11,"bold"))
search_btn.grid(row=0,column=4,padx=10)

clear_btn = Button(dtl_frm,text="Clear",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=10,font=("times new roman",11,"bold"),command=clear_details_func)
clear_btn.grid(row=0,column=5,padx=10)

#======= Details show =======

table_frm = Frame(dtl_frm,bg="white",relief=RAISED,bd=4)
table_frm.place(x=30,y=95,width=750,height=720)

x_scrollbar = Scrollbar(table_frm,orient=HORIZONTAL)
y_scrollbar = Scrollbar(table_frm,orient=VERTICAL)
st_table = ttk.Treeview(table_frm,columns=("sr_id","roll","name","email","gender","contect","dob","address"),xscrollcommand=x_scrollbar.set,yscrollcommand=y_scrollbar.set)
x_scrollbar.pack(side=BOTTOM,fill=X)
y_scrollbar.pack(side=RIGHT,fill=Y)

x_scrollbar.config(command=st_table.xview)
y_scrollbar.config(command=st_table.yview)
st_table.heading("sr_id",text="Sl No.")
st_table.heading("roll",text="Roll No.")
st_table.heading("name",text="Name")
st_table.heading("email",text="Email Id")
st_table.heading("gender",text="Gender")
st_table.heading("contect",text="Contect")
st_table.heading("dob",text="D.O.B")
st_table.heading("address",text="Address")
st_table["show"] = "headings"
st_table.column("sr_id",width=30)
st_table.column("roll",width=50)
st_table.column("name",width=100)
st_table.column("email",width=100)
st_table.column("gender",width=60)
st_table.column("contect",width=100)
st_table.column("dob",width=80)
st_table.column("address",width=100)

st_table.pack(fill=BOTH,expand=TRUE)
st_table.bind("<ButtonRelease>",table_data)
#================== View Deitels Closed ====================

fetch_data()
changecolor()
now_datetime()
root.mainloop()