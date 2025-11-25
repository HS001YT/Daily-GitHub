#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */

string timeInWords(int h, int m) {
    vector<string> words(31);
    words[1] = "one";
    words[2] = "two";
    words[3] = "three";
    words[4] = "four";
    words[5] = "five";
    words[6] = "six";
    words[7] = "seven";
    words[8] = "eight";
    words[9] = "nine";
    words[10] = "ten";
    words[11] = "eleven";
    words[12] = "twelve";
    words[13] = "thirteen";
    words[14] = "fourteen";
    words[15] = "quarter";
    words[16] = "sixteen";
    words[17] = "seventeen";
    words[18] = "eighteen";
    words[19] = "nineteen";
    words[20] = "twenty";
    words[21] = "twenty one";
    words[22] = "twenty two";
    words[23] = "twenty three";
    words[24] = "twenty four";
    words[25] = "twenty five";
    words[26] = "twenty six";
    words[27] = "twenty seven";
    words[28] = "twenty eight";
    words[29] = "twenty nine";
    words[30] = "half";

    string result;

    if (m == 0) {
        result = words[h] + " o' clock";
    }
    else if (m == 15) {
        result = "quarter past " + words[h];
    }
    else if (m == 30) {
        result = "half past " + words[h];
    }
    else if (m == 45) {
        int nextHour = (h == 12) ? 1 : h + 1;
        result = "quarter to " + words[nextHour];
    }
    else if (m < 30) {
        string minuteWord = (m == 1) ? " minute" : " minutes";
        result = words[m] + minuteWord + " past " + words[h];
    }
    else {
        int rem = 60 - m;
        int nextHour = (h == 12) ? 1 : h + 1;
        string minuteWord = (rem == 1) ? " minute" : " minutes";
        result = words[rem] + minuteWord + " to " + words[nextHour];
    }

    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string h_temp;
    getline(cin, h_temp);

    int h = stoi(ltrim(rtrim(h_temp)));

    string m_temp;
    getline(cin, m_temp);

    int m = stoi(ltrim(rtrim(m_temp)));

    string result = timeInWords(h, m);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
