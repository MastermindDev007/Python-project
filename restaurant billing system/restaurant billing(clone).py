from tkinter import *
import random
import os
import sys
from tkinter import messagebox
import tkinter as tk
from fpdf import FPDF

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#F4EBD0")
        self.root.title("Resturent Billing System - CodeWithCurious.com")

        # Maximize the window when the app starts
        self.root.state('zoomed')

        # Main title label with the desired background color
        title = Label(self.root, text="MY RESTAURANT BILLING SYSTEM", bd=0, font=("Arial Black", 20), bg="#122620", fg="#F3B44B")
        title.pack(fill=X, pady=10)
        #===================================variables=======================================================================================
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()

        #==========================================customer details label frame=================================================

        # LabelFrame without borders
        details = LabelFrame(self.root, text="CUSTOMER DETAILS", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#F3B44B", relief=FLAT, padx=15, pady=15)  # Larger padding for better spacing
        details.place(x=0, y=80, relwidth=1)

        # Customer Name Label
        cust_name = Label(details, text="Customer Name: ", font=("Arial Black", 14), bg="#122620", fg="#fff", padx=5, pady=5)
        cust_name.grid(row=0, column=0, padx=(5, 0))  # Reduced padx on the right side

        # Customer Name Entry (borderless)
        cust_entry = Entry(details, width=25, textvariable=self.c_name, font=("Arial Black", 12), relief=FLAT)
        cust_entry.grid(row=0, column=1, padx=(0, 5))  # Reduced padx on the left side

        # Contact No Label
        contact_name = Label(details, text="Contact No: ", font=("Arial Black", 14), bg="#122620", fg="#fff", padx=5, pady=5)
        contact_name.grid(row=0, column=2, padx=(50, 0))  # Increased padx on the left side

        # Contact Entry (borderless)
        contact_entry = Entry(details, width=25, textvariable=self.phone, font=("Arial Black", 12), relief=FLAT)
        contact_entry.grid(row=0, column=3, padx=(0, 20))  # Increased padx on the right side

        # Bill No Label
        bill_name = Label(details, text="Bill.No: ", font=("Arial Black", 14), bg="#122620", fg="#fff", padx=5, pady=5)
        bill_name.grid(row=0, column=4, padx=(50, 0))  # Increased padx on the left side

        # Bill No Entry (borderless)
        bill_entry = Entry(details, width=25, textvariable=self.bill_no, font=("Arial Black", 12), relief=FLAT)
        bill_entry.grid(row=0, column=5, padx=(0, 50))  # Increased padx on the right side

        #=======================================Starter================================================================-

        snacks = LabelFrame(self.root, text="Starter", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#F3B44B",relief=FLAT, padx=30 , pady=30)
        snacks.place(x=0, y=210, height=400, width=350)

        item1 = Label(snacks, text="Nutella", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=0, column=0, pady=7, sticky="w")
        item1_entry=Entry(snacks, width=15, textvariable = self.nutella, font=("Arial Black", 11), relief=FLAT).grid(row=0,column=1,padx=40)

        item2 = Label(snacks, text="Noodles", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=1, column=0, pady=7, sticky="w")
        item2_entry=Entry(snacks,width=15,textvariable=self.noodles, font=("Arial Black", 11), relief=FLAT).grid(row=1,column=1,padx=40)

        item3 = Label(snacks, text="Lays", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=2, column=0, pady=7, sticky="w")
        item3_entry=Entry(snacks,width=15,textvariable=self.lays, font=("Arial Black", 11), relief=FLAT).grid(row=2,column=1,padx=40)

        item4 = Label(snacks, text="Oreo", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=3, column=0, pady=7, sticky="w")
        item4_entry=Entry(snacks,width=15,textvariable=self.oreo, font=("Arial Black", 11), relief=FLAT).grid(row=3,column=1,padx=40)

        item5 = Label(snacks, text="Muffin", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=4, column=0, pady=7, sticky="w")
        item5_entry=Entry(snacks,width=15,textvariable=self.muffin, font=("Arial Black", 11), relief=FLAT).grid(row=4,column=1,padx=40)

        item6 = Label(snacks, text="Silk", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=5, column=0, pady=7, sticky="w")
        item6_entry=Entry(snacks,width=15,textvariable=self.silk, font=("Arial Black", 11), relief=FLAT).grid(row=5,column=1,padx=40)

        item7 = Label(snacks, text="Namkeen", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=6, column=0, pady=7, sticky="w")
        item7_entry=Entry(snacks, width=15,textvariable=self.namkeen, font=("Arial Black", 11), relief=FLAT).grid(row=6,column=1,padx=40)

        #=================================== Main Course =====================================================================================

        grocery = LabelFrame(self.root, text="Main Course", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#F3B44B",relief=FLAT, padx=30, pady=30)
        grocery.place(x=395, y=210, height=400, width=350)

        item8=Label(grocery, text="Atta", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=0, column=0, pady=7, sticky="w")
        item8_entry=Entry(grocery, width=15, textvariable=self.atta, font=("Arial Black", 11), relief=FLAT).grid(row=0,column=1,padx=80)

        item9=Label(grocery ,text="Pasta", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=1,column=0,pady=7, sticky="w")
        item9_entry=Entry(grocery, width=15,textvariable=self.pasta, font=("Arial Black", 11), relief=FLAT).grid(row=1,column=1,padx=80)

        item10=Label(grocery ,text="Rice", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=2,column=0,pady=7, sticky="w")
        item10_entry=Entry(grocery, width=15,textvariable=self .rice, font=("Arial Black", 11), relief=FLAT).grid(row=2,column=1,padx=80)

        item11=Label(grocery ,text="Oil", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=3,column=0,pady=7, sticky="w")
        item11_entry=Entry(grocery, width=15,textvariable=self.oil, font=("Arial Black", 11), relief=FLAT).grid(row=3,column=1,padx=80)

        item12=Label(grocery ,text="Sugar", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=4,column=0,pady=7, sticky="w")
        item12_entry=Entry(grocery, width=15,textvariable=self.sugar, font=("Arial Black", 11), relief=FLAT).grid(row=4,column=1,padx=80)

        item13=Label(grocery ,text="Daal", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=5,column=0,pady=7, sticky="w")
        item13_entry=Entry(grocery, width=15,textvariable=self.dal, font=("Arial Black", 11), relief=FLAT).grid(row=5,column=1,padx=80)

        item14=Label(grocery ,text="Tea", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=6,column=0,pady=7, sticky="w")
        item14_entry=Entry(grocery, width=15,textvariable=self.tea, font=("Arial Black", 11), relief=FLAT).grid(row=6,column=1,padx=80)

        #========================================Snacks===============================================================================

        hygine = LabelFrame(self.root, text="Snacks", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#F3B44B",relief=FLAT, padx=30, pady=30)
        hygine.place(x=790, y=210, height=400, width=350)

        item15=Label(hygine,text="Soap", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=0, column=0, pady=7, sticky="w")
        item15_entry=Entry(hygine,width=15,textvariable=self.soap, font=("Arial Black", 11), relief=FLAT).grid(row=0,column=1,padx=40)

        item16=Label(hygine,text="Shampoo", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=1,column=0,pady=7, sticky="w")
        item16_entry=Entry(hygine,width=15,textvariable=self.shampoo, font=("Arial Black", 11), relief=FLAT).grid(row=1,column=1,padx=40)

        item17=Label(hygine,text="Lotion", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=2,column=0,pady=7, sticky="w")
        item17_entry=Entry(hygine,width=15,textvariable=self.lotion, font=("Arial Black", 11), relief=FLAT).grid(row=2,column=1,padx=40)

        item18=Label(hygine,text="Cream", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=3,column=0,pady=7, sticky="w")
        item18_entry=Entry(hygine,width=15,textvariable=self.cream, font=("Arial Black", 11), relief=FLAT).grid(row=3,column=1,padx=40)

        item19=Label(hygine,text="Foam", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=4,column=0,pady=7, sticky="w")
        item19_entry=Entry(hygine,width=15,textvariable=self.foam, font=("Arial Black", 11), relief=FLAT).grid(row=4,column=1,padx=40)

        item20=Label(hygine,text="Mask", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=5,column=0,pady=7, sticky="w")
        item20_entry=Entry(hygine,width=15,textvariable=self.mask, font=("Arial Black ", 11), relief=FLAT).grid(row=5,column=1,padx=40)

        item21=Label(hygine,text="Sanitizer", font=("Arial Black", 14), bg="#122620", fg="#fff", anchor="w").grid(row=6,column=0,pady=7, sticky="w")
        item21_entry=Entry(hygine,width=15,textvariable=self.sanitizer, font=("Arial Black", 11), relief=FLAT).grid(row=6,column=1,padx=40)

        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,relief=FLAT, bg="#122620")
        billarea.place(x=1186, y=210, height=400, width=350)

        bill_title=Label(billarea,text="Bill Area", font=("Arial Black", 14, 'bold'), relief=FLAT, bg="#122620", fg="#F3B44B").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set, font=("Arial", 11, 'bold'), bg="#122620", fg="#fff")
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=================================================billing menu=========================================================================================

        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",20,'bold'),relief=FLAT,bg="#122620",fg="#F3B44B")
        billing_menu.place(x=0,y=650,relwidth=1,height=195)

        #starter label
        total_snacks = Label(billing_menu, text="Total Starter Price: ", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#fff", padx=5, pady=5, anchor="w")  # Reduced padx on the right side
        total_snacks.grid(row=0, column=0, padx=(5, 0), sticky="w")
        #starter entry
        total_snacks_entry = Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0, column=1, padx=40)  # Reduced padx on the left side

        #main course label
        total_grocery=Label(billing_menu,text="Total Main Course Price: ", font=("Arial Black", 14, 'bold'),bg="#122620",fg="#fff", padx=5, pady=0, anchor="w")
        total_grocery.grid(row=1, column=0, padx=(5, 0), sticky="w")
        #main course entry
        total_grocery_entry=Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT,textvariable=self.total_gro)
        total_grocery_entry.grid(row=1, column=1, padx=40)

        #snacks label
        total_hygine=Label(billing_menu,text="Total Hygine Price: ", font=("Arial Black", 14, 'bold'),bg="#122620", fg="#fff", padx=5, pady=5, anchor="w")
        total_hygine.grid(row=2, column=0, padx=(5, 0), sticky="w")
        #snacks entry
        total_hygine_entry=Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT,textvariable=self.total_hyg)
        total_hygine_entry.grid(row=2, column=1, padx=40)

        # starter tax label
        total_snacks = Label(billing_menu, text="Total Starter Tax: ", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#fff", padx=5, pady=5, anchor="w")  # Reduced padx on the right side
        total_snacks.grid(row=0, column=3, padx=(5, 0), sticky="w")
        # starter tax entry
        total_snacks_entry = Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT, textvariable=self.a)
        total_snacks_entry.grid(row=0, column=4, padx=40)  # Reduced padx on the left side

        # main course tax label
        total_grocery = Label(billing_menu, text="Total Main Course Tax: ", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#fff", padx=5, pady= 5, anchor="w")
        total_grocery.grid(row=1, column=3, padx=(5, 0), sticky="w")
        # main course tax entry
        total_grocery_entry = Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT, textvariable=self.b)
        total_grocery_entry.grid(row=1, column=4, padx=40)

        # snacks tax label
        total_hygine = Label(billing_menu, text="Total Hygine Tax: ", font=("Arial Black", 14, 'bold'), bg="#122620", fg="#fff", padx=5, pady=5, anchor="w")
        total_hygine.grid(row=2, column=3, padx=(5, 0), sticky="w")
        # snacks tax entry
        total_hygine_entry = Entry(billing_menu, width=15, font=("Arial Black", 12, 'bold'), relief=FLAT, textvariable=self.c)
        total_hygine_entry.grid(row=2, column=4, padx=40)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#122620")
        button_frame.place(x=1050,width=450,height=120)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15, 'bold'),pady=10,bg="#F3B44B",fg="#122620",command=lambda:total(self)).grid(row=0,column=0,padx=6, pady=20)
        button_print=Button(button_frame,text="Print Bill",font=("Arial Black",15, 'bold'),pady=10,bg="#F3B44B",fg="#122620",command=lambda:print_bill(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15, 'bold'),pady=10,bg="#F3B44B",fg="#122620",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.nutella.get()*120
    self.no=self.noodles.get()*40
    self.la=self.lays.get()*10
    self.ore=self.oreo.get()*20
    self.mu=self.muffin.get()*30
    self.si=self.silk.get()*60
    self.na=self.namkeen.get()*15
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    self.at=self.atta.get()*42
    self.pa=self.pasta.get()*120
    self.oi=self.oil.get()*113
    self.ri=self.rice.get()*160
    self.su=self.sugar.get()*55
    self.te=self.tea.get()*480
    self.da=self.dal.get()*76
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    self.so=self.soap.get()*30
    self.sh=self.shampoo.get()*180
    self.cr=self.cream.get()*130
    self.lo=self.lotion.get()*500
    self.fo=self.foam.get()*85
    self.ma=self.mask.get()*100
    self.sa=self.sanitizer.get()*20

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.nutella.get()!=0:
        self.txtarea.insert(END,f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.lays.get()!=0:
        self.txtarea.insert(END,f"Lays\t\t {self.lays.get()}\t{self.la}\n")
    if self.oreo.get()!=0:
        self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get()!=0:
        self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"Silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.namkeen.get()!=0:
        self.txtarea.insert(END,f"Namkeen\t\t {self.namkeen.get()}\t{self.na}\n")
    if self.atta.get()!=0:
        self.txtarea.insert(END,f"Atta\t\t {self.atta.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.oil.get()!=0:
        self.txtarea.insert(END,f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
    if self.sugar.get()!=0:
        self.txtarea.insert(END,f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.tea.get()!=0:
        self.txtarea.insert(END,f"Tea\t\t {self.tea.get()}\t{self.te}\n")
    if self.soap.get()!=0:
        self.txtarea.insert(END,f"Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get()!=0:
        self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get()!=0:
        self.txtarea.insert(END,f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get()!=0:
        self.txtarea.insert(END,f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get()!=0:
        self.txtarea.insert(END,f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get()!=0:
        self.txtarea.insert(END,f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get()!=0:
        self.txtarea.insert(END,f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def print_bill(self):
    bill = self.txtarea.get("1.0", "end-1c")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "WELCOME TO SUPER MARKET", ln = True, align = 'C')
    pdf.ln(10)
    pdf.set_font("Arial", size = 12)
    for line in bill.split('\n'):
        pdf.cell(200, 10, txt = line, ln = True, align = 'L')
    pdf.output("bill.pdf")
    os.startfile("bill.pdf")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()