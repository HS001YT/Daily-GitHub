#ifndef USER_H
#define USER_H

#include <string>
#include <vector>

class User {
protected:
    std::string userId;
    std::string name;
    std::string email;
    std::string password;

public:
    User(const std::string& id, const std::string& name, 
         const std::string& email, const std::string& password);
    virtual ~User() = default;
    
    // Getters
    std::string getUserId() const;
    std::string getName() const;
    std::string getEmail() const;
    
    // Authentication
    bool authenticate(const std::string& inputPassword) const;
    
    // Virtual function for polymorphism
    virtual void displayProfile() const = 0;
    virtual std::string getUserType() const = 0;
};

#endif