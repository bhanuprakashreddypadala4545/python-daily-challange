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



