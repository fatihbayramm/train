import csv


class FamilyMember:
    def __init__(self, name, surname, age,   family):
        self.name = name
        self.surname = surname
        self.age = age
        self.family = family
        

with open("./family.csv" , "r") as csv_file:
    csv_reader = csv.reader(csv_file , delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("         VERİLER")
            line_count += 1
        else:
            a = FamilyMember(row[0], row[1], row[2], row[3])
            




          
