from astropy.cosmology import parameter
from tabulate import tabulate

anaylisis = []
personal = []
dean = []
ap = []
mentor = []
mentees = []
ge = []
me = []
head_ge = ["EYMP ID", "NAME", "POST ASSIGNED"]
head_me = [["EYMP ID", "NAME", "POST ASSIGNED"]]
currentexp = []
workinghistory = []
timeinfo = []
salaryinfo = []
holiday = []
head_pd = ["EYMP. ID", "NAME", "PH. NO.", "HOMETOWN", "CURRUNT CITY", "ADDRESS", "QUALIFICATION", "Gender"]
head_wh = ["EYMP. ID", "NAME", "WORK EXP", "PREVIOUS COMPANY NAME", "TIME PERIOD", "POST IN THAT COMPANY ",
           "YEAR YOU LEFT THAT COMPANY"]
head_cd = ["EYMP. ID", "NAME", "POST ASSINGENED", "NET PACAKAGE GIVEN", " IN HAND SALARY", "PAYMENT MODE",
           "TIME PERIOD OF CONTRACT", " HOLIDAYS ASSIGNED"]
x = int(input('''WELCOME TO CSE MANGMENT SYSTEM 🙏🙏

                 ENTER SECURITY KEY: '''))
if x == 1234568:
     def add():

            l = []


            global int
            global input
            global ppp
            ppp = []
            global pp
            pp = []
            A = "ID" + "[" + str(len(personal)) + "]"
            l.append(A)

            y = input('  ENTER  PERSONAL DETAILS \n'
                      '                                   \n'
                      '    ENTER FIRST NAME ::      ')


            y = y.upper()
            z = input("    ENTER LAST NAME  ::     ")
            z = z.upper()
            z_l = input("    ENTER D.O.B  ::     ")
            l.append(z_l)
            s = y + " " + z
            l.append(s)
            z = int(input("    ENTER PH. NO.  ::     "))
            l.append(z)
            g = input("    ENTER HOMETOWN  ::     ")
            l.append(g)
            C = input("    ENTER CURRUNT CITY  ::     ")
            l.append(C)
            j = input("    ENTER COMPLETE ADDRESS  ::     ")
            l.append(j)
            xx = input("    ENTER QUALIFICATION  ::     ")
            l.append(xx)
            o = input("    ENTER  Gender  ::     ")
            o = o.upper()
            l.append((o))
            if o == "MALE":
                A1 = "ID" + "[" + str(len(personal)) + "]"
                pp.append(A1)
                pp.append(s)
            if o == "FEMALE":
                A2 = "ID" + "[" + str(len(personal)) + "]"
                ppp.append(A2)
                ppp.append(s)
            personal.append(l)
            kk = input('''  ENTER  WORKING HISTORY  DETAILS 

     ENTER  NAME ::      ''')
        
            kk = kk.upper()
            i = []
            i.append(A)
            i.append(kk)
            y = input("     WITH EXP. OR NOT")
            y = y.upper()
            i.append(y)
            if y == "WITH EXP":
                QW = input("      PREVIOUS COMPANY NAME   ")
                i.append(QW)
                YU = input("      TIME PERIOD  ")
                i.append(YU)
                io = input("      POST IN THAT COMPANY  ")
                i.append(io)
                r = input("      YEAR YOU LEFT THAT COMPANY   ")
                i.append(r)
                workinghistory.append(i)
            if y == "NOT":
                QW = "NONE"
                i.append(QW)
                YU = "NONE"
                i.append(YU)
                io = "NONE"
                i.append(io)
                r = "NONE"
                i.append(r)
                workinghistory.append(i)

            k3 = input('''  ENTER  CONTRACT DETAILS  DETAILS 

     ENTER  NAME ::      ''')

            O = []
            O.append(A)
            k3 = k3.upper()
            O.append(k3)
            N = input("    POST ASSINGENED")
            O.append(N)

            if o == "FEMALE":
                ppp.append(N)
            if o == "MALE":
                pp.append(N)
            ge.append(ppp)
            me.append(pp)

            K = input("    NET PACAKAGE GIVEN")
            O.append(K)
            U = input("    IN HAND SALARY")
            O.append(U)

            R = input("    PAYMENT MODE")
            O.append(R)
            P = input("    TIME PERIOD OF CONTRACT")
            O.append(P)
            '''
            L = input = ("    HOLIDAYS ASSIGNED")
            O.append(L)
            '''
            timeinfo.append(O)
     # def update():

     def retrive() :
            t = input(''' ENTER WHAT YOU WANT GET INFO OF EMPLOYEES TO  
                                     1.PERSONAL DETAILS 
                                     2.WORKING DETAILS
                                     3.CONTRACT DETAILS
                                     4.GENDER WISE
                                        ''')
            t = t.upper()
            if (t == "PERSONAL DETAILS"):
                a = input("Whole list or particular employee")

                if a == "whole list":
                    print(tabulate(personal, headers=head_pd, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = personal[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_pd, tablefmt="grid"))
                    print()
                    print()
            if (t == "WORKING HISTORY"):
                a = input("Whole list or particular employee")
                if a == "whole list":
                    print(tabulate(workinghistory, headers=head_wh, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = workinghistory[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_wh, tablefmt="grid"))
                    print()
                    print()

            if (t == "CONTRACT DETAILS"):

                a = input("Whole list or particular employee")
                if a == "whole list":
                    print(tabulate(timeinfo, headers=head_cd, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = timeinfo[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_pd, tablefmt="grid"))
                    print()
                    print()
            if (t == "GENDER WISE"):
                XXXC = input("ENTER MALE OR FEMALE LIST ")
                XXXC = XXXC.upper()
                if XXXC == "MALE":
                    a = input("Whole list or particular employee")
                    if a == "whole list":
                        print(tabulate(me, headers=head_me, tablefmt="grid"))
                    elif a == "particular employee":
                        n = int(input("ENTER ID NO"))
                        poo = me[n]
                        aa = [poo]
                        print(tabulate(aa, headers=head_me, tablefmt="grid"))
                        print()
                        print()
                if (XXXC == "FEMALE"):
                    a = input("Whole list or particular employee")
                    if a == "whole list":
                        print(tabulate(ge, headers=head_ge, tablefmt="grid"))
                    elif a == "particular employee":
                        n = int(input("ENTER ID NO"))
                        poo = ge[n]
                        aa = [poo]
                        print(tabulate(aa, headers=head_ge, tablefmt="grid"))
                        print()
                        print()

            

     while True:
          print('''ENTER WHAT YOU WANT TO DO
                         1.ADD 
                         2.GET_INFO
                         3.DELETE
                         4.UPDATE
                         5.HOLIDAY STATUS
                             ''')
          t22=""
          t22=input()
          n1 = t22.lower()
          if (n1 == "add"):
              add()
        # if (n=="delete"):
        # delete()
          #if (n1 == "get_info"):

           #   retrive()