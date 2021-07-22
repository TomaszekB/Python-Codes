import tkinter
from tkinter.filedialog import asksaveasfile


####################################################

def savebutton():
    print("Kliknięto przycisk zapisz")
    a = ('1. ' + ' ' + sventry1.get() + ' ' + sbox1.get() + '-' + sbox2.get() + '-' + sbox3.get()) + '\n' + ('2. ' + sventry2.get()) + '\n' + ('3. ' + sventry3.get()) \
        + '\n' + ('4. ' + sventry4.get()) + '\n' + ('5. ' + sventry5.get()) + '\n' + ('6. ' + sventry6.get())\
        + '\n' + ('7. ' + sventry7.get()) + '\n' + ('8. ' + sventry8.get()) + '\n' + ('9. ' + sventry9.get()) \
        + '\n' + ('10. ' + sventry10.get()) + '\n' + ('11. ' + sventry11.get()) + '\n' + ('12. ' + sventry12.get()) \
        + '\n' + ('13. ' + sventry13.get()) + '\n'
    file = asksaveasfile(defaultextension=".txt")
    file.write(a)


#############################################

def clearbutton():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    entry12.delete(0, 'end')
    entry13.delete(0, 'end')

    spinbox1.delete(0, 'end')
    spinbox2.delete(0, 'end')
    spinbox3.delete(0, 'end')


if __name__ == '__main__':
    glowneOkno = tkinter.Tk()

    ##### ENTRY TUTAJ BEDA WPISYWANE DANE ####

    sventry1 = tkinter.StringVar()
    sventry2 = tkinter.StringVar()
    sventry3 = tkinter.StringVar()
    sventry4 = tkinter.StringVar()
    sventry5 = tkinter.StringVar()
    sventry6 = tkinter.StringVar()
    sventry7 = tkinter.StringVar()
    sventry8 = tkinter.StringVar()
    sventry9 = tkinter.StringVar()
    sventry10 = tkinter.StringVar()
    sventry11 = tkinter.StringVar()
    sventry12 = tkinter.StringVar()
    sventry13 = tkinter.StringVar()

    entry1 = tkinter.Entry(glowneOkno, textvariable=sventry1)
    entry2 = tkinter.Entry(glowneOkno, textvariable=sventry2)
    entry3 = tkinter.Entry(glowneOkno, textvariable=sventry3)
    entry4 = tkinter.Entry(glowneOkno, textvariable=sventry4)
    entry5 = tkinter.Entry(glowneOkno, textvariable=sventry5)
    entry6 = tkinter.Entry(glowneOkno, textvariable=sventry6)
    entry7 = tkinter.Entry(glowneOkno, textvariable=sventry7)
    entry8 = tkinter.Entry(glowneOkno, textvariable=sventry8)
    entry9 = tkinter.Entry(glowneOkno, textvariable=sventry9)
    entry10 = tkinter.Entry(glowneOkno, textvariable=sventry10)
    entry11 = tkinter.Entry(glowneOkno, textvariable=sventry11)
    entry12 = tkinter.Entry(glowneOkno, textvariable=sventry12)
    entry13 = tkinter.Entry(glowneOkno, textvariable=sventry13)

    ##SPINBOXY##

    sbox1 = tkinter.StringVar()
    sbox2 = tkinter.StringVar()
    sbox3 = tkinter.StringVar()

    spinbox1 = tkinter.Spinbox(glowneOkno, from_=0, to=31, textvariable=sbox1)
    spinbox2 = tkinter.Spinbox(glowneOkno, from_=1, to=12, textvariable=sbox2)
    spinbox3 = tkinter.Spinbox(glowneOkno, from_=1940, to=2021, textvariable=sbox3)

    #### ETYKIETY ( PRZYPISY ) #####

    label1 = tkinter.Label(glowneOkno, text='1. Miejscowość i data: ')
    label2 = tkinter.Label(glowneOkno, text='2. Imię i nazwisko: ')
    label3 = tkinter.Label(glowneOkno, text='3. Adres zamieszkania: ')
    label4 = tkinter.Label(glowneOkno, text='4. Numer telefonu: ')
    label5 = tkinter.Label(glowneOkno, text='5. PESEL/REGON: ')
    label6 = tkinter.Label(glowneOkno, text='6. FORMULARZ DANYCH: \n\n\n\n\n')
    label7 = tkinter.Label(glowneOkno, text='7. Wydział Spraw Obywatelskich \nURZĄD MIASTA SZCZECIN \npl. Armii Krajowej 1'
                                            ' \n70-456 Szczecin \n\n\n\n')
    label8 = tkinter.Label(glowneOkno, text='8. ZAWIADOMIENIE \no zbyciu/nabyciu* pojazdu \n\n\n\n\n')
    label9 = tkinter.Label(glowneOkno, text='9. Zgłaszam, że w dniu')
    label10 = tkinter.Label(glowneOkno, text='10. zawarto umowę przeniesienia własności pojazdu (marka, model pojazdu)')
    label11 = tkinter.Label(glowneOkno, text='11. numer rejestracyjny')
    label12 = tkinter.Label(glowneOkno, text='12. Imię/nazwisko/nazwa \n/adres zbywcy**/nabywcy***: ')
    label13 = tkinter.Label(glowneOkno, text='\n\nZałączam ksero/skan dokumentu \nprzenoszącego własność pojazdu. '
                                             '\n\n\n(*proszę wykreślić niepotrzebne) \n(**w przypadku zgłoszenia '
                                             'nabycia pojazdu) \n(***w przypadku zgłoszenia zbycia pojazdu)')

    ################# PRZYCISKI ##########################################

    cButton = tkinter.Button(glowneOkno, text='Wyczyść', command=clearbutton)
    sButton = tkinter.Button(glowneOkno, text='Zapisz', command=savebutton)

    ################ USTAWIENIA W OKNIE ####################################

    label1.grid(row=1, column=3)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    label4.grid(row=4, column=0)
    label5.grid(row=5, column=0)
    label6.grid(row=0, column=2)
    label7.grid(row=6, column=7)
    label8.grid(row=7, column=3)
    label9.grid(row=8, column=0)
    label10.grid(row=8, column=2)
    label11.grid(row=9, column=0)
    label12.grid(row=10, column=0)
    label13.grid(row=11, column=0)

    ###################################################

    spinbox1.grid(row=1, column=5)
    spinbox2.grid(row=1, column=6)
    spinbox3.grid(row=1, column=7)

    ####################################################

    entry1.grid(row=1, column=4)
    entry2.grid(row=2, column=1)
    entry3.grid(row=3, column=1)
    entry4.grid(row=4, column=1)
    entry5.grid(row=5, column=1)
    entry6.grid(row=8, column=1)
    entry7.grid(row=8, column=3)
    entry8.grid(row=8, column=4)
    entry9.grid(row=9, column=1)
    entry10.grid(row=10, column=1)
    entry11.grid(row=10, column=2)
    entry12.grid(row=10, column=3)
    entry13.grid(row=10, column=4)

    cButton.grid(row=15, column=2)
    sButton.grid(row=15, column=3)
    glowneOkno.mainloop()
