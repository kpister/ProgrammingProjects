f = open("names.txt")
w = open("first.txt", "w")
tencounter = 3
elecounter = 3
twecounter = 3
onecounter = 3

count = 0
col = "AL"
time = "am"

for line in f:
	line = line.rstrip()
	if (line == "10"):
		count = tencounter
		time = "am"
		tencounter += 1
	elif (line == "11"):
		count = elecounter
		time = "am"
		elecounter += 1
	elif (line == "12"):
		count = twecounter
		time = "pm"
		twecounter += 1
	elif (line == "1"):
		count = onecounter
		time = "pm"
		onecounter += 1
	w.write("=\'" + line + time + " Studio\'!" + col + str(count) + "\n")
	print ("=\'" + line + time + " Studio\'!" + col + str(count))

