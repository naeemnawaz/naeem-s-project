from tkinter import *
from tkinter import ttk
from pymysql import *
from tkinter import messagebox
import mysql.connector

import pymysql
root = Tk()
root.title('project')
root.geometry('1350x700')
title=Label(root,text="FEES MANAGEMENTS",bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='blue',fg='black')
title.pack(side=TOP,fill=X)



#decler variables
id_v = StringVar()
name_v = StringVar()
class_v = StringVar()
jan_v = StringVar()
feb_v =StringVar()
mar_v = StringVar()
apr_v = StringVar()
may_v = StringVar()
jun_v = StringVar()
jul_v = StringVar()
aug_v = StringVar()
spt_v = StringVar()
oct_v = StringVar()
nov_v = StringVar()
dec_v = StringVar()
search_by = StringVar()
search_var = StringVar()

# define clear function
def clear_for_add():
    id_v.set('')
    name_v.set('')
    class_v.set('')
    jan_v.set('')
    feb_v.set('')
    mar_v.set('')
    apr_v.set('')
    may_v.set('')
    jun_v.set('')
    jul_v.set('')
    aug_v.set('')
    spt_v.set('')
    oct_v.set('')
    nov_v.set('')
    dec_v.set('')

# searcing function decleartion
def search_data():
    search = (search_by.get())
    print((search, ),'thsi')
    if ((search, ))== (('ID',)):
        con = pymysql.connect(host="localhost",user="root",password="",database="record")
        c = con.cursor()
        #c.execute("SELECT * FROM student where"+str(search_by.get()+"LIKE '%"+str(search_var.get()+"%'")))
        sql = "SELECT * from fees WHERE id = %s "
        val = (search_var.get())
        c.execute(sql, (val, ))
        rows = c.fetchall()
        if len(rows)!=0:
            record.delete(*record.get_children())
            for row in rows:
                record.insert('',END,values=row)
                con.commit()
        con.close()
        print('roll HERE IS')
    elif ((search, )) == (('NAME',)):
        con = pymysql.connect(host="localhost",user="root",password="",database="record")
        c = con.cursor()
        #c.execute("SELECT * FROM student where"+str(search_by.get()+"LIKE '%"+str(search_var.get()+"%'")))
        sql = "SELECT * from fees WHERE name = %s "
        val = (search_var.get())
        c.execute(sql, (val, ))
        rows = c.fetchall()
        if len(rows)!=0:
            record.delete(*record.get_children())
            for row in rows:
                record.insert('',END,values=row)
                con.commit()
        con.close()
        print('name HERE IS')


# define fetch function
def fetch_data():
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()
    c.execute("SELECT * FROM fees")
    rows=c.fetchall()
    if len(rows)!=0:
        record.delete(*record.get_children())
        for row in rows:
            record.insert('',END,values=row)
            con.commit()
    con.close()

# deifne delete function
def delete_data():
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()
    c.execute("delete from fees where id= %s ",id_v.get())
    con.commit()
    con.close()
    fetch_data()
    clear_for_add()


def add_studnet():
    global jan_v, feb_v, mar_v,apr_v , may_v, jun_v, jul_v , aug_v , spt_v , oct_v , nov_v , dec_v

    # if for null VALUES
    if jan_v == '':
        jan_v = ''

    if feb_v == '':
        feb_v = ''

    if mar_v =='':
        mar_v = ''

    if apr_v == '':
        apr_v = ''

    if may_v == '':
        may_v= ''

    if jun_v == '':
        jun_v=''

    if jul_v == '':
        jul_v = ''
    if aug_v =='':
        aug_v = ''

    if spt_v =='':
        spt_v = ''

    if oct_v == '':
        oct_v = ''

    if nov_v == '':
        nov_v= ''

    if dec_v =='':
        dec_v = ''
    if id_v.get()=="" or name_v.get()=="":
        messagebox.showerror("ERROR","ID AND NAME MUST INSERT")
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="",database="record")
            cur = con.cursor()
            change = "insert into fees (id ,name,class,jan,feb,mar,apr,may,jun,jul,aug,spt,oct,nov,de ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = ( id_v.get() ,name_v.get() ,class_v.get() , jan_v.get() , feb_v.get() , mar_v.get() , apr_v.get() , may_v.get() , jun_v.get() , jul_v.get() , aug_v.get() , spt_v.get() , oct_v.get() , nov_v.get() ,  dec_v.get())
            cur.execute(change,value)
            fetch_data()
            clear_for_add()
            print('the record are submmited ')
            con.commit()
            con.close()
            messagebox.showinfo("INFO","data have been inserted")
        except:
            messagebox.showerror('ERROR','ID NO IS ALREADY EXIST')




