#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>   // IMPORTANT for stringstream
using namespace std;

int main() {
    string s;
    cin >> s;

    stringstream ss(s);
    int num;
    char comma;

    while (ss >> num) {
        cout << num << endl;
        ss >> comma;   // consume the comma
    }

    return 0;
}
