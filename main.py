from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime
import time


class Payroll:

    def __init__(self,root):
        self.root = root
        self.root.title("Система клиентских платежей")
        self.root.geometry("1350x600+0+0")
        self.root.configure(background='gainsboro')


        EmployeeName = StringVar()
        Address = StringVar()
        Reference = StringVar()
        EmployerName = StringVar()
        CityWeighting = IntVar()
        BasicSalary = IntVar()
        OverTime = StringVar()
        GrossPay = StringVar()
        NetPay = StringVar()
        Tax = StringVar()
        Pension = StringVar()
        EmployerLoan = StringVar()
        NIPayment = StringVar()
        Deductions = StringVar()
        PostCode = StringVar()
        Gender = StringVar()
        Payday = StringVar()
        TaxPeriod = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        TaxablePay = StringVar()
        PensionablePay = StringVar()
        OtherPaymentDue = StringVar()
        TaxCode = StringVar()

        CityWeighting.set("")
        BasicSalary.set("")



        #========================Exit========================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Система платежей", "Подтвредить выход?")
            if iExit > 0:
                root.destroy()
                return

        #==============Reset===================================================================================================
        def Reset():
            EmployeeName.set("")
            Address.set("")
            Reference.set("")
            EmployerName.set("")
            CityWeighting.set("")
            BasicSalary.set("")
            OverTime.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            EmployerLoan.set("")
            NIPayment.set("")
            Deductions.set("")
            PostCode.set("")
            Gender.set("")
            Payday.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            OtherPaymentDue.set("")
            TaxCode.set("")
            self.txtReceipt.delete("1.0", END)





        #===========Payment=======================================================================================================

        def PayRef():
            Payday.set(time.strftime("%d/%m/%Y"))
            Refpay = random.randint(20000, 709494)
            Refpaid = ("PR" + str(Refpay))
            Reference.set(Refpaid)


            NIpay = random.randint(34051, 409123)
            NIpaid = str(NIpay)
            NINumber.set(NIpaid)

            iDate = datetime.datetime.now()
            TaxPeriod.set(iDate.month)


            Ncode = random.randint(1290, 13123)
            CodeNI = str(Ncode)
            NICode.set(CodeNI)


            iTaxCode = random.randint(7900, 13230)
            PaymentTaxCode = str(iTaxCode)
            TaxCode.set(PaymentTaxCode)


        def MonthlySalary():
            PayRef()
            BS = float(BasicSalary.get())
            CW = float(CityWeighting.get())
            OT = float(OverTime.get())

            MTax = ((BS + CW + OT) * 0.3)
            TTax = "£", str('%.2f'%(MTax))
            Tax.set(TTax)

            M_Pension = ((BS + CW + OT) * 0.02)
            MM_Pension = "£", str('%.2f'%(M_Pension))
            Pension.set(MM_Pension)

            M_EmployerLoan = ((BS + CW + OT) * 0.012)
            MM_EmployerLoan = "£", str('%.2f'%(M_EmployerLoan))
            EmployerLoan.set(MM_EmployerLoan)

            M_NIPayment = ((BS + CW + OT) * 0.011)
            MM_NIPayment = "£", str('%.2f'%(M_NIPayment))
            NIPayment.set(MM_NIPayment)

            Deduct = (MTax + MM_Pension + M_WorkerLoan+ MM_NIPayment)
            Deduct_Payment = "£", str('%.2f'%(Deduct))
            Deductions.set(Deduct_Payment)
            GrossPay = "£",  str('%.2f' % (BS+ CW + OT))
            GrossPay.set(GrossPay)

            NetPayAfter = ((BS + CW + OT) - Deduct)
            NetAfter = "£", str('%.2f'%(NetPayAfter))
            NetPay.set(NetAfter)


            TaxablePay.set(TTax)
            PensionablePay.set(MM_Pension)
            OtherPaymentDue.set('0.00')















        MainFrame = Frame(self.root, bd=10, width=1800, height= 700, bg="gainsboro", relief=RIDGE)
        MainFrame.grid()




        TopFrame1 = Frame(MainFrame, bd=10, width=1350, height= 500, bg="gainsboro", relief=RIDGE)
        TopFrame1.grid()


        TopFrame2 = Frame(MainFrame, bd=10, width=1350, height= 100, bg="gainsboro", relief=RIDGE)
        TopFrame2.grid()

        TopFrame3 = Frame(MainFrame, bd=10, width=1350, height= 100, bg="gainsboro", relief=RIDGE)
        TopFrame3.grid()




        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height= 400, bg="gainsboro", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height= 180, bg="gainsboro", relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height= 180, bg="gainsboro", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame2, bd=5, width=300, height= 170, padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2, bd=5, width=300, height= 170, padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)



        LeftFrame3Left = Frame(LeftFrame, bd=5, width=320, height= 50, padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame3Left.pack(side=LEFT)
        LeftFrame3Right = Frame(LeftFrame2, bd=5, width=320, height= 50, padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame3Right.pack(side=RIGHT)

        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height= 400, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height= 300, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        RightFrame1b = Frame(RightFrame1, bd=5, width=310, height=100, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1b.pack(side=TOP)


        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height= 400, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2.pack(side=RIGHT)
        RightFrame2a = Frame(RightFrame2, bd=5, width=280, height= 50, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2, bd=5, width=280, height= 180, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2, bd=5, width=280, height= 100, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2, bd=5, width=280, height= 50, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2d.pack(side=TOP)
        RightFrame2e = Frame(RightFrame2, bd=5, width=280, height= 50, padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2e.pack(side=TOP)



        #=====================Title===========================
        self.lblTitle = Label(TopFrame1, font=('arial', 40 , 'bold'), text= "                           Система клиентских платежей             ", bd=10,
        bg="gainsboro" , justify =CENTER)
        self.lblTitle.grid(row=0, column=0)


        #===============================================================
        self.lblEmployeeName = Label(TopFrame2, font=('arial', 12 , 'bold'), text= "Имя работника", bd=10,
        bg="gainsboro" , justify =CENTER)
        self.lblEmployeeName.grid(row=0, column=0)
        self.txtEmployeeName = Entry(TopFrame2, font=('arial', 12 , 'bold'), bd=5, width=59, justify='left', textvariable=EmployeeName)
        self.txtEmployeeName.grid(row=0, column=1)



        self.lblAddress = Label(TopFrame2, font=('arial', 12 , 'bold'), text= "Адрес", bd=10,
        bg="gainsboro" , justify =CENTER)
        self.lblAddress.grid(row=1, column=0)
        self.txtAddress = Entry(TopFrame2, font=('arial', 12 , 'bold'), bd=5, width=59, justify='left', textvariable=Address)
        self.txtAddress.grid(row=1, column=1)

        self.lblPostCode = Label(TopFrame2, font=('arial', 12 , 'bold'), text= "Почтовый код", bd=5,
        bg="gainsboro" , anchor='w')
        self.lblPostCode.grid(row=0, column=2)
        self.txtPostCode = Entry(TopFrame2, font=('arial', 12 , 'bold'), bd=5, width=58, justify='left', textvariable=PostCode)
        self.txtPostCode.grid(row=0, column=3)



        self.lblGender = Label(TopFrame2, font=('arial', 12 , 'bold'), text= "Пол", bd=10,
        bg="gainsboro" ,anchor='w' )
        self.lblGender.grid(row=1, column=2)
        self.txtGender = Entry(TopFrame2, font=('arial', 12 , 'bold'), bd=5, width=59, justify='left', textvariable=Gender)
        self.txtGender.grid(row=1, column=3)

        self.lblReference = Label(LeftFrame1, font=('arial', 12 , 'bold'), text= "Справка", bd=10,
        bg="gainsboro" ,anchor='e' )
        self.lblReference.grid(row=0, column=0)
        self.txtReference = Entry(LeftFrame1, font=('arial', 12 , 'bold'), bd=5, width=57, justify='left', textvariable=Reference)
        self.txtReference.grid(row=0, column=1)

        self.lblEmployerName = Label(LeftFrame1, font=('arial', 12 , 'bold'), text= "Имя работадателя", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT )
        self.lblEmployerName.grid(row=1, column=0)
        self.txtEmployerName = Entry(LeftFrame1, font=('arial', 12 , 'bold'), bd=5, width=57, justify='left', textvariable=EmployerName)
        self.txtEmployerName.grid(row=1, column=1)


        self.lblEmployeeName = Label(LeftFrame1, font=('arial', 12 , 'bold'), text= "Имя сотрудника", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT )
        self.lblEmployeeName.grid(row=2, column=0)
        self.txtEmployeeName = Entry(LeftFrame1, font=('arial', 12 , 'bold'), bd=5, width=57, justify='left', textvariable=EmployeeName)
        self.txtEmployeeName.grid(row=2, column=1)


        self.lblCityWeighting = Label(LeftFrame2Left, font=('arial', 12 , 'bold'), text= "Надбавки", bd=10,
        bg="gainsboro" ,anchor='e', justify=LEFT )
        self.lblCityWeighting.grid(row=0, column=0)
        self.txtCityWeighting = Entry(LeftFrame2Left, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=CityWeighting)
        self.txtCityWeighting.grid(row=0, column=1)


        self.lblBasicSalary = Label(LeftFrame2Left, font=('arial', 12 , 'bold'), text= "Зарплата", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT )
        self.lblBasicSalary.grid(row=1, column=0)
        self.txtBasicSalary = Entry(LeftFrame2Left, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=BasicSalary)
        self.txtBasicSalary.grid(row=1, column=1)



        self.lblOverTime = Label(LeftFrame2Left, font=('arial', 12 , 'bold'), text= "Сверхурочная работа", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT )
        self.lblOverTime.grid(row=2, column=0)
        self.txtOverTime = Entry(LeftFrame2Left, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=OverTime)
        self.txtOverTime.grid(row=2, column=1)


        self.lblOtherPaymentDue = Label(LeftFrame2Left, font=('arial', 12 , 'bold'), text= "Прочие платежи", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT )
        self.lblOtherPaymentDue.grid(row=3, column=0)
        self.txtOtherPaymentDue = Entry(LeftFrame2Left, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=OtherPaymentDue)
        self.txtOtherPaymentDue.grid(row=3, column=1)



        self.lblTax = Label(LeftFrame2Right, font=('arial', 12 , 'bold'), text= "Налогооблажение", bd=10,
        bg="gainsboro" ,anchor='e')
        self.lblTax.grid(row=0, column=0)
        self.txtTax = Entry(LeftFrame2Right, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=Tax)
        self.txtTax.grid(row=0, column=1)



        self.lblPension = Label(LeftFrame2Right, font=('arial', 12 , 'bold'), text= "Пенсия", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblPension.grid(row=1, column=0)
        self.txtPension = Entry(LeftFrame2Right, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=Pension)
        self.txtPension.grid(row=1, column=1)


        self.lblEmployerLoan = Label(LeftFrame2Right, font=('arial', 12 , 'bold'), text= "Задоженность выплат для сотрудника", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblEmployerLoan.grid(row=2, column=0)
        self.txtEmployerLoan = Entry(LeftFrame2Right, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=EmployerLoan)
        self.txtEmployerLoan.grid(row=2, column=1)

        self.lblNIPayment = Label(LeftFrame2Right, font=('arial', 12 , 'bold'), text= "Государственное страхование", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblNIPayment.grid(row=3, column=0)
        self.txtNIPayment = Entry(LeftFrame2Right, font=('arial', 12 , 'bold'), bd=5, width=20, justify='left', textvariable=NIPayment)
        self.txtNIPayment.grid(row=3, column=1)

        self.lblGrossPay = Label(LeftFrame3Left, font=('arial', 12 , 'bold'), text= "Валовый размер выплат", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblGrossPay.grid(row=3, column=0)
        self.txtGrossPay = Entry(LeftFrame3Left, font=('arial', 12 , 'bold'), bd=5, width=23, justify='left', textvariable=GrossPay)
        self.txtGrossPay.grid(row=3, column=1)


        self.lblDeductions = Label(LeftFrame3Right, font=('arial', 12 , 'bold'), text= "Вычеты", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblDeductions.grid(row=3, column=0)
        self.txtDeductions = Entry(LeftFrame3Right, font=('arial', 12 , 'bold'), bd=5, width=23, justify='left', textvariable=Deductions)
        self.txtDeductions.grid(row=3, column=1)


        self.lblPayday = Label(RightFrame2a, font=('arial', 12 , 'bold'), text= "День зарплаты", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblPayday.grid(row=0, column=0)
        self.txtPayday = Entry(RightFrame2a, font=('arial', 12 , 'bold'), bd=5, width=19, justify='left', textvariable=Payday)
        self.txtPayday.grid(row=0, column=1)


        self.lblTaxPeriod = Label(RightFrame2b, font=('arial', 12 , 'bold'), text= "Период выплаты по налогам", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblTaxPeriod.grid(row=0, column=0)
        self.txtTaxPeriod = Entry(RightFrame2b, font=('arial', 12 , 'bold'), bd=5, width=19, justify='left', textvariable=TaxPeriod)
        self.txtTaxPeriod.grid(row=0, column=1)


        self.lblTaxCode = Label(RightFrame2b, font=('arial', 12 , 'bold'), text= "Налоговый номер", bd=5,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblTaxCode.grid(row=1, column=0)
        self.txtTaxCode = Entry(RightFrame2b, font=('arial', 12 , 'bold'), bd=5, width=16, justify='left', textvariable=TaxCode)
        self.txtTaxCode.grid(row=1, column=1)

        self.lblNINumber = Label(RightFrame2b, font=('arial', 12 , 'bold'), text= "Номер государственного страхования", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblNINumber.grid(row=2, column=0)
        self.txtNINumber = Entry(RightFrame2b, font=('arial', 12 , 'bold'), bd=5, width=16, justify='left', textvariable=NINumber)
        self.txtNINumber.grid(row=2, column=1)


        self.lblNICode = Label(RightFrame2b, font=('arial', 12 , 'bold'), text= "Код государственного страхования", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblNICode.grid(row=1, column=0)
        self.txtNICode = Entry(RightFrame2b, font=('arial', 12 , 'bold'), bd=5, width=16, justify='left', textvariable=NICode)
        self.txtNICode.grid(row=1, column=1)


        self.lblTaxablePay = Label(RightFrame2c, font=('arial', 12 , 'bold'), text= "Оплата налогов", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblTaxablePay.grid(row=0, column=0)
        self.txtTaxablePay = Entry(RightFrame2c, font=('arial', 12 , 'bold'), bd=5, width=11, justify='left', textvariable=TaxablePay)
        self.txtTaxablePay.grid(row=0, column=1)


        self.lblPensionablePay = Label(RightFrame2c, font=('arial', 12 , 'bold'), text= "Выплаты по пенсии", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblPensionablePay.grid(row=1, column=0)
        self.txtPensionablePay= Entry(RightFrame2c, font=('arial', 12 , 'bold'), bd=5, width=11, justify='left', textvariable=PensionablePay)
        self.txtPensionablePay.grid(row=1, column=1)


        self.lblNetPay = Label(RightFrame2d, font=('arial', 12 , 'bold'), text= "Выплаты online", bd=10,
        bg="gainsboro" ,anchor='w', justify=LEFT)
        self.lblNetPay.grid(row=0, column=0)
        self.txtNetPay = Entry(RightFrame2d, font=('arial', 12 , 'bold'), bd=5, width=11, justify='left', textvariable=NetPay)
        self.txtNetPay.grid(row=0, column=1)


        #============================================================================
        self.txtReceipt = Text(RightFrame2e, height = 20, width=40, bd=1,font=('arial', 9, 'bold'), bg='light cyan')
        self.txtReceipt.grid(row=1, column=0)

        self.btnPayment = Button(RightFrame2e, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), width=4,  text="Оплатить", command=MonthlySalary).grid(row=0, column=0)
        self.btnPayment = Button(RightFrame2e, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), width=4,  text="Очистить", command=Reset).grid(row=0, column=1)
        self.btnPayment = Button(RightFrame2e, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), width=4,  text="Выход", command=iExit).grid(row=0, column=2)















































if __name__ == "__main__":
    root = Tk()
    application = Payroll(root)
    root.mainloop()
