import random
import string
import tkinter.messagebox
from datetime import date
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
from PIL import ImageTk


def std():
    pass


today = date.today()
print('work in progress')
firstw = Tk()
firstw.title("shriyash jr. college ")
firstw.geometry("1600x1000+0+0")
lablbg = Label(firstw, bg='black')
lablbg.place(x=00, y=0, relheight=1, relwidth=1)
# bg2 = ImageTk.PhotoImage(file="b.jpg")
# lablbg = Label(firstw, image=bg2)
# lablbg.place(x=200, y=62, relheight=1, relwidth=1)

label = Label(text="shriyash jr. college", font=("times new roman", 40), bg="aqua")
label.pack(side=TOP, fill=X)


def std():
    enquiry_1()



bg1 = ImageTk.PhotoImage(file="a.jpg")
lablee = Label(firstw, image=bg1)
lablee.place(x=130, y=200, width=600, height=450)

fram = Frame(firstw, bd=1, bg='white', relief=RIDGE)
fram.place(x=700, y=200, width=600, height=450)
login1 = Label(fram, text='Login Here', bg='white', fg='blue', font=('times new roman', '25', 'bold'))
login1.place(x=30, y=20)
user1 = Label(fram, bg='white', text="USERNAME", font=("arial", 23))
user1.place(x=190, y=70)
user = Entry(fram, width=17, bd=5, font=("arial", 20))
user.place(x=150, y=150)
user2 = Label(fram, text="PASSWORD", bg='white', font=("arial", 23))
user2.place(x=190, y=220)
user3 = Entry(fram, width=17, show="*", bd=5, font=("arial", 20))
user3.place(x=150, y=290)
student = Button(firstw, text='Student Queries', width=25, font=('times new roman', '25'), command=std, bg='green')
student.place(x=200, y=550)


# login field

def distroy():
    firstw.destroy()


def login():
    if user.get() == "" and user3.get() == '':
        main_window()
        distroy()

    else:
        t = tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ",
                                        "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
        user.delete(0, END)
        user3.delete(0, END)


# all the functions are here which relates to the main window

# registration is started from here


