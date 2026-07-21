import argparse
import requests
import os

# Create Argument Parser
parser = argparse.ArgumentParser(description="Simple File Downloader")

# Add command-line arguments
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", help="Output filename")

# Parse arguments
args = parser.parse_args()

url = args.url

# If output file is not provided, use the filename from the URL
if args.output:
    filename = args.output
else:
    filename = os.path.basename(url)

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"✅ File downloaded successfully as '{filename}'")

except requests.exceptions.RequestException as e:
    print("❌ Download failed!")
    print(e)