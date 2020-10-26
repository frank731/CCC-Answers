#define _CRT_SECURE_NO_WARNINGS 1
#include <algorithm>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <cmath>
#include <set>
#include <vector>

using namespace std;

int main() {
	int cities[5] = { 0 };
	int cities_dist[5] = { 0 };
	int sum = 0;
	for (int i = 1; i < 5; i++)
	{
		int temp;
		cin >> temp;
		sum += temp;
		cities[i] = temp;
		cities_dist[i] = sum;
	}
	for (int i = 0; i < 5; i++)
	{
		int current_dest = cities[i];
		for (int o  = 0; o < 5; o++)
		{
			cities_dist[o] = cities_dist[o] - current_dest;
			cout << abs(cities_dist[o]) << " ";
		}
		cout << "\n";
	}
	
	return 0;
}