from tkinter import*
import tkinter as tk
import random
import time
import datetime

root = tk.Tk()
root.geometry("1350x750+0+0")
root.title("Finalmenu")
root.configure(background='pale turquoise')

Tops = Frame(root, width=500, height=100, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=500, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=500, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=200, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=200, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width=460, height=500, bd=4, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=460, height=50, bd=4, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=200, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=200, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=440, height=200, bd=8, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=200, bd=8, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='steel blue')
f1.configure(background='pale turquoise')
f2.configure(background='steel blue')
f1a.configure(background='black')
f2a.configure(background='black')
fb2.configure(background='black')
f1aa.configure(background='steel blue')
f1ab.configure(background='steel blue')
f2aa.configure(background='steel blue')
f2ab.configure(background='steel blue')

def CostofItem():
    Item1=float(E_Latta.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latte.get())
    Item4 = float(E_Cappuccino.get())
    Item5 = float(E_Vale_Coffee.get())
    Item6 = float(E_American_Coffee.get())
    Item7 = float(E_African_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())
    Item9 = float(E_CoffeeCake.get())
    Item10 = float(E_CheeseCake.get())
    Item11 = float(E_Red_velvet.get())
    Item12 = float(E_Sponge_cake.get())
    Item13 = float(E_Shortcake.get())
    Item14 = float(E_Cookie.get())
    Item15 = float(E_Coconut_cake.get())
    Item16 = float(E_Custard_tart.get())

    PriceofDrinks=(Item1 * 50) + (Item2 * 60) + (Item3 * 70) \
                    +(Item4 * 50) + (Item5 * 100) + (Item6 * 65) + (Item7 * 55) + (Item8 * 60)
    PriceofCakes= (Item9 * 150) + (Item10 * 200) + (Item11 * 250) \
                    + (Item12 * 200) + (Item13 * 170) + (Item14 * 180) + (Item15 * 270) + (Item16 * 300)

    DrinksPrice="Rs."+ str(PriceofDrinks)
    CakesPrice = "Rs."+ str('%.2f' % (PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="Rs."+str('%.2f'%(2))
    ServiceCharge.set(SC)
    SubTotalofITEMS="Rs."+str('%.2f'%(PriceofDrinks + PriceofCakes + 1))
    SubTotal.set(SubTotalofITEMS)

    Tax="Rs."+str('%.2f'%((PriceofDrinks + PriceofCakes + 1)*0.10))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofCakes + 1)*0.05)
    TC="Rs."+str('%.2f'%(PriceofDrinks + PriceofCakes + 1 + TT))
    TotalCost.set(TC)


def qExit():
    qExit= messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
 PaidTax.set("")
 SubTotal.set("")
 TotalCost.set("")
 CostofCakes.set("")
 CostofDrinks.set("")
 ServiceCharge.set("")
 txtReceipt.delete("1.0",END)

 E_Latta.set("0")
 E_Espresso.set("0")
 E_Iced_Latte.set("0")
 E_Cappuccino.set("0")
 E_Vale_Coffee.set("0")
 E_American_Coffee.set("0")
 E_African_Coffee.set("0")
 E_Iced_Cappuccino.set("0")

 E_CoffeeCake.set("0")
 E_CheeseCake.set("0")
 E_Red_velvet.set("0")
 E_Sponge_cake.set("0")
 E_Shortcake.set("0")
 E_Cookie.set("0") 
 E_Coconut_cake.set("0")
 E_Custard_tart.set("0")

 var1.set(0)
 var2.set(0)
 var3.set(0)
 var4.set(0)
 var5.set(0)
 var6.set(0)
 var7.set(0)
 var8.set(0)
 var9.set(0)
 var10.set(0)
 var11.set(0)
 var12.set(0)
 var13.set(0)
 var14.set(0)
 var15.set(0)
 var16.set(0)

 txtLatta.configure(state=NORMAL)
 txtEspresso.configure(state=NORMAL)
 txtIced_Latte.configure(state=NORMAL)
 txtCappuccino.configure(state=NORMAL)
 txtVale_Coffee.configure(state=NORMAL)
 txtAmerican_Coffee.configure(state=NORMAL)
 txtAfrican_Coffee.configure(state=NORMAL)
 txtIced_Cappuccino.configure(state=NORMAL)

 txtCoffeeCake.configure(state=NORMAL)
 txtCheeseCake.configure(state=NORMAL)
 txtRed_velvet.configure(state=NORMAL)
 txtSponge_cake.configure(state=NORMAL)
 txtShortcake.configure(state=NORMAL)
 txtCookie.configure(state=NORMAL)
 txtCoconut_cake.configure(state=NORMAL)
 txtCustard_tart.configure(state=NORMAL)

