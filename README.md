# Student Database Integration (v2)
A Python project designed to manage and process student records using core data structures. This application emphasizes the importance of unique identifiers, data immutability, and nested data organization.

---------------------

## Objective
To build a robust student database system that:
- Ensures data integrity using Unique IDs.
- Organizes complex data using Nested Structures.
- Protects critical configuration using Immutable Constants.

 -----------------------------------
 
## Key Concepts & Implementation

This project utilizes specific Python data structures to solve distinct problems:

1. Unique IDs (Sets)
A set enrolled_roll_nos is used to store Roll Numbers.

Purpose: Sets automatically discard duplicate values, ensuring every student ID remains unique without manual checks.
Efficiency: Checking if an ID exists in a set is significantly faster than searching through a list.


2. Nested Records (Dictionary)
The main student_database maps Roll Numbers to student details.

Structure: Roll No (Key) → {'name': String, 'marks': List} (Value)
Flexibility: This allows storing diverse data types (names as strings, marks as lists) under a single unique identifier.

3. Constants (Tuple)
The passing threshold is stored in a tuple PASSING_THRESHOLD = (40,).

Immutability: Unlike lists, tuples cannot be modified after creation. This prevents accidental changes to the passing criteria during program execution.


-------------------

## Features
Duplicate Handling: Automatically prevents duplicate Roll Number entries.

Record Management:
.update(): Adds new sets of Roll Numbers efficiently.
.append(): Adds new marks to existing student records.

Result Processing: Calculates averages and determines pass/fail status based on immutable constants.

--------------------

## Usage
Clone the repository or download the script.
Run the Python file:
python student_database.py
Enter a Roll Number when prompted to verify the student and view their results.

--------------------------------

## Example Output


Initial Enrolled Roll Numbers: {101, 102, 103}


--- Demonstrating Set Uniqueness ---

Attempting to add duplicate Roll No 101...

Current Roll Numbers: {101, 102, 103} (No change observed)



--- Managing Records ---

Added new student Roll No 104.

Updated marks for Mohan (101): [80, 90, 85, 95]



--- Student Result Processing ---

Enter Roll Number to check result: 101

Mohan passed with 87 average marks.


-------------------------------------

## Logic Flow
Input: User enters a Roll Number.
Verification: The program checks if the Roll Number exists in the Set.
Retrieval: If valid, the program retrieves the name and marks list from the Dictionary.
Calculation: The average of the marks is calculated.
Comparison: The average is compared against the Tuple threshold.
Output: The program prints the formatted result.

-------------------------------------

## Contact

If you have any questions or would like to discuss commercial licensing, feel free to reach out:

LinkedIn: https://www.linkedin.com/in/prerna-pramod-671667301/
