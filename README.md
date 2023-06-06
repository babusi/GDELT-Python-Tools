# GDELT Python Tools

Working with the [GDELT Visual Global Knowledge Graph](https://www.gdeltproject.org/data.html) can be intimidating and resource intensive. I've created this repo that breaks down the steps I took using python, including cleaning and transforming the data, to make it suitable for use by beginners.

## "smaller_files.py"

This script takes the GDELT file and breaks it down into smaller, more manageable files. By splitting the file into smaller chunks, it's easier to visualise, work with, and manipulate the data.

## "clean_face.py"

This script removes rows from the CSV file that do not have any faces in them. This is important when working with images because we only want to use images that have faces in them for analysis and visualization.

## "remove_cols.py"

This script removes unnecessary columns from the CSV file. Sometimes a CSV file can have a lot of columns, and not all of them are relevant to the analysis or visualization. By removing unnecessary columns, we can focus on the important data.

## "clean_images.py"

This script checks if the image URLs in the CSV file are accessible within a specified timeout. This is important because if an image URL is not accessible, we won't be able to use it for analysis or visualization. The script loops through each row in the CSV file, checks if the URL is accessible, and writes the row to a new CSV file if it is.
