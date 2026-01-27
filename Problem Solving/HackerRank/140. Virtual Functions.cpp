#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
public:
    string name;
    int age;

    virtual void getdata() = 0;
    virtual void putdata() = 0;
};

class Professor : public Person {
public:
    int publications;
    int cur_id;
    static int id;

    Professor() {
        cur_id = ++id;
    }

    void getdata() {
        cin >> name >> age >> publications;
    }

    void putdata() {
        cout << name << " " << age << " " << publications << " " << cur_id << endl;
    }
};

int Professor::id = 0;

class Student : public Person {
public:
    int marks[6];
    int cur_id;
    static int id;

    Student() {
        cur_id = ++id;
    }

    void getdata() {
        cin >> name >> age;
        for (int i = 0; i < 6; i++) {
            cin >> marks[i];
        }
    }

    void putdata() {
        int sum = 0;
        for (int i = 0; i < 6; i++) {
            sum += marks[i];
        }
        cout << name << " " << age << " " << sum << " " << cur_id << endl;
    }
};

int Student::id = 0;

int main() {
    int n;
    cin >> n;

    Person *per[n];

    for (int i = 0; i < n; i++) {
        int type;
        cin >> type;

        if (type == 1)
            per[i] = new Professor;
        else
            per[i] = new Student;

        per[i]->getdata();
    }

    for (int i = 0; i < n; i++) {
        per[i]->putdata();
    }

    return 0;
}