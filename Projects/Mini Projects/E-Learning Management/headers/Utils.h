#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <cstdlib>
#include <ctime>

class Utils {
public:
    static std::string generateId(const std::string& prefix) {
        int randomNum = std::rand() % 10000;
        return prefix + std::to_string(randomNum);
    }
    
    static void initializeRandom() {
        std::srand(std::time(0));
    }
};

#endif