
students = {}

def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add student")
    print("0. Exit")

def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks_input = input("Marks separated by spaces: ")
    try:
        marks = [float(m) for m in marks_input.split()]
        if not marks:
            print("Enter at least one mark.")
            return
        if any(m < 0 or m > 100 for m in marks):
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid marks. Enter numbers only.")
        return

    students[name] = marks
    print(f"Added {name}.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_student()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
