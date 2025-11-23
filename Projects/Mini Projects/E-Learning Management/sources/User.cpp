#include "../headers/User.h"

User::User(const std::string& id, const std::string& name, 
           const std::string& email, const std::string& password)
    : userId(id), name(name), email(email), password(password) {}

std::string User::getUserId() const { return userId; }
std::string User::getName() const { return name; }
std::string User::getEmail() const { return email; }

bool User::authenticate(const std::string& inputPassword) const {
    return password == inputPassword;
}