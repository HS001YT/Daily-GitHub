#ifndef COURSE_H
#define COURSE_H

#include <string>
#include <vector>
#include <memory>

class Content;
class Assessment;

class Course {
private:
    std::string courseId;
    std::string title;
    std::string description;
    std::string instructorId;
    std::vector<std::shared_ptr<Content>> contents;
    std::vector<std::shared_ptr<Assessment>> assessments;
    double price;
    bool isPublished;

public:
    Course(const std::string& id, const std::string& title, 
           const std::string& desc, const std::string& instructorId, double price);
    
    // Getters
    std::string getCourseId() const;
    std::string getTitle() const;
    std::string getDescription() const;
    std::string getInstructorId() const;
    double getPrice() const;
    bool getIsPublished() const;
    
    // Content management
    void addContent(std::shared_ptr<Content> content);
    void removeContent(const std::string& contentId);
    std::vector<std::shared_ptr<Content>> getContents() const;
    
    // Assessment management
    void addAssessment(std::shared_ptr<Assessment> assessment);
    std::vector<std::shared_ptr<Assessment>> getAssessments() const;
    
    // Course status
    void publish();
    void unpublish();
    
    void displayCourseInfo() const;
};

#endif