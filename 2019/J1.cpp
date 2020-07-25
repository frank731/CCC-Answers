#include <bits/stdc++.h>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int main()
{
    int apples[3];
    int bananas[3];
    int ascore;
    int bscore;
    scanf("%d %d %d %d %d %d", &apples[0], &apples[1], &apples[2], &bananas[0], &bananas[1], &bananas[2]);
    ascore = apples[0] * 3 + apples[1] * 2 + apples[2];
    bscore = bananas[0] * 3 + bananas[1] * 2 + bananas[2];
    if (ascore > bscore) {
        printf("A");
    }
    else if (bscore > ascore) {
        printf("B");
    }
    else {
        printf("T");
    }
}
