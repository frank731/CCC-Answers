#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int count;
    string temp;
    cin >> count;
    vector<string> print;
    for (int i = 0; i < count; i++) {
        cin >> temp;
        string topprint = "";
        char past = temp[0];
        int count = 0;
        for (char c: temp) {
            if (c != past) {
                topprint += to_string(count) + " " + past + " ";
                past = c;
                count = 1;
            }
            else {
                count += 1;
            }
        }
        topprint += to_string(count) + " " + past + " ";
        print.push_back(topprint);
    }
    for (string s : print) {
        cout << s << "\n";
    }
    
}