#course code pt2

def GetEmpInfo():
    EmpName = input("Enter Employee Name: ")
    return EmpName

def GetTimeframe():
    firstday = input("Enter Start Date mm\dd\yyyy: ")
    lastday = input("Enter End Date mm\dd\yyyy: ")
    return firstday, lastday

def GetHoursWorked():
    hours = float(input("Enter Hours Worked: "))
    return hours

def GetHourlyRate():
    hourrate = float(input("Enter Hourly Rate: "))
    return hourrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate


def CalcTaxNetPay(hours, hourrate, taxrate):
    grosspay = hours * hourrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpName, hours, hourrate, grosspay, taxrate, incometax, netpay ):
    print(EmpName, f"{hours:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.2%}", f"${incometax:,.2f}", f"${netpay:,.2f}")

def PrintTotals(TotEmp, TotHours, TotGp, TotTax, TotNp):
    print()
    print(f"Total Number of Employees: {TotEmp}")
    print(f"Total Hours Work: {TotHours:,.2f}")
    print(f"Total Gross Pay: ${TotGp:,.2f}")
    print(f"Total Income Tax: ${TotTax:,.2f}")
    print(f"Total Net Pay: ${TotNp:,.2f}")

if __name__== "__main__":
    TotEmp = 0
    TotHours = 0.00
    TotGp = 0.00
    TotTax = 0.00
    TotNp = 0.00
    while True:
        EmpName = GetEmpInfo()
        if (EmpName.upper() == "END"):
            break
        firstday, lastday = GetTimeframe ()
        hours = GetHoursWorked()
        hourrate = GetHourlyRate()
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourrate, taxrate)
        printinfo(EmpName, hours, hourrate, grosspay, taxrate, incometax, netpay)
        TotEmp += 1
        TotHours += hours
        TotGp += grosspay
        TotTax += incometax
        TotNp += netpay
        
    PrintTotals (TotEmp, TotHours, TotGp, TotTax, TotNp)

