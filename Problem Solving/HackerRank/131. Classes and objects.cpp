#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Student {
private:
    vector<int> scores;

public:
    void input() {
        scores.resize(5);
        for (int i = 0; i < 5; i++) {
            cin >> scores[i];
        }
    }

    int calculateTotalScore() {
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        return total;
    }
};

int main() {
    int n;
    cin >> n;

    vector<Student> students(n);

    for (int i = 0; i < n; i++) {
        students[i].input();
    }

    int kristenScore = students[0].calculateTotalScore();
    int count = 0;

    for (int i = 1; i < n; i++) {
        if (students[i].calculateTotalScore() > kristenScore) {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}
