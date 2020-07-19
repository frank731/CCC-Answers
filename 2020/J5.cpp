#include <bits/stdc++.h>

using namespace std;

vector<pair<long, long>> factors(int num, long width, long length){
    vector<pair<long, long>> returned;
    pair<long, long> temp;
    int temp2;
    for (int i = 1; i < sqrt(num) + 1; i++) {
        if (num % i == 0) {
            temp2 = num / i;
            if (i <= width && temp2 <= length) {
                temp = make_pair(i, temp2);
                returned.push_back(temp);
            }
            if (temp2 <= width && i <= length) {
                temp = make_pair(temp2, i);
                returned.push_back(temp);
            }
        }
    }
    return returned;
}

int main()
{
    long width;
    long length;
    long temp;
    bool works = false;
    unordered_map<long, bool> visited;
    stack<pair<long, long>> q;
    q.push(make_pair(1, 1));
    cin >> width >> length;
    vector<vector<long>> graph(width, vector<long>(length, 0));
    for (int i = 0; i < width; i++) {
        for (int j = 0; j < length; j++) {
            scanf("%ld", &temp);         
            graph[i][j] = temp;
            visited[temp] = false;
        }
    }
    while (q.empty() == false)
    {
        pair<long, long>& coords = q.top();
        q.pop();
        long& num = graph[coords.first - 1][coords.second - 1];
        if (visited[num] == false) {
            visited[num] = true;
            vector<pair<long, long>> f = factors(num, width, length);
            for (pair<long, long> p : f) {
                q.push(p);
                if (p.first == width && p.second == length) {
                    printf("yes");
                    works = true;
                    break;
                }
            }
        }   
        if (works) {
            break;
        }
    }
    if (!works) {
        printf("no");
    }
}
