def entries():
    num=int(input("Enter the number of students:"))
    
    for i in range(num):
        name=input("Enter the name of student:")
        marks=int(input(f"{name}'s Marks:"))
        my_dict[name]=marks
def show():
    print("Student Details:")
    for key in my_dict:
        print(f"Name:{key}, Marks:{my_dict[key]}")
    else:
        print("No more entries.")
my_dict={}
choice=int(input("Enter 1 to add entries, 2 to show details:"))
if choice==1:
    entries()
elif choice==2:
    show()
else:
    print("Invalid choice. Please enter 1 or 2.")