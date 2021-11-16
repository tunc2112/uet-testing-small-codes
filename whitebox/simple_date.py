def is_valid_day(date, month, year):
	if not isinstance(year, int) or year == 0:
		return False

	if not isinstance(month, int) or month < 1 or month > 12:
		return False

	if not isinstance(date, int) or date < 1:
		return False

	if month in [1, 3, 5, 7, 8, 10, 12]:
		return date <= 31

	elif month in [4, 6, 9, 11]:
		return date <= 30

	else:  # month == 2:
		if year % 400 == 0 or year % 4 == 0 < year % 100:
			return date <= 29
		else:
			return date <= 28
