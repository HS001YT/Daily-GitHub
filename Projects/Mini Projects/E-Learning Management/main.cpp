#include "headers/LMS.h"
#include "headers/Content.h"
#include "headers/Assessment.h"
#include <iostream>
#include <memory>
#include <limits>
#include <cstdlib>
#include <ctime>

// ==================== INPUT VALIDATION FUNCTIONS ====================

// Helper function for ID generation in main.cpp
std::string generateId(const std::string& prefix) {
    int randomNum = std::rand() % 10000;
    return prefix + std::to_string(randomNum);
}

bool isValidEmail(const std::string& email) {
    return email.find('@') != std::string::npos && 
           email.find('.') != std::string::npos;
}

bool isValidName(const std::string& name) {
    return !name.empty() && name.length() >= 2;
}

bool isValidPassword(const std::string& password) {
    return password.length() >= 4;
}

double getValidatedDouble(const std::string& prompt, double min = 0.0, double max = 10000.0) {
    double value;
    while (true) {
        std::cout << prompt;
        std::cin >> value;
        if (std::cin.fail() || value < min || value > max) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input! Please enter a number between " << min << " and " << max << ": ";
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return value;
        }
    }
}

int getValidatedInt(const std::string& prompt, int min = 0, int max = 10000) {
    int value;
    while (true) {
        std::cout << prompt;
        std::cin >> value;
        if (std::cin.fail() || value < min || value > max) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input! Please enter a number between " << min << " and " << max << ": ";
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return value;
        }
    }
}

std::string getValidatedString(const std::string& prompt, bool allowEmpty = false) {
    std::string input;
    while (true) {
        std::cout << prompt;
        std::getline(std::cin, input);
        
        if (!allowEmpty && input.empty()) {
            std::cout << "This field cannot be empty. Please enter a value: ";
        } else {
            return input;
        }
    }
}

std::string getValidatedEmail(const std::string& prompt) {
    std::string email;
    while (true) {
        email = getValidatedString(prompt);
        if (isValidEmail(email)) {
            return email;
        } else {
            std::cout << "Invalid email format! Please enter a valid email (example@domain.com): ";
        }
    }
}

std::string getValidatedName(const std::string& prompt) {
    std::string name;
    while (true) {
        name = getValidatedString(prompt);
        if (isValidName(name)) {
            return name;
        } else {
            std::cout << "Name must be at least 2 characters long. Please try again: ";
        }
    }
}

std::string getValidatedPassword(const std::string& prompt) {
    std::string password;
    while (true) {
        password = getValidatedString(prompt);
        if (isValidPassword(password)) {
            return password;
        } else {
            std::cout << "Password must be at least 4 characters long. Please try again: ";
        }
    }
}

void clearInputBuffer() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

// ==================== PRELOAD SAMPLE DATA ====================

