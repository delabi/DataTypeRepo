def data_type(a):
	if isinstance(a, str):
		return len(a)
	if a == None :
		return 'no value'
	if isinstance(a, list):
		if  len(a) > 2:
			return a[2]
		return None
	if isinstance(a, bool):
		return a
	if isinstance(a, int):
		msg = ''
		if a < 100:
			msg = 'less than 100'
		if a > 100:
			msg = 'more than 100'
		if a == 100:
			msg = 'equal to 100'
		return msg

