//not done

#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>
#include <fstream>
using namespace std;

int main()
{
	string key;
	string full;
	char last;
	int count = 0;
	unordered_map<char, int> key_frequency;
	unordered_map<char, int> temp_frequency;
	//unordered_map<long, unordered_set<string>> seen;
	unordered_set<int> seen;
	vector<string> see;
	long long cut_hash = 0;
	long h = 1;
	ifstream file;
	file.open("s3/s3.2-11.in", ios::out);
	getline(file, key);
	getline(file, full);
	//cin >> key >> full;
	int key_len = key.length();
	int full_len = full.length();
	for (char i : key)
	{
		if (key_frequency.find(i) == key_frequency.end())
		{
			key_frequency[i] = 1;
		}
		else
		{
			key_frequency[i] += 1;
		}
	}
	string cut = full.substr(0, key_len);
	for (char i : cut)
	{
		if (temp_frequency.find(i) == temp_frequency.end())
		{
			temp_frequency[i] = 1;
		}
		else
		{
			temp_frequency[i] += 1;
		}
	}
	last = 'A';
	
	h = pow(26, key_len - 1);
	h %= 1000000007;
	
	//std::cout << h << "\n";
	for (int i = 0; i < key_len; i++)
	{
		cut_hash = (26 * cut_hash + full[i]) % 1000000007;
	}
	//hashes.push_back(cut_hash);
	for (int i = 0; i < full_len - key_len + 1; i++)
	{
		cut = full.substr(i, key_len);
		//std::cout << cut << " " << i << " " << cut_hash << "\n";
		if (last != 'A')
		{
			temp_frequency[last] -= 1;
			if (temp_frequency[last] == 0)
			{
				temp_frequency.erase(last);
			}
			if (temp_frequency.find(cut.back()) == temp_frequency.end())
			{
				temp_frequency[cut.back()] = 1;
			}
			else
			{
				temp_frequency[cut.back()] += 1;
			}
		}
		last = cut.front();
		if (seen.find(cut_hash) == seen.end())
		{
			
			if (temp_frequency == key_frequency)
			{
				count += 1;
				//seen[cut_hash] = { cut };
				seen.insert(cut_hash);
				
				if (std::find(see.begin(), see.end(), cut) == see.end())
				{
					see.push_back(cut);
					std::cout << cut_hash << " " << cut << "\n";
				}
				else
				{
					std::cout << cut << " " << cut_hash << "\n";
				}
				
			}
			
		}
		/*
		else if (seen[cut_hash].find(cut) == seen[cut_hash].end())
		{
			if (temp_frequency == key_frequency)
			{
				count += 1;
				seen[cut_hash].insert(cut);
			}
		}*/
		if (i < full_len - key_len) {
			cut_hash = (26 * (cut_hash - full[i] * h) + full[i + key_len]) % 1000000007;

			if (cut_hash < 0)
			{
				cut_hash += 1000000007;
			}	
		}
		//hashes.push_back(cut_hash);
		
	}
	/*
	for (long h: hashes)
	{
		std::cout << h << "\n";
	}
	std::cout << "done\n";
	*/
	if(see.size() != seen.size())
	{
		std::cout << see.size() << " " << seen.size() << "\n";
	}
	std::cout << count;
}




