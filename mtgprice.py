import urllib2

commonAvg = 0.0
uncommonAvg = 0.0
rareAvg = 0.0
mythicAvg = 0.0

cardNum = 1
while cardNum < 206:
    req = urllib2.Request("http://magiccards.info/emn/en/" + str(cardNum) + ".html")
    req.add_header('User-agent', 'Chrome')
    response = urllib2.urlopen(req)

    text = response.read()
    print text
    break

    if text.find ("(Uncommon)") != -1:
        uncommonAvg += 1
    elif text.find("(Common)") != -1:
        commonAvg += 1
    elif text.find("(Rare)") != -1:
        rareAvg += 1
    elif text.find("(Mythic Rare)") != -1:
        mythicAvg += 1
    else:
        response = urllib2.urlopen("http://magiccards.info/emn/en/" + str(cardNum) + "a.html")
        text = response.read()
        if text.find ("(Uncommon)") != -1:
            uncommonAvg += 1
        elif text.find("(Common)") != -1:
            commonAvg += 1
        elif text.find("(Rare)") != -1:
            rareAvg += 1
        elif text.find("(Mythic Rare)") != -1:
            mythicAvg += 1
        else:
            break

    print(cardNum)

    cardNum += 1

print ("Average common: ", commonAvg, "Average Uncommon: ", uncommonAvg, "Average Rare: ", rareAvg, "Average Mythic: ", mythicAvg)
print ("Average wealth per pack: ", (commonAvg * 10 + uncommonAvg * 3 + rareAvg * .875 + mythicAvg * .125))