def Receipt():
    CostofItem()
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("BILL"+randomRef)
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() +'\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t\t'+"Number of Items\n\n")
    if(E_Latta.get()!='0'):
        txtReceipt.insert(END, 'Latte: \t\t\t\t\t'+E_Latta.get()+"\n")    
    if(E_Espresso.get()!='0'):
        txtReceipt.insert(END, 'Espresso: \t\t\t\t\t' + E_Espresso.get() + "\n")
    if(E_Iced_Latte.get()!='0'):
        txtReceipt.insert(END, 'Iced_Latte: \t\t\t\t\t' + E_Iced_Latte.get() + "\n")
    if(E_Cappuccino.get()!='0'):
        txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() + "\n")
    if(E_Vale_Coffee.get()!='0'):
        txtReceipt.insert(END, 'Vale_Coffee: \t\t\t\t\t' + E_Vale_Coffee.get() + "\n")
    if(E_American_Coffee.get()!='0'):
        txtReceipt.insert(END, 'American_Coffee: \t\t\t\t\t' + E_American_Coffee.get() + "\n")
    if(E_African_Coffee.get()!='0'):
        txtReceipt.insert(END, 'African_Coffee: \t\t\t\t\t' + E_African_Coffee.get() + "\n")
    if(E_Iced_Cappuccino.get()!='0'):
        txtReceipt.insert(END, 'Iced_Cappuccino: \t\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")
    if(E_CoffeeCake.get()!='0'):
        txtReceipt.insert(END, 'CoffeeCake: \t\t\t\t\t' + E_CoffeeCake.get() + "\n")
    if(E_CheeseCake.get()!='0'):
        txtReceipt.insert(END, 'CheeseCake: \t\t\t\t\t' + E_CheeseCake.get() + "\n")
    if(E_Red_velvet.get()!='0'):
        txtReceipt.insert(END, 'Red_velvet: \t\t\t\t\t' + E_Red_velvet.get() + "\n")
    if(E_Sponge_cake.get()!='0'):
        txtReceipt.insert(END, 'Sponge_cake: \t\t\t\t\t' + E_Sponge_cake.get() + "\n")
    if(E_Shortcake.get()!='0'):
        txtReceipt.insert(END, 'Shortcake: \t\t\t\t\t' + E_Shortcake.get() + "\n")
    if(E_Coconut_cake.get()!='0'):
        txtReceipt.insert(END, 'Coconut_cake: \t\t\t\t\t' + E_Coconut_cake.get() + "\n")
    if(E_Custard_tart.get()!='0'):
        txtReceipt.insert(END, 'Custard_tart: \t\t\t\t\t' + E_Custard_tart.get() + "\n")
    
    txtReceipt.insert(END,"\n"+'Cost of Drinks:\t\t' + CostofDrinks.get() + '\tTax Paid:\t' + PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Cakes:\t\t' + CostofCakes.get() + '\tSubTotal:\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t' + ServiceCharge.get() + '\tTotal Cost:\t' + TotalCost.get() + "\n")

lblInfo = Label(Tops, font=('Comic Sans MS',50),fg='blue4',text="   Menu Card   ", bd=3)
lblInfo.grid(row=0,column=0)
#================================================Methods==============================================================



def chkbutton_value():
    if(var1.get() == 1):
        txtLatta.configure(state= NORMAL)
    elif var1.get()==0:
        txtLatta.configure(state= DISABLED)
        E_Latta.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
    elif var3.get() == 0:
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latte.set("0")
    if (var4.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var4.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if (var5.get() == 1):
        txtVale_Coffee.configure(state=NORMAL)
    elif var5.get() == 0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
    if (var6.get() == 1):
        txtAmerican_Coffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")
    if (var7.get() == 1):
        txtAfrican_Coffee.configure(state=NORMAL)
    elif var7.get() == 0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
    if (var8.get() == 1):
        txtIced_Cappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")
    if (var9.get() == 1):
        txtCoffeeCake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffeeCake.configure(state=DISABLED)
        E_CoffeeCake.set("0")
    if (var10.get() == 1):
        txtCheeseCake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtCheeseCake.configure(state=DISABLED)
        E_CheeseCake.set("0")
    if (var11.get() == 1):
        txtRed_velvet.configure(state=NORMAL)
    elif var11.get() == 0:
        txtRed_velvet.configure(state=DISABLED)
        E_Red_velvet.set("0")
    if (var12.get() == 1):
        txtSponge_cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtSponge_cake.configure(state=DISABLED)
        E_Sponge_cake.set("0")
    if (var13.get() == 1):
        txtShortcake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtShortcake.configure(state=DISABLED)
        E_Shortcake.set("0")
    if (var14.get() == 1):
        txtCookie.configure(state=NORMAL)
    elif var14.get() == 0:
        txtCookie.configure(state=DISABLED)
        E_Cookie.set("0")
    if (var15.get() == 1):
        txtCoconut_cake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtCoconut_cake.configure(state=DISABLED)
        E_Coconut_cake.set("0")
    if (var16.get() == 1):
        txtCustard_tart.configure(state=NORMAL)
    elif var16.get() == 0:
        txtCustard_tart.configure(state=DISABLED)
        E_Custard_tart.set("0")





DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()



var1=IntVar()
E_Latta=StringVar()
E_Latta.set("0")

var2=IntVar()
E_Espresso=StringVar()
E_Espresso.set("0")

var3=IntVar()
E_Iced_Latte=StringVar()
E_Iced_Latte.set("0")

var4=IntVar()
E_Cappuccino=StringVar()
E_Cappuccino.set("0")

var5=IntVar()
E_Vale_Coffee=StringVar()
E_Vale_Coffee.set("0")

var6=IntVar()
E_American_Coffee=StringVar()
E_American_Coffee.set("0")

var7=IntVar()
E_African_Coffee=StringVar()
E_African_Coffee.set("0")

var8=IntVar()
E_Iced_Cappuccino=StringVar()
E_Iced_Cappuccino.set("0")

var9=IntVar()
E_CoffeeCake=StringVar()
E_CoffeeCake.set("0")

var10=IntVar()
E_CheeseCake=StringVar()
E_CheeseCake.set("0")

var11=IntVar()
E_Red_velvet=StringVar()
E_Red_velvet.set("0")

var12=IntVar()
E_Sponge_cake=StringVar()
E_Sponge_cake.set("0")

var13=IntVar()
E_Shortcake=StringVar()
E_Shortcake.set("0")

var14=IntVar()
E_Cookie=StringVar()
E_Cookie.set("0")

var15=IntVar()
E_Coconut_cake=StringVar()
E_Coconut_cake.set("0")

var16=IntVar()
E_Custard_tart=StringVar()
E_Custard_tart.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#==================================================Drinks=============================================================#
Latta = Checkbutton(f1aa, text="Latte - 50Rs.\t",variable= var1, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=0, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso - 60Rs.\t",variable= var2, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=1, sticky=W)
Iced_Latte = Checkbutton(f1aa, text="Iced_Latte - 70Rs.\t",variable= var3, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=2, sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino - 50Rs.\t",variable= var4, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=3, sticky=W)
Vale_Coffee = Checkbutton(f1aa, text="Vale_Coffee - 100Rs.\t",variable= var5, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=4, sticky=W)
American_Coffee = Checkbutton(f1aa, text="American_Coffee - 65Rs.\t",variable= var6, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=5, sticky=W)
African_Coffee = Checkbutton(f1aa, text="African_Coffee - 55Rs.\t",variable= var7, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=6, sticky=W)
Iced_Cappuccino = Checkbutton(f1aa, text="Iced_Cappuccino - 60Rs.\t",variable= var8, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=7, sticky=W)

#==============================================Cakes================================================================#
CoffeeCake = Checkbutton(f1ab, text="CoffeeCake - 150Rs.\t",variable= var9, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=0, sticky=W)
CheeseCake = Checkbutton(f1ab, text="CheeseCake - 200Rs.\t",variable= var10, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=1, sticky=W)
Red_velvet = Checkbutton(f1ab, text="Red_velvet - 250Rs.\t",variable= var11, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=2, sticky=W)
Sponge_cake = Checkbutton(f1ab, text="Sponge_cake - 200Rs.\t",variable= var12, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=3, sticky=W)
Shortcake = Checkbutton(f1ab, text="Shortcake - 170Rs.\t",variable= var13, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=4, sticky=W)
Cookie = Checkbutton(f1ab, text="Cookie - 180Rs.\t",variable= var14, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=5, sticky=W)
Coconut_cake = Checkbutton(f1ab, text="Coconut_cake - 270Rs.\t",variable= var15, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=6, sticky=W)
Custard_tart = Checkbutton(f1ab, text="Custard_tart - 300Rs.\t",variable= var16, onvalue=1, offvalue=0,bg="steel blue",
                    font=('Comic Sans MS',18,'bold')).grid(row=7, sticky=W)
#==============================================Enter Widgets for Drinks======================================================#
txtLatta = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Latta, state=NORMAL)
txtLatta.grid(row=0,column=1)
txtEspresso = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Espresso, state=NORMAL)
txtEspresso.grid(row=1,column=1)
txtIced_Latte = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Iced_Latte, state=NORMAL)
txtIced_Latte.grid(row=2,column=1)
txtCappuccino = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Cappuccino, state=NORMAL)
txtCappuccino.grid(row=3,column=1)
txtVale_Coffee = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Vale_Coffee, state=NORMAL)
txtVale_Coffee.grid(row=4,column=1)
txtAmerican_Coffee = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_American_Coffee, state=NORMAL)
txtAmerican_Coffee.grid(row=5,column=1)
txtAfrican_Coffee = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_African_Coffee, state=NORMAL)
txtAfrican_Coffee.grid(row=6,column=1)
txtIced_Cappuccino = Entry(f1aa, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Iced_Cappuccino, state=NORMAL)
txtIced_Cappuccino.grid(row=7,column=1)
#==============================================Enter Widgets for Cakes======================================================#

