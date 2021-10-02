from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("BIC")
window.minsize(350, 525)
window.resizable(0, 0)
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='Favicon.png'))

canvas = Canvas(width=500, height=400)
logo = PhotoImage(file="images/Logo2.png")
canvas.create_image(100, 112, image=logo)
canvas.place(x=75, y=-80)

app_name_top = Label(window, text="Bank Interest Calculator", font=("Cascadia Mono Semibold", 15, "normal"))
app_name_top.place(x=35, y=70)

# Choice Options
my_label = Label(window, text="Primary Amount :", font=("Cambria", 12, "italic"))
my_label.place(x=10, y=160)
choices = ["Choose Duration", "Year", "Months"]

variable = StringVar()
variable.set("")
w = OptionMenu(window, variable, *choices)
w.place(x=210, y=238)

# Creating Entry
creating_entry = Entry(window, font=("Cambria", 12, "normal"))
creating_entry.place(x=145, y=163, width=150)

my_label = Label(window, text="Interest Rate (%) :", font=("Cambria", 12, "italic"))
my_label.place(x=10, y=200)

creating_entry2 = Entry(window, font=("Cambria", 12, "normal"))
creating_entry2.place(x=145, y=200, width=150)

duration_label = Label(window, text="Duration :", font=("Cambria", 12, "italic"))
duration_label.place(x=10, y=240)

creating_entry3 = Entry(window, font=("Cambria", 12, "normal"))
creating_entry3.place(x=145, y=240, width=50)

tax_label = Label(window, text="Tax (%) :", font=("Cambria", 12, "italic"))
tax_label.place(x=10, y=280)

creating_entry4 = Entry(window, font=("Cambria", 12, "normal"))
creating_entry4.place(x=145, y=283, width=150)


# Converter Function
def converter():
    convert = variable.get()
    # convert_to = to.get()
    num = float(creating_entry.get())
    num2 = float(creating_entry2.get())
    num3 = float(creating_entry3.get())
    num4 = float(creating_entry4.get())

    # Inch To Cm & Cm to Inch
    if convert == 'Months':
        conversion = num * (num2 / 100) / 365
        conversion2 = num3 * 30
        conversion3 = conversion * conversion2
        conversion4 = (conversion3 * num4) / 100
        taxes = conversion3 - conversion4
        total_amount = num + taxes

    elif convert == "Year":
        conversion = num * (num2 / 100) / 365
        conversion2 = num3 * 365
        conversion3 = conversion * conversion2
        conversion4 = (conversion3 * num4) / 100
        taxes = conversion3 - conversion4
        total_amount = num + taxes

    else:
        converted_num = num

    result_label.config(text=f"{taxes:.5}", font=("Cambria", 13, "bold"))

    result_label2.config(text=f"{total_amount:.8}", font=("Cambria", 13, "bold"))

    notice_label = Label(window, text="*Results are showing after deducting tax.", font=("Cambria", 8, "bold"),
                         foreground="red")
    notice_label.place(x=13, y=470)


def about():
    messagebox.showinfo(title="About Us",
                        message="Developer Name : Niaz Mahmud Akash\nContributor         : Jalish Mahmud Nill\n"
                                "\nGithub Page : https://www.github.com/Viperz75")


def question():
    messagebox.showinfo(title="Question", message="How is it calculated (Month)?\n» Excuse me, why would i tell you that?")


# Calculate Button
photo = PhotoImage(file="images/Calculate2.png")
calculate = Button(window, text="calculate", image=photo, style="flat.TButton", command=converter)

# calculate = Button(window, text="Calculate", image=photo, command=converter).pack(side=TOP)

calculate.place(x=135, y=320)

# Result Label
result_before_label = Label(window, text="Interest Earned :", font=("Cambria", 12, "bold"))
result_before_label.place(x=10, y=385)

result_before_label = Label(window, text="Total Amount :", font=("Cambria", 12, "bold"))
result_before_label.place(x=10, y=415)

result_label = Label(window, text="")
result_label.place(x=170, y=385)

result_label2 = Label(window, text="")
result_label2.place(x=170, y=412)

menu_bar = Menu(window)
menu = Menu(menu_bar, tearoff=0)
menu.add_command(label="❌ Exit", command=window.quit)
menu_bar.add_cascade(label="Close", menu=menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="⭐ About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)
# # splash_window.after(3000, main_window)
# main_window()
mainloop()
