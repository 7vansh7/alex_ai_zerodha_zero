# Import necessary libraries
import re

# Function to extract links containing '/articles'
def extract_article_links(input_file, output_file):
    # List to store extracted links
    article_links = []

    # Read the input file
    with open(input_file, 'r') as file:
        for line in file:
            # Find all URLs in the line using regex
            urls = re.findall(r'https?://[^\s]+', line)
            # Filter for links containing '/articles'
            for url in urls:
                if '/articles' in url:
                    article_links.append(url)

    # Write extracted links to the output file
    with open(output_file, 'w') as file:
        for link in article_links:
            file.write(link + '\n')

# Specify input and output file paths
input_file = 'links2.txt'  # Replace with your input file name
output_file = 'article_links.txt'  # Output file name

# Call the function
extract_article_links(input_file, output_file)

print(f'Extracted links containing "/articles" have been saved to "{output_file}".')