def registration_main():
    root = Tk()
    root.geometry("1600x1000+0+0")
    root.title("Registration Form")
   
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global box
    global box1
    global name
    global radio1
    global radio2
    global sur
    global gender
    global var1
    global var2
    global branch
    global box1
    global email
    global calculate
    global prn
    global s_earch
    branch = StringVar()
    name = StringVar()
    sur = StringVar()
    gender = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    course = StringVar()
    email = StringVar()
    box1 = StringVar()
    calculate = StringVar()
    id = IntVar()
    search = IntVar()
    prnt = IntVar()
    s_earch = StringVar()

    CALCULATE = calculate.get()
    calculation2 = 0
    prnt.set("")
    label = Label(root, text="REGISTRATION FORM", font=("times new roman", 25), bg="violetred1")
    label.pack(side=TOP, fill=X)

    label1 = Label(root, text="NAME:", font=("arial", 17))
    label1.place(x=300, y=150)

    label2 = Label(root, text="SURNAME:", font=("arial", 17))
    label2.place(x=300, y=210)

    label3 = Label(root, text="EMAIL:", font=("arial", 17))
    label3.place(x=300, y=270)

    label3 = Label(root, text="GANDER:", font=("arial", 17))
    label3.place(x=300, y=330)

    label4 = Label(root, text="BRANCH:", font=("arial", 17))
    label4.place(x=300, y=390)

    label4 = Label(root, text="COURSE", font=("arial", 17))
    label4.place(x=300, y=450)

    label4 = Label(root, text="TOTAL FEE", font=("arial", 17))
    label4.place(x=300, y=520)
    prnl = Label(root, text="User ID ", font=("arial", 17))
    prnl.place(x=1200, y=150)
    # ==============================entryfield========================================

    entry5 = Entry(root, textvariable=calculate, state="readonly", width=20, font=("arial", 15, "bold"), bd=5)
    entry5.place(x=500, y=515)

    entry1 = Entry(root, bd=5, width=20, textvariable=name, font=("arial", 15))
    entry1.place(x=500, y=150)


    entry2 = Entry(root, bd=5, width=20, textvariable=sur, font=("arial", 15))
    entry2.place(x=500, y=210)

    entry3 = Entry(root, bd=5, width=20, textvariable=email, font=("arial", 15))
    entry3.place(x=500, y=270)

    entry4 = Entry(root, bd=5, width=30, textvariable=search, font=("arial", 15))
    entry4.place(x=1000, y=70)
    search.set('')

    prn = Entry(root, bd=5, width=30, textvariable=prnt, state='disabled', font=("arial", 15))
    prn.place(x=800, y=150)

    # ================================radio buttton=======================================

    radio1 = Radiobutton(root, text="MALE", variable=gender, value=1, font=("arial", 13))
    radio1.place(x=510, y=340)

    radio2 = Radiobutton(root, text="FEMALE", variable=gender, padx=20, value=2, font=("arial", 13))
    radio2.place(x=590, y=340)
    gender.set(3)

    # ================================droplist======================================

    box = ttk.Combobox(root, textvariable=branch, state="readonly", font=("arial", 12, "bold"), width=22)
    box['values'] = ['SELECT', 'COMPUTER SCINCE', 'MACHENICAL', 'CIVIL', 'IT', 'ELECTRICAL', 'E&TC']
    box.current(0)
    box.place(x=503, y=395)

    box_search = ttk.Combobox(root, textvariable=s_earch, state="readonly", font=("arial", '15', "bold"), width=22)
    box_search['values'] = ['Sarch By', 'Name', 'Surname', 'User Id']
    box_search.current(0)
    box_search.place(x=720, y=70)

    # ===============================checkbutton====================================
    #
    # checkbutton1 = Checkbutton(root, text="JAVA", variable=java)
    # checkbutton1.place(x=502, y=455)
    #
    # checkbutton1 = Checkbutton(root, text="C", variable=c)
    # checkbutton1.place(x=555, y=455)
    #
    # checkbutton1 = Checkbutton(root, text="C++", variable=cpp)
    # checkbutton1.place(x=600, y=455, )
    # checkbutton1 = Checkbutton(root, text="PYTHON", variable=python)
    # checkbutton1.place(x=650, y=455)

    box1 = ttk.Combobox(root, textvariable=course, state="readonly", font=("arial", 12, "bold"), width=22)
    box1['values'] = ['SELECT', 'JAVA', 'C', 'CPP', 'PYTHON', 'JAVASCRIPT']
    box1.current(0)
    box1.place(x=502, y=455)

    def dis():
        # this will destroy the another window which is already open
        root.destroy()

    def calculation():

        if box1.get() == 'PYTHON':
            entry5.configure(state="normal")
            entry5.delete(0, END)
            entry5.insert(0, 9000)
            entry5.configure(state="disabled")
        elif box1.get() == 'CPP':
            entry5.configure(state="normal")
            entry5.delete(0, END)
            entry5.insert(0, 4000)
            entry5.configure(state="disabled")
        elif box1.get() == 'C':
            entry5.configure(state="normal")
            entry5.delete(0, END)
            entry5.insert(0, 5000)
            entry5.configure(state="disabled")
        elif box1.get() == 'JAVASCRIPT':
            entry5.configure(state="normal")
            entry5.delete(0, END)
            entry5.insert(0, 1000)
            entry5.configure(state="disabled")
        elif box1.get() == 'JAVA':
            entry5.configure(state="normal")
            entry5.delete(0, END)
            entry5.insert(0, 8000)
            entry5.configure(state="disabled")

    def msg():

        FEE = calculate.get()
        NAME = name.get()
        SUR = sur.get()
        EMAIL = email.get()
        BRANCH = branch.get()
        GENDER = gender.get()
        COURSE = box1.get()
        print(NAME, SUR, EMAIL, BRANCH, COURSE, GENDER)
        # print(name.get(),branch.get(),sur.get(),course.get(),email.get())
        if NAME == ("") and SUR == ("") and EMAIL == ("") and BRANCH == ("SELECT") and GENDER == (3) and COURSE == (
                "SELECT"):
            messagebox.showinfo(" DETAILS INVALID", "FILL ALL THE DETAILS")

        nums = list(string.digits)
        pas = []
        for i in range(5):
            pas.append(random.choice(nums))

        a = ''.join(pas)
        PRN = f'ST{a}'
        print(PRN)

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor = mysqldb.cursor()

        try:
            sql = "INSERT INTO  registration (name_db,userid,sur_db,email_db,branch_db,course_db,fee_db,gender_db,rfee_db) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (NAME, PRN, SUR, EMAIL, BRANCH, COURSE, FEE, GENDER, FEE)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.fetchone()
            print(lastid)
            messagebox.showinfo("information", "Employee inserted successfully...")

            prn.configure(state='normal')
            prn.insert(END, PRN)
            prn.configure(state='disabled')

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def clear():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        box.set("SELECT")
        gender.set(3)
        calculate.set("0.00")
        entry4.delete(0, END)
        box1.set("SELECT")
        prn.configure(state='normal')
        prn.delete(0, END)
        prn.configure(state='disabled')

    def all():
        search1 = s_earch.get()
        print(search1)
        if search1 == 'Name':
            search_db = entry4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
            mycursor = mysqldb.cursor()

            try:
                mycursor.execute("SELECT * FROM registration where name_db = '" + search_db + " '")
                records = mycursor.fetchall()
                print(list(records))
                for i in records:
                    b = i[4]
                    c = i[5]
                    print(i)
                    entry1.delete(0, END)
                    entry1.insert(END, i[1])
                    entry2.delete(0, END)
                    entry2.insert(END, i[2])
                    entry3.delete(0, END)
                    entry3.insert(END, i[3])
                    gender.set(i[7])
                    branch.set(f"{b}")
                    course.set(f'{c}')
                    entry5.configure(state='normal')
                    entry5.delete(0, END)
                    entry5.insert(END, i[6])
                    entry5.configure(state='disabled')

            except:
                mysqldb.rollback()
                mysqldb.close()



        elif search1 == 'Surname':
            search_db = entry4.get()

            mysqldb1 = mysql.connector.connect(host="localhost", user="root", password="", database="course")
            mycursor1 = mysqldb1.cursor()
            print('hii')
            try:
                mycursor1.execute("SELECT * FROM registration where sur_db = '" + search_db + " '")
                records1 = mycursor1.fetchall()
                print(list(records1))
                for i in records1:
                    b = i[4]
                    c = i[5]
                    print(i)
                    entry1.delete(0, END)
                    entry1.insert(END, i[1])
                    entry2.delete(0, END)
                    entry2.insert(END, i[2])
                    entry3.delete(0, END)
                    entry3.insert(END, i[3])
                    gender.set(i[7])
                    branch.set(f"{b}")
                    course.set(f'{c}')
                    entry5.configure(state='normal')
                    entry5.delete(0, END)
                    entry5.insert(END, i[6])
                    entry5.configure(state='disabled')
                print('hii')
            except:
                mysqldb1.rollback()
                mysqldb1.close()

        #
        #
        #
        elif search1 == 'User Id':
            search_db = entry4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
            mycursor = mysqldb.cursor()

            try:
                mycursor.execute("SELECT * FROM registration where userid = '" + search_db + " '")
                records = mycursor.fetchall()
                print(list(records))
                for i in records:
                    b = i[4]
                    c = i[5]
                    print(i)
                    entry1.delete(0, END)
                    entry1.insert(END, i[1])
                    entry2.delete(0, END)
                    entry2.insert(END, i[2])
                    entry3.delete(0, END)
                    entry3.insert(END, i[3])
                    gender.set(i[7])
                    branch.set(f"{b}")
                    course.set(f'{c}')
                    entry5.configure(state='normal')
                    entry5.delete(0, END)
                    entry5.insert(END, i[6])
                    entry5.configure(state='disabled')

            except:
                mysqldb.rollback()
                mysqldb.close()

        else:
            search_db = entry4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
            mycursor = mysqldb.cursor()

            try:
                mycursor.execute("SELECT * FROM registration where id = '" + search_db + " '")
                records = mycursor.fetchall()
                print(list(records))
                for i in records:
                    b = i[4]
                    c = i[5]
                    print(i)
                    entry1.delete(0, END)
                    entry1.insert(END, i[1])
                    entry2.delete(0, END)
                    entry2.insert(END, i[2])
                    entry3.delete(0, END)
                    entry3.insert(END, i[3])
                    gender.set(i[7])
                    branch.set(f"{b}")
                    course.set(f'{c}')
                    entry5.configure(state='normal')
                    entry5.delete(0, END)
                    entry5.insert(END, i[6])
                    entry5.configure(state='disabled')

            except:
                mysqldb.rollback()
                mysqldb.close()

    def update():
        FEE = calculate.get()
        NAME = name.get()
        SUR = sur.get()
        EMAIL = email.get()
        BRANCH = branch.get()
        GENDER = gender.get()
        COURSE = box1.get()
        ID = entry4.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor = mysqldb.cursor()

        try:
            sql = "Update  registration set name_db= %s,sur_db= %s,email_db= %s,branch_db= %s,course_db= %s,fee_db= %s,gender_db=%s where id= %s"
            val = (NAME, SUR, EMAIL, BRANCH, COURSE, FEE, GENDER, ID)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Updateddddd successfully...")

            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            box.set("SELECT")
            gender.set(3)
            calculate.set("")
            entry4.delete(0, END)
            box1.set("SELECT")

        except Exception as e:

            print(e)
            mysqldb.rollback()
            mysqldb.close()

    # =========================buttton==========================

    button1 = Button(root, text="CALCULATE FEE", width=14, font=("arial", 10), bg="indianred1", command=calculation)
    button1.place(x=530, y=630)

    button12 = Button(root, text="BACK", width=17, font=("arial", 17), bg="indianred1", command=dis)
    button12.place(x=0, y=0)

    button2 = Button(root, text="SUBMIT FORM", width=14, font=("arial", 10), bg="indianred1", command=msg)
    button2.place(x=660, y=630)

    button4 = Button(root, text="SEARCH", width=14, font=("arial", 10), bg="indianred1", command=all)
    button4.place(x=1400, y=70)
    # button7 = Button(root, text="UPLOAD PHOTO", width=14, font=("arial", 10), bg="indianred1",command=file)
    # button7.place(x=1100, y=210)

    button4 = Button(root, text="UPDATE", width=14, font=("arial", 10), bg="indianred1", command=update)
    button4.place(x=950, y=630)

    button5 = Button(root, text="DELETE", width=14, font=("arial", 10), bg="indianred1", command=clear)
    button5.place(x=800, y=630)


