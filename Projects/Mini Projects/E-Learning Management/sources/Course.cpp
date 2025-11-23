#include "../headers/Course.h"
#include "../headers/Content.h"
#include "../headers/Assessment.h"
#include <iostream>
#include <algorithm>

Course::Course(const std::string& id, const std::string& title, 
               const std::string& desc, const std::string& instructorId, double price)
    : courseId(id), title(title), description(desc), 
      instructorId(instructorId), price(price), isPublished(false) {}

std::string Course::getCourseId() const { return courseId; }
std::string Course::getTitle() const { return title; }
std::string Course::getDescription() const { return description; }
std::string Course::getInstructorId() const { return instructorId; }
double Course::getPrice() const { return price; }
bool Course::getIsPublished() const { return isPublished; }

void Course::addContent(std::shared_ptr<Content> content) {
    contents.push_back(content);
}

void Course::removeContent(const std::string& contentId) {
    for (auto it = contents.begin(); it != contents.end(); ) {
        if ((*it)->getContentId() == contentId) {
            it = contents.erase(it);
        } else {
            ++it;
        }
    }
}

std::vector<std::shared_ptr<Content>> Course::getContents() const {
    return contents;
}

void Course::addAssessment(std::shared_ptr<Assessment> assessment) {
    assessments.push_back(assessment);
}

std::vector<std::shared_ptr<Assessment>> Course::getAssessments() const {
    return assessments;
}

void Course::publish() {
    isPublished = true;
}

void Course::unpublish() {
    isPublished = false;
}

void Course::displayCourseInfo() const {
    std::cout << "Course ID: " << courseId << std::endl;
    std::cout << "Title: " << title << std::endl;
    std::cout << "Description: " << description << std::endl;
    std::cout << "Price: $" << price << std::endl;
    std::cout << "Status: " << (isPublished ? "Published" : "Draft") << std::endl;
    std::cout << "Contents: " << contents.size() << std::endl;
    std::cout << "Assessments: " << assessments.size() << std::endl;
}