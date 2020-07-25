#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int count;
    int temp1;
    char temp2;
    cin >> count;
    vector<string> print;
    for (int i = 0; i < count; i++) {
        scanf("%d %c", &temp1, &temp2);
        string topprint = "";
        for (int o = 0; o < temp1; o++) {
            topprint += temp2;
        }
        print.push_back(topprint);
    }
    for (string s : print) {
        cout << s << "\n";
    }
    
}