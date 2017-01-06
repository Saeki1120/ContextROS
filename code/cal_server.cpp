	long int cal_indoor(long int val1, long int val2)
	{
		long int val;
		val = val1 + val2;
		return val;
	}

	long int cal_outdoor(long int val1, long int val2)
	{
		long int val;
		val = val1 - val2;
		return val;
	}

	long int cal(long int val1, long int val2)
	{
		if (l_name.layer_name == "indoor") {
			return cal_indoor((long int)req.number1, (long int)req.number2);			//indoor振る舞い
		} else if (l_name.layer_name == "outdoor") {
			return cal_outdoor((long int)req.number1, (long int)req.number2);		//outdoor振る舞い
		}
	}
