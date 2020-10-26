#define _CRT_SECURE_NO_WARNINGS 1
#include <algorithm>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;


int main() {
	int page_count;
	scanf("%d", &page_count);
	unordered_map<int, vector<int>> pages;
	for (int i = 1; i <= page_count; i++)
	{
		int next_page_count, temp;
		vector<int> next_pages = {};
		scanf("%d", &next_page_count);
		for (int o = 0; o < next_page_count; o++)
		{
			scanf("%d", &temp);
			next_pages.push_back(temp);
		}
		pages[i] = next_pages;
	}

	queue<int> queue = {};
	unordered_map<int, int> seen = { {1, 1} };
	int shortest_path = numeric_limits<int>::max();
	queue.push(1);
	
	while (!queue.empty())
	{
		int page = queue.front();
		queue.pop();
		if (pages[page].empty())
		{
			
			if(seen[page] < shortest_path)
			{
				shortest_path = seen[page];
			}
		}
		else
		{
			for (int new_page : pages[page])
			{
				if (seen.find(new_page) == seen.end())
				{
					seen[new_page] = seen[page] + 1;
					queue.push(new_page);
				}
				else if(seen[page] + 1 < seen[new_page])
				{
					seen[new_page] = seen[page] + 1;
				}
			}
		}
	}
	
	if(seen.size() == page_count)
	{
		printf("Y\n");
	}
	else
	{
		printf("N\n");
	}

	cout << shortest_path;
	
	return 0;
}