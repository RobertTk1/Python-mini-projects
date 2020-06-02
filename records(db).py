from tkinter import *
from PIL import ImageTk, Image
import sqlite3
root = Tk()
root.title('Image display')
root.iconbitmap("iconx.ico")
root.geometry('300x350')


dab = sqlite3.connect('address.db')

c = dab.cursor()

'''
c.execute(""" CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)

""")
'''


def submit():

    c = dab.cursor()

    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    dab.commit()

    dab.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    dab = sqlite3.connect('address.db')

    c = dab.cursor()

    c.execute('SELECT *, oid FROM addresses')

    records = c.fetchall()

    print(records)

    print_records = ''

    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(root, text = print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    dab.commit()

    dab.close()

def delete():
    dab = sqlite3.connect('address.db')

    c = dab.cursor()
    c.execute('DELETE from addresses WHERE oid=' + delete_box.get())

    dab.commit()

    dab.close()


def update():
    global up
    up = Tk()
    up.title('Update record')
    up.iconbitmap("iconx.ico")
    up.geometry('300x200')

    dab = sqlite3.connect('address.db')

    c = dab.cursor()

    record_id = delete_box.get()

    c.execute('SELECT * FROM addresses where oid= ' + record_id)

    records = c.fetchall()
    global f_name_up
    global l_name_up
    global address_up
    global city_up
    global state_up
    global zipcode_up

    f_name_up = Entry(up, width=30)
    f_name_up.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_up = Entry(up, width=30)
    l_name_up.grid(row=1, column=1, padx=20)
    address_up = Entry(up, width=30)
    address_up.grid(row=2, column=1, padx=20)
    city_up = Entry(up, width=30)
    city_up.grid(row=3, column=1, padx=20)
    state_up = Entry(up, width=30)
    state_up.grid(row=4, column=1, padx=20)
    zipcode_up = Entry(up, width=30)
    zipcode_up.grid(row=5, column=1, padx=20)

    f_name_la = Label(up, text='First Name').grid(row=0, column=0)
    l_name_la = Label(up, text='Last Name').grid(row=1, column=0)
    address_la = Label(up, text='Address').grid(row=2, column=0)
    city_la = Label(up, text='City').grid(row=3, column=0)
    state_la = Label(up, text='State').grid(row=4, column=0)
    zipcode_la = Label(up, text='Zipcode').grid(row=5, column=0)



    save_btn = Button(up, text='Save changes', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, ipadx=80, pady=5, padx=10)

    for record in records:
        f_name_up.insert(0,record[0])
        l_name_up.insert(0,record[1])
        address_up.insert(0,record[2])
        city_up.insert(0,record[3])
        state_up.insert(0,record[4])
        zipcode_up.insert(0,record[5])

    dab.commit()

    dab.close()

def save():
    dab = sqlite3.connect('address.db')

    c = dab.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
    {'first': f_name_up.get(),
     'last': l_name_up.get(),
     'address': address_up.get(),
     'city': city_up.get(),
     'state': state_up.get(),
     'zipcode': zipcode_up.get(),
     'oid': record_id}
    
    )

    dab.commit()

    dab.close()
    up.destroy()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=25)
delete_box.grid(row=8, column=1, columnspan=1)

f_name_la = Label(root, text='First Name').grid(row=0, column=0)
l_name_la = Label(root, text='Last Name').grid(row=1, column=0)
address_la = Label(root, text='Address').grid(row=2, column=0)
city_la = Label(root, text='City').grid(row=3, column=0)
state_la = Label(root, text='State').grid(row=4, column=0)
zipcode_la = Label(root, text='Zipcode').grid(row=5, column=0)

delete_la = Label(root, text='Select ID').grid(row=8, column=0, padx=10)

submit_btn = Button(root, text='Add record to database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, ipadx=80, pady=5, padx=10)

query_btn = Button(root, text='Show records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


edit_btn = Button(root, text='update record', command=update)
edit_btn.grid(row=9, column=0, columnspan=2, ipadx=100, pady=10)

delete_btn = Button(root, text='Delete record', command=delete)
delete_btn.grid(row=10, column=0,columnspan=2, ipadx=100, pady=10, padx=10)



dab.commit()

dab.close()


mainloop()
