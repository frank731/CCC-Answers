#include <bits/stdc++.h>

using namespace std;

int main()
{
    int p;
    int n;
    int r;
    int day = 0;
    scanf("%d %d %d", &p, &n, &r);
    int add = n;
    while (n <= p) {
        add *= r;
        n += add;
        day++;
    }
    printf("%d", day);
    
}
