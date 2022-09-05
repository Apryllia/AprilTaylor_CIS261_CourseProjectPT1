def GetUserName():
    username = ("Enter User Name: ")
    return username

def GetUserPw():
    pwd = input("Enter Password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or user): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return
        else:
            userrole = input("Enter Role (Admin or User): ")

def printinfo():
    UserFile = open("userrole.txt","r")
    while True:
        UserDetails = UserFile.readline()
        if not UserDetails:
            break
        UserDetails = UserDetails.replace("\n","")
        UserList = UserDetails.split("|")
        username = UserList[0]
        userpwd = UserList[1]
        userrole = UserList[2]
        print("User Name:", username, "Password: ", userpwd, "Role: ", userrole)

if __name__=="__main__":
    UserFile = open("userrole.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPw()
        userrole = GetUserRole
        UserDetails = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetails)

    UserFile.close()
    printinfo()