# add fee section is started from here


def add_fee():
    global main
    global namee
    global phone
    global purpose
    global entry23
    global entry24
    global entry25
    global entry26
    global entry27
    global entry28
    global box2
    global key
    global fee3
    global KEY
    global ley
    global sey
    global ADDFEE
    global entry29
    global s_earch

    addfee = Tk()
    addfee.geometry("1600x1000+0+0")
    addfee.title("enqiry")
    namee = StringVar()
    phone = IntVar()
    purpose = StringVar()
    fe = StringVar()
    key = IntVar()
    ley = StringVar()
    sey = StringVar()
    s_earch = StringVar()

    def exit1():
        addfee.destroy()

    def login_id():
        show = entry11.get()
        search1 = s_earch.get()
        print(search1)
        ls = ['id', 'name_db', 'sur_db', 'userid']

        if box_search1.get() == 'Name':
            k = 'name_db'
        elif box_search1.get() == 'Surname':
            k = ls[2]
        elif box_search1.get() == 'User Id':
            k = ls[3]
        print(k)
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor = mysqldb.cursor()

        try:
            mycursor.execute(f"SELECT * FROM registration where {k} = '" + show + " '")
            records = mycursor.fetchall()
            print(list(records))
            for j in records:
                x = j[6]
                n = j[1]
                s = j[2]
                name = f"{n} {s}"
                entry12.configure(state='normal')
                entry16.configure(state='normal')
                entry14.configure(state='normal')
                entry14.delete(0, END)
                entry14.insert(END, j[8])
                entry16.delete(0, END)
                entry12.delete(0, END)
                entry12.insert(END, x)
                entry16.insert(END, name)
                entry16.configure(state='disabled')
                entry12.configure(state='disabled')
                entry14.configure(state='disabled')



        except:
            mysqldb.rollback()
            mysqldb.close()

        
    def feeadd():
        show = entry11.get()

        mysqldb1 = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor1 = mysqldb1.cursor()

        ls = ['id', 'name_db', 'sur_db', 'userid']

        if box_search1.get() == 'Name':
            k = 'name_db'
        elif box_search1.get() == 'Surname':
            k = ls[2]
        elif box_search1.get() == 'User Id':
            k = ls[3]
        print(k)

        try:
            mycursor1.execute(f"SELECT * FROM registration where {k} = '" + show + " '")
            record = mycursor1.fetchall()
            print(list(record))
            for i in record:
                y = i[8]
                fee_paid = int(entry15.get())
                remain = int(y) - fee_paid
                print(remain)
                entry13.configure(state='normal')
                entry14.configure(state='normal')
                entry13.delete(0, END)
                entry14.delete(0, END)
                entry14.insert(END, remain)
                entry13.insert(END, fee_paid)
                entry13.configure(state='disabled')
                entry14.configure(state='disabled')

        except:
            mysqldb1.rollback()
            mysqldb1.close()

    def save():
        ID = entry11.get()
        remain = entry14.get()
        ls = ['id', 'name_db', 'sur_db', 'userid']

        if box_search1.get() == 'Name':
            k = 'name_db'
        elif box_search1.get() == 'Surname':
            k = ls[2]
        elif box_search1.get() == 'User Id':
            k = ls[3]
        print(k)

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor = mysqldb.cursor()

        try:
            sql = f"Update  registration set rfee_db= %s where {k}= %s"
            val = (remain, ID)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Updateddddd successfully...")

        except:
            mysqldb.rollback()
            mysqldb.close()

    def reset():
        entry12.configure(state="normal")
        entry13.configure(state="normal")
        entry14.configure(state="normal")
        entry16.configure(state="normal")
        entry15.delete(0, END)
        entry14.delete(0, END)
        entry13.delete(0, END)
        entry12.delete(0, END)
        entry11.delete(0, END)
        entry16.delete(0, END)
        entry16.configure(state="disabled")
        entry12.configure(state="disabled")
        entry13.configure(state="disabled")
        entry14.configure(state="disabled")
        messagebox.showwarning('Reset', 'After clicking OK , all the data will be erase')

    button = Button(addfee, text="BACK", width=30, bg="violetred1", command=exit1)
    button.place(x=0, y=0)
    buttons = Button(addfee, text="Update", width=30, bg="violetred1", command=save)
    buttons.place(x=570, y=350)
    label3 = Label(addfee, text="ENTER STUDENT ID", font=("arial", 17))
    label3.place(x=500, y=100)
    button22 = Button(addfee, text="LOGIN", width=26, font=("arial", 10), bg="indianred1", command=login_id)
    button22.place(x=450, y=290)
    button23 = Button(addfee, text="ADD FEE", width=26, font=("arial", 10), bg="indianred1", command=feeadd)
    button23.place(x=700, y=290)
    entry15 = Entry(addfee, bd=5, width=20, font=("arial", 15))
    entry15.place(x=700, y=200)
    button28 = Button(addfee, text="RESET", width=26, font=("arial", 10), bg="indianred1", command=reset)
    button28.place(x=1150, y=0)

    label31 = Label(addfee, text="TOTEL FEE", font=("arial", 17))
    label31.place(x=900, y=550)
    label32 = Label(addfee, text="PAID FEE", font=("arial", 17))
    label32.place(x=600, y=550)
    label33 = Label(addfee, text="REMAIN FEE", font=("arial", 17))
    label33.place(x=300, y=550)
    entry11 = Entry(addfee, bd=5, width=20, font=("arial", 15))
    entry11.place(x=450, y=200)
    entry12 = Entry(addfee, bd=5, state='readonly', width=20, font=("arial", 15))
    entry12.place(x=900, y=600)
    entry13 = Entry(addfee, bd=5, state='readonly', width=20, font=("arial", 15))
    entry13.place(x=600, y=600)
    entry14 = Entry(addfee, bd=5, state='readonly', width=20, font=("arial", 15))
    entry14.place(x=300, y=600)
    entry16 = Entry(addfee, bd=5, state='readonly', width=60, font=("arial", 15))
    entry16.place(x=380, y=480)
    box_search1 = ttk.Combobox(addfee, textvariable=s_earch, state="readonly", font=("arial", '15', "bold"), width=18)
    box_search1['values'] = ['Sarch By', 'Name', 'Surname', 'User Id']
    box_search1.current(0)
    box_search1.place(x=220, y=200)


