
fi = open ("links.txt")
fo = open ("outs.txt", "w")

for line in fi:
    line = line.rstrip("\n")
    if (line != ""):
        fo.write("=HYPERLINK(\"" + line + "\", \"link\")\n")
    else:
        fo.write("\n")


fi.close()
fo.close()
