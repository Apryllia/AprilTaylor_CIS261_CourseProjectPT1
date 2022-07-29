def GetEmpInfo():
    EmpName = input("Enter Employee Name:")
    hours = int(input("Enter Number of Hours Worked:"))
    PayRate = float(input("Enter Hourly Pay Rate:"))
    return EmpName, hours, PayRate

def CalcWklyPay(hours, PayRate):
    return hours * PayRate

def IncomeTaxRate(WeeklyPay):
    ITR = 10
    if WeeklyPay >= 1000:
       ITR = 12
    elif WeeklyPay >= 2000:
       ITR = 22
    elif WeeklyPay < 1000:
        ITR = 10
    return ITR

if __name__== "__main__":
    #main()
    EmpName, hours, PayRate = GetEmpInfo()
    print(EmpName)
    print(hours)
    print("$" + format(PayRate, ",.2f"))
    WKP = CalcWklyPay(hours, PayRate)
    print("$" + format(WKP, ",.2f"))
    print("$" + format(IncomeTaxRate(WKP)))

def IncomeTaxRate(WeeklyPay):
    ITR = 10
    if WeeklyPay >= 1000:
       ITR = 12
    elif WeeklyPay >= 2000:
       ITR = 22
    elif WeeklyPay < 1000:
        ITR = 10
    return ITR