# add fee ends here


# enquiry section is starts here

def enquiry_1():
    enquiry1 = Tk()
    enquiry1.title("ENQUIRY")
    enquiry1.geometry("1600x1000+0+0")
    purpose = StringVar()
    global entry23
    global entry24
    global box2

    def enquiry1destroy():
        enquiry1.destroy()

    def submit():
        ename = entry23.get()
        ephone = entry24.get()
        ereason = box2.get()
        eemail = email.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
        mycursor = mysqldb.cursor()

        try:
            sql = "INSERT INTO  enquiry (name,phone,reason,email) VALUES (%s,%s,%s,%s)"
            val = (ename, ephone, ereason, eemail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.fetchone()
            print(lastid)


        except:
            mysqldb.rollback()
            mysqldb.close()

        messagebox.showinfo('Enquiry', 'Your enquiry sent successfully.')

    label22 = Label(enquiry1, text="ENQUIRY", font=("times new roman", 25), bg="violetred1")
    label22.pack(side=TOP, fill=X)
    label1 = Label(enquiry1, text="NAME:", font=("arial", 17))
    label1.place(x=300, y=150)

    label2 = Label(enquiry1, text="PHONE NO.:", font=("arial", 17))
    label2.place(x=300, y=210)

    label3 = Label(enquiry1, text="PURPOSE:", font=("arial", 17))
    label3.place(x=300, y=270)
    entry23 = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    entry23.place(x=500, y=150)
    button = Button(enquiry1, text="submit", width=30, bg="violetred1", command=submit)
    button.place(x=500, y=420)
    labele = Label(enquiry1, text="Email:", font=("arial", 17))
    labele.place(x=300, y=320)
    email = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    email.place(x=500, y=320)
    button1 = Button(enquiry1, text="<< BACK", width=30, bg="violetred1", command=enquiry1destroy)
    button1.place(x=0, y=0)
    entry24 = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    entry24.place(x=500, y=210)
    box2 = ttk.Combobox(enquiry1, textvariable=purpose, state="readonly", font=("arial", 12, "bold"), width=22)
    box2['values'] = ['SELECT', 'TO LEARN PROGRAMMING', 'TO LEARN MACHINE LEARNING', 'FEE DETAILS']
    box2.current(0)
    box2.place(x=500, y=270)


# enquiry section is ends here


# enquiry details section is starts from here


def view_enquiry():
    rt = Tk()
    rt.title("VISITORS")
    rt.geometry("1600x1000+0+0")
    mainlabel = Label(rt, text="Student Enquiries", font=("times new roman", 35), bg="grey")
    mainlabel.pack(side=TOP, fill=X)
    chat1 = ttk.Treeview(rt, height=20, columns=('EMAIL', 'ENQUIRY', 'DATE'), selectmode="extended")
    chat1.heading('#0', text='NAME', anchor=CENTER)
    chat1.heading('#1', text='PHONE NO. ', anchor=CENTER)
    chat1.heading('#2', text='ENQUIRY', anchor=CENTER)
    chat1.heading('#3', text="DATE", anchor=CENTER)
    chat1.column('#1', stretch=YES, minwidth=50, width=200)
    chat1.column('#3', stretch=YES, minwidth=50, width=150)
    chat1.column('#2', stretch=YES, minwidth=50, width=300)
    chat1.column('#0', stretch=YES, minwidth=50, width=200)
    srb = ttk.Scrollbar(rt, orient="vertical", command=chat1.yview)
    srb.place(x=1200, y=170, height=400 + 20)
    chat1.configure(yscrollcommand=srb.set)
    chat1.place(x=350, y=170)
    ttk.Style().configure("Treeview", background="#383838", foreground="yellow")
    ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
    rt.configure(background="white")

    mysqldb1 = mysql.connector.connect(host="localhost", user="root", password="", database="course")
    mycursor = mysqldb1.cursor()
    print('yes')
    try:
        mycursor.execute("SELECT * FROM enquiry")
        record = mycursor.fetchall()
        print(list(record))
        for row in record:
            chat1.insert('', 0, text=row[1], values=(row[2], row[3], row[4]))
    except:
        mysqldb1.rollback()
        mysqldb1.close()

    def out():
        rt.destroy()

    button1 = Button(rt, text="<< BACK", width=10, font=('arial', '23'), bg="violetred1", command=out)
    button1.place(x=0, y=0)


# enquiry section is ends here


# all student id section is started from here
def studentid():
    lwin = Tk()
    lwin.title("VISITORS")
    lwin.geometry("1600x1000+0+0")
    mainlabel = Label(lwin, text="ENQUIRY DETAILS", font=("times new roman", 35), bg="MediumOrchid2")
    mainlabel.pack(side=TOP, fill=X)
    chat1 = ttk.Treeview(lwin, height=20, columns=('name', 'sur', 'email', 'branch', 'course', 'remain', 'fee'),
                         selectmode="extended")
    chat1.heading('#0', text='ID', anchor=CENTER)
    chat1.heading('#1', text=' NAME', anchor=W)
    chat1.heading('#3', text='EMAIL', anchor=W)
    chat1.heading('#2', text="LAST NAME", anchor=W)
    chat1.heading('#4', text='BRANCH', anchor=CENTER)
    chat1.heading('#5', text='COURSE', anchor=CENTER)
    chat1.heading('#6', text='FEE', anchor=CENTER)
    chat1.heading('#7', text='REMAINING FEES', anchor=CENTER)

    chat1.column('#1', stretch=YES, minwidth=50, width=100)
    chat1.column('#3', stretch=YES, minwidth=50, width=200)
    chat1.column('#2', stretch=YES, minwidth=50, width=300)
    chat1.column('#0', stretch=YES, minwidth=50, width=70)
    chat1.column('#4', stretch=YES, minwidth=50, width=200)
    chat1.column('#5', stretch=YES, minwidth=50, width=200
                 )
    chat1.column('#6', stretch=YES, minwidth=50, width=200)
    chat1.column('#7', stretch=YES, minwidth=30, width=200)

    chat1.place(x=30, y=100)
    ttk.Style().configure("Treeview", background="black", foreground="coral1")
    ttk.Style().configure("Treeview.Heading", background="blue", foreground="palevioletRed1")
    lwin.configure(background='white')

    vsb = ttk.Scrollbar(lwin, orient="vertical", command=chat1.yview)
    vsb.place(x=1500, y=100, height=400 + 20)
    chat1.configure(yscrollcommand=vsb.set)

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="course")
    mycursor = mysqldb.cursor()

    try:
        mycursor.execute("SELECT * FROM registration")
        records = mycursor.fetchall()
        print(list(records))

        for row1 in records:
            chat1.insert('', 0, text=row1[0], values=(row1[1], row1[2], row1[3], row1[4], row1[5], row1[6], row1[8],))

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

    def last_win():
        lwin.destroy()

    button1 = Button(lwin, text="<< BACK", width=10, font=('arial', '23'), bg="violetred1", command=last_win)
    button1.place(x=0, y=0)


