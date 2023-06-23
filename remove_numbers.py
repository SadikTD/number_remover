import re

def fix_paragraph(paragraph):
    lines = paragraph.split('\n')
    fixed_lines = [line.strip() for line in lines if line.strip()]
    fixed_paragraph = ""
    for i in range(len(fixed_lines)):
        if fixed_lines[i] == ".":
            fixed_paragraph = fixed_paragraph.rstrip() + ".\n\n"
        else:
            fixed_paragraph += fixed_lines[i] + " "
    return fixed_paragraph

# Ask for the input file names
file_names = input("Enter the input file names, separated by commas: ").split(',')

for file_name in file_names:
    # Read the content from each specified document
    with open(file_name.strip(), 'r') as file:
        content = file.read()

    # Remove the numbers enclosed in square brackets or at the end of a line
    modified_content = re.sub(r'\[(\d+)\]|\b(\d+)\b(?=\n|[^\w\s])', '', content)

    # Remove unnecessary line breaks
    modified_content = re.sub(r'\n+', '\n', modified_content)

    # Fix the paragraph organization
    modified_content = fix_paragraph(modified_content)

    # Create a modified document's name
    modified_document_name = "modified_" + file_name.strip()

    # Write the modified content to a new file
    with open(modified_document_name, 'w') as file:
        file.write(modified_content)

    print("Modification completed. The modified document", file_name.strip(), "is saved as", modified_document_name)

    input("Press Enter to exit...")
