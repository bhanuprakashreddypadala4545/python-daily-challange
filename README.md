# python-daily-challange
# python-assignment-1
Problem Statement
The program asks for four things:
- Full Name
- Email ID
- Mobile Number
- Age
- 
  It checks each one based on certain rules. If everything’s good, you get “User Profile is VALID.” If not, you get “User Profile is INVALID.

   
Validation Rules
  
   - Full Name: Has to have at least two words. Can’t start or end with a space.
   - Email ID: Needs at least one @ and one . Can’t start with @.
  -  Mobile Number: Exactly 10 digits, only numbers, and shouldn’t start with 0.
  -  Age: Must be over 18 and no more than 60.


  
Algorithm
- Ask for your full name, email, mobile number, and age.
- Check the full name for the right number of spaces and no leading or trailing spaces.
- Check the email for @ and . and make sure it’s not starting with @.
- Check the mobile number for length, digits, and starting digit.
- Make sure the age is in the right range.
- Print out if the profile is valid or not.

 Code Snippets
 
<img width="1920" height="1080" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/8b3174c2-9a20-47dc-a81e-1285cc47df4f" />



# python-daily-challange
# python-assignment-2
The goal is to create a program that checks student details before approving their account. The program uses only:
strings
Conditional statements Problem Statement The program takes four inputs:
Student ID
Email ID
Password
Referral Code 
It checks if these inputs follow the university rules. If all are valid → it prints APPROVED If any rule fails → it prints REJECTED
Validation Rules Student ID

Format: CSE-XXX
Must start with "CSE"
4th character must be "-"
Last 3 characters must be digits
Example: CSE-245 → Valid, cse-245 → Invalid Email ID
Must contain @ and .
@ cannot be the first or last character
Must end with .edu
Example: student@univ.edu → Valid, student@gmail.com → Invalid Password
Must be at least 8 characters long
First character must be uppercase
Must contain at least one digit
Example: Aman1234 → Valid, amanabcd → Invalid Referral Code
Format: REF##@
Must start with "REF"
Next 2 characters must be digits
Last character must be @
Example: REF45@ → Valid, RE45@ → Invalid
 Code Snippets
 <img width="1920" height="1080" alt="Screenshot (44)" src="https://github.com/user-attachments/assets/8cdcfad5-cdb0-482a-ac10-4a9f95be38f1" />

# python-daily-challange
# python-assignment-3
## Code2Xplore – 60 Days Challenge (Day‑3)
  Goal
    The goal is to create a program that checks student marks and classifies them into grades, while also counting valid and failed students.
    Inputs
The program takes:
  - Number of subjects (m)
  - Marks of each subject<img width="1920" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/7caccdc0-e38f-47a6-bb03-e399563a5449" />

  - A fixed username ("bhanu")

Logic
  - If the username length is >5, each student’s mark is increased by 1.
  - If the username length is <=5 each student’s mark is decreased by 1.
Since "bhanu" has only 4 characters, all marks are reduced by 2.
  
Validation Rules (Grading)

  - 91–100 → Excellent
  - 76–89 → Very Good
  - 61–74 → Good
  - 41–59 → Average
  - 0–39 → Fail
  - Marks outside 0–100 → Invalid

Counters
  - valid → counts all students whose marks fall into valid ranges (0–100).
  - fail → counts students who fall into the Fail category.

Output
  - Prints each student’s adjusted mark with its grade.
  - Prints total valid students.
  - Prints total failed students.


    
# python-daily-challange
# python-assignment-4Problem
This program takes integer values (requests) from the user and categorizes them into different demand levels. It also removes some values based on a personalization rule using the length of a name.
Categories
Invalid Demand: Negative values
No Demand: Value equal to 0
Low Demand: 1 to 20
Moderate Demand: 21 to 50
High Demand: Above 50
How It Works
The program first takes the number of inputs and then reads all values. Each value is checked and placed into the correct category. Valid values are counted, and negative values are treated as invalid. Then, the length of a given name is calculated and a personalization value is found using length mod 3.
If result is 0, low demand values are removed
If result is 1, high demand values are removed
If result is 2, both low and high demand values are removed
Output
The program displays the name length, personalization value, total valid requests, number of removed requests, and the final categorized lists.



    
# python-daily-challange
# python-assignment-5
Demand Categorization System
Problem

This program takes integer values (requests) from the user and categorizes them into different demand levels. It also removes some values based on a personalization rule using the length of a name.

Categories

Invalid Demand: Negative values
No Demand: Value equal to 0
Low Demand: 1 to 20
Moderate Demand: 21 to 50
High Demand: Above 50

How It Works

The program first takes the number of inputs and then reads all values. Each value is checked and placed into the correct category. Valid values are counted, and negative values are treated as invalid. Then, the length of a given name is calculated and a personalization value is found using length mod 3. If result is 0, low demand values are removed. If result is 1, high demand values are removed. If result is 2, both low and high demand values are removed.

Output

The program displays the name length, personalization value, total valid requests, number of removed requests, and the final categorized lists.


