import re

def extract_token_ids(md_file):
    # Read the .md file
    with open(md_file, 'r') as file:
        content = file.read()

    # Extract token IDs using regex
    token_ids = re.findall(r'(\b\w{25,}\b)', content)

    return token_ids

def write_links(token_ids, output_file):
    # Write links to a plain text file
    with open(output_file, 'w') as file:
        for token_id in token_ids:
            file.write(f'[link](https://ergexplorer.com/token#{token_id})\n')

if __name__ == "__main__":
    # Specify input .md file
    input_md_file = 'token-ids.md'

    # Specify output text file
    output_txt_file = 'output.txt'

    # Extract token IDsfrom .md file
    token_ids = extract_token_ids(input_md_file)

    # Write links to plain text file
    write_links(token_ids, output_txt_file)

    print("Links extracted and written to output.txt")
