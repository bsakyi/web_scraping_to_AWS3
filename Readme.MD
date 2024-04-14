# Web Scraping Script: Extracting Links from Multiple Directories and Uploading to AWS S3

## Overview
This Python script is designed to extract links from multiple webpage directories. It utilizes the `requests` library for making HTTP requests, `BeautifulSoup` for parsing HTML content, `csv` for handling CSV files, and `boto3` for interacting with AWS S3. The script is configured to process a list of URLs, extract links from each URL's HTML content, append unique links to a CSV file, and then upload the CSV file to an AWS S3 bucket.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `boto3` library

## Usage
1. Clone or download the repository containing the script.
2. Install the required Python libraries if not already installed:
    ```
    pip install requests
    pip install beautifulsoup4
    pip install boto3
    ```
3. Modify the AWS credentials (`aws_access_key_id`, `aws_secret_access_key`, `region_name`) in the script to match your AWS IAM user credentials and desired AWS region.
4. Specify the list of URLs to process in the `urls` variable within the script.
5. Run the script:
    ```
    python web_scraping_script.py
    ```
6. Check the output:
    - For each URL:
        - If successful, the script will append the extracted links to `links.csv` in the same directory, print "Links appended to links.csv successfully for URL:", and upload the CSV file to the specified AWS S3 bucket, printing "CSV file uploaded to S3 bucket successfully for URL:".
        - If unsuccessful, it will print "Failed to retrieve the webpage for URL:" followed by the URL.

## Notes
- Ensure that the specified URLs are accessible and return valid HTML responses.
- The script assumes that the directory structure and link format are consistent for each URL. Modify the parsing logic as needed for different directory structures.
- Take into consideration the website's terms of service and legal implications before scraping.
- Ensure that your AWS IAM user has the necessary permissions to interact with the specified S3 bucket.

## Author
Github: bsakyi
Linkedin: www.linkedin.com/in/benjamin-a-sakyi-111b0319a </br>
Telegram: t.me/bsakyi  


