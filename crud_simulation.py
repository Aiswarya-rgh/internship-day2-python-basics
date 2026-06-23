students=[]
while True:
    print("\n Student Menu")
    print("1.Add Students")
    print("2.View Students")
    print("3.Update Students")
    print("4.Delete Students")
    print("5.Exit")

    choice=input("Enter your choice")
    if choice=="1":
        name=input("Enter Student Name:")
        students.append(name)
        print("student added successfully!")
    elif choice=="2":
        print("students:",students)
    elif choice=="3":
        old_name=input("enter the name to update:")
        if old_name in students:
            new_name =input("enter new name:") 
            index=students.index(old_name)
            students[index]=new_name
            print("updated successfully!")
        else:
            print("student not found")          
    elif choice=="4":
        name=input("enter the name to delete:")
        if name in students:
            students.remove(name)
            print("student deleted successfully!")
        else:
            print("student not found")
    elif choice=="5":
        print("byee") 
        break
    else:
        print("Invalid Choice!")   