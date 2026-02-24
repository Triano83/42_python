def ft_harvest_total():
	result = 0
	n = 0
	i = 1
	while n < 3:
		n += 1
		result = result + int(input(f"Day {n} harvest: "))
	print(f"Total harvest: {result}")