#include <bits/stdc++.h>

using namespace std;

int main()
{
    string full;
    string key;
    int found;
    cin >> full;
    cin >> key;
    int length = key.length();
    for (int i = 0; i < length; i++) {
        found = full.find(key);
        if (found != string::npos) {
            printf("yes");
            break;
        }
        key.push_back(key.front());
        key.erase(0, 1);
    }
    if (found == -1) {
        printf("no");
    }
}
