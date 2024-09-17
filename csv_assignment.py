# Upgift 8 bis Patrick Royer Introduction to Python

# Import csv module
import csv

# Open a reader object
with open("brca_cnvs_tcga-1-2.csv","r") as input_csv_file:
    # Open a writer object 
    with open("brca_cnvs_tcga-1-2_modified.csv", "w") as output_csv_file:
        writer = csv.writer(output_csv_file, lineterminator='\n')
        reader = csv.reader(input_csv_file)
        
        # Create an empty list "everything"
        everything = []
        # Access the first row = header
        line = next(reader)
        # Add the name "seq_length" for the fifth column
        line.append("seq_length")
        # Add the first row = header to the empty list
        everything.append(line)
        
        # Iterate over rows
        for line in reader:
            # For each row
            # Add the length of the sequence in the fifth column
            # length = loc.end - loc.start
            # Had to convert loc.end and Loc.start to integer
            line.append(int(line[3]) - int(line[2]))
            # Add the modified row in the list "everything"
            everything.append(line)
        
        # Write the modified rows in the writer object
        writer.writerows(everything)
        
# I got some inspiration from Google...
# I prefer using Pandas module!