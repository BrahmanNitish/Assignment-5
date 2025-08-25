def entries():
    num=int(input("Enter the number of students:"))
    
    for i in range(num):
        name=input("Enter the name of student:")
        marks=int(input(f"{name}'s Marks:"))
        my_dict[name]=marks
    show()
def show():
    std=input("Enter the name of student to show details or 'all' to show all details:")
    if std in my_dict:
        print(f"Name:{std}, Marks:{my_dict[std]}")
    elif std=="all":
        for name,marks in my_dict.items():
            print(f"Name:{name}, Marks:{marks}")
    else:
        print("Student not found.")
    x=input("Do you want to continue? (yes/no):")
    if x.lower()=="yes":
        entries()
    else:
        print("Exiting the program.")
my_dict={}
entries()
