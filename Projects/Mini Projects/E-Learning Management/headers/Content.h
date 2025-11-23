#ifndef CONTENT_H
#define CONTENT_H

#include <string>
#include <iostream>  // ADD THIS LINE

// Abstract base class for content (Abstraction)
class Content {
protected:
    std::string contentId;
    std::string title;
    std::string courseId;
    int duration; // in minutes

public:
    Content(const std::string& id, const std::string& title, 
            const std::string& courseId, int duration);
    virtual ~Content() = default;
    
    // Getters
    std::string getContentId() const;
    std::string getTitle() const;
    std::string getCourseId() const;
    int getDuration() const;
    
    // Pure virtual function - makes this class abstract
    virtual void displayContent() const = 0;
    virtual std::string getContentType() const = 0;
    virtual bool completeLesson() = 0;  // ADD THIS LINE
};

// Derived classes for different content types (Inheritance)
class VideoContent : public Content {
private:
    std::string videoUrl;
    std::string transcript;

public:
    VideoContent(const std::string& id, const std::string& title, 
                 const std::string& courseId, int duration,
                 const std::string& videoUrl, const std::string& transcript);
    
    void displayContent() const override;
    std::string getContentType() const override;
    bool completeLesson() override {
        std::cout << "✅ Completed Video: " << title << std::endl;
        return true;
    }
};

class DocumentContent : public Content {
private:
    std::string documentUrl;
    int pageCount;

public:
    DocumentContent(const std::string& id, const std::string& title, 
                    const std::string& courseId, int duration,
                    const std::string& documentUrl, int pageCount);
    
    void displayContent() const override;
    std::string getContentType() const override;
    bool completeLesson() override {
        std::cout << "✅ Completed Document: " << title << std::endl;
        return true;
    }
};

class QuizContent : public Content {
private:
    int questionCount;

public:
    QuizContent(const std::string& id, const std::string& title, 
                const std::string& courseId, int duration, int questionCount);
    
    void displayContent() const override;
    std::string getContentType() const override;
    bool completeLesson() override {
        std::cout << "✅ Completed Quiz: " << title << std::endl;
        return true;
    }
};

#endif