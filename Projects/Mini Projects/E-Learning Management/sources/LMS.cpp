#include "../headers/LMS.h"
#include <iostream>
#include <algorithm>

LMS::LMS() : currentUser(nullptr) {
    // Seed random number generator for ID generation
    std::srand(static_cast<unsigned int>(std::time(0)));
}

std::string LMS::generateId(const std::string& prefix) {
    int randomNum = std::rand() % 10000;
    return prefix + std::to_string(randomNum);
}

void LMS::registerStudent(const std::string& name, const std::string& email, 
                         const std::string& password) {
    std::string studentId = generateId("STU");
    auto student = std::make_shared<Student>(studentId, name, email, password);
    students.push_back(student);
    std::cout << "Student registered successfully! ID: " << studentId << std::endl;
}

void LMS::registerInstructor(const std::string& name, const std::string& email, 
                            const std::string& password, const std::string& department, 
                            const std::string& bio) {
    std::string instructorId = generateId("INS");
    auto instructor = std::make_shared<Instructor>(instructorId, name, email, password, department, bio);
    instructors.push_back(instructor);
    std::cout << "Instructor registered successfully! ID: " << instructorId << std::endl;
}

bool LMS::login(const std::string& email, const std::string& password) {
    // Check students
    for (auto& student : students) {
        if (student->getEmail() == email && student->authenticate(password)) {
            currentUser = student;
            return true;
        }
    }
    
    // Check instructors
    for (auto& instructor : instructors) {
        if (instructor->getEmail() == email && instructor->authenticate(password)) {
            currentUser = instructor;
            return true;
        }
    }
    
    return false;
}

void LMS::logout() {
    currentUser = nullptr;
}

bool LMS::isLoggedIn() const {
    return currentUser != nullptr;
}

std::string LMS::getCurrentUserType() const {
    if (currentUser) {
        return currentUser->getUserType();
    }
    return "None";
}

void LMS::createCourse(const std::string& title, const std::string& description, double price) {
    if (getCurrentUserType() != "Instructor") {
        std::cout << "Only instructors can create courses!" << std::endl;
        return;
    }
    
    std::string courseId = generateId("CRS");
    auto instructor = getCurrentInstructor();
    auto course = std::make_shared<Course>(courseId, title, description, instructor->getUserId(), price);
    courses.push_back(course);
    instructor->addCourse(courseId);
    std::cout << "Course created successfully! ID: " << courseId << std::endl;
}

std::vector<std::shared_ptr<Course>> LMS::getAvailableCourses() const {
    std::vector<std::shared_ptr<Course>> availableCourses;
    for (auto& course : courses) {
        if (course->getIsPublished()) {
            availableCourses.push_back(course);
        }
    }
    return availableCourses;
}

std::vector<std::shared_ptr<Course>> LMS::getInstructorCourses() const {
    std::vector<std::shared_ptr<Course>> instructorCourses;
    if (getCurrentUserType() == "Instructor") {
        auto instructor = getCurrentInstructor();
        for (auto& course : courses) {
            if (course->getInstructorId() == instructor->getUserId()) {
                instructorCourses.push_back(course);
            }
        }
    }
    return instructorCourses;
}

void LMS::enrollStudentInCourse(const std::string& courseId) {
    if (getCurrentUserType() != "Student") {
        std::cout << "Only students can enroll in courses!" << std::endl;
        return;
    }
    
    auto course = getCourseById(courseId);
    if (!course) {
        std::cout << "Course not found!" << std::endl;
        return;
    }
    
    if (!course->getIsPublished()) {
        std::cout << "Course is not available for enrollment!" << std::endl;
        return;
    }
    
    auto student = getCurrentStudent();
    if (student->isEnrolled(courseId)) {
        std::cout << "Already enrolled in this course!" << std::endl;
        return;
    }
    
    student->enrollInCourse(courseId);
    std::cout << "Enrolled in course successfully!" << std::endl;
}

