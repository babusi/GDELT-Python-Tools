csv.field_size_limit(sys.maxsize)

input_file = 'GDELT_Sample_part_1.csv'
output_file = 'all_faces.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row['Faces']:
            writer.writerow(row)