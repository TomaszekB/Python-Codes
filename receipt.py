import tkinter
import datetime
import random
import time
from tkinter.filedialog import asksaveasfile

p1 = "Kołowrotek QUICK 5 LC DAM"
p2 = "Żyłka 20 KG"
p3 = "Skrzynka wędkarska 3-DRAWER"
p4 = "Podbierak"
p5 = "Zanęta SWEET BEAM BROWNING"
p6 = "Haczyki Karpiowe"
kasa = "Numer kasy" + "\t" + "\t" + "\t" + "\t" + str(random.randint(1, 8))
divide = ("*" * 45)
t = time.localtime()
actual_date = datetime.date.today()
current_time = "\t" + "\t" + "\t" + "\t" + time.strftime("%H:%M", t)


####################################################


#############################################


def savebutton():
    textfile = (head + "\n" + str(var_check1()) + "\t\t" + str(vatcal1())
                + "\n" + str(var_check2()) + "\t\t\t\t" + str(vatcal2())
                + "\n" + str(var_check3()) + "\t\t" + str(vatcal3())
                + "\n" + str(var_check4()) + "\t\t\t\t" + str(vatcal4())
                + "\n" + str(var_check5()) + "\t\t" + str(vatcal5())
                + "\n" + str(var_check6()) + "\t\t\t" + str(vatcal6())
                + "\n" + divide + "\n" + str(totalnotax()) + "\n" + str(vat_total())
                + "\n" + str((totaltax())) + "\n" + divide
                + "\n" + str(payment_choice())
                )
    file = asksaveasfile(defaultextension=".txt")
    file.write(textfile)


def clearbutton():
    p1cnEntry.delete(0, 'end')
    p2cnEntry.delete(0, 'end')
    p3cnEntry.delete(0, 'end')
    p4cnEntry.delete(0, 'end')
    p5cnEntry.delete(0, 'end')
    p6cnEntry.delete(0, 'end')
    ilosc1Entry.delete(0, 'end')
    ilosc2Entry.delete(0, 'end')
    ilosc3Entry.delete(0, 'end')
    ilosc4Entry.delete(0, 'end')
    ilosc5Entry.delete(0, 'end')
    ilosc6Entry.delete(0, 'end')
    cashEntry.delete(0, 'end')
    P1Var.set(0)
    P2Var.set(0)
    P3Var.set(0)
    P4Var.set(0)
    P5Var.set(0)
    P6Var.set(0)


# TOTAL TAX / NO TAX  DEF

def totaltax():
    notax1 = p1cn.get()
    notax2 = p2cn.get()
    notax3 = p3cn.get()
    notax4 = p4cn.get()
    notax5 = p5cn.get()
    notax6 = p6cn.get()

    quantity1 = ilosc1.get()
    quantity2 = ilosc2.get()
    quantity3 = ilosc3.get()
    quantity4 = ilosc4.get()
    quantity5 = ilosc5.get()
    quantity6 = ilosc6.get()

    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    bt1 = (notax1 * taxcalc * quantity1)
    bt2 = (notax2 * taxcalc + quantity2)
    bt3 = (notax3 * taxcalc * quantity3)
    bt4 = (notax4 * taxcalc * quantity4)
    bt5 = (notax5 * taxcalc * quantity5)
    bt6 = (notax6 * taxcalc * quantity6)
    taxprice = bt1 + bt2 + bt3 + bt4 + bt5 + bt6
    return "SUMA BRUTTO\t\t\t\t" + str(taxprice)


def totalnotax():
    notax1 = p1cn.get()
    notax2 = p2cn.get()
    notax3 = p3cn.get()
    notax4 = p4cn.get()
    notax5 = p5cn.get()
    notax6 = p6cn.get()

    quantity1 = ilosc1.get()
    quantity2 = ilosc2.get()
    quantity3 = ilosc3.get()
    quantity4 = ilosc4.get()
    quantity5 = ilosc5.get()
    quantity6 = ilosc6.get()

    nt1 = (notax1 * quantity1)
    nt2 = (notax2 * quantity2)
    nt3 = (notax3 * quantity3)
    nt4 = (notax4 * quantity4)
    nt5 = (notax5 * quantity5)
    nt6 = (notax6 * quantity6)

    notax = (nt1 + nt2 + nt3 + nt4 + nt5 + nt6)
    return "SUMA NETTO\t\t\t\t" + str(notax)


# TOTAL VAT TO PAY