# update function declartion
def update():
    global name_v , id_v
    mydb = pymysql.connect(host="localhost",user="root",password="",database="record")
    mycursor = mydb.cursor()

    sql = "UPDATE fees SET name = %s , class = %s, jan = %s, feb = %s, mar = %s , apr = %s , may = %s ,jun = %s, jul = %s,aug = %s,spt = %s,oct = %s,nov = %s,de = %s WHERE id = %s "
    val = (name_v.get(), class_v.get(),jan_v.get(), feb_v.get(),mar_v.get(),apr_v.get(),may_v.get(),jun_v.get(),jul_v.get(),aug_v.get(),spt_v.get(),oct_v.get(),nov_v.get(),dec_v.get(),id_v.get())

    mycursor.execute(sql,val)

    mydb.commit()
    clear_for_add()
    fetch_data()
    messagebox.showinfo('INFO','Data has been updated!')
    print('name is updated')






# define fetch function

#
# record name etc frame
record1 = Frame(root,bd=4,relief=RIDGE,bg='gray')
record1.place(x=10,y=100,width=650,height='150')

lid = Label(record1,text='ID NO',bg='gray',fg='black',font=('times new roman',20,'bold'))
lid.grid(row=0,column=0,pady=10,padx=20,sticky='w')
txt_id=Entry(record1,width=10,textvariable=id_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_id.grid(row=0,column=1,pady=10,padx=20,sticky='w')

lname = Label(record1,text='NAME',bg='gray',fg='black',font=('times new roman',20,'bold'))
lname.grid(row=0,column=2,pady=10,padx=20,sticky='w')
txt_name=Entry(record1,width=18,textvariable=name_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_name.grid(row=0,column=3,pady=10,padx=20,sticky='w')
lcls = Label(record1,text='CLASS:',bg='gray',fg='black',font=('times new roman',20,'bold'))
lcls.grid(row=1,column=0,pady=10,padx=20,sticky='w')
txt_cls=Entry(record1,width=10,textvariable=class_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_cls.grid(row=1,column=1,pady=10,padx=20,sticky='w')
# maagement fream
manage_fram=Frame(root,bd=4,relief=RIDGE,bg='blue')
manage_fram.place(x=10,y=250,width=650,height=400)

#button frame inside managements frames



ljen = Label(manage_fram,text='January',bg='blue',fg='black',font=('times new roman',20,'bold'))
ljen.grid(row=1,column=0,pady=10,padx=20,sticky='w')
txt_roll=Entry(manage_fram,width=10,textvariable=jan_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

lfeb = Label(manage_fram,text='February',bg='blue',fg='black',font=('times new roman',20,'bold'))
lfeb.grid(row=1,column=2,pady=10,padx=20,sticky='w')
txt_feb=Entry(manage_fram,width=10,textvariable=feb_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_feb.grid(row=1,column=3,pady=10,padx=20,sticky='w')

lmar = Label(manage_fram,text='march',bg='blue',fg='black',font=('times new roman',20,'bold'))
lmar.grid(row=2,column=0,pady=10,padx=20,sticky='w')
txt_mar=Entry(manage_fram,width=10,textvariable=mar_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_mar.grid(row=2,column=1,pady=10,padx=20,sticky='w')

lapr = Label(manage_fram,text='April',bg='blue',fg='black',font=('times new roman',20,'bold'))
lapr.grid(row=2,column=2,pady=10,padx=20,sticky='w')
apr=Entry(manage_fram,width=10,textvariable=apr_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
apr.grid(row=2,column=3,pady=10,padx=20,sticky='w')

lmay = Label(manage_fram,text='May',bg='blue',fg='black',font=('times new roman',20,'bold'))
lmay.grid(row=3,column=0,pady=10,padx=20,sticky='w')
may =Entry(manage_fram,width=10,textvariable=may_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
may.grid(row=3,column=1,pady=10,padx=20,sticky='w')

ljun = Label(manage_fram,text='June',bg='blue',fg='black',font=('times new roman',20,'bold'))
ljun.grid(row=3,column=2,pady=10,padx=20,sticky='w')
jun=Entry(manage_fram,width=10,textvariable=jun_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
jun.grid(row=3,column=3,pady=10,padx=20,sticky='w')

ljul = Label(manage_fram,text='July',bg='blue',fg='black',font=('times new roman',20,'bold'))
ljul.grid(row=4,column=0,pady=10,padx=20,sticky='w')
jul=Entry(manage_fram,width=10,textvariable=jul_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
jul.grid(row=4,column=1,pady=10,padx=20,sticky='w')

laug= Label(manage_fram,text='August',bg='blue',fg='black',font=('times new roman',20,'bold'))
laug.grid(row=4,column=2,pady=10,padx=20,sticky='w')
aug=Entry(manage_fram,width=10,textvariable=aug_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
aug.grid(row=4,column=3,pady=10,padx=20,sticky='w')

lspt = Label(manage_fram,text='September',bg='blue',fg='black',font=('times new roman',20,'bold'))
lspt.grid(row=5,column=0,pady=10,padx=20,sticky='w')
spt=Entry(manage_fram,width=10,textvariable=spt_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
spt.grid(row=5,column=1,pady=10,padx=20,sticky='w')

loct = Label(manage_fram,text='October',bg='blue',fg='black',font=('times new roman',20,'bold'))
loct.grid(row=5,column=2,pady=10,padx=20,sticky='w')
oct=Entry(manage_fram,width=10,textvariable=oct_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
oct.grid(row=5,column=3,pady=10,padx=20,sticky='w')

lnmb = Label(manage_fram,text='November',bg='blue',fg='black',font=('times new roman',20,'bold'))
lnmb.grid(row=6,column=0,pady=10,padx=20,sticky='w')
nmb=Entry(manage_fram,width=10,textvariable=nov_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
nmb.grid(row=6,column=1,pady=10,padx=20,sticky='w')

ldec = Label(manage_fram,text='December',bg='blue',fg='black',font=('times new roman',20,'bold'))
ldec.grid(row=6,column=2,pady=10,padx=20,sticky='w')
dec=Entry(manage_fram,width=10,textvariable=dec_v,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
dec.grid(row=6,column=3,pady=10,padx=20,sticky='w')
#print(id_v,'id_v')
iid = id_v.get()
iname =name_v.get()
iclass=class_v.get()
ijan=jan_v.get()
ifeb=feb_v.get()
imar=mar_v.get()
iapr=apr_v.get()
imay=may_v.get()
ijun=jun_v.get()
ijul=jul_v.get()
iaug=aug_v.get()
ispt=spt_v.get()
ioct=oct_v.get()
inov=nov_v.get()
idec=dec_v.get()
#print(iid,iname,"iid iname")


# detial frames
detial_fram=Frame(root,bd=4,relief=RIDGE,bg='blue')
detial_fram.place(x=650,y=100,width=700,height=600)

#btn frames
btn_fram=Frame(root,bd=4,relief=RIDGE,bg='gray')
btn_fram.place(x=10,y=600 ,width=650,height='150')



addbtn = Button(btn_fram,text='Add',width=15,height=3,command=add_studnet).grid(row=0,column=0,pady=10,padx=20,sticky='w')
update = Button(btn_fram,text='update',width=15,height=3,command=update).grid(row=0,column=1,pady=10,padx=20,sticky='w')
delete = Button(btn_fram,text='delete',width=15,height=3,command=delete_data).grid(row=0,column=2,pady=10,padx=20,sticky='w')
clear = Button(btn_fram,text='clear',width=15,height=3,command=clear_for_add).grid(row=0,column=3,pady=10,padx=20,sticky='w')
#
# search frames
search_frame = Frame(detial_fram,bd=4,relief=RIDGE,bg='gray')
search_frame.place(width=700,height=70)


combo_search=ttk.Combobox(detial_fram,width=10,textvariable=search_by,font=('times new roman',15,'bold'))
combo_search['values']=('ID','NAME')
combo_search.grid(row=0,column=1,padx=20,pady=10)

       # gender


txt_search=Entry(detial_fram,width=20,textvariable=search_var,font=('times new roman','10','roman'),bd=5,relief=GROOVE)
txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

searchbtn=Button(detial_fram,text='Search',width=10,command=search_data).grid(row=0,column=3,padx=10,pady=10)
showbtn=Button(detial_fram,text='Show all',width=10,command=fetch_data).grid(row=0,column=4,padx=10,pady=10)

# table frames
table_fram=Frame(detial_fram,bd=4,relief=RIDGE,bg='green')
table_fram.place(width=700,height=510,y=60)




scroll_x=Scrollbar(table_fram,orient=HORIZONTAL)
scroll_y=Scrollbar(table_fram,orient=VERTICAL)
record = ttk.Treeview(table_fram,columns=('Id','Name','Class','January','February','March','April','May','June','July','August','September','October','November','December'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=record.xview)
scroll_y.config(command=record.yview)
record.heading('Id',text='Id')
record.heading('Name',text='Name')
record.heading('Class',text='Class')
record.heading('January',text='January')
record.heading('February',text='February')
record.heading('March',text='march')
record.heading('April',text='April')
record.heading('May',text='May')
record.heading('June',text='June')
record.heading('July',text='July')
record.heading('August',text='August')
record.heading('September',text='September')
record.heading('October',text='October')
record.heading('November',text='November')
record.heading('December',text='December')
record['show']='headings'
record.column('Id',width=40)
record.column('Name',width=150)
record.column('Class',width=100)
record.column('January',width=50)
record.column('February',width=50)
record.column('March',width=50)
record.column('April',width=50)
record.column('May',width=50)
record.column('June',width=50)
record.column('July',width=50)
record.column('August',width=50)
record.column('September',width=50)
record.column('October',width=50)
record.column('November',width=50)
record.column('December',width=50)
record.pack(fill=BOTH,expand=1)

# get cursor
def get_cursor(ev):
    cursor_row=record.focus()
    contents=record.item(cursor_row)
    row=contents['values']
#    print(row)
    roll_no_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])
    dob_var.set(row[5])


def get_cursor(ev):
    cursor_row=record.focus()
    contents=record.item(cursor_row)
    row=contents['values']
#    pr row)
    id_v.set(row[0])
    name_v.set(row[1])
    class_v.set(row[2])
    jan_v.set(row[3])
    feb_v.set(row[4])
    mar_v.set(row[5])
    apr_v.set(row[6])
    may_v.set(row[7])
    jun_v.set(row[8])
    jul_v.set(row[9])
    aug_v.set(row[10])
    spt_v.set(row[11])
    oct_v.set(row[12])
    nov_v.set(row[13])
    dec_v.set(row[14])


# record.bind("<ButtonRelease-1>",get_cursor)
# get function
record.bind("<ButtonRelease-1>",get_cursor)

fetch_data()




root.mainloop()
