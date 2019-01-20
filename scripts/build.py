import csv
import glob


for name in glob.glob('scripts/build.csv'):
    textString = name

csvFile = textString
xmlFile = 'manifest/package.xml'

csvData = csv.reader(open(csvFile, 'rU'))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
xmlData.write(
    '<Package xmlns="http://soap.sforce.com/2006/04/metadata">' + "\n")


rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<types>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>'
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</types>' + "\n")

    rowNum += 1

xmlData.write('<version>45.0</version>' + "\n")
xmlData.write('</Package>' + "\n")
xmlData.close()