# student id section is ends here


# main window and all will saperate from here

def main_window():
    mainwindow = Tk()
    mainwindow.geometry('1280x900')

    mainlabel = Label(mainwindow, text="shriyash JR college", font=("times new roman", 35),
                      bg="MediumOrchid2")
    mainlabel.pack(side=TOP, fill=X)
    button = Button(mainwindow, width=15, font=("arial", 20), text="Registration", bg="MediumOrchid2",
                    command=registration_main)
    button.place(x=30, y=480)
    enquiry = Button(mainwindow, width=15, font=("arial", 20), text="Fee Details", bg="MediumOrchid2", command=add_fee)
    enquiry.place(x=310, y=480)
    fee_details = Button(mainwindow, width=15, font=("arial", 20), text="Enquiry", bg="MediumOrchid2",
                         command=enquiry_1)
    fee_details.place(x=600, y=480)
    viewenquiry = Button(mainwindow, width=15, font=("arial", 20), text="View Enquiry", bg="MediumOrchid2",
                         command=view_enquiry)
    viewenquiry.place(x=900, y=480)
    viewenquiry1 = Button(mainwindow, width=15, font=("arial", 20), text="Student Data ", bg="MediumOrchid2",
                          command=studentid)
    viewenquiry1.place(x=1200, y=480)


INQUIRY = Button(fram, text="LOGIN", width=20, font=("arial", 20), bg="MediumOrchid2", command=login, cursor="hand2")
INQUIRY.place(x=120, y=360)

firstw.mainloop()
