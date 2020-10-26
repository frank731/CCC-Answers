#define _CRT_SECURE_NO_WARNINGS 1
#include <fstream>


using namespace std;

int main() {
	int first, second, third, fourth;
	bool ignore = false;
	scanf("%d %d %d %d", &first, &second, &third, &fourth);
	if (first == 9 || first == 8)
	{
		if(fourth == 9 || fourth == 8)
		{
			if (second == third)
			{
				printf("ignore");
				ignore = true;
			}
		}
	}
	if (!ignore)
	{
		printf("answer");
	}
	return 0;
}