class emp:
    def __init__(self):
        pass;

    def create(self, ch1):
        self.uid = int(input("Enter ID :"));
        self.name = input("Enter name :");
        self.age = int(input("Enter age :"));
        self.salary = int(input("Enter salary :"));
        if (ch1 == 1):
            self.desig = "Clerk";
        elif (ch1 == 2):
            self.desig = "Programmer";
        elif (ch1 == 3):
            self.desig = "Developer";
        elif (ch1 == 4):
            self.desig = "Manager";
        else:
            self.desig = "Invalid input";

    def display(self):
        print("ID :", self.uid);
        print("Name :", self.name);
        print("Age :", self.age);
        print("Salary :", self.salary);
        print("Desig :", self.desig);

    def raisesal(self):
        print("ID :", self.uid);
        print("Name :", self.name);
        print("Age :", self.age);
        print("Salary :", self.salary + 20000);
        print("Desig :", self.desig);


ch = 0;
e = emp();
while (ch != 5):
    ch = int(input("MENU:\n 1.Create\n 2.Display\n 3.RaiseSalary\n 4.Exit\n"));
    if (ch == 1):
        ch1 = int(input("MENU\n 1.clerk\n 2.programmer\n 3.developer\n 4.manager\n 5.exit\n"));
        e.create(ch1);
    elif (ch == 2):
        e.display();
    elif (ch == 3):
        e.raisesal();
    elif (ch == 4):
        break;
    else:
        print("Invalid Input");