# python-daily-challange
# python-assignment-5
Problem Overview
This program analyzes transaction amounts entered by the user.
It identifies risky spending patterns based on frequency and total amount.
Transactions are grouped into categories for better analysis.
Objective
Accept multiple transaction values
Classify transactions into categories
Detect spending patterns
Calculate total and frequency
Assign a final risk level
Provide a summary using a tuple
How the Program Works
The user enters the number of transactions and their values.
All values are stored in a list.
Using list comprehension, transactions are classified into:
invalid (≤ 0)
normal (1–500)
large (501–2000)
high risk (> 2000)
A separate list is created for valid transactions (greater than 0).
A loop is used to calculate total spending.
Conditions are used to detect:
frequent transactions
large spending
suspicious patterns
Risk Classification Logic
The program uses three factors:
number of valid transactions (freq)
total transaction value (total)
number of high-risk transactions
Decision Rules
High Risk

freq > 4 AND total > 3000
Moderate Risk

freq > 3 OR total > 2500 OR high-risk transactions ≥ 3
Low Risk

when none of the above conditions are satisfied
Output
Categorized transactions:
Invalid
Normal
Large
High Risk
Pattern detection:
Frequent Transactions
Large Spending
Suspicious Pattern
Total transaction value
Number of transactions
Final Risk Classification
Summary tuple:
(total transactions, valid transactions, total amount, risk)
My Approach / Logic Decisions
I separated classification and analysis to keep the code simple.
I considered only positive values as valid transactions.
I used both frequency and total amount to determine risk level.
I used list comprehension for cleaner classification.
Reflection
This program helped me understand how multiple conditions affect decision making.
Combining frequency and amount gives better results than using a single factor.
The logic can be extended for real-world fraud detection systems.
Concepts Used
Lists

Loops (for)

Conditional statements (if-elif)

List comprehension

Dictionary

Tuple








# python-daily-challange
# python-assignment-6
Transaction Risk Analysis Program
Problem Overview
This program analyzes transaction amounts entered by the user.
It identifies risky spending patterns based on frequency and total amount.
Transactions are grouped into categories for better analysis.
Objective
Accept multiple transaction values
Classify transactions into categories
Detect spending patterns
Calculate total and frequency
Assign a final risk level
Provide a summary using a tuple
How the Program Works
The user enters the number of transactions and their values.
All values are stored in a list.
Using list comprehension, transactions are classified into:
invalid (≤ 0)
normal (1–500)
large (501–2000)
high risk (> 2000)
A separate list is created for valid transactions (greater than 0).
A loop is used to calculate total spending.
Conditions are used to detect:
frequent transactions
large spending
suspicious patterns
Risk Classification Logic
The program uses three factors:
number of valid transactions (freq)
total transaction value (total)
number of high-risk transactions
Decision Rules
High Risk

freq > 4 AND total > 3000
Moderate Risk

freq > 3 OR total > 2500 OR high-risk transactions ≥ 3
Low Risk

when none of the above conditions are satisfied
Output
Categorized transactions:
Invalid
Normal
Large
High Risk
Pattern detection:
Frequent Transactions
Large Spending
Suspicious Pattern
Total transaction value
Number of transactions
Final Risk Classification
Summary tuple:
(total transactions, valid transactions, total amount, risk)
My Approach / Logic Decisions
I separated classification and analysis to keep the code simple.
I considered only positive values as valid transactions.
I used both frequency and total amount to determine risk level.
I used list comprehension for cleaner classification.
Reflection
This program helped me understand how multiple conditions affect decision making.
Combining frequency and amount gives better results than using a single factor.
The logic can be extended for real-world fraud detection systems.
Concepts Used
Lists

Loops (for)

Conditional statements (if-elif)

List comprehension

Dictionary

Tuple

Screenshot (23)



# python-daily-challange
# python-assignment-6
Problem Overview
This program analyzes student performance.
It uses marks, attendance, and assignment scores.
It classifies students into categories.
It gives overall class performance.
Objective
Generate student data using random values
Store data using list, tuple, and dictionary
Convert data into DataFrame using Pandas
Use NumPy for calculations
Classify students into categories
Detect patterns in data
Provide final system result
Return summary using a tuple
How the Program Works
The program generates n students based on roll number.
Each student has:
marks (0–100)
attendance (0–100)
assignment (0–50)
Data is stored in a list as tuples.
Data is converted into a DataFrame.
Classification is done using conditions.
Analysis is done using NumPy and manual calculation.
Student Classification Logic
At Risk
marks < 40 OR attendance < 50
Average
marks between 40 and 70
Good
marks between 71 and 90
Top Performer
marks > 90 AND attendance > 80
Analysis Performed
Mean (calculated manually)
Median (NumPy)
Standard Deviation (NumPy)
Correlation (Marks vs Attendance)
Normalization of marks
Pattern Detection
Consistency
standard deviation < 15
Attendance Risk
more than 3 students with attendance < 50
High Achievement
at least 2 top performers
Performance Index Formula
performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)

Output
DataFrame (table format)
Student category dictionary
Unique categories (set)
Statistical values:
mean
median
standard deviation
correlation
Final system insight:
Stable Academic System
Moderate Performance
Critical Attention Required
Summary tuple:
(mean, std_dev, max_marks)
Personalization Applied
Last digit of Register Number = 6
Hence, n = 6 students generated
My Approach / Logic Decisions
I used three functions:
generate_data()
classify_students()
analyze_data()
I used random values to simulate data.
I used conditions to classify students.
I calculated mean manually.
Concepts Used
Lists
Tuples
Dictionary
Set
Functions
List comprehension
NumPy
Pandas
Random module
Math module
Reflection
I learned how to use NumPy and Pandas.
I understood how to analyze data step by step.
I learned classification using conditions.
I learned manual calculation of mean.
Output Screenshot
Screenshot (54)
