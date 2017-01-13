#include <string>

using namespace std;

Layer indoor [
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 + val2;
		return val;
	}

	string connect(string name1, string name2)
	{
		string name;
		name = name1 + name2;
		return name;
	}

	int hoge(int name1, int name2)
	{
		int name;
		name = name1 + name2;
		return name;
	}
]

Layer outdoor [
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 - val2;
		return val;
	}
	string connect(string name1, string name2)
	{
		string name;
		name = name2 + name1;
		return name;
	}

	int hoge(int name1, int name2)
	{
		int name;
		name = name1 + name2;
		return name;
	}
]