def vat_total():
    notax1 = p1cn.get()
    notax2 = p2cn.get()
    notax3 = p3cn.get()
    notax4 = p4cn.get()
    notax5 = p5cn.get()
    notax6 = p6cn.get()

    quantity1 = ilosc1.get()
    quantity2 = ilosc2.get()
    quantity3 = ilosc3.get()
    quantity4 = ilosc4.get()
    quantity5 = ilosc5.get()
    quantity6 = ilosc6.get()

    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    bt1 = (notax1 * taxcalc * quantity1)
    bt2 = (notax2 * taxcalc + quantity2)
    bt3 = (notax3 * taxcalc * quantity3)
    bt4 = (notax4 * taxcalc * quantity4)
    bt5 = (notax5 * taxcalc * quantity5)
    bt6 = (notax6 * taxcalc * quantity6)

    nt1 = (notax1 * quantity1)
    nt2 = (notax2 * quantity2)
    nt3 = (notax3 * quantity3)
    nt4 = (notax4 * quantity4)
    nt5 = (notax5 * quantity5)
    nt6 = (notax6 * quantity6)

    notax = (nt1 + nt2 + nt3 + nt4 + nt5 + nt6)
    taxprice = (bt1 + bt2 + bt3 + bt4 + bt5 + bt6)
    total_vat = taxprice - notax
    return "KWOTA PTU 23%\t\t\t\t" + str(total_vat)


# VAT CALCULATION DEF

def vatcal1():
    quantity = ilosc1.get()
    notax = p1cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


def vatcal2():
    quantity = ilosc2.get()
    notax = p2cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


def vatcal3():
    quantity = ilosc3.get()
    notax = p3cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


def vatcal4():
    quantity = ilosc4.get()
    notax = p4cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


def vatcal5():
    quantity = ilosc5.get()
    notax = p5cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


def vatcal6():
    quantity = ilosc6.get()
    notax = p6cn.get()
    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)
    taxprice = notax * taxcalc
    if notax and quantity > 0:
        return float(taxprice * quantity)


# CHECKING VALUE OF CHECK BUTTONS

def var_check1():
    my_var1 = P1Var.get()
    if my_var1 == True:
        return p1


def var_check2():
    my_var = P2Var.get()
    if my_var == True:
        return p2


def var_check3():
    my_var = P3Var.get()
    if my_var == True:
        return p3


def var_check4():
    my_var = P4Var.get()
    if my_var == True:
        return p4


def var_check5():
    my_var = P5Var.get()
    if my_var == True:
        return p5


def var_check6():
    my_var = P6Var.get()
    if my_var == True:
        return p6


# DEF FOR PAYMENT_METHOD

def payment_choice():
    text = "WYBRANO PLATNOSC:"
    choice = str(p_method_variable.get())
    transaction = str("Nr transakcji" + "\t\t\t" + str("       ") + str(random.randint(100000, 999999)))
    cart_opt1 = "Nr rachunku został obciążony kwotą:\t"
    cash_opt1 = "WPLACONO:\t\t\t"


    notax1 = p1cn.get()
    notax2 = p2cn.get()
    notax3 = p3cn.get()
    notax4 = p4cn.get()
    notax5 = p5cn.get()
    notax6 = p6cn.get()

    quantity1 = ilosc1.get()
    quantity2 = ilosc2.get()
    quantity3 = ilosc3.get()
    quantity4 = ilosc4.get()
    quantity5 = ilosc5.get()
    quantity6 = ilosc6.get()

    cash_opt2 = float(cashE1.get())
    cash_opt3 = cashE1.get()

    VAT1 = 23
    taxcalc = (1 + VAT1 / 100)

    bt1 = (notax1 * taxcalc * quantity1)
    bt2 = (notax2 * taxcalc + quantity2)
    bt3 = (notax3 * taxcalc * quantity3)
    bt4 = (notax4 * taxcalc * quantity4)
    bt5 = (notax5 * taxcalc * quantity5)
    bt6 = (notax6 * taxcalc * quantity6)

    taxprice = (bt1 + bt2 + bt3 + bt4 + bt5 + bt6)


    inputres = float(cash_opt2 - taxprice)


    if p_method_variable.get() == "GOTOWKA":
        return str(text + "\n" + choice + "\n" + cash_opt1 + "\t" + str(float(cash_opt2)) + "\n" + "RESZTA:\t\t\t\t\t" + str(float(inputres)))
    elif p_method_variable.get() == "KARTA":
        return str(text + "\n" + choice + "\n" + transaction + "\n" + cart_opt1 + str(taxprice))

# HEAD OF RECEIPT

head = ("\t" + "   Sklep wędkarski sp z.o.o." + "\n" +
        "\t" + "\t" + "ul.Węgierska 3a" + "\n" +
        "\t" + "\t" + "Stargard 73-110" + "\n" +
        "\t" + "\t" + "NIP 765-23-11-048" + "\n" +
        str(actual_date) +
        str(current_time) + "\n" +
        str(kasa) + "\n" +
        "\t" + "\t" + "PARAGON FISKALNY" "\n" +
        str(divide)
        )

