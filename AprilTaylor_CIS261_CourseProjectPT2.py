#course code pt2

def GetEmpInfo():
    empname = input("Enter Employee Name: ")
    return empname

def GetTimeframe():
    firstday = input("Enter Start Date as mm\dd\yyyy: ")
    lastday = input("Enter Stop Date as mm\dd\yyyy: ")
    return firstday, lastday

def GetHoursWorked():
    hours = float(input("Enter Hours Worked: "))
    return hours

def GetHourlyRate():
    hourrate = float(input("Enter Hourly Rate: "))
    return hourrate

def GetTaxRate():
    taxrate = float(input("Enter Tax Rate as decimal: "))
    return taxrate

def CalcTaxNetPay(hours, hourrate, taxrate):
    grosspay = hours * hourrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpTotalData):
    TotEmp = 0
    TotHours = 0.00
    TotGp = 0.00
    TotTax = 0.00
    TotNp = 0.00
    for EmpData in EmpTotalDataList:
        firstday = EmpData[0]
        lastday = EmpData[1]
        empname = EmpData[2]
        hours = EmpData[3]
        hourrate = EmpData[4]
        taxrate = EmpData[5]
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourrate, taxrate)
        print(firstday,lastday, empname, f"{hours:,.2f}", f"${hourrate:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.1%}", f"${incometax:,.2f}", f"${netpay:,.2f}")
        TotEmp += 1
        TotHours += hours
        TotGp += grosspay
        TotTax += incometax
        TotNp += netpay
        EmpTotals["TotEmp"] = TotEmp
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGp"] = TotGp
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNp"] = TotNp

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Work: {EmpTotals["TotHours"]:,.2f}')
    print(f'Total Gross Pay: ${EmpTotals["TotGp"]:,.2f}')
    print(f'Total Income Tax: ${EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: ${EmpTotals["TotNp"]:,.2f}')

if __name__== "__main__":
    EmpTotalDataList = []
    EmpTotals = {}
    while True:
        empname = GetEmpInfo()
        if (empname.upper() == "END"):
            break
        firstday, lastday = GetTimeframe()
        hours = GetHoursWorked()
        hourrate = GetHourlyRate()
        taxrate = GetTaxRate()
        EmpData = [firstday, lastday, empname, hours, hourrate, taxrate]
        EmpTotalDataList.append(EmpData)

    printinfo(EmpTotalDataList)    
    PrintTotals(EmpTotals)

