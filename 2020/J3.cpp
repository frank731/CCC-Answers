#include <bits/stdc++.h>

using namespace std;

int main()
{
    int count;
    int x1 = 100;
    int y1 = 100;
    int x2 = 0;
    int y2 = 0;
    int tempx;
    int tempy;
    scanf("%d", &count);
    for (int i = 0; i < count; i++) {  
        scanf("%d,%d", &tempx, &tempy);
        if (tempx < x1) {
            x1 = tempx;
        }
        if(tempx > x2){
            x2 = tempx;
        }
        if (tempy < y1) {
            y1 = tempy;
        }
        if (tempy > y2) {
            y2 = tempy;
        }
    }
    printf("%d,%d\n", x1 - 1, y1 - 1);
    printf("%d,%d", x2 + 1, y2 + 1);
}
