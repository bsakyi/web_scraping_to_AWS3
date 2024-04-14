import requests
from bs4 import BeautifulSoup
import csv
import boto3

# AWS credentials
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'
region_name = 'your-region'

# Initialize Boto3 S3 client
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)

# List of URLs to process
urls = [
    "https://citinewsroom.com/2024/04/",
    # Add more URLs here
]

for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <a> tags which represent links
        links = soup.find_all('a')

        # Initialize a set to store unique hrefs
        unique_hrefs = set()

        # Open the CSV file in read mode to check for existing hrefs
        try:
            with open('links.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    unique_hrefs.add(row[0])
        except FileNotFoundError:
            pass

        # Open the CSV file in append mode and specify the delimiter as comma
        with open('links.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Extract the href attribute from each <a> tag and write it to the CSV file if it starts with the specified URL and is not already present
            for link in links:
                href = link.get('href')
                if href and href.startswith(url) and href not in unique_hrefs:
                    writer.writerow([href])
                    unique_hrefs.add(href)

        print("Links appended to links.csv successfully for URL:", url)

        # Upload the CSV file to S3 bucket
        s3.upload_file('links.csv', 'your-s3-bucket-name', 'links.csv')
        print("CSV file uploaded to S3 bucket successfully for URL:", url)
    else:
        print("Failed to retrieve the webpage for URL:", url)
