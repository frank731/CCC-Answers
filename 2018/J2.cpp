#define _CRT_SECURE_NO_WARNINGS 1
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	int count;
	int both = 0;
	string yesterday, today;
	scanf("%d", &count);
	cin >> yesterday >> today;

	for (int i = 0; i < count; i++)
	{
		if(yesterday[i] == today[i] && yesterday[i] == 'C')
		{
			both++;
		}
	}

	cout << both;
	
	return 0;
}