
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [ random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [ random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)  
    pyperclip.copy(password)

  
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_entry_value = website_entry.get()
    email_entry_value = email_entry.get()
    password_entry_value = password_entry.get()
    new_data = {
        web_entry_value:{
            "email":email_entry_value,
            "password":password_entry_value
        }
    }
    if len(email_entry_value) == 0 or len(password_entry_value) == 0:
        is_not_ok = messagebox.showwarning(title="Attention", message="Value are umpty")
    else:
        is_ok = messagebox.askokcancel( message=f"These are the details entred: \nEmail: {email_entry_value}\nPassword: {password_entry_value}\nis it ok to save")
    if is_ok:
        try:
            with open("data.json" ,mode="r") as data_file:
                    #rading la data_file ,le lire, puis l'assigner a un variable data 
                    data = json.load(data_file)
                    
        except FileNotFoundError:
             with open("data.json" ,mode="w") as data_file:
                  json.dump(new_data,data_file, indent=4 )
        else:
            #mise ajour de la variable data en ajoutant la nouvelle new_Data sans l'envoyer en data_file
            data.update(new_data)          
            with open("data.json" ,mode="w") as data_file:
                #une fois la data a été mis a jour je l'envois vers data_file par dump 
                json.dump(data,data_file, indent=4 )
        finally:
             email_entry.delete(0, END)
             password_entry.delete(0, END )     
         
     
   
    
# ---------------------------- FINDE PASSWORD ------------------------------- #
def find_password():
    
     web_site_name = website_entry.get()
     try:
        with open("data.json" ,mode="r") as data_file:
                data = json.load(data_file)

     except FileNotFoundError:
          messagebox.showwarning(title="FileNotFoundError", message="file not found")
          
     else:
       
        if web_site_name in data.keys():
                email = data[web_site_name]["email"]
                password = data[web_site_name]["password"]
                messagebox.showwarning(title=web_site_name, message=f"{email}\n {password}")
        else: 
                messagebox.showwarning(title=ValueError, message=f"no details for {web_site_name}")
          
  
         
   

    
          
     
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=400, width=400)
image = PhotoImage(file="./logo.png")
canvas.create_image(200,200, image=image)
canvas.grid()

#labels
website_lebel = Label(text="Website:")
website_lebel.grid(row=1,column=0)
email_level = Label(text="Email/Username:")
email_level.grid(row=2,column=0)
password_lebel = Label(text="Password:")
password_lebel.grid(row=3,column=0)

#entries

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35,)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"djamel@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add" ,width=36 ,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search" ,width=36 ,command=find_password)
search_button.grid(row=1,column=2)








window.mainloop()
