#course code pt2

def GetEmpInfo():
    empname = input("Enter Employee Name: ")
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

#def printinfo(empname, hours, hourrate, grosspay, taxrate, incometax, netpay ):
#   print(empname, f"{hours:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.2%}", f"${incometax:,.2f}", f"${netpay:,.2f}")

def printinfo(EmpTotalData):
    TotEmp = 0
    TotHours = 0.00
    TotGp = 0.00
    TotTax = 0.00
    TotNp = 0.00
    for EmpTotals in EmpTotalDataList:
        firstday = EmpData[0]
        lastday = EmpData[1]
        empname = EmpData[2]
        hour = EmpData[3]
        hourrate = EmpData[4]
        taxrate = EmpData[5]
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourrate, taxrate)
        print(firstday,lastday, empname, f"{hours:,.2f}", f"${hourrate:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.1%}", f"${incometax:,.2f}", f"${netpay:,.2f}")
        TotEmp += 1
        TotHours += hours
        TotGp += grosspay
        TotTax += incometax
        TotNp += netpay



#def PrintTotals(TotEmp, TotHours, TotGp, TotTax, TotNp):
#    print()
    #print(f"Total Number of Employees: {TotEmp}")
    #print(f"Total Hours Work: {TotHours:,.2f}")
    #print(f"Total Gross Pay: ${TotGp:,.2f}")
    #print(f"Total Income Tax: ${TotTax:,.2f}")
    #print(f"Total Net Pay: ${TotNp:,.2f}")

if __name__== "__main__":
    #TotEmp = 0
    #TotHours = 0.00
    #TotGp = 0.00
    #TotTax = 0.00
    #TotNp = 0.00

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
#        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourrate, taxrate)
#        printinfo(empname, hours, hourrate, grosspay, taxrate, incometax, netpay)
#        TotEmp += 1
#        TotHours += hours
#        TotGp += grosspay
#        TotTax += incometax
#        TotNp += netpay
    printinfo(EmpTotalDataList)    
    PrintTotals(TotEmp, TotHours, TotGp, TotTax, TotNp)

