//Dsa mini project

#include <iostream>
#include <stack>
#include <vector>      // Array like with mutable in nature
#include <string>
using namespace std;

class BrowserHistory {
private:
    stack<string> backStack;
    stack<string> forwardStack;
    vector<string> fullHistory;
    string current;

public:
    // Visit a new page
    void visit(const string& url) {
        if (!current.empty()) {
            backStack.push(current);
        }
        current = url;
        while (!forwardStack.empty()) {
            forwardStack.pop(); // clear forward history
        }
        fullHistory.push_back(current);
        cout << "Visited: " << current << endl;
    }

    // Go back
    void back() {
        if (backStack.empty()) {
            cout << "No previous page exist.\n";
            return;
        }
        forwardStack.push(current);
        current = backStack.top();
        backStack.pop();
        fullHistory.push_back(current);
        cout << "Moved Back to: " << current << endl;
    }

    // Go forward
    void forward() {
        if (forwardStack.empty()) {
            cout << "Go back to move forward.\n";
            return;
        }
        backStack.push(current);
        current = forwardStack.top();
        forwardStack.pop();
        fullHistory.push_back(current);
        cout << "Moved Forward to: " << current << endl;
    }

    // Show current page
    void showCurrent() {
        if (current.empty()) {
            cout << "No page opened yet.\n";
        } else {
            cout << "Current Page: " << current << endl;
        }
    }

    // Show complete reshaped history
    void showFullHistory() {
        if (fullHistory.empty()) {
            cout << "No history available.\n";
            return;
        }
        
        cout << "\nFull Search History (recent first):\n";
        for (int i = (int)fullHistory.size() - 1; i >= 0; i--) {
            cout << fullHistory[i] << endl;
        }
    }
};

int main() {
    BrowserHistory browser;
    int choice;
    string url;

    do {
        cout << "\n--- Browser Menu ---\n";
        cout << "1. Visit new page\n";
        cout << "2. Go Back\n";
        cout << "3. Go Forward\n";
        cout << "4. Show Current Page\n";
        cout << "5. Show Full Reshaped History\n";
        cout << "6. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter page name (e.g., Home1): ";
            cin >> url;
            browser.visit(url);
            break;
        case 2:
            browser.back();
            break;
        case 3:
            browser.forward();
            break;
        case 4:
            browser.showCurrent();
            break;
        case 5:
            browser.showFullHistory();
            break;
        case 6:
            cout << "Exiting Browser...\n";
            break;
        default:
            cout << "Invalid choice! Try again.\n";
        }
    } while (choice != 6);

    return 0;
}