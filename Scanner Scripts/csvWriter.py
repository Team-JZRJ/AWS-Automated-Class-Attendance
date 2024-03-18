import reading
import csv

with open("testing.csv", "a", newline="\n") as csvFile:
    id = str(reading.read_nfc()).split("=")[1]

    writer = csv.writer(csvFile)
    writer.writerow([id, "first name", "last name"])
csvFile.close()
