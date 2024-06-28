import time
import os
from tkinter import *
from PIL import Image, ImageTk
from employee import EmployeeClass
from supplier import SupplierClass  
from category import CategoryClass
from product import ProductClass  
from sales import salesClass
import sqlite3
from tkinter import messagebox

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("INVENTORY MANAGEMENT SYSTEM | DEVELOPED BY ARCHANA AND DIVYA")
        self.root.config(bg="white")
        
        ## Title
        self.icon_title = PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout button
        btn_logout = Button(self.root, text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Clock
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Left menu
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=104, width=200, height=565)
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file="images/side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688", cursor="hand2")
        lbl_menu.pack(side=TOP, fill=X)

        buttons = [
            ("Employee", self.employee),
            ("Supplier", self.supplier),
            ("Category", self.category),
            ("Product", self.product),
            ("Sales", self.sales),
            ("Exit", root.quit)
        ]

        for text, command in buttons:
            btn = Button(LeftMenu, text=text, compound=LEFT, font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2", command=command)
            btn.pack(side=TOP, fill=X)

        # Content
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # Footer
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Developed by Divya and Archana\nFor any technical issue contact: 91xxxxxx02", font=("times new roman", 12), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)
        self.update_content()

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)  

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win) 

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)  

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)  

    def update_content(self):
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            try:
                cur.execute("select * from product")
                product=cur.fetchall()
                self.lbl_product.config(text=f'Total Product\n[ {str(len(product))}]')

                cur.execute("select * from employee")
                employee=cur.fetchall()
                self.lbl_employee.config(text=f'Total Employees\n[ {str(len(employee))}]')

                cur.execute("select * from supplier")
                supplier=cur.fetchall()
                self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))}]')

                cur.execute("select * from category")
                category=cur.fetchall()
                self.lbl_category.config(text=f'Total Category\n[ {str(len(category))}]')

                bill=len(os.listdir('bill'))
                self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

                time_=time.strftime("%I:%M:%S")
                date_=time.strftime("%d-%m-%Y")
                self.lbl_clock.config( text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
                self.lbl_clock.after(200,self.update_content)

            except Exception as ex:
                messagebox.showerror("Error",f"Error dur to: {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
