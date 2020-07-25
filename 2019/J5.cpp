//works but is slower than python so currently in progress

#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>
using namespace std;

vector<int> rabin_karp(string word, string text)
{
	vector<int> returned;
	int wordlength = word.length();
	int textlength = text.length();
	int whash = 0;
	int thash = 0;
	int prime = 7;
	int inputcharcount = 2;
	int i;
	int j;
	int hash = pow(inputcharcount, wordlength - 1);
	hash %= prime;

	for (i = 0; i < wordlength; i++)
	{
		whash = (inputcharcount * whash + word[i]) % prime;
		thash = (inputcharcount * thash + text[i]) % prime;
	}

	for (i = 0; i <= textlength - wordlength; i++)
	{
		if (whash == thash)
		{
			for (j = 0; j < wordlength; j++)
			{
				if (text[i + j] != word[j])
					break;
			}
			if(j == wordlength)
			{
				returned.push_back(i);
			}
		}

		if (i < textlength - wordlength)
		{
			thash = inputcharcount * (thash - text[i] * hash) + text[i + wordlength];
			thash %= prime;

			if (thash < 0)
			{
				thash = (thash + prime);
			}
		}
	}
	return returned;
}

bool found = false;
unordered_map<string, vector<string>> memoize;
//unordered_map<string, unordered_map<string, vector<string>>> memoizeparams;
bool loop(string currentstring, string endstring, vector<string> rulesnum, vector<int> indexes, vector<string> past, int iteration, int maxiteration, unordered_map<string, vector<string>> rules)
{
	if (!found)
	{
		if (iteration == maxiteration)
		{
			if (currentstring == endstring)
			{
				for (int i = 0; i < maxiteration; i++)
				{
					cout << rulesnum[i] << " " << indexes[i] << " "<< past[i] << "\n";
				}
				found = true;
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			if (memoize.find(currentstring) == memoize.end())
			{
				memoize[currentstring] = {};
				//memoizeparams[currentstring] = {};
				for (pair<string, vector<string>> rule : rules)
				{
					vector<int> found = rabin_karp(rule.first, currentstring);
					if (!found.empty())
					{
						for (int index : found)
						{
							string newstring = currentstring;
							string tempstring1;
							string tempstring2;
							tempstring1 = newstring.substr(0, index);
							if (index == 0)
							{
								tempstring1 = "";
							}
							newstring = currentstring;
							if (index + rule.first.length() > newstring.length())
							{
								tempstring2 = "";
							}
							else
							{
								tempstring2 = newstring.substr(index + rule.first.length());
							}
							newstring = tempstring1 + rule.second[0] + tempstring2;
							//cout << currentstring << " " << newstring << " " << index << " " << rule.second[1] << " " << iteration + 1<< "\n";
							//memoize[currentstring].push_back(newstring);
							//memoizeparams[currentstring][newstring] = {};
							//memoizeparams[currentstring][newstring].push_back(rule.second[1]);
							//memoizeparams[currentstring][newstring].push_back(to_string(index + 1));
							vector<string> arg1 = rulesnum;
							vector<int> arg2 = indexes;
							vector<string> arg3 = past;
							arg1.push_back(rule.second[1]);
							arg2.push_back(index + 1);
							arg3.push_back(newstring);
							bool out = loop(newstring, endstring, arg1, arg2, arg3, iteration + 1, maxiteration, rules);
							if (out)
							{
								return true;
							}
						}
					}
				}
			}
			else
			{
				/*
				for (string next: memoize[currentstring])
				{
					vector<string> arg1 = rulesnum;
					vector<int> arg2 = indexes;
					vector<string> arg3 = past;
					arg1.push_back(memoizeparams[currentstring][next][0]);
					arg2.push_back(stoi(memoizeparams[currentstring][next][1]));
					arg3.push_back(next);
					bool out = loop(next, endstring, arg1, arg2, arg3, iteration + 1, maxiteration, rules);
					if (out)
					{
						return true;
					}
				}
				*/
				
			}
			
		}
	}
	return false;
	
}

int main()
{
    unordered_map<string, vector<string>> rules;
	string temp1;
	string temp2;
	string start;
	string finish;
	int count;
	for (int i = 1; i < 4; i++)
	{
		cin >> temp1 >> temp2;
		vector<string> tempv_vector = { temp2, to_string(i) };
		rules[temp1] = tempv_vector;
	}
	cin >> count >> start >> finish;
	loop(start, finish, {}, {}, {}, 0, count, rules);
}