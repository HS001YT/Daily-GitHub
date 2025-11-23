#include "../headers/Instructor.h"
#include <iostream>
#include <algorithm>

Instructor::Instructor(const std::string& id, const std::string& name, 
                       const std::string& email, const std::string& password,
                       const std::string& department, const std::string& bio)
    : User(id, name, email, password), department(department), bio(bio) {}

void Instructor::addCourse(const std::string& courseId) {
    // Check if course already exists
    bool courseExists = false;
    for (const auto& course : coursesTaught) {
        if (course == courseId) {
            courseExists = true;
            break;
        }
    }
    
    if (!courseExists) {
        coursesTaught.push_back(courseId);
    }
}

void Instructor::removeCourse(const std::string& courseId) {
    for (auto it = coursesTaught.begin(); it != coursesTaught.end(); ) {
        if (*it == courseId) {
            it = coursesTaught.erase(it);
        } else {
            ++it;
        }
    }
}

std::vector<std::string> Instructor::getCoursesTaught() const {
    return coursesTaught;
}

std::string Instructor::getDepartment() const { return department; }
std::string Instructor::getBio() const { return bio; }

void Instructor::displayProfile() const {
    std::cout << "Instructor Profile:" << std::endl;
    std::cout << "ID: " << getUserId() << std::endl;
    std::cout << "Name: " << getName() << std::endl;
    std::cout << "Email: " << getEmail() << std::endl;
    std::cout << "Department: " << department << std::endl;
    std::cout << "Bio: " << bio << std::endl;
    std::cout << "Courses Taught: " << coursesTaught.size() << std::endl;
}

std::string Instructor::getUserType() const {
    return "Instructor";
}