def split_csv(input_file, output_prefix, chunk_size=2000000):
    # Read the large CSV file in chunks
    chunks = pd.read_csv(input_file, sep=',', chunksize=chunk_size)

    # Iterate through the chunks and save each one to a separate CSV file
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_part_{i + 1}.csv"
        chunk.to_csv(output_file, sep=',', index=False, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
        print(f"Saved {output_file}")

# Customize input_file and output_prefix to your needs
input_file = "GDELT_VGKG_Export-2016-02-21.csv"
output_prefix = "GDELT_Sample"

split_csv(input_file, output_prefix)