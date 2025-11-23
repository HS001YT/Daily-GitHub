#ifndef INSTRUCTOR_H
#define INSTRUCTOR_H

#include "User.h"
#include <vector>

class Instructor : public User {
private:
    std::vector<std::string> coursesTaught;
    std::string department;
    std::string bio;

public:
    Instructor(const std::string& id, const std::string& name, 
               const std::string& email, const std::string& password,
               const std::string& department, const std::string& bio);
    
    // Course management
    void addCourse(const std::string& courseId);
    void removeCourse(const std::string& courseId);
    std::vector<std::string> getCoursesTaught() const;
    
    // Getters
    std::string getDepartment() const;
    std::string getBio() const;
    
    // Overridden virtual functions
    void displayProfile() const override;
    std::string getUserType() const override;
};

#endif