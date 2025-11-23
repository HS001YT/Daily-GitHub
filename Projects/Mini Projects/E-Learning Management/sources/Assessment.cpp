#include "../headers/Assessment.h"
#include <iostream>

// Base Assessment class
Assessment::Assessment(const std::string& id, const std::string& title, 
                       const std::string& courseId, double totalMarks)
    : assessmentId(id), title(title), courseId(courseId), totalMarks(totalMarks) {}

std::string Assessment::getAssessmentId() const { return assessmentId; }
std::string Assessment::getTitle() const { return title; }
std::string Assessment::getCourseId() const { return courseId; }
double Assessment::getTotalMarks() const { return totalMarks; }

// Quiz implementation
Quiz::Quiz(const std::string& id, const std::string& title, 
           const std::string& courseId, double totalMarks,
           int timeLimit, int questionCount)
    : Assessment(id, title, courseId, totalMarks), 
      timeLimit(timeLimit), questionCount(questionCount) {}

double Quiz::calculateGrade(double obtainedMarks) const {
    return (obtainedMarks / totalMarks) * 100;
}

std::string Quiz::getAssessmentType() const {
    return "Quiz";
}

void Quiz::displayAssessmentInfo() const {
    std::cout << "Quiz: " << title << std::endl;
    std::cout << "Total Marks: " << totalMarks << std::endl;
    std::cout << "Time Limit: " << timeLimit << " minutes" << std::endl;
    std::cout << "Questions: " << questionCount << std::endl;
}

// Assignment implementation
Assignment::Assignment(const std::string& id, const std::string& title, 
                       const std::string& courseId, double totalMarks,
                       const std::string& dueDate, const std::string& submissionFormat)
    : Assessment(id, title, courseId, totalMarks), 
      dueDate(dueDate), submissionFormat(submissionFormat) {}

double Assignment::calculateGrade(double obtainedMarks) const {
    return (obtainedMarks / totalMarks) * 100;
}

std::string Assignment::getAssessmentType() const {
    return "Assignment";
}

void Assignment::displayAssessmentInfo() const {
    std::cout << "Assignment: " << title << std::endl;
    std::cout << "Total Marks: " << totalMarks << std::endl;
    std::cout << "Due Date: " << dueDate << std::endl;
    std::cout << "Submission Format: " << submissionFormat << std::endl;
}

// Exam implementation
Exam::Exam(const std::string& id, const std::string& title, 
           const std::string& courseId, double totalMarks,
           const std::string& examDate, int duration)
    : Assessment(id, title, courseId, totalMarks), 
      examDate(examDate), duration(duration) {}

double Exam::calculateGrade(double obtainedMarks) const {
    return (obtainedMarks / totalMarks) * 100;
}

std::string Exam::getAssessmentType() const {
    return "Exam";
}

void Exam::displayAssessmentInfo() const {
    std::cout << "Exam: " << title << std::endl;
    std::cout << "Total Marks: " << totalMarks << std::endl;
    std::cout << "Exam Date: " << examDate << std::endl;
    std::cout << "Duration: " << duration << " minutes" << std::endl;
}