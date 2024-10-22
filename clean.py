import re

# File containing the links
input_file = "extracted_links.txt"
output_file = "category_links.txt"

# Regular expression pattern to match links starting with '/category'
pattern = r"/category\S*"

# Read the file and extract matching links
with open(input_file, 'r') as file:
    content = file.read()

# Find all matching links
category_links = re.findall(pattern, content)

# Save the extracted links to an output file
with open(output_file, 'w') as file:
    for link in category_links:
        file.write(f"{link}\n")

print(f"Extracted {len(category_links)} links starting with '/category' and saved to {output_file}")