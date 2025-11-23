#include "../headers/Content.h"
#include <iostream>

// Base Content class
Content::Content(const std::string& id, const std::string& title, 
                 const std::string& courseId, int duration)
    : contentId(id), title(title), courseId(courseId), duration(duration) {}

std::string Content::getContentId() const { return contentId; }
std::string Content::getTitle() const { return title; }
std::string Content::getCourseId() const { return courseId; }
int Content::getDuration() const { return duration; }

// VideoContent implementation
VideoContent::VideoContent(const std::string& id, const std::string& title, 
                           const std::string& courseId, int duration,
                           const std::string& videoUrl, const std::string& transcript)
    : Content(id, title, courseId, duration), videoUrl(videoUrl), transcript(transcript) {}

void VideoContent::displayContent() const {
    std::cout << "Video: " << title << std::endl;
    std::cout << "Duration: " << duration << " minutes" << std::endl;
    std::cout << "URL: " << videoUrl << std::endl;
    std::cout << "Transcript: " << (transcript.empty() ? "Not available" : "Available") << std::endl;
}

std::string VideoContent::getContentType() const {
    return "Video";
}

// DocumentContent implementation
DocumentContent::DocumentContent(const std::string& id, const std::string& title, 
                                 const std::string& courseId, int duration,
                                 const std::string& documentUrl, int pageCount)
    : Content(id, title, courseId, duration), documentUrl(documentUrl), pageCount(pageCount) {}

void DocumentContent::displayContent() const {
    std::cout << "Document: " << title << std::endl;
    std::cout << "Duration: " << duration << " minutes" << std::endl;
    std::cout << "URL: " << documentUrl << std::endl;
    std::cout << "Pages: " << pageCount << std::endl;
}

std::string DocumentContent::getContentType() const {
    return "Document";
}

// QuizContent implementation
QuizContent::QuizContent(const std::string& id, const std::string& title, 
                         const std::string& courseId, int duration, int questionCount)
    : Content(id, title, courseId, duration), questionCount(questionCount) {}

void QuizContent::displayContent() const {
    std::cout << "Quiz: " << title << std::endl;
    std::cout << "Duration: " << duration << " minutes" << std::endl;
    std::cout << "Questions: " << questionCount << std::endl;
}

std::string QuizContent::getContentType() const {
    return "Quiz";
}