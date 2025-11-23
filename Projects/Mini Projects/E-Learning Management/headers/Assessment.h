#ifndef ASSESSMENT_H
#define ASSESSMENT_H

#include <string>
#include <iostream>  // ADD THIS LINE

// Abstract base class for assessments
class Assessment {
protected:
    std::string assessmentId;
    std::string title;
    std::string courseId;
    double totalMarks;

public:
    Assessment(const std::string& id, const std::string& title, 
               const std::string& courseId, double totalMarks);
    virtual ~Assessment() = default;
    
    // Getters
    std::string getAssessmentId() const;
    std::string getTitle() const;
    std::string getCourseId() const;
    double getTotalMarks() const;
    
    // Pure virtual function for grading (Polymorphism)
    virtual double calculateGrade(double obtainedMarks) const = 0;
    virtual std::string getAssessmentType() const = 0;
    virtual void displayAssessmentInfo() const = 0;
    virtual bool takeAssessment() = 0;  // ADD THIS LINE
};

// Derived classes for different assessment types (Inheritance)
class Quiz : public Assessment {
private:
    int timeLimit; // in minutes
    int questionCount;

public:
    Quiz(const std::string& id, const std::string& title, 
         const std::string& courseId, double totalMarks,
         int timeLimit, int questionCount);
    
    double calculateGrade(double obtainedMarks) const override;
    std::string getAssessmentType() const override;
    void displayAssessmentInfo() const override;
    bool takeAssessment() override {
        std::cout << "📝 Taking Quiz: " << title << std::endl;
        std::cout << "Time Limit: " << timeLimit << " minutes" << std::endl;
        std::cout << "Questions: " << questionCount << std::endl;
        
        // Simulate quiz taking
        std::cout << "Quiz completed! Submitting answers..." << std::endl;
        return true;
    }
};

class Assignment : public Assessment {
private:
    std::string dueDate;
    std::string submissionFormat;

public:
    Assignment(const std::string& id, const std::string& title, 
               const std::string& courseId, double totalMarks,
               const std::string& dueDate, const std::string& submissionFormat);
    
    double calculateGrade(double obtainedMarks) const override;
    std::string getAssessmentType() const override;
    void displayAssessmentInfo() const override;
    bool takeAssessment() override {
        std::cout << "📄 Working on Assignment: " << title << std::endl;
        std::cout << "Due Date: " << dueDate << std::endl;
        std::cout << "Format: " << submissionFormat << std::endl;
        
        // Simulate assignment submission
        std::cout << "Assignment submitted successfully!" << std::endl;
        return true;
    }
};

class Exam : public Assessment {
private:
    std::string examDate;
    int duration; // in minutes

public:
    Exam(const std::string& id, const std::string& title, 
         const std::string& courseId, double totalMarks,
         const std::string& examDate, int duration);
    
    double calculateGrade(double obtainedMarks) const override;
    std::string getAssessmentType() const override;
    void displayAssessmentInfo() const override;
    bool takeAssessment() override {
        std::cout << "🏫 Taking Exam: " << title << std::endl;
        std::cout << "Exam Date: " << examDate << std::endl;
        std::cout << "Duration: " << duration << " minutes" << std::endl;
        
        // Simulate exam taking
        std::cout << "Exam completed! Answers submitted." << std::endl;
        return true;
    }
};

#endif