void preloadSampleData(LMS& lms) {
    std::cout << "Loading sample courses and content..." << std::endl;
    
    // Create sample instructor
    lms.registerInstructor("Dr. Smith", "smith@university.edu", "pass123", "Computer Science", "Senior Professor with 10+ years experience");
    
    // Create sample student with completed course
    lms.registerStudent("John Doe", "john@student.edu", "student123");
    
    // Login as instructor to create courses
    if (lms.login("smith@university.edu", "pass123")) {
        
        // Course 1: C++ Programming
        lms.createCourse("C++ Programming Fundamentals", 
                        "Learn the basics of C++ programming language from scratch", 
                        49.99);
        
        // Course 2: Web Development
        lms.createCourse("Web Development Bootcamp", 
                        "Full-stack web development with HTML, CSS, JavaScript", 
                        79.99);
        
        // Course 3: Data Structures
        lms.createCourse("Data Structures and Algorithms", 
                        "Master fundamental data structures and algorithm design", 
                        89.99);
        
        // Get the created courses and add content to them
        auto courses = lms.getInstructorCourses();
        
        if (courses.size() >= 3) {
            // Course 1: C++ Programming
            auto cppCourse = courses[0];
            
            // Add content to C++ course
            lms.addContentToCourse(cppCourse->getCourseId(), 
                std::make_shared<VideoContent>(generateId("CNT"), "Introduction to C++", cppCourse->getCourseId(), 30, 
                                              "https://example.com/cpp-intro", "Welcome to C++ programming course"));
            
            lms.addContentToCourse(cppCourse->getCourseId(), 
                std::make_shared<DocumentContent>(generateId("CNT"), "C++ Syntax Guide", cppCourse->getCourseId(), 45, 
                                                 "https://example.com/cpp-syntax.pdf", 25));
            
            lms.addContentToCourse(cppCourse->getCourseId(), 
                std::make_shared<QuizContent>(generateId("CNT"), "C++ Basics Quiz", cppCourse->getCourseId(), 20, 10));
            
            // Add assessments to C++ course
            lms.addAssessmentToCourse(cppCourse->getCourseId(),
                std::make_shared<Quiz>(generateId("ASS"), "C++ Fundamentals Quiz", cppCourse->getCourseId(), 100, 30, 15));
            
            // Publish the course
            cppCourse->publish();
            
            // Course 2: Web Development
            auto webCourse = courses[1];
            
            // Add content to Web Development course
            lms.addContentToCourse(webCourse->getCourseId(), 
                std::make_shared<VideoContent>(generateId("CNT"), "HTML Basics", webCourse->getCourseId(), 40, 
                                              "https://example.com/html-basics", "Learn HTML structure and tags"));
            
            lms.addContentToCourse(webCourse->getCourseId(), 
                std::make_shared<VideoContent>(generateId("CNT"), "CSS Styling", webCourse->getCourseId(), 50, 
                                              "https://example.com/css-styling", "Master CSS for beautiful websites"));
            
            lms.addContentToCourse(webCourse->getCourseId(), 
                std::make_shared<DocumentContent>(generateId("CNT"), "JavaScript Guide", webCourse->getCourseId(), 60, 
                                                 "https://example.com/js-guide.pdf", 35));
            
            // Add assessments
            lms.addAssessmentToCourse(webCourse->getCourseId(),
                std::make_shared<Assignment>(generateId("ASS"), "Build a Portfolio Website", webCourse->getCourseId(), 100, 
                                            "2024-12-31", "ZIP file containing HTML, CSS, JS"));
            
            // Publish the course
            webCourse->publish();
            
            // Course 3: Data Structures
            auto dsCourse = courses[2];
            
            // Add content to Data Structures course
            lms.addContentToCourse(dsCourse->getCourseId(), 
                std::make_shared<VideoContent>(generateId("CNT"), "Arrays and Linked Lists", dsCourse->getCourseId(), 55, 
                                              "https://example.com/arrays-lists", "Understanding linear data structures"));
            
            lms.addContentToCourse(dsCourse->getCourseId(), 
                std::make_shared<DocumentContent>(generateId("CNT"), "Algorithm Complexity", dsCourse->getCourseId(), 40, 
                                                 "https://example.com/big-o.pdf", 20));
            
            // Add assessments
            lms.addAssessmentToCourse(dsCourse->getCourseId(),
                std::make_shared<Exam>(generateId("ASS"), "Midterm Exam", dsCourse->getCourseId(), 100, "2024-11-15", 120));
            
            // Publish the course
            dsCourse->publish();
            
            std::cout << "Sample data loaded successfully!" << std::endl;
            std::cout << "Available courses:" << std::endl;
            std::cout << "   • " << cppCourse->getTitle() << " ($" << cppCourse->getPrice() << ")" << std::endl;
            std::cout << "   • " << webCourse->getTitle() << " ($" << webCourse->getPrice() << ")" << std::endl;
            std::cout << "   • " << dsCourse->getTitle() << " ($" << dsCourse->getPrice() << ")" << std::endl;
        }
        
        lms.logout();
        
        // Login as student and complete a course
        if (lms.login("john@student.edu", "student123")) {
            auto student = lms.getCurrentStudent();
            
            // Enroll and complete C++ course
            auto availableCourses = lms.getAvailableCourses();
            if (!availableCourses.empty()) {
                student->enrollInCourse(availableCourses[0]->getCourseId());
                student->updateProgress(availableCourses[0]->getCourseId(), 100.0);
                student->submitAssessment(availableCourses[0]->getCourseId(), "ASS0", 85.0); // Sample quiz score
                
                // Generate certificate
                student->generateCertificate(availableCourses[0]->getCourseId(), 
                                           availableCourses[0]->getTitle(), 85.0);
                std::cout << "Pre-created student 'John Doe' has completed C++ course with certificate!" << std::endl;
            }
            lms.logout();
        }
    } else {
        std::cout << "Failed to load sample data: Could not login as sample instructor" << std::endl;
    }
}

