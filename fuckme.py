import datetime

def calculate_age(year_of_birth):
    current_year = datetime.datetime.now().year
    return current_year - year_of_birth

def main():
    print("STUDENT AGE CALCULATOR")
    name = input("Enter student name: ")
    
    try:
        year_of_birth = int(input("Enter year of birth: "))
        age = calculate_age(year_of_birth)
        print(f"{name} is {age} years old.")
    except ValueError:
        print("Invalid year! Enter a valid number.")

if __name__ == "__main__":
    main()
