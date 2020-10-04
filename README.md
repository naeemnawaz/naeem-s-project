# just for fun
# this project is created by python tkinter mysql , perpos of this project collect the data of students 

from tkinter import *
import pymysql
from tkinter import ttk

from tkinter import messagebox

root = Tk()
root.title('project')
root.geometry('1350x700')
con = pymysql.connect(host="localhost",user="root",password="",database="record")
c = con.cursor()
# head lebel
title=Label(root,text="naeem's  project",bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='black',fg='white')
title.pack(side=TOP,fill=X)
# make variables


roll_no_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var = StringVar()
addres = StringVar()
search_by = StringVar()
search_var = StringVar()
# define all funcitonss
def fetch_data():
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()
    c.execute("SELECT * FROM student")
    rows=c.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',END,values=row)
            con.commit()
    con.close()




# function for search data
def search_data():
    search = (search_by.get())
    print((search, ),'thsi')
    if ((search, ))== (('ROLL',)):
        con = pymysql.connect(host="localhost",user="root",password="",database="record")
        c = con.cursor()
        #c.execute("SELECT * FROM student where"+str(search_by.get()+"LIKE '%"+str(search_var.get()+"%'")))
        sql = "SELECT * from student WHERE roll = %s "
        val = (search_var.get())
        c.execute(sql, (val, ))
        rows = c.fetchall()
        if len(rows)!=0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('',END,values=row)
                con.commit()
        con.close()
        print('roll HERE IS')
    elif ((search, )) == (('NAME',)):
        con = pymysql.connect(host="localhost",user="root",password="",database="record")
        c = con.cursor()
        #c.execute("SELECT * FROM student where"+str(search_by.get()+"LIKE '%"+str(search_var.get()+"%'")))
        sql = "SELECT * from student WHERE name = %s "
        val = (search_var.get())
        c.execute(sql, (val, ))
        rows = c.fetchall()
        if len(rows)!=0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('',END,values=row)
                con.commit()
        con.close()
        print('name HERE IS')

#
# define add function
def nnn():
    global roll_no_var , name_var , email_var , gender_var , contact_var , dob_var
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()
    query = "INSERT INTO student (roll , name , email, gender , contact, dob, text='') VALUES(%s,%s,%s,%s,%s,%s,%s,)"
    val = (roll_no_var.get(),name_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get())
    clear_for_add()
    c.execute(query , val)
    print('inserted data')
    con.commit()
    fetch_data()
    c.close()

# define clear function
def clear_for():
    roll_no_var.set('')
    name_var.set('')
    email_var.set('')
    gender_var.set('')
    contact_var.set('')
    dob_var.set('')
    #txt_address.set('')
def add_Student():
    naeem ='empty'
    if roll_no_var.get()=="" or name_var=="":
        messagebox.showerror("error","ROLL AND NAME MUST INSERT!")
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="",database="record")
            cur = con.cursor()
            change = "insert into student (roll , name , email , gender , contact ,dob , text ) values(%s,%s,%s,%s,%s,%s,%s)"
            value = (roll_no_var.get(),name_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get(),naeem)
            cur.execute(change,value)
            print(gender_var.get())
            fetch_data()
            clear_for()
            print('the record are submmited ')
            con.commit()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
        except:
            messagebox.showerror("ERROR","Roll NO is already exist")






#    SELECT * FROM Customers
#WHERE City='Berlin' OR City='München';
# update function
def update():
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()

    sql = "UPDATE student SET name =%s,email =%s,gender=%s,contact=%s,dob=%s WHERE roll = %s "
    val = (name_var.get(),email_var.get(),gender_var.get(),contact_var.get(),dob_var.get(),roll_no_var.get())

    c.execute(sql,val)

    con.commit()
    con.close()
    clear_for()
    fetch_data()
    print('name is updated')




# define clear function
def clear_for_add():
    roll_no_var.set('')
    name_var.set('')
    email_var.set('')
    gender_var.set('')
    contact_var.set('')
    dob_var.set('')
    #txt_address.set('')

# define delete function
def delete_data():
    con = pymysql.connect(host="localhost",user="root",password="",database="record")
    c = con.cursor()
    c.execute("delete from student where roll= %s ",roll_no_var.get())
    con.commit()
    con.close()
    fetch_data()
    clear_for_add()


# magage frame
manage_fram=Frame(root,bd=4,relief=RIDGE,bg='blue')
manage_fram.place(x=20,y=100,width=450,height=600)

m_title = Label(manage_fram,text='MANAGEMENTS',bg='blue',fg='white',font=('times new roman',20,'bold'))
m_title.grid(row=0,columnspan=2,pady=20,sticky='w')

roll = Label(manage_fram,text='Roll No',bg='blue',fg='white',font=('times new roman',20,'bold'))
roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

