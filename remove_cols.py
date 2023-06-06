# Load the CSV file
filename = 'all_faces.csv'
df = pd.read_csv(filename)

# List of columns to drop
columns_to_drop = [
    'GeoLandmarks',
    'Logos',
    'SafeSearch',
    'Faces',
    'OCR',
    'LangHints',
    'WidthHeight',
    'RawJSON',
]

# Drop the specified columns
df = df.drop(columns=columns_to_drop)

# Save the modified DataFrame to a new CSV file
df.to_csv('updated_face.csv', index=False)

print('Columns dropped and updated_example.csv created.')