// ==================== STUDENT MENU ====================

void studentMenu(LMS& lms) {
    auto student = lms.getCurrentStudent();
    int choice;
    
    do {
        lms.displayStudentDashboard();
        std::cin >> choice;
        clearInputBuffer();
        
        switch (choice) {
            case 1: {
                // View Available Courses
                auto courses = lms.getAvailableCourses();
                std::cout << "\nAvailable Courses:" << std::endl;
                if (courses.empty()) {
                    std::cout << "No courses available." << std::endl;
                } else {
                    for (size_t i = 0; i < courses.size(); i++) {
                        std::cout << i + 1 << ". ";
                        courses[i]->displayCourseInfo();
                        std::cout << std::endl;
                    }
                }
                break;
            }
            case 2: {
                // Enroll in Course
                auto courses = lms.getAvailableCourses();
                if (courses.empty()) {
                    std::cout << "No courses available for enrollment." << std::endl;
                    break;
                }
                
                std::cout << "\nAvailable Courses:" << std::endl;
                for (size_t i = 0; i < courses.size(); i++) {
                    std::cout << i + 1 << ". " << courses[i]->getTitle() 
                              << " (ID: " << courses[i]->getCourseId() << ")" << std::endl;
                }
                
                std::string courseId = getValidatedString("Enter Course ID to enroll: ");
                lms.enrollStudentInCourse(courseId);
                break;
            }
            case 3: {
                // View My Courses
                auto enrolledCourses = student->getEnrolledCourses();
                std::cout << "\nMy Enrolled Courses:" << std::endl;
                if (enrolledCourses.empty()) {
                    std::cout << "You are not enrolled in any courses." << std::endl;
                } else {
                    for (size_t i = 0; i < enrolledCourses.size(); i++) {
                        auto course = lms.getCourseById(enrolledCourses[i]);
                        if (course) {
                            std::cout << i + 1 << ". ";
                            course->displayCourseInfo();
                            std::cout << "Progress: " << student->getProgress(enrolledCourses[i]) << "%" << std::endl;
                            std::cout << std::endl;
                        }
                    }
                }
                break;
            }
            case 4: {
                // View Progress
                auto enrolledCourses = student->getEnrolledCourses();
                std::cout << "\nCourse Progress:" << std::endl;
                if (enrolledCourses.empty()) {
                    std::cout << "You are not enrolled in any courses." << std::endl;
                } else {
                    for (const auto& courseId : enrolledCourses) {
                        auto course = lms.getCourseById(courseId);
                        if (course) {
                            std::cout << "Course: " << course->getTitle() << std::endl;
                            std::cout << "Progress: " << student->getProgress(courseId) << "%" << std::endl;
                            
                            // Show assessment scores
                            auto assessments = course->getAssessments();
                            if (!assessments.empty()) {
                                std::cout << "Assessment Scores:" << std::endl;
                                for (const auto& assessment : assessments) {
                                    double score = student->getAssessmentScore(courseId, assessment->getAssessmentId());
                                    std::cout << assessment->getTitle() << ": " << score << "/" 
                                              << assessment->getTotalMarks() << std::endl;
                                }
                            }
                            std::cout << std::endl;
                        }
                    }
                }
                break;
            }
            case 5: {
                // View Certificates
                auto certificates = student->getCertificates();
                std::cout << "\nMy Certificates:" << std::endl;
                if (certificates.empty()) {
                    std::cout << "No certificates earned yet." << std::endl;
                } else {
                    for (size_t i = 0; i < certificates.size(); i++) {
                        std::cout << i + 1 << ". " << certificates[i] << std::endl;
                    }
                }
                break;
            }
            case 6: {
                // Continue Learning - INTERACTIVE COURSE COMPLETION SYSTEM
                auto enrolledCourses = student->getEnrolledCourses();
                if (enrolledCourses.empty()) {
                    std::cout << "You are not enrolled in any courses." << std::endl;
                    break;
                }
                
                std::cout << "\n🎓 Continue Learning - Your Courses:" << std::endl;
                for (size_t i = 0; i < enrolledCourses.size(); i++) {
                    auto course = lms.getCourseById(enrolledCourses[i]);
                    if (course) {
                        double progress = student->getProgress(enrolledCourses[i]);
                        std::cout << i + 1 << ". " << course->getTitle() 
                                  << " [" << progress << "% Complete]" << std::endl;
                    }
                }
                
                std::string courseId = getValidatedString("Enter Course ID to continue: ");
                
                if (!student->isEnrolled(courseId)) {
                    std::cout << "You are not enrolled in this course!" << std::endl;
                    break;
                }
                
                auto course = lms.getCourseById(courseId);
                if (!course) {
                    std::cout << "Course not found!" << std::endl;
                    break;
                }
                
                // Interactive learning session
                bool continueLearning = true;
                while (continueLearning && student->getProgress(courseId) < 100.0) {
                    std::cout << "\nCourse: " << course->getTitle() << std::endl;
                    std::cout << "Current Progress: " << student->getProgress(courseId) << "%" << std::endl;
                    std::cout << "\nWhat would you like to do?\n";
                    std::cout << "1. Continue with Lessons\n";
                    std::cout << "2. Take Assessments\n";
                    std::cout << "3. Check Progress\n";
                    std::cout << "4. Return to Main Menu\n";
                    
                    int learningChoice = getValidatedInt("Choose option: ", 1, 4);
                    
                    switch (learningChoice) {
                        case 1: {
                            // Continue with Lessons
                            auto contents = course->getContents();
                            if (contents.empty()) {
                                std::cout << "No lessons available in this course." << std::endl;
                                break;
                            }
                            
                            std::cout << "\nAvailable Lessons:" << std::endl;
                            for (size_t i = 0; i < contents.size(); i++) {
                                std::cout << i + 1 << ". " << contents[i]->getTitle() 
                                          << " [" << contents[i]->getContentType() << "]" << std::endl;
                            }
                            
                            int lessonChoice = getValidatedInt("Choose lesson to complete (0 to cancel): ", 0, contents.size());
                            if (lessonChoice > 0) {
                                contents[lessonChoice - 1]->completeLesson();
                                std::cout << "Marked as completed!" << std::endl;
                                
                                // Update progress (each lesson contributes to progress)
                                double currentProgress = student->getProgress(courseId);
                                double progressPerLesson = 100.0 / (contents.size() + course->getAssessments().size());
                                double newProgress = currentProgress + progressPerLesson;
                                if (newProgress > 100.0) newProgress = 100.0;
                                student->updateProgress(courseId, newProgress);
                            }
                            break;
                        }
                        case 2: {
                            // Take Assessments
                            auto assessments = course->getAssessments();
                            if (assessments.empty()) {
                                std::cout << "No assessments available in this course." << std::endl;
                                break;
                            }
                            
                            std::cout << "\nAvailable Assessments:" << std::endl;
                            for (size_t i = 0; i < assessments.size(); i++) {
                                std::cout << i + 1 << ". " << assessments[i]->getTitle() 
                                          << " [" << assessments[i]->getAssessmentType() << "]" << std::endl;
                            }
                            
                            int assessmentChoice = getValidatedInt("Choose assessment to take (0 to cancel): ", 0, assessments.size());
                            if (assessmentChoice > 0) {
                                assessments[assessmentChoice - 1]->takeAssessment();
                                
                                // Simulate score (in real system, this would be based on actual performance)
                                double score = 70.0 + (std::rand() % 30); // Random score between 70-100
                                student->submitAssessment(courseId, assessments[assessmentChoice - 1]->getAssessmentId(), score);
                                std::cout << "Score: " << score << "/" << assessments[assessmentChoice - 1]->getTotalMarks() << std::endl;
                                
                                // Update progress
                                double currentProgress = student->getProgress(courseId);
                                double progressPerAssessment = 100.0 / (course->getContents().size() + assessments.size());
                                double newProgress = currentProgress + progressPerAssessment;
                                if (newProgress > 100.0) newProgress = 100.0;
                                student->updateProgress(courseId, newProgress);
                            }
                            break;
                        }
                        case 3: {
                            // Check Progress
                            std::cout << "\nCurrent Progress: " << student->getProgress(courseId) << "%" << std::endl;
                            if (student->getProgress(courseId) >= 100.0) {
                                std::cout << "Congratulations! You've completed the course!" << std::endl;
                                
                                // Generate certificate
                                double finalScore = 85.0; // Calculate based on actual scores in real system
                                student->generateCertificate(courseId, course->getTitle(), finalScore);
                                continueLearning = false;
                            }
                            break;
                        }
                        case 4: {
                            // Return to Main Menu
                            continueLearning = false;
                            break;
                        }
                    }
                    
                    // Check if course is completed
                    if (student->getProgress(courseId) >= 100.0) {
                        std::cout << "\nCOURSE COMPLETED! " << std::endl;
                        std::cout << "Congratulations! You've successfully completed: " << course->getTitle() << std::endl;
                        
                        // Generate final certificate
                        double finalScore = 85.0; // Calculate based on actual scores
                        student->generateCertificate(courseId, course->getTitle(), finalScore);
                        break;
                    }
                }
                break;
            }
            case 7:
                lms.logout();
                std::cout << "Logged out successfully!" << std::endl;
                break;
            default:
                std::cout << "Invalid choice! Please try again." << std::endl;
        }
    } while (choice != 7 && lms.isLoggedIn());
}

