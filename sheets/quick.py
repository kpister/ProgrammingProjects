f = open("names.txt")
w = open("first.txt", "w")
y = open("last.txt", "w")

for line in f:
	names = line.split(", ")

	y.write(names[0])
	y.write("\n")
	w.write(names[1])