void LMS::addContentToCourse(const std::string& courseId, std::shared_ptr<Content> content) {
    if (getCurrentUserType() != "Instructor") {
        std::cout << "Only instructors can add content!" << std::endl;
        return;
    }
    
    auto course = getCourseById(courseId);
    if (!course) {
        std::cout << "Course not found!" << std::endl;
        return;
    }
    
    auto instructor = getCurrentInstructor();
    if (course->getInstructorId() != instructor->getUserId()) {
        std::cout << "You can only add content to your own courses!" << std::endl;
        return;
    }
    
    course->addContent(content);
    std::cout << "Content added successfully!" << std::endl;
}

void LMS::addAssessmentToCourse(const std::string& courseId, std::shared_ptr<Assessment> assessment) {
    if (getCurrentUserType() != "Instructor") {
        std::cout << "Only instructors can add assessments!" << std::endl;
        return;
    }
    
    auto course = getCourseById(courseId);
    if (!course) {
        std::cout << "Course not found!" << std::endl;
        return;
    }
    
    auto instructor = getCurrentInstructor();
    if (course->getInstructorId() != instructor->getUserId()) {
        std::cout << "You can only add assessments to your own courses!" << std::endl;
        return;
    }
    
    course->addAssessment(assessment);
    std::cout << "Assessment added successfully!" << std::endl;
}

void LMS::updateStudentProgress(const std::string& courseId, double progress) {
    if (getCurrentUserType() != "Student") {
        std::cout << "Only students can update progress!" << std::endl;
        return;
    }
    
    auto student = getCurrentStudent();
    if (!student->isEnrolled(courseId)) {
        std::cout << "Not enrolled in this course!" << std::endl;
        return;
    }
    
    student->updateProgress(courseId, progress);
    std::cout << "Progress updated successfully!" << std::endl;
}

std::shared_ptr<Student> LMS::getCurrentStudent() const {
    if (getCurrentUserType() == "Student") {
        return std::dynamic_pointer_cast<Student>(currentUser);
    }
    return nullptr;
}

std::shared_ptr<Instructor> LMS::getCurrentInstructor() const {
    if (getCurrentUserType() == "Instructor") {
        return std::dynamic_pointer_cast<Instructor>(currentUser);
    }
    return nullptr;
}

std::shared_ptr<Course> LMS::getCourseById(const std::string& courseId) const {
    for (auto& course : courses) {
        if (course->getCourseId() == courseId) {
            return course;
        }
    }
    return nullptr;
}

void LMS::displayMainMenu() const {
    std::cout << "\n=== E-Learning Management System ===" << std::endl;
    std::cout << "1. Register Student" << std::endl;
    std::cout << "2. Register Instructor" << std::endl;
    std::cout << "3. Login" << std::endl;
    std::cout << "4. Exit" << std::endl;
    std::cout << "Choose an option: ";
}

void LMS::displayStudentDashboard() const {
    std::cout << "\n=== Student Dashboard ===" << std::endl;
    std::cout << "1. View Available Courses" << std::endl;
    std::cout << "2. Enroll in Course" << std::endl;
    std::cout << "3. View My Courses" << std::endl;
    std::cout << "4. View Progress" << std::endl;
    std::cout << "5. View Certificates" << std::endl;
    std::cout << "6. Continue Learning" << std::endl;
    std::cout << "7. Logout" << std::endl;
    std::cout << "Choose an option: ";
}

void LMS::displayInstructorDashboard() const {
    std::cout << "\n=== Instructor Dashboard ===" << std::endl;
    std::cout << "1. Create Course" << std::endl;
    std::cout << "2. View My Courses" << std::endl;
    std::cout << "3. Add Content to Course" << std::endl;
    std::cout << "4. Add Assessment to Course" << std::endl;
    std::cout << "5. Publish Course" << std::endl;
    std::cout << "6. Logout" << std::endl;
    std::cout << "Choose an option: ";
}