# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv('updated_face.csv')

# Function to check if the URL is accessible within the specified timeout
def is_url_accessible(url, timeout):
    try:
        response = urllib.request.urlopen(url, timeout=timeout)
        return response.status == 200
    except (URLError, ValueError, SocketTimeout, RemoteDisconnected, OSError):
        return False

# Set the timeout in seconds
timeout = 5

# Wrap the DataFrame iterrows() method with tqdm to create a progress bar
with open('clean_data.csv', 'w', newline='') as outfile:
    # Initialize a CSV writer
    csv_writer = csv.writer(outfile)
    
    # Write the header to the output CSV file
    csv_writer.writerow(df.columns)

    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Checking images"):
        if is_url_accessible(row['ImageURL'], timeout):
            # Write the row to the output CSV file if the URL is accessible
            csv_writer.writerow(row.values)
            outfile.flush()  # Flush the file buffer to write the data to disk immediately