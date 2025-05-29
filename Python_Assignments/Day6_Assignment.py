# 1. create  a class dept add deptid,deptname,loc of dept,head of the dept
# through the constructor initilaize the dept ,attributes,
#create a method to display the dept info
#display total depts in your organisation

#2. take input from user of no of depts. create a list or dict to store dept info
#Use forloop to get the dept info, u can add that into the list or dictionary
#search dept by deptid(ask user for search dept by deptid else dept is not available with us has to be displayed)
#add a func to search dept by deptname

#Question1
class Department:
    def _init_(self,deptid,deptname,deptloc,depthead):
        self.deptid=deptid
        self.deptname=deptname
        self.deptloc=deptloc
        self.depthead=depthead

    def deptinfo(self):
        print("Department information")
        print("-------------------------")
        print(f"Department ID: {self.deptid}")
        print(f'Department name: {self.deptname}')
        print(f'Department location: {self.deptloc}')
        print(f'Department head: {self.depthead}')

num_depts = int(input("Enter the number of departments: "))

#Question2:

class Department:
    l1 = []

    def _init_(self, deptid, deptname, deptloc, depthead):
        self.deptid = deptid
        self.deptname = deptname
        self.deptloc = deptloc
        self.depthead = depthead

    def display_deptinfo(self):
        print("Department information")
        print("-------------------------")
        print(f"Department ID: {self.deptid}")
        print(f'Department name: {self.deptname}')
        print(f'Department location: {self.deptloc}')
        print(f'Department head: {self.depthead}')


def user_input():
    flag = 1
    while flag:
        print('1. Add the department details\n2. Search department by department ID\n3. Search department by department name\n4. Exit')
        choice = int(input("Select your choice: "))
        
        if choice == 1:
            n = int(input("Enter no of departments: "))
            while n != 0:
                id = int(input("Enter department id: "))
                name = input("Enter department name: ")
                loc = input("Enter department location: ")
                hod = input("Enter department head: ")
                Department.l1.append((id, name, loc, hod))
                n -= 1
            for i in Department.l1:
                dept1 = Department(*i)
                dept1.display_deptinfo()

        elif choice == 2:
            id = int(input("Enter department ID: "))
            searchByID(id)

        elif choice == 3:
            name = input("Enter department name: ")
            searchByName(name)

        elif choice == 4:
            break

        else:
            print("Invalid choice. Try again.")


def searchByID(id):
    found = False
    for id1 in Department.l1:
        if id1[0] == id:
            print(f"Department name: {id1[1]}")
            print(f"Location: {id1[2]}")
            print(f"Head: {id1[3]}")
            found = True
            break
    if not found:
        print('Department does not exist')


def searchByName(name):
    found = False
    for id1 in Department.l1:
        if id1[1] == name:
            print(f"Department ID: {id1[0]}, Department name: {id1[1]}")
            print(f"Location: {id1[2]}, Head: {id1[3]}")
            found = True
            break
    if not found:
        print("Department does not exist")


user_input()