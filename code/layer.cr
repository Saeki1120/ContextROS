Layer indoor [
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 + val2;
		return val;
	}
]

Layer outdoor [
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 - val2;
		return val;
	}
]