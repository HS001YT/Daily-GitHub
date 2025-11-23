#ifndef STUDENT_H
#define STUDENT_H

#include "User.h"
#include <map>
#include <vector>
#include <string>

class Student : public User {
private:
    std::vector<std::string> enrolledCourses;
    std::map<std::string, double> courseProgress; // courseId -> progress percentage
    std::map<std::string, std::map<std::string, double>> assessmentScores; // courseId -> (assessmentId -> score)
    std::vector<std::string> certificates;

public:
    Student(const std::string& id, const std::string& name, 
            const std::string& email, const std::string& password);
    
    // Course enrollment
    void enrollInCourse(const std::string& courseId);
    void unenrollFromCourse(const std::string& courseId);
    bool isEnrolled(const std::string& courseId) const;
    std::vector<std::string> getEnrolledCourses() const;
    
    // Progress tracking
    void updateProgress(const std::string& courseId, double progress);
    double getProgress(const std::string& courseId) const;
    
    // Assessment management
    void submitAssessment(const std::string& courseId, const std::string& assessmentId, double score);
    double getAssessmentScore(const std::string& courseId, const std::string& assessmentId) const;
    
    // Certification
    void addCertificate(const std::string& certificate);
    std::vector<std::string> getCertificates() const;
    void generateCertificate(const std::string& courseId, const std::string& courseTitle, double finalScore);  // ADD THIS LINE
    
    // Overridden virtual functions
    void displayProfile() const override;
    std::string getUserType() const override;
};

#endif