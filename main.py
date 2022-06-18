
from tkinter import*
import json

#from numpy import insert
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
from tkinter import messagebox
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    pwd_input.delete(0,END)
    pwd_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    email = email_input.get()
    pwd = pwd_input.get()
    website = website_input.get()
    new_data = {
        website:{
            "email": email,
            "password": pwd
        }
        }
    
    if len(email)==0 or len(pwd) ==0 or len(website) ==0:
        messagebox.showinfo("Information","Please fill all the fields")
    else :
        is_ok= messagebox.askokcancel("Website",f"Website: {website} \nEmail : {email} \nPassword {pwd}")
        if is_ok:
            print(website, email, pwd)
            try:
                with open("Password_Manager.json", "r") as pwd_file:
                    #json.dump(new_data , pwd_file, indent =4)
                    #pwd_file.write(f"{website}|{email}|{pwd}")
                    #Reading old data
                    data =json.load(pwd_file)
                    #print(data)
                    
            except FileNotFoundError:
                with open("Password_manager.json", "w") as pwd_file:
                    json.dump(new_data, pwd_file, indent = 4)
            else:
                #updating old data with new data
                data.update(new_data)

                with open("Password_manager.json", "w") as pwd_file:
                    #saving the updated data
                    json.dump(data, pwd_file, indent =4)
            finally:        
                    website_input.delete(0,END)
                    pwd_input.delete(0,END)

#-------------------------find password-----------------------------------#
def find_password():
    website = website_input.get()
    with open("Password_manager.json","r") as file:
        data = json.load(file)
        print(data)
        if website in data:
            email = data[website]["email"]
            pwd = data[website]["password"]
            messagebox.showinfo(title = website,message = f"Email: {email} \nPassword: {pwd}")
        else:
            messagebox.showinfo(title = "oops",message = f"Website not there ")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")

canvas.create_image(100,100,image = lock_img)
canvas.grid(column=1,row=0)
canvas.grid()

website_label = Label(text = "Website")
website_label.grid(column =0,row =1)
website_input = Entry(width = 50)
website_input.grid(column=1, row=1,columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)
email_input = Entry(width = 50,)
email_input.insert(0, "mitraraunak388@gmail.com")
email_input.grid(column = 1,row =2,columnspan=2)

pwd_label = Label(text="Password")
pwd_label.grid(column=0,row=3)
pwd_input = Entry(width = 50)
pwd_input.grid(column = 1,row =3, columnspan=2)

generate_button = Button(text = "Generate Password", command = generate_pwd)
generate_button.grid(column =2 , row = 3)

search_button = Button(text = "Search", width = 15,command= find_password)
search_button.grid(column=2 , row = 1)

add_button = Button(text="Add",width = 40, command=save_data)
add_button.grid(column =1 , row=4,columnspan=2)
window.mainloop()