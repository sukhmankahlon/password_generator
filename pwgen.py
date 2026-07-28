#Sukhman Kahlon
#July 26, 2026
#Sheridan College 991550833
#Password Generator v1.0
import secrets
import string
import tkinter as tk
from tkinter import messagebox
import random
class PasswordGen(tk.Tk):
    def __init__(self):
        
        self.tk=tk.Tk()
        self.title('Password Generator') #tkinter window title
        self.geometry('400x300')#pre defined window dimensions

        self.label1 = tk.Label(text='Welcome to the Password Generator!',font=('','15')) #welcome label
        self.label1.pack(padx=10,pady=5)

        self.label3= tk.Label(text='Minimum length must be no less than 12!',font=('',10))#set minimum requirement for password
        self.label3.pack(padx=2,pady=2)

        self.label4= tk.Label(text='Note each password will contain 2 digits and 1 symbol',font=('','8'))
        self.label4.pack()
        self.label2 = tk.Label(text='Enter number of characters in password',font=('','10'))
        self.label2.pack(padx=10,pady=10)

        self.textbox = tk.Text(height=1,width=5)#text field for desired character length of password
        self.textbox.pack(padx=5,pady=5)

        self.button1= tk.Button(self.tk,text='Generate',command=self.getinput)#button to send to getinput method
        self.button1.pack()

        self.text=tk.Label(text='Waiting...')#waiting for user input
        self.text.pack(padx=3,pady=3)

        self.button2 = tk.Button(text='Quit',command=self.quit)#quit button to exit program
        self.button2.pack(padx=3,pady=3)
  
    def getinput(self):
        getstr =self.textbox.get('1.0','end-1c')#retrieve input form text box for desired character length
        num = int(getstr)#convert string to integer
        if num < 12:#check to see if number is less than 12
            popup = messagebox.showinfo('Error','The entered number is less than 12!')
        else:#send integer to creation method
            self.creation(num)

    def creation(self,num):
        
        password=[]#list for all characters in password
        selectchar = string.ascii_letters #uppercase and lowercase letters
        selectdig = string.digits #all digits 0-9
        selectsym = string.punctuation # all symbols

        char = num-3 #to keep password length at users choice and factor in 2 digits and special character

        
        for i in range(1,char+1): #select characters
            i = secrets.choice(selectchar)
            if i in password:#to check for any repeating characters
                i = secrets.choice(selectchar)
            else:#append to list
                password.append(i)

        for i in range(1,3):#select 2 digits
            i=secrets.choice(selectdig)
            password.append(i)
        
        for i in range(1,2):#select a symbol
            i=secrets.choice(selectsym)
            password.append(i)
        
        if len(password) != num:#if the length of password does not match desired length, run creation method again
            self.creation(num)
        else:
            random.shuffle(password)#further randomization of selected characters
            joined = ''.join(password)#join all items in a list to create a string
            self.text.config(text=f'Generated Password: {joined}')#prompt generated password
            
        

        


def main(): #start tkinter loop
    start = PasswordGen()
    start.mainloop()
main()