// ==================== INSTRUCTOR MENU ====================

void instructorMenu(LMS& lms) {
    auto instructor = lms.getCurrentInstructor();
    int choice;
    
    do {
        lms.displayInstructorDashboard();
        std::cin >> choice;
        clearInputBuffer();
        
        switch (choice) {
            case 1: {
                // Create Course
                std::string title = getValidatedString("Enter course title: ");
                std::string description = getValidatedString("Enter course description: ");
                double price = getValidatedDouble("Enter course price: $", 0.0, 1000.0);
                
                lms.createCourse(title, description, price);
                break;
            }
            case 2: {
                // View My Courses
                auto courses = lms.getInstructorCourses();
                std::cout << "\nMy Courses:" << std::endl;
                if (courses.empty()) {
                    std::cout << "You haven't created any courses yet." << std::endl;
                } else {
                    for (size_t i = 0; i < courses.size(); i++) {
                        std::cout << i + 1 << ". ";
                        courses[i]->displayCourseInfo();
                        std::cout << std::endl;
                    }
                }
                break;
            }
            case 3: {
                // Add Content to Course
                auto courses = lms.getInstructorCourses();
                if (courses.empty()) {
                    std::cout << "No courses available. Please create a course first." << std::endl;
                    break;
                }
                
                std::cout << "\nYour Courses:" << std::endl;
                for (size_t i = 0; i < courses.size(); i++) {
                    std::cout << i + 1 << ". " << courses[i]->getTitle() 
                              << " (ID: " << courses[i]->getCourseId() << ")" << std::endl;
                }
                
                std::string courseId = getValidatedString("Enter Course ID: ");
                
                std::cout << "Select content type:" << std::endl;
                std::cout << "1. Video" << std::endl;
                std::cout << "2. Document" << std::endl;
                std::cout << "3. Quiz" << std::endl;
                
                int contentChoice = getValidatedInt("Enter choice: ", 1, 3);
                
                std::string title = getValidatedString("Enter content title: ");
                int duration = getValidatedInt("Enter duration (minutes): ", 1, 480);
                
                std::shared_ptr<Content> content;
                
                switch (contentChoice) {
                    case 1: {
                        std::string videoUrl = getValidatedString("Enter video URL: ");
                        std::string transcript = getValidatedString("Enter transcript: ", true);
                        content = std::make_shared<VideoContent>(generateId("CNT"), title, courseId, duration, videoUrl, transcript);
                        break;
                    }
                    case 2: {
                        std::string documentUrl = getValidatedString("Enter document URL: ");
                        int pageCount = getValidatedInt("Enter page count: ", 1, 1000);
                        content = std::make_shared<DocumentContent>(generateId("CNT"), title, courseId, duration, documentUrl, pageCount);
                        break;
                    }
                    case 3: {
                        int questionCount = getValidatedInt("Enter number of questions: ", 1, 100);
                        content = std::make_shared<QuizContent>(generateId("CNT"), title, courseId, duration, questionCount);
                        break;
                    }
                }
                
                if (content) {
                    lms.addContentToCourse(courseId, content);
                }
                break;
            }
            case 4: {
                // Add Assessment to Course
                auto courses = lms.getInstructorCourses();
                if (courses.empty()) {
                    std::cout << "No courses available. Please create a course first." << std::endl;
                    break;
                }
                
                std::cout << "\nYour Courses:" << std::endl;
                for (size_t i = 0; i < courses.size(); i++) {
                    std::cout << i + 1 << ". " << courses[i]->getTitle() 
                              << " (ID: " << courses[i]->getCourseId() << ")" << std::endl;
                }
                
                std::string courseId = getValidatedString("Enter Course ID: ");
                
                std::cout << "Select assessment type:" << std::endl;
                std::cout << "1. Quiz" << std::endl;
                std::cout << "2. Assignment" << std::endl;
                std::cout << "3. Exam" << std::endl;
                
                int assessmentChoice = getValidatedInt("Enter choice: ", 1, 3);
                
                std::string title = getValidatedString("Enter assessment title: ");
                double totalMarks = getValidatedDouble("Enter total marks: ", 1, 1000);
                
                std::shared_ptr<Assessment> assessment;
                
                switch (assessmentChoice) {
                    case 1: {
                        int timeLimit = getValidatedInt("Enter time limit (minutes): ", 1, 480);
                        int questionCount = getValidatedInt("Enter number of questions: ", 1, 100);
                        assessment = std::make_shared<Quiz>(generateId("ASS"), title, courseId, totalMarks, timeLimit, questionCount);
                        break;
                    }
                    case 2: {
                        std::string dueDate = getValidatedString("Enter due date (YYYY-MM-DD): ");
                        std::string submissionFormat = getValidatedString("Enter submission format: ");
                        assessment = std::make_shared<Assignment>(generateId("ASS"), title, courseId, totalMarks, dueDate, submissionFormat);
                        break;
                    }
                    case 3: {
                        std::string examDate = getValidatedString("Enter exam date (YYYY-MM-DD): ");
                        int duration = getValidatedInt("Enter duration (minutes): ", 1, 480);
                        assessment = std::make_shared<Exam>(generateId("ASS"), title, courseId, totalMarks, examDate, duration);
                        break;
                    }
                }
                
                if (assessment) {
                    lms.addAssessmentToCourse(courseId, assessment);
                }
                break;
            }
            case 5: {
                // Publish Course
                auto courses = lms.getInstructorCourses();
                if (courses.empty()) {
                    std::cout << "No courses available." << std::endl;
                    break;
                }
                
                std::cout << "\nYour Courses:" << std::endl;
                for (size_t i = 0; i < courses.size(); i++) {
                    std::cout << i + 1 << ". " << courses[i]->getTitle() 
                              << " (ID: " << courses[i]->getCourseId() << ")" 
                              << " [" << (courses[i]->getIsPublished() ? "Published" : "Draft") << "]" << std::endl;
                }
                
                std::string courseId = getValidatedString("Enter Course ID to publish: ");
                
                auto course = lms.getCourseById(courseId);
                if (course && course->getInstructorId() == instructor->getUserId()) {
                    course->publish();
                    std::cout << "Course published successfully!" << std::endl;
                } else {
                    std::cout << "Course not found or you don't have permission!" << std::endl;
                }
                break;
            }
            case 6:
                lms.logout();
                std::cout << "Logged out successfully!" << std::endl;
                break;
            default:
                std::cout << "Invalid choice! Please try again." << std::endl;
        }
    } while (choice != 6 && lms.isLoggedIn());
}

