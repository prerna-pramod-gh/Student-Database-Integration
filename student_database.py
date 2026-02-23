def main():
    # ==========================================
    # 1. Unique IDs (Sets)
    # ==========================================
    # Creating a set to store unique Roll Numbers
    enrolled_roll_nos = {101, 102, 103}
    
    print(f"Initial Enrolled Roll Numbers: {enrolled_roll_nos}")
    
    # Demonstrating how sets automatically discard duplicate entries
    print("\n--- Demonstrating Set Uniqueness ---")
    enrolled_roll_nos.add(101) # Attempting to add a duplicate
    print("Attempting to add duplicate Roll No 101...")
    print(f"Current Roll Numbers: {enrolled_roll_nos} (No change observed)")

    # ==========================================
    # 2. Nested Records (Dictionary)
    # ==========================================
    # Mapping Roll Numbers to a dictionary containing 'name' and 'marks' list
    student_database = {
        101: {'name': 'Mohan', 'marks': [80, 90, 85]},
        102: {'name': 'Sohan', 'marks': [30, 35, 40]},
        103: {'name': 'Rohan', 'marks': [50, 60, 55]}
    }

    # ==========================================
    # 3. Constants (Tuple)
    # ==========================================
    # Storing the passing threshold in a Tuple to ensure data immutability
    PASSING_THRESHOLD = (40,) 
    
    # We access the value using index 0 because it's a tuple
    passing_marks = PASSING_THRESHOLD[0]

    # ==========================================
    # 5. Management (Update & Append)
    # ==========================================
    print("\n--- Managing Records ---")
    
    # Using .update() to add new records (Roll No 104)
    new_roll_no = 104
    enrolled_roll_nos.update([new_roll_no])
    student_database[new_roll_no] = {'name': 'New Student', 'marks': [70, 75]}
    print(f"Added new student Roll No {new_roll_no}.")

    # Using .append() to modify existing marks lists (Adding a mark for Mohan)
    student_database[101]['marks'].append(95)
    print(f"Updated marks for Mohan (101): {student_database[101]['marks']}")

    # ==========================================
    # 4. Processing (Logic)
    # ==========================================
    print("\n--- Student Result Processing ---")
    
    # Take a Roll Number as input
    try:
        user_input = input("Enter Roll Number to check result: ")
        roll_no = int(user_input)

        # Verify its existence using the Set
        if roll_no in enrolled_roll_nos:
            
            # If valid, retrieve marks from the Dictionary
            student_record = student_database[roll_no]
            name = student_record['name']
            marks_list = student_record['marks']
            
            # Calculate the average
            average = sum(marks_list) / len(marks_list)
            
            # Compare it against the passing tuple
            if average >= passing_marks:
                # Output format for passed student
                print(f"{name} passed with {int(average)} average marks.")
            else:
                # Output format for failed student
                print(f"{name} failed. Total average marks are {int(average)}.")
        else:
            print(f"Error: Roll Number {roll_no} does not exist in the database.")

    except ValueError:
        print("Invalid input! Please enter a numeric Roll Number.")

if __name__ == "__main__":
    main()