txt_roll=Entry(manage_fram,textvariable=roll_no_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

name = Label(manage_fram,text='Name',bg='blue',fg='white',font=('times new roman',20,'bold'))
name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

txtname=Entry(manage_fram,textvariable=name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txtname.grid(row=2,column=1,pady=10,padx=20,sticky='w')

email = Label(manage_fram,text='Father Name',bg='blue',fg='white',font=('times new roman',20,'bold'))
email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

txtemail=Entry(manage_fram,textvariable=email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txtemail.grid(row=3,column=1,pady=10,padx=20,sticky='w')

gender = Label(manage_fram,text='Gender',bg='blue',fg='white',font=('times new roman',20,'bold'))
gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

combo_gender=ttk.Combobox(manage_fram,textvariable=gender_var,font=('times new roman',15,'bold'))
combo_gender['values']=('male','female','other')
combo_gender.grid(row=4,column=1,padx=10,pady=20)
       # gender
       #txt_gender=Entry(manage_fram,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
       #txt_roll.grid(row=4,column=1,pady=10,padx=20,sticky='w')
contact = Label(manage_fram,text='Contact',bg='blue',fg='white',font=('times new roman',20,'bold'))
contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

txt_contact=Entry(manage_fram,textvariable=contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

dob = Label(manage_fram,text='D O B',bg='blue',fg='white',font=('times new roman',20,'bold'))
dob.grid(row=6,column=0,pady=10,padx=20,sticky='w')

txt_dob=Entry(manage_fram,textvariable=dob_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')

address = Label(manage_fram,text='Address',bg='blue',fg='white',font=('times new roman',20,'bold'))
address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

txt_address = Entry(manage_fram,textvariable=addres,font=("times new roman",15,'bold'),bd=5,relief=GROOVE)
txt_address.grid(row=7,column=1,padx=10,pady=20,sticky='w')
       #change entry into textvariable
rroll=roll_no_var.get()
nname=name_var.get()
eemail=email_var.get()
ggender=gender_var.get()
ccontact= contact_var.get()
ddob=dob_var.get()
#ttxt_address=txt_address.get()

###### button frame
btn_fram=Frame(root,bd=4,relief=RIDGE,bg='blue')
btn_fram.place(x=20,y=630 ,width=430)



addbtn = Button(btn_fram,text='Add',width=10,command=add_Student).grid(row=0,column=0,padx=10,pady=10)
update = Button(btn_fram,text='update',width=10,command=update).grid(row=0,column=1,padx=10,pady=10)
delete = Button(btn_fram,text='delete',width=10,command=delete_data).grid(row=0,column=2,padx=10,pady=10)
clear = Button(btn_fram,text='clear',width=10,command=clear_for_add).grid(row=0,column=3,padx=10,pady=10)

# detial frames
detial_fram=Frame(root,bd=4,relief=RIDGE,bg='blue')
detial_fram.place(x=500,y=100,width=800,height=600)

lblsearch = Label(detial_fram,width = 10,text='search by',bg='blue',fg='white',font=('times new roman',20,'bold'))
lblsearch.grid(row=0,column=0,pady=10,padx=20,sticky='w')
RR = 'ROLL'
NN = 'NAME'
CO = 'Contact'
#combo_search=ttk.Combobox(detial_fram,textvariable=search_by,width=10,font=('times new roman',13,'bold'),state='readnoly')
#combo_search['values']=(RR,NN,CO)
#combo_search.grid(row=0,column=1,padx=20,pady=10)

combo_search=ttk.Combobox(detial_fram,width=10,textvariable=search_by,font=('times new roman',15,'bold'))
combo_search['values']=('ROLL','NAME','contact')
combo_search.grid(row=0,column=1,padx=20,pady=10)

       # gender


txt_search=Entry(detial_fram,width=20,textvariable=search_var,font=('times new roman','10','roman'),bd=5,relief=GROOVE)
txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

searchbtn=Button(detial_fram,text='Search',width=10,command=search_data).grid(row=0,column=3,padx=10,pady=10)
showbtn=Button(detial_fram,text='Show all',width=10,command=fetch_data).grid(row=0,column=4,padx=10,pady=10)

# tables frames in the detial tables
table_fram=Frame(detial_fram,bd=4,relief=RIDGE,bg='crimson')
table_fram.place(x=10,y=70,width=750,height=500)

scroll_x=Scrollbar(table_fram,orient=HORIZONTAL)
scroll_y=Scrollbar(table_fram,orient=VERTICAL)
student_table = ttk.Treeview(table_fram,columns=('roll','name','Father Name','gender','contact','D O B','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading('roll',text='Roll NO')
student_table.heading('name',text='Name')
student_table.heading('Father Name',text='Father Name')
student_table.heading('contact',text='contact')
student_table.heading('gender',text='Gender')
student_table.heading('D O B',text='D O B')
student_table.heading('address',text='Address')
student_table['show']='headings'
student_table.column('roll',width=50)
student_table.column('name',width=150)
student_table.column('Father Name',width=150)
student_table.column('contact',width=150)
student_table.column('gender',width=50)
student_table.column('D O B',width=150)
student_table.column('address',width=200)
student_table.pack(fill=BOTH,expand=1)
def get_cursor(ev):
    cursor_row=student_table.focus()
    contents=student_table.item(cursor_row)
    row=contents['values']
#    print(row)
    roll_no_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])
    dob_var.set(row[5])

#this clear fucntion is for add_studnet function
def clear_for_add():
    roll_no_var.set('')
    name_var.set('')
    email_var.set('')
    gender_var.set('')
    contact_var.set('')
    dob_var.set('')

student_table.bind("<ButtonRelease-1>",get_cursor)
# get function

fetch_data()



con.commit()
con.close()
root.mainloop()
