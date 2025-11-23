#include "../headers/Student.h"
#include <iostream>
#include <algorithm>
#include <fstream>
#include <ctime>
#include <string>

Student::Student(const std::string& id, const std::string& name, 
                 const std::string& email, const std::string& password)
    : User(id, name, email, password) {}

void Student::enrollInCourse(const std::string& courseId) {
    // Check if already enrolled
    if (!isEnrolled(courseId)) {
        enrolledCourses.push_back(courseId);
        courseProgress[courseId] = 0.0;
    }
}

void Student::unenrollFromCourse(const std::string& courseId) {
    // Remove from enrolled courses
    for (auto it = enrolledCourses.begin(); it != enrolledCourses.end(); ) {
        if (*it == courseId) {
            it = enrolledCourses.erase(it);
        } else {
            ++it;
        }
    }
    
    // Remove progress and assessment data
    courseProgress.erase(courseId);
    assessmentScores.erase(courseId);
}

bool Student::isEnrolled(const std::string& courseId) const {
    for (const auto& course : enrolledCourses) {
        if (course == courseId) {
            return true;
        }
    }
    return false;
}

std::vector<std::string> Student::getEnrolledCourses() const {
    return enrolledCourses;
}

void Student::updateProgress(const std::string& courseId, double progress) {
    if (progress >= 0.0 && progress <= 100.0) {
        courseProgress[courseId] = progress;    
    }
}

double Student::getProgress(const std::string& courseId) const {
    auto it = courseProgress.find(courseId);
    return it != courseProgress.end() ? it->second : 0.0;
}

void Student::submitAssessment(const std::string& courseId, const std::string& assessmentId, double score) {
    assessmentScores[courseId][assessmentId] = score;
}

double Student::getAssessmentScore(const std::string& courseId, const std::string& assessmentId) const {
    auto courseIt = assessmentScores.find(courseId);
    if (courseIt != assessmentScores.end()) {
        auto assessmentIt = courseIt->second.find(assessmentId);
        if (assessmentIt != courseIt->second.end()) {
            return assessmentIt->second;
        }
    }
    return 0.0;
}

void Student::generateCertificate(const std::string& courseId, const std::string& courseTitle, double finalScore) {
    std::string filename = "certificate_" + userId + "_" + courseId + ".txt";
    std::ofstream certFile(filename);
    
    if (certFile.is_open()) {
        certFile << "=============================================\n";
        certFile << "           CERTIFICATE OF COMPLETION         \n";
        certFile << "=============================================\n\n";
        certFile << "This certifies that\n\n";
        certFile << "         " << name << "\n\n";
        certFile << "has successfully completed the course\n\n";
        certFile << "         \"" << courseTitle << "\"\n\n";
        certFile << "with an overall score of: " << finalScore << "%\n\n";
        certFile << "Student ID: " << userId << "\n";
        certFile << "Email: " << email << "\n";
        certFile << "Course ID: " << courseId << "\n";
        
        // Get current date
        time_t now = time(0);
        char* dt = ctime(&now);
        certFile << "Date of Completion: " << dt;
        certFile << "\n=============================================\n";
        certFile << "         E-LEARNING MANAGEMENT SYSTEM        \n";
        certFile << "=============================================\n";
        
        certFile.close();
        
        // Add to certificates list - ONLY ONCE with proper format
        std::string certificate = "Certificate for: " + courseTitle;
        
        // Check if certificate already exists to avoid duplicates
        bool certificateExists = false;
        for (const auto& cert : certificates) {
            if (cert == certificate) {
                certificateExists = true;
                break;
            }
        }
        
        if (!certificateExists) {
            certificates.push_back(certificate);
            std::cout << "Certificate generated: " << filename << std::endl;
        } else {
            std::cout << "Certificate already exists for this course." << std::endl;
        }
    } else {
        std::cout << "Error: Could not create certificate file: " << filename << std::endl;
    }
}

void Student::addCertificate(const std::string& certificate) {
    certificates.push_back(certificate);
}

std::vector<std::string> Student::getCertificates() const {
    return certificates;
}

void Student::displayProfile() const {
    std::cout << "Student Profile:" << std::endl;
    std::cout << "ID: " << getUserId() << std::endl;
    std::cout << "Name: " << getName() << std::endl;
    std::cout << "Email: " << getEmail() << std::endl;
    std::cout << "Enrolled Courses: " << enrolledCourses.size() << std::endl;
    std::cout << "Certificates: " << certificates.size() << std::endl;
}

std::string Student::getUserType() const {
    return "Student";
}