if __name__ == '__main__':
    receipt = tkinter.Tk()

    # ENTRY TUTAJ BEDA WPISYWANE DANE
    p1cn = tkinter.IntVar()
    p2cn = tkinter.IntVar()
    p3cn = tkinter.IntVar()
    p4cn = tkinter.IntVar()
    p5cn = tkinter.IntVar()
    p6cn = tkinter.IntVar()

    ilosc1 = tkinter.IntVar()
    ilosc2 = tkinter.IntVar()
    ilosc3 = tkinter.IntVar()
    ilosc4 = tkinter.IntVar()
    ilosc5 = tkinter.IntVar()
    ilosc6 = tkinter.IntVar()

    cashE1 = tkinter.IntVar()

    p1cnEntry = tkinter.Entry(receipt, textvariable=p1cn)
    p2cnEntry = tkinter.Entry(receipt, textvariable=p2cn)
    p3cnEntry = tkinter.Entry(receipt, textvariable=p3cn)
    p4cnEntry = tkinter.Entry(receipt, textvariable=p4cn)
    p5cnEntry = tkinter.Entry(receipt, textvariable=p5cn)
    p6cnEntry = tkinter.Entry(receipt, textvariable=p6cn)

    ilosc1Entry = tkinter.Entry(receipt, textvariable=ilosc1)
    ilosc2Entry = tkinter.Entry(receipt, textvariable=ilosc2)
    ilosc3Entry = tkinter.Entry(receipt, textvariable=ilosc3)
    ilosc4Entry = tkinter.Entry(receipt, textvariable=ilosc4)
    ilosc5Entry = tkinter.Entry(receipt, textvariable=ilosc5)
    ilosc6Entry = tkinter.Entry(receipt, textvariable=ilosc6)

    cashEntry = tkinter.Entry(receipt, textvariable=cashE1)

    # LABELS

    label1 = tkinter.Label(receipt, text="WITAJ W KREATORZE PARAGONU SKLEPU WĘDKARSKIEGO")
    label2 = tkinter.Label(receipt, text='WYBIERZ SWOJE PRODUKTY:')
    label3 = tkinter.Label(receipt, text='CENA NETTO PRODUKTU')
    label4 = tkinter.Label(receipt, text='ILOSC')
    label5 = tkinter.Label(receipt, text='WYBIERZ METODĘ PLATNOSCI:')
    label6 = tkinter.Label(receipt, text='\n\n')
    label7 = tkinter.Label(receipt, text='Tutaj wpisz ilość \n wpłacanej gotówki.')
    # PRODUKTY I WYBORY (CHECK BUTTON)

    P1Var = tkinter.IntVar()
    P2Var = tkinter.IntVar()
    P3Var = tkinter.IntVar()
    P4Var = tkinter.IntVar()
    P5Var = tkinter.IntVar()
    P6Var = tkinter.IntVar()

    P1 = tkinter.Checkbutton(text=p1, onvalue=1, offvalue=0, variable=P1Var)
    P2 = tkinter.Checkbutton(text=p2, onvalue=1, offvalue=0, variable=P2Var)
    P3 = tkinter.Checkbutton(text=p3, onvalue=1, offvalue=0, variable=P3Var)
    P4 = tkinter.Checkbutton(text=p4, onvalue=1, offvalue=0, variable=P4Var)
    P5 = tkinter.Checkbutton(text=p5, onvalue=1, offvalue=0, variable=P5Var)
    P6 = tkinter.Checkbutton(text=p6, onvalue=1, offvalue=0, variable=P6Var)

    # CLEAR / SAVE
    cButton = tkinter.Button(receipt, text='Wyczyść', command=clearbutton)
    saveButton = tkinter.Button(receipt, text='Zapisz swój paragon', command=savebutton)

    # PAYMENT_METHOD BUTTON

    p_method_variable = tkinter.StringVar()
    choice1 = p_method_variable.set(" ")
    choice2 = p_method_variable.set(" ")
    pmethod1 = tkinter.Radiobutton(receipt, text="PLATNOSC GOTOWKA", variable=p_method_variable, value="GOTOWKA",
                                   indicatoron=0)
    pmethod2 = tkinter.Radiobutton(receipt, text="PLATNOSC KARTA", variable=p_method_variable, value="KARTA",
                                   indicatoron=0)

    # CREATOR_SETUP

    p1cnEntry.grid(row=4, column=1)
    p2cnEntry.grid(row=5, column=1)
    p3cnEntry.grid(row=6, column=1)
    p4cnEntry.grid(row=7, column=1)
    p5cnEntry.grid(row=8, column=1)
    p6cnEntry.grid(row=9, column=1)
    ilosc1Entry.grid(row=4, column=2)
    ilosc2Entry.grid(row=5, column=2)
    ilosc3Entry.grid(row=6, column=2)
    ilosc4Entry.grid(row=7, column=2)
    ilosc5Entry.grid(row=8, column=2)
    ilosc6Entry.grid(row=9, column=2)
    cashEntry.grid(row=16, column=0)
    # LABELS
    label1.grid(row=1, column=1)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=1)
    label4.grid(row=3, column=2)
    label5.grid(row=13, column=0)
    label6.grid(row=14, column=0)
    label7.grid(row=17, column=0)

    # CHECKBUTTONS
    P1.grid(row=4, column=0)
    P2.grid(row=5, column=0)
    P3.grid(row=6, column=0)
    P4.grid(row=7, column=0)
    P5.grid(row=8, column=0)
    P6.grid(row=9, column=0)

    # CHOICE BUTTONS

    cButton.grid(row=13, column=2)
    saveButton.grid(row=18, column=2)
    pmethod1.grid(row=15, column=0)
    pmethod2.grid(row=15, column=1)
    receipt.mainloop()
