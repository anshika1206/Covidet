from tkinter import *
import tkinter.ttk as table
import webbrowser as web
import people
import dashboard
import transaction
import medicalRecord


# TODO: Testing the switching between frames (change_frame meethod)

def change_frame(frame, name, prev="None"):
    global window, people_button, transactions_button, medicalRecord_button
    frame.destroy()
    if name == "Dashboard":
        frame = dashboard.get_frame(window)
        frame.pack(side=TOP)
        if prev == "People" or prev == "Transaction" or prev == "medicalRecord":
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Dashboard"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "Dashboard"))
            medicalRecord_button.config(text="medicalRecord", command=lambda: change_frame(frame, "medicalRecord", "Dashboard"))
            people_button.pack(side=LEFT)
            transactions_button.pack(side=LEFT)
            medicalRecord_button.pack(side=LEFT)

    elif name == "People":
        if prev == "Transaction":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(text="Transaction", command=lambda: change_frame(frame, "Transaction", "People"))
            medicalRecord_button.config(text="medicalRecord", command=lambda: change_frame(frame, "medicalRecord", "People"))
        if prev == "medicalRecord":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(text="Transaction", command=lambda: change_frame(frame, "Transaction", "People"))
            medicalRecord_button.config(text="medicalRecord", command=lambda: change_frame(frame, "medicalRecord", "People"))
        if prev == "Dashboard":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(command=lambda: change_frame(frame, "Transaction", "People"))
            medicalRecord_button.config(command=lambda: change_frame(frame, "medicalRecord", "People"))

        frame = people.get_frame(window)
        frame.pack(side=TOP)

    elif name == "Transaction":
        if prev == "People":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Transaction"))
            medicalRecord_button.config(text="medicalRecord", command=lambda: change_frame(frame, "medicalRecord", "Transaction"))
        if prev == "medicalRecord":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Transaction"))
            medicalRecord_button.config(text="medicalRecord", command=lambda: change_frame(frame, "medicalRecord", "Transaction"))
        if prev == "Dashboard":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(command=lambda: change_frame(frame, "People", "Transaction"))
            medicalRecord_button.config(command=lambda: change_frame(frame, "medicalRecord", "Transaction"))
        frame = transaction.get_frame(window)
        frame.pack(side=TOP)

    elif name == "medicalRecord":
        if prev == "People":
            medicalRecord_button.config(text="Dashboard",
                                   command=lambda: change_frame(frame, "Dashboard", "medicalRecord"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "medicalRecord"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "medicalRecord"))
        if prev == "Transaction":
            medicalRecord_button.config(text="Dashboard",
                                   command=lambda: change_frame(frame, "Dashboard", "medicalRecord"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "medicalRecord"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "medicalRecord"))
        if prev == "Dashboard":
            medicalRecord_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "medicalRecord"))
            transactions_button.config(command=lambda: change_frame(frame, "Transaction", "medicalRecord"))
            people_button.config(command=lambda: change_frame(frame, "People", "medicalRecord"))
        frame = medicalRecord.get_frame(window)
        frame.pack(side=TOP)


# This method adds the menu to the program.
def add_menu(window):
    menu = Menu(window)
    window.config(menu=menu)

    files_menu = Menu(menu)
    help_menu = Menu(menu)

    files_menu.add_command(label="Exit", command=window.quit)

    about_menu = Menu(help_menu)
    about_menu.add_command(label="Anshika",
                           command=lambda: web.open("https://www.linkedin.com/in/anshika-kakani-b4018b202/"))
    about_menu.add_command(label="Alaina",
                           command=lambda: web.open("https://www.linkedin.com/in/alaina-aanam-359a14211/"))

    help_menu.add_cascade(label="About", menu=about_menu)

    menu.add_cascade(label="File", menu=files_menu)
    menu.add_cascade(label="Help", menu=help_menu)


# Main Logic of the function
window = Tk()
window.title("COVIDET")
add_menu(window)
frame = dashboard.get_frame(window)
frame.pack(side=TOP)
navigation_frame = Frame(window)
people_button = Button(navigation_frame, text="People", command=lambda: change_frame(frame, "People", "Dashboard"))
transactions_button = Button(navigation_frame, text="Transactions",
                             command=lambda: change_frame(frame, "Transaction", "Dashboard"))
medicalRecord_button = Button(navigation_frame, text="medicalRecord",
                         command=lambda: change_frame(frame, "medicalRecord", "Dashboard"))
quit_button = Button(navigation_frame, text="Quit", command=window.quit)
people_button.pack(side=LEFT)
transactions_button.pack(side=LEFT)
medicalRecord_button.pack(side=LEFT)
quit_button.pack(side=LEFT)
navigation_frame.pack(side=BOTTOM)
window.mainloop()
