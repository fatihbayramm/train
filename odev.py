import csv

with open("./family.csv" , "r") as csv_file:
    csv_reader = csv.reader(csv_file , delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Aile")
            line_count += 1
        else:
            print(f"\t{row[0]}" , f"{row[1]}" , f"{row[2]}" , f"{row[3]}")

    
    
       