txtCoffeeCake = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_CoffeeCake, state=NORMAL)
txtCoffeeCake.grid(row=0,column=1)
txtCheeseCake = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_CheeseCake, state=NORMAL)
txtCheeseCake.grid(row=1,column=1)
txtRed_velvet = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Red_velvet, state=NORMAL)
txtRed_velvet.grid(row=2,column=1)
txtSponge_cake = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Sponge_cake, state=NORMAL)
txtSponge_cake.grid(row=3,column=1)
txtShortcake = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Shortcake, state=NORMAL)
txtShortcake.grid(row=4,column=1)
txtCookie = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Cookie, state=NORMAL)
txtCookie.grid(row=5,column=1)
txtCoconut_cake = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Coconut_cake, state=NORMAL)
txtCoconut_cake.grid(row=6,column=1)
txtCustard_tart = Entry(f1ab, font=('Comic Sans MS',18,'bold'), bd=8, width=6, justify='left', textvariable=E_Custard_tart, state=NORMAL)
txtCustard_tart.grid(row=7,column=1)
#==============================================Information================================================================#
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, bd=8, height=22)
txtReceipt.grid(row=1,column=0)
#========================================Cost Items Information=======================================================
lblCostofDrinks=Label(f2aa,font=('arial', 16, 'bold'), text="Cost of Drinks", bd=8, anchor='w',bg="steel blue")
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks=Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=1, justify='left', textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2, column=1)

