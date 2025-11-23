====================================================================
          E-LEARNING MANAGEMENT SYSTEM - USER GUIDE
====================================================================

📋 TABLE OF CONTENTS:
1. How to Compile and Run
2. Pre-Installed Courses & Content
3. Pre-Installed User Accounts
4. Basic Usage Instructions
5. Certificate System
6. Features Overview

====================================================================
1. 🚀 HOW TO COMPILE AND RUN
====================================================================

WINDOWS:
1. Open Command Prompt in the project directory
2. Compile the program:
   g++ -std=c++11 -Iheaders main.cpp sources\*.cpp -o elearning_system.exe
3. Run the program:
   elearning_system.exe

LINUX/MAC:
1. Open Terminal in the project directory
2. Compile the program:
   g++ -std=c++11 -Iheaders main.cpp sources/*.cpp -o elearning_system
3. Run the program:
   ./elearning_system

====================================================================
2. 📚 PRE-INSTALLED COURSES & CONTENT
====================================================================

The system comes with 3 ready-to-use courses:

🎯 COURSE 1: C++ Programming Fundamentals
   • Price: $49.99
   • Status: Published ✅
   • Content:
     - Video: "Introduction to C++" (30 minutes)
     - Document: "C++ Syntax Guide" (45 minutes, 25 pages)
     - Quiz: "C++ Basics Quiz" (20 minutes, 10 questions)
   • Assessment:
     - Quiz: "C++ Fundamentals Quiz" (100 marks, 30 minutes, 15 questions)

🎯 COURSE 2: Web Development Bootcamp
   • Price: $79.99
   • Status: Published ✅
   • Content:
     - Video: "HTML Basics" (40 minutes)
     - Video: "CSS Styling" (50 minutes)
     - Document: "JavaScript Guide" (60 minutes, 35 pages)
   • Assessment:
     - Assignment: "Build a Portfolio Website" (100 marks)
       Due: 2024-12-31
       Format: ZIP file containing HTML, CSS, JS

🎯 COURSE 3: Data Structures and Algorithms
   • Price: $89.99
   • Status: Published ✅
   • Content:
     - Video: "Arrays and Linked Lists" (55 minutes)
     - Document: "Algorithm Complexity" (40 minutes, 20 pages)
   • Assessment:
     - Exam: "Midterm Exam" (100 marks, 120 minutes)
       Date: 2024-11-15

====================================================================
3. 👥 PRE-INSTALLED USER ACCOUNTS
====================================================================

🏫 INSTRUCTOR ACCOUNT:
• Name: Dr. Smith
• Email: smith@university.edu
• Password: pass123
• Department: Computer Science
• Bio: Senior Professor with 10+ years experience

🎓 STUDENT ACCOUNT (WITH COMPLETED COURSE):
• Name: John Doe
• Email: john@student.edu
• Password: student123
• Status: Already enrolled in C++ Programming Fundamentals (100% Complete)
• Certificate: Pre-generated certificate file available

====================================================================
4. 📝 BASIC USAGE INSTRUCTIONS
====================================================================

STEP 1 - STARTUP:
• Program automatically loads 3 sample courses
• Pre-created users are ready for immediate testing
• You'll see welcome message with login credentials

STEP 2 - CHOOSE YOUR ROLE:

OPTION A: Register as New Student
1. Select option 1 from main menu
2. Enter: Name, Email, Password (validated inputs)
3. System creates Student ID automatically

OPTION B: Register as New Instructor
1. Select option 2 from main menu
2. Enter: Name, Email, Password, Department, Bio
3. System creates Instructor ID automatically

OPTION C: Login with Pre-Installed Accounts
• Instructor: smith@university.edu / pass123
• Student: john@student.edu / student123

STEP 3 - USING THE SYSTEM:

AS A STUDENT:
1. View Available Courses - See all published courses with IDs
2. Enroll in Course - Use Course ID shown in the list
3. View My Courses - See enrolled courses with progress
4. View Progress - Check progress and assessment scores
5. View Certificates - See earned certificates
6. Continue Learning - Interactive course completion system

AS AN INSTRUCTOR:
1. Create Course - Add new courses (title, description, price)
2. View My Courses - See courses you've created
3. Add Content to Course - Add videos, documents, or quizzes
4. Add Assessment to Course - Add quizzes, assignments, or exams
5. Publish Course - Make course available for enrollment

====================================================================
5. 🏆 CERTIFICATE SYSTEM
====================================================================

AUTOMATIC CERTIFICATE GENERATION:
• Certificates are automatically generated when course progress reaches 100%
• Text file certificates are created in the project folder
• Certificate format: certificate_[StudentID]_[CourseID].txt
• Each certificate includes:
  - Student name and details
  - Course title and ID
  - Completion date and score
  - Professional certificate format

PRE-GENERATED CERTIFICATE:
• Student "John Doe" already has a certificate for C++ Programming
• File: certificate_STU[number]_CRS[number].txt
• This demonstrates the certificate system without needing to complete a course

====================================================================
6. ⭐ ENHANCED FEATURES
====================================================================

✅ CORE FEATURES:
• User Registration & Authentication with input validation
• Course Management System with publishing
• Content Management (Videos, Documents, Quizzes)
• Assessment System (Quizzes, Assignments, Exams)
• Student Enrollment & Progress Tracking
• Automatic Certificate Generation
• Interactive Learning System

✅ INPUT VALIDATION:
• Email format validation (must contain @ and .)
• Name validation (minimum 2 characters)
• Password validation (minimum 4 characters)
• Number range validation for prices, durations, marks
• Clear error messages with emoji indicators

✅ INTERACTIVE LEARNING:
• "Continue Learning" option for progressive course completion
• Step-by-step lesson completion
• Assessment taking with simulated scoring
• Real-time progress tracking
• Automatic certificate upon 100% completion

✅ OOP CONCEPTS IMPLEMENTED:
• ENCAPSULATION: Course and content data hiding
• INHERITANCE: Course types, assessment types, user roles
• POLYMORPHISM: Grading system, content display, lesson completion
• ABSTRACTION: Learning management system design

====================================================================
💡 QUICK START GUIDE FOR TESTING:
====================================================================

1. IMMEDIATE TESTING:
   • Login as: john@student.edu / student123
   • View certificates to see pre-generated certificate
   • Use "Continue Learning" to test interactive system

2. CREATE NEW STUDENT:
   • Register new student account
   • Enroll in any course using the displayed Course ID
   • Use "Continue Learning" to complete lessons and assessments
   • Watch progress increase and certificate generate at 100%

3. TEST INSTRUCTOR FEATURES:
   • Login as: smith@university.edu / pass123
   • Create new courses and add content
   • Publish courses for student enrollment

4. CERTIFICATE VERIFICATION:
   • Complete any course to 100% progress
   • Check project folder for .txt certificate files
   • Certificates contain professional formatting with student/course details

====================================================================
🛠 TROUBLESHOOTING:
====================================================================

• Certificate Files Empty: Ensure proper file permissions in project directory
• Login Failed: Verify exact email and password (case-sensitive)
• Course Not Found: Use exact Course ID as shown in menus
• Progress Not Updating: Complete both lessons and assessments for full progress

====================================================================
📞 SUPPORT:
====================================================================

For any issues:
1. Ensure all .h files are in "headers" directory
2. Ensure all .cpp files are in "sources" directory  
3. Compiler must support C++11 standard
4. Check console for specific error messages

Enjoy using the Enhanced E-Learning Management System!