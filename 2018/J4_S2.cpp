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

bool check(const vector<vector<int>> &matrix, const int &size)
{
	for (vector<int> line : matrix)
	{
		for (int i = 1; i < size; i++)
		{
			if (line[i] <= line[i - 1])
			{
				return false;
			}
		}
	}
	for (int i = 0; i < size; i++)
	{
		for (int o = 1; o < size; o++)
		{
			if (matrix[o][i] <= matrix[o - 1][i])
			{
				return false;
			}
		}
	}
	return true;
}

void rotate(vector<vector<int>> &matrix, const int &size)
{
	vector<vector<int>> rotated = {};
	for (int i = size - 1; i >= 0; i--)
	{
		vector<int> temp = {};
		for (int o = 0; o < size; o++)
		{
			temp.push_back(matrix[o][i]);
		}
		rotated.push_back(temp);
	}
	matrix = rotated;
}

int main() {
	int size;
	bool found = false;
	scanf("%d", &size);
	vector<vector<int>> matrix = {};
	for (int i = 0; i < size; i++)
	{
		vector<int> line = {};
		int temp;
		for (int o = 0; o < size; o++)
		{
			scanf("%d", &temp);
			line.push_back(temp);
		}
		matrix.push_back(line);
	}

	while (!found)
	{
		if(check(matrix, size))
		{
			found = true;
			for (vector<int> line : matrix)
			{
				for (int i : line)
				{
					printf("%d ", i);
				}
				printf("\n");
			}
		}
		else
		{
			rotate(matrix, size);
		}
	}
	
	return 0;
}