lblCostofCakes=Label(f2aa,font=('arial', 16, 'bold'), text="Cost of Cakes", bd=8, anchor='w',bg="steel blue")
lblCostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes=Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=CostofCakes)
txtCostofCakes.grid(row=3, column=1)

lblServiceCharge=Label(f2aa,font=('arial', 16, 'bold'), text="GST", bd=8, anchor='w',bg="steel blue")
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge=Entry(f2aa, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left')
txtServiceCharge.grid(row=4, column=1)
#========================================Payment Information==========================================================
lblPaidTax=Label(f2ab,font=('arial', 16, 'bold'), text="Paid Tax", bd=8,bg="steel blue")
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax=Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=2, column=1)

lblSubTotal=Label(f2ab,font=('arial', 16, 'bold'), text="Sub Total", bd=8,bg="steel blue")
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal=Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotalCost=Label(f2ab,font=('arial', 16, 'bold'), text="Total", bd=8,bg="steel blue")
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost=Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1)

#==============================================button=================================================================#

btnTotal=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                text="Total ", command=CostofItem).grid(row=0, column=0)

btnReceipt=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                text="Receipt", command=Receipt).grid(row=0, column=1)

btnReset=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                text="Reset",command=Reset).grid(row=0, column=2)

btnExit=Button(fb2,padx=16,pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                text="Exit",command=qExit).grid(row=0, column=3)

root.mainloop()
