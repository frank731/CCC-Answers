#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h> 
using namespace std;

int main()
{
    string rotates;
	cin >> rotates;
	int h = count(rotates.begin(), rotates.end(), 'H') % 2;
	int v = count(rotates.begin(), rotates.end(), 'V') % 2;
	if (h == 1 && v == 1)
	{
		cout << "4 3\n2 1";
	}
	else if (h == 1)
	{
		cout << "3 4\n1 2";
	}
	else if (v == 1)
	{
		cout << "2 1\n4 3";
	}
	else
	{
		cout << "1 2\n3 4";
	}
}
