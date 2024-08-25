import urllib.parse

def encode_url_part(url):
    """Encodes the URL part, preserving URL special characters."""
    return urllib.parse.quote(url, safe='~()*!.\'')  # Extended safe characters to handle more URL characters

def process_m3u_file(input_file, output_file):
    """Reads the M3U file, encodes the stream URLs, and writes to a new file."""
    base_url = 'http://192.168.1.123:6090/stream?url='

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            line = line.strip()
            if line.startswith('#EXTINF'):
                # Write the #EXTINF line unchanged
                file.write(line + '\n')
            elif line.startswith(base_url):
                # Extract and encode only the part after 'url='
                url_part = line[len(base_url):]
                print(f"Original URL part: {url_part}")  # Debugging statement

                # URL decode the part before encoding
                url_part = urllib.parse.unquote(url_part)
                print(f"Decoded URL part: {url_part}")  # Debugging statement

                encoded_url_part = encode_url_part(url_part)
                print(f"Encoded URL part: {encoded_url_part}")  # Debugging statement

                encoded_line = f"{base_url}{encoded_url_part}"
                file.write(encoded_line + '\n')
            else:
                # Write other lines unchanged
                file.write(line + '\n')

# Define input and output file paths
input_file = 'input.m3u'
output_file = 'output_encoded.m3u'

# Process the M3U file
process_m3u_file(input_file, output_file)
