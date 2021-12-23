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

#======All Varibles=======
roll_var = StringVar()
name_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
contect_var = StringVar()
dob_var = StringVar()

def add_data():
    cunn = sqlite3.connect("stm_database.db")
    cunn.execute()

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
gender = ttk.Combobox(eny_frm,font=("times new roman",19,"bold"),state="readonly",textvariable=gender_var)
gender["values"] = ("Male","Female","Other")
gender.grid(row=4,column=1)

cont_no = Label(eny_frm,bg="crimson",text="Contect",fg='white',font=("times new roman",20,"bold"))
cont_no.grid(row=5,column=0,sticky=W,padx=25,pady=20)
cont_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=contect_var)
cont_ent.grid(row=5,column=1)

dob_lbl = Label(eny_frm,bg="crimson",text="D.O.B",fg='white',font=("times new roman",20,"bold"))
dob_lbl.grid(row=6,column=0,sticky=W,padx=25,pady=20)
dob_ent = Entry(eny_frm,font=("times new roman",20,"bold"),relief=GROOVE,bd=3,textvariable=dob_var)
dob_ent.grid(row=6,column=1)

add_lbl = Label(eny_frm,bg="crimson",text="Address",fg='white',font=("times new roman",20,"bold"))
add_lbl.grid(row=7,column=0,sticky=W,padx=25,pady=25)
add_ent = Text(eny_frm,relief=GROOVE,bd=3,height=5,width=35)
add_ent.grid(row=7,column=1,pady=25)

#==== Buttom ====
btn_frm = Frame(eny_frm,bg="crimson",relief=RAISED,bd=2)
btn_frm.place(x=30,y=700,width=407,height=120)

add_btn = Button(btn_frm,text="Add",fg="black",bg="white",bd=4,cursor="hand2",relief=RAISED,width=14,font=("times new roman",15,"bold"))
add_btn.grid(row=0,column=0,pady=8,padx=13)

update_btn = Button(btn_frm,text="Update",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=13,font=("times new roman",15,"bold"))
update_btn.grid(row=0,column=2,pady=8,padx=10)

delete_btn = Button(btn_frm,text="Delete",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=14,font=("times new roman",15,"bold"))
delete_btn.grid(row=1,column=0,padx=13)

clr_btn = Button(btn_frm,text="Clear",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=13,font=("times new roman",15,"bold"))
clr_btn.grid(row=1,column=2,padx=10)


#================== View Deitels ==================== 

dtl_frm = Frame(root,bg="crimson",relief=RAISED,bd=4)
dtl_frm.place(x=530,y=135,width=820,height=845)

d_title = Label(dtl_frm,text="Search By",fg="white",font=("times new roman",19,"bold"),bg="crimson")
d_title.grid(row=0,columnspan=1,pady=20,padx=30)

sort = ttk.Combobox(dtl_frm,font=("times new roman",13,"bold"),state="readonly",width=15)
sort.grid(row=0,column=2)

search_ent = Entry(dtl_frm,font=("times new roman",13,"bold"),relief=GROOVE,bd=3,width=15)
search_ent.grid(row=0,column=3,padx=22)

search_btn = Button(dtl_frm,text="Delete",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=10,font=("times new roman",11,"bold"))
search_btn.grid(row=0,column=4,padx=10)

clear_btn = Button(dtl_frm,text="Clear",fg="black",cursor="hand2",bg="white",bd=4,relief=RAISED,width=10,font=("times new roman",11,"bold"))
clear_btn.grid(row=0,column=5,padx=10)

#======= Details show =======

table_frm = Frame(dtl_frm,bg="white",relief=RAISED,bd=4)
table_frm.place(x=30,y=95,width=750,height=720)

x_scrollbar = Scrollbar(table_frm,orient=HORIZONTAL)
y_scrollbar = Scrollbar(table_frm,orient=VERTICAL)
st_table = ttk.Treeview(table_frm,columns=("roll","name","email","gender","contect","dob","address"),xscrollcommand=x_scrollbar.set,yscrollcommand=y_scrollbar.set)
x_scrollbar.pack(side=BOTTOM,fill=X)
y_scrollbar.pack(side=RIGHT,fill=Y)

x_scrollbar.config(command=st_table.xview)
y_scrollbar.config(command=st_table.yview)

st_table.heading("roll",text="Roll No.")
st_table.heading("name",text="Name")
st_table.heading("email",text="Email Id")
st_table.heading("gender",text="Gender")
st_table.heading("contect",text="Contect")
st_table.heading("dob",text="D.O.B")
st_table.heading("address",text="Address")
st_table["show"] = "headings"
st_table.column("roll",width=50)
st_table.column("name",width=100)
st_table.column("email",width=100)
st_table.column("gender",width=60)
st_table.column("contect",width=100)
st_table.column("dob",width=80)
st_table.column("address",width=100)

st_table.pack(fill=BOTH,expand=TRUE)
#================== View Deitels Closed ====================

changecolor()
now_datetime()
root.mainloop()