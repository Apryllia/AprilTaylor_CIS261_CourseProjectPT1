def GetEmpInfo():
    EmpName = input("Enter Employee Name:")
    hours = int(input("Enter Number of Hours Worked:"))
    PayRate = float(input("Enter Hourly Pay Rate:"))
    return EmpName, hours, PayRate

def CalcWklyPay(hours, PayRate):
    return hours * PayRate

if __name__== "__main__":
    #main()
    EmpName, hours, PayRate = GetEmpInfo()
    print(EmpName)
    print(hours)
    print(PayRate)
    print(CalcWklyPay(hours, PayRate))
