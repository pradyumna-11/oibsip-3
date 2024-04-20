from customtkinter import *
import random

set_appearance_mode("dark")  
set_default_color_theme("green")

def generate_password():
    if(length_input_box.get()=='' or (int(length_input_box.get()) <0)):
        err_msg.configure(text = "Please Enter valid length to generate password")
        password_label.configure(text = '')
    else:
        err_msg.configure(text = '')
        length = int(length_input_box.get())
        all_chars = ''
        lower_chars = "abcdefghijklmnopqrstuvwxtxyz"
        upper_chars = lower_chars.upper()
        numbers = "1234567890"
        special_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        is_lower_selected = lower_checkbox.get()
        is_upper_selected = upper_checkbox.get()
        is_number_selected = number_checkbox.get()
        is_sepcial_selected = special_checkbox.get()
        if(is_lower_selected=="on"):
            all_chars+=lower_chars
        if(is_upper_selected=="on"):
            all_chars+=upper_chars
        if(is_number_selected=="on"):
            all_chars+=numbers
        if(is_sepcial_selected=="on"):
            all_chars+=special_chars
        if(all_chars==''):
            err_msg.configure(text = "Please Select an option to generate password")
            password_label.configure(text = '')
        else:
            err_msg.configure(text = '')
            password = ''.join(random.choice(all_chars) for _ in range(length))
            text_display = "Your generated password is : "+password
            password_label.configure(text = text_display)
    
root = CTk()
root.title("Password Generator-Pradyumna")
root.geometry("600x600")
label = CTkLabel(root,text = "Password Generator-Pradyumna",font = ('Bree Serif',30))
label.pack(pady="20")

sub_label = CTkLabel(root,text = "Enter Password length",font = ('Bree Serif',15))
sub_label.pack(pady=(20,0))

length_input_box = CTkEntry(root,placeholder_text="Enter password length",border_width=0,fg_color="white",corner_radius=2,width=200,text_color="black")
length_input_box.pack(pady = (0,20))

options_frame = CTkFrame(root,height=300,width=300,fg_color="transparent")
options_frame.pack(pady="20")


check_lower_var = StringVar(value="off")
lower_checkbox = CTkCheckBox(options_frame, text="Lower case",variable=check_lower_var, onvalue="on", offvalue="off",checkbox_height=18,checkbox_width=18,corner_radius=2,border_width=1,hover_color = "#4169e1")
lower_checkbox.grid(row = 0,column= 0,pady="8")

check_upper_var = StringVar(value="off")
upper_checkbox = CTkCheckBox(options_frame, text="Upper case",variable=check_upper_var, onvalue="on", offvalue="off",checkbox_height=18,checkbox_width=18,corner_radius=2,border_width=1,hover_color = "#4169e1")
upper_checkbox.grid(row = 1,column= 0,pady="8")

check_special_var = StringVar(value="off")
special_checkbox = CTkCheckBox(options_frame, text="Special Characters",variable=check_special_var, onvalue="on", offvalue="off",checkbox_height=18,checkbox_width=18,corner_radius=2,border_width=1,hover_color = "#4169e1")
special_checkbox.grid(row = 2,column= 0,padx = "30",pady="8")

check_numeric_var = StringVar(value="off")
number_checkbox = CTkCheckBox(options_frame, text="Numbers",variable=check_numeric_var, onvalue="on", offvalue="off",checkbox_height=18,checkbox_width=18,corner_radius=2,border_width=1,hover_color = "#4169e1")
number_checkbox.grid(row = 3,column= 0,pady="8")


generate_button = CTkButton(root,text="Generate Password",hover_color="black",command = generate_password)
generate_button.pack()


password_label = CTkLabel(root,text = "",font = ('Bree Serif',15),text_color="green")
password_label.pack(pady="20")

err_msg = CTkLabel(root,text = "",font = ('Bree Serif',15),text_color="red")
err_msg.pack()

root.mainloop()