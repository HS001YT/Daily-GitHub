#ifndef LMS_H
#define LMS_H

#include "Course.h"
#include "Student.h"
#include "Instructor.h"
#include <vector>
#include <memory>
#include <map>
#include <string>
#include <cstdlib>
#include <ctime>

class LMS {
private:
    std::vector<std::shared_ptr<Course>> courses;
    std::vector<std::shared_ptr<Student>> students;
    std::vector<std::shared_ptr<Instructor>> instructors;
    std::shared_ptr<User> currentUser;
    
    // Helper methods
    std::string generateId(const std::string& prefix);

public:
    LMS();
    
    // User management
    void registerStudent(const std::string& name, const std::string& email, 
                        const std::string& password);
    void registerInstructor(const std::string& name, const std::string& email, 
                           const std::string& password, const std::string& department, 
                           const std::string& bio);
    bool login(const std::string& email, const std::string& password);
    void logout();
    bool isLoggedIn() const;
    std::string getCurrentUserType() const;
    
    // Course management
    void createCourse(const std::string& title, const std::string& description, 
                     double price);
    std::vector<std::shared_ptr<Course>> getAvailableCourses() const;
    std::vector<std::shared_ptr<Course>> getInstructorCourses() const;
    
    // Enrollment
    void enrollStudentInCourse(const std::string& courseId);
    
    // Content management
    void addContentToCourse(const std::string& courseId, 
                           std::shared_ptr<Content> content);
    
    // Assessment management
    void addAssessmentToCourse(const std::string& courseId, 
                              std::shared_ptr<Assessment> assessment);
    
    // Progress tracking
    void updateStudentProgress(const std::string& courseId, double progress);
    
    // Getters
    std::shared_ptr<Student> getCurrentStudent() const;
    std::shared_ptr<Instructor> getCurrentInstructor() const;
    std::shared_ptr<Course> getCourseById(const std::string& courseId) const;
    
    // Frontend helper methods
    void displayMainMenu() const;
    void displayStudentDashboard() const;
    void displayInstructorDashboard() const;
};

#endif