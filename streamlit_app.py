from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
from datetime import date
from data_collection import *
#from calculations import *
window=Tk()
command=""


#------------------- enable text boxes -------------
def start_break(children):
    for child in children:
        child.configure(state='enable')
    submit.configure(state='enable')
    start.configure(state='disable')
    day.insert(0, str(date.today().day))
    month.insert(0, str(date.today().month))
    year.insert(0, str(date.today().year))
    global time_start
    time_start=datetime.datetime.now()
    return time_start


#------------------- Submitting function -----------
def submit_break(window):
    coffee_break=[]
         
    #name_list="TK-PB-NV-DB-FLG-SHK-TB"
    #if(p1name.get()!=""):
    #    name_list=name_list+"-"+str(p1name.get()).upper()      #get name 1
    #if(p2name.get()!=""):
    #    name_list=name_list+"-"+str(p2name.get()).upper()      #get name 2
    
    name_list=[]     
    n_coffees=[]
    if(tkfld.get()!=""):                            #check if boxes are empty
        n_coffees.append(tkfld.get())        #if no fill in numbers of coffees
        name_list.append("TK")                    #if no fill in name
    if(pbfld.get()!=""):
        n_coffees.append(pbfld.get())
        name_list.append("PB")  
    if(nvfld.get()!=""):
        n_coffees.append(nvfld.get())
        name_list.append("NV")
    if(dbfld.get()!=""):
        n_coffees.append(dbfld.get())
        name_list.append("DB")
    if(flgfld.get()!=""):
        n_coffees.append(flgfld.get())
        name_list.append("FLG")
    if(shkfld.get()!=""):
        n_coffees.append(shkfld.get())
        name_list.append("SHK") 
    if(p1fld.get()!=""):
        n_coffees.append(p1fld.get())
        name_list.append(str(p1name.get()).upper())
    if(p2fld.get()!=""):
        n_coffees.append(p2fld.get())
        name_list.append(str(p2name.get()).upper())
    #print(name_list)
    #print(n_coffees)

    temp=0

    for i in range(len(n_coffees)):                  #check if no coffees are submitted
        temp=temp+int(n_coffees[i])
    if(temp==0):
        messagebox.showerror("Error", "No coffees submitted!")
        for child in frame1.winfo_children():       #grey out all text boxes
            child.delete(0, 'end')                  #delete all text box texts
            child.configure(state='disable')
        submit.configure(state='disable')
        start.configure(state='enable')
    else:
        date_break=[]
        error=False
        if(day.get()=="" and month.get()=="" and year.get()==""):
            date_break.append(datetime.datetime.now().day)
            date_break.append(datetime.datetime.now().month)
            date_break.append(datetime.datetime.now().year)

        elif(day.get()=="" or month.get()=="" or year.get()==""):
            messagebox.showerror("Error", "Invalid date entered!")
            error=True
        else:
            date_break.append(int(day.get()))
            date_break.append(int(month.get()))
            date_break.append(int(year.get()))
            day_entered=int(day.get())
            month_entered=int(month.get())
            year_entered=int(year.get())
            date_str=str(day_entered)+"-"+str(month_entered)+"-"+str(year_entered)+" 0:00"
            
            if(datetime.datetime.now() < datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M")):
                messagebox.showerror("Error", "Invalid date entered!")
                error=True
        if(error==False): 
            for child in frame1.winfo_children():       #grey out all text boxes
                child.delete(0, 'end')                  #delete all text box texts
                child.configure(state='disable')
            submit.configure(state='disable')
            start.configure(state='enable')
            coffee_break.append(date_break)
            print(coffee_break)
            coffee_break.append(name_list)
            print(coffee_break)
            coffee_break.append(n_coffees)
            print(coffee_break)
            #print(coffee_break[1][2])
            time_end=datetime.datetime.now()
            breaklen=time_end-time_start

            write_break(coffee_break,breaklen)                   #calling routine from data_collection to collect data

def delete():
    answer = messagebox.askokcancel("Confirmation", "Are you sure to clear the database?",icon="warning")
    if answer:
        command="delete_db"
        safety_check(command)
        #messagebox.showinfo("Deletion status", "The database has successfully been cleared.")
        #messagebox.showinfo("Deletion status", "Sorry! Deleting the database is currently not possible. Please talk to the admin.")

def delete_one_break():
    command="delete_one"
    safety_check(command)


 
 


#------------------ Creates frame -----------------
frame1 = LabelFrame(window, width= 400, height= 165, bd=5)
frame1.place(x=0, y=60)



#------------------ Header -------------------------
header=Label(window, text="Please enter a coffee break", fg='red', font=("Helvetica", 16))
header.place(x=70, y=20)

#------------------ Date ---------------------------
date_label=Label(window, text="Date:", fg='black', font=("Helvetica", 12))
date_label.place(x=40, y=70)
day=ttk.Entry(frame1, text="", width=3)
day.place(x=85, y=5)
dot1=Label(window, text=".", fg='black', font=("Helvetica", 16))
dot1.place(x=108, y=68)
month=ttk.Entry(frame1, text="", width=3)
month.place(x=115, y=5)
dot2=Label(window, text=".", fg='black', font=("Helvetica", 16))
dot2.place(x=138, y=68)
year=ttk.Entry(frame1, text="", width=5)
year.place(x=145, y=5)


#------------------ Name labels --------------------
drinkers=Label(window, text="Number of coffees:", fg='black', font=("Helvetica", 12))
drinkers.place(x=10, y=110)

tk=Label(window, text="TK", fg='black', font=("Calibri", 12))
tk.place(x=40, y=140)
pb=Label(window, text="PB", fg='black', font=("Helvetica", 10))
pb.place(x=80, y=140)
nv=Label(window, text="NV", fg='black', font=("Helvetica", 10))
nv.place(x=120, y=140)
db=Label(window, text="DB", fg='black', font=("Helvetica", 10))
db.place(x=160, y=140)
flg=Label(window, text="FLG", fg='black', font=("Helvetica", 10))
flg.place(x=200, y=140)
shk=Label(window, text="SHK", fg='black', font=("Helvetica", 10))
shk.place(x=240, y=140)
p1name=ttk.Entry(frame1, text="", width=4)
p1name.place(x=275, y=75)
p2name=ttk.Entry(frame1, text="", width=4)
p2name.place(x=315, y=75)


#-------------------- n_coffee text boxes----------
tkfld=ttk.Entry(frame1, text="", width=3)
tkfld.place(x=35, y=115)
pbfld=ttk.Entry(frame1, text="", width=3)
pbfld.place(x=75, y=115)
nvfld=ttk.Entry(frame1, text="", width=3)
nvfld.place(x=115, y=115)
dbfld=ttk.Entry(frame1, text="", width=3)
dbfld.place(x=155, y=115)
flgfld=ttk.Entry(frame1, text="", width=3)
flgfld.place(x=195, y=115)
shkfld=ttk.Entry(frame1, text="", width=3)
shkfld.place(x=235, y=115)
p1fld=ttk.Entry(frame1, text="", width=3)
p1fld.place(x=275, y=115)
p2fld=ttk.Entry(frame1, text="", width=3)
p2fld.place(x=315, y=115)

#-------------------- Start button -----------------
start = ttk.Button(window, text="Start break", command=lambda: start_break(frame1.winfo_children()))
start.place(x=40, y=237)
for child in frame1.winfo_children():
    child.configure(state='disable')



#-------------------- End button -------------------
submit=ttk.Button(window, text="End break", command=lambda: submit_break(window))
submit.place(x=268, y=237)
submit.configure(state='disable')


#-------------------- Clear break button ---------------
delete_all=ttk.Button(window, text="Delete break", command=lambda: delete_one_break())
delete_all.place(x=145, y=237)

#-------------------- Clear database button ---------------
delete_all=ttk.Button(window, text="Clear database", command=lambda: delete())
delete_all.place(x=145, y=280)


#------------------ total coffees button ---------
tot_coffees=ttk.Button(window, text="Total coffees", command=lambda: total_coffees())
tot_coffees.place(x=40, y=280)

#------------------ coffees per month button
coffees_per_month=ttk.Button(window, text="Coffees per month", command=lambda: coffees_p_month())
coffees_per_month.place(x=40, y=323)



#-------------------- Main window ------------------
window.title('Data collection: please enter coffee break')
window.geometry("400x400+10+20")
window.mainloop()



