#include <bits/stdc++.h>
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;



int main()
{
    int s;
    int m;
    int l;
    scanf("%d %d %d", &s, &m, &l);
    if (s + m * 2 + l * 3 >= 10) {
        printf("happy");
    }
    else {
        printf("sad");
    }
    
}