// ==================== MAIN FUNCTION ====================

int main() {
    LMS lms;
    int choice;
    
    // Initialize random number generator
    std::srand(static_cast<unsigned int>(std::time(0)));
    
    // Preload sample courses and content
    preloadSampleData(lms);
    
    std::cout << "\nWelcome to E-Learning Management System!" << std::endl;
    std::cout << "Sample courses are pre-loaded. Students can enroll immediately!" << std::endl;
    std::cout << "Pre-created student: John Doe (john@student.edu / student123)" << std::endl;
    std::cout << "Pre-created instructor: Dr. Smith (smith@university.edu / pass123)" << std::endl;
    
    do {
        if (!lms.isLoggedIn()) {
            lms.displayMainMenu();
            
            // Get validated menu choice
            choice = getValidatedInt("", 1, 4);
            clearInputBuffer();
            
            switch (choice) {
                case 1: {
                    // Register Student
                    std::string name = getValidatedName("Enter name: ");
                    std::string email = getValidatedEmail("Enter email: ");
                    std::string password = getValidatedPassword("Enter password: ");
                    
                    lms.registerStudent(name, email, password);
                    break;
                }
                case 2: {
                    // Register Instructor
                    std::string name = getValidatedName("Enter name: ");
                    std::string email = getValidatedEmail("Enter email: ");
                    std::string password = getValidatedPassword("Enter password: ");
                    std::string department = getValidatedString("Enter department: ");
                    std::string bio = getValidatedString("Enter bio: ");
                    
                    lms.registerInstructor(name, email, password, department, bio);
                    break;
                }
                case 3: {
                    // Login
                    std::string email = getValidatedEmail("Enter email: ");
                    std::string password = getValidatedPassword("Enter password: ");
                    
                    if (lms.login(email, password)) {
                        std::string userType = lms.getCurrentUserType();
                        std::string userName;
                        
                        if (userType == "Student") {
                            auto student = lms.getCurrentStudent();
                            userName = student->getName();
                        } else if (userType == "Instructor") {
                            auto instructor = lms.getCurrentInstructor();
                            userName = instructor->getName();
                        }
                        
                        std::cout << "Login successful! Welcome, " << userName << " (" << userType << ")" << std::endl;
                    } else {
                        std::cout << "Login failed! Invalid email or password." << std::endl;
                    }
                    break;
                }
                case 4:
                    std::cout << "Thank you for using E-Learning Management System!" << std::endl;
                    break;
                default:
                    std::cout << "Invalid choice! Please try again." << std::endl;
            }
        } else {
            // User is logged in
            std::string userType = lms.getCurrentUserType();
            if (userType == "Student") {
                studentMenu(lms);
            } else if (userType == "Instructor") {
                instructorMenu(lms);
            }
        }
    } while (choice != 4 || lms.isLoggedIn());
    
    return 0;
}