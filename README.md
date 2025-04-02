# LinkedIn Job Scraper

This script scrapes job listings from LinkedIn using `BeautifulSoup` and `requests`. It extracts job titles, company names, locations, job descriptions, and URLs, then saves the data to an Excel file.

## Features
- Scrapes multiple pages of job listings.
- Extracts job title, company name, location, and job description.
- Saves the collected data in an Excel file.

## Prerequisites
Before running the script, ensure you have the following dependencies installed:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Usage
1. Clone this repository or download the script.
2. Navigate to the script directory.
3. Run the script using Python:

```bash
python script.py
```

4. The scraped data will be saved as `linkedin_jobs.xlsx` in the same directory.

## Code Overview
- **Requests**: Fetches job listings from LinkedIn.
- **BeautifulSoup**: Parses the HTML content to extract job data.
- **Pandas**: Stores data and exports it to an Excel file.

## Output
The script generates an Excel file (`linkedin_jobs.xlsx`) containing:
- **Company**: Name of the employer.
- **Title**: Job title.
- **Location**: Job location.
- **URL**: Link to the job listing.
- **Description**: Job description.

## Notes
- LinkedIn may block automated scraping. Consider adding headers or using an API.
- Some job descriptions may not be extracted due to page structure changes.

## License
This project is for educational purposes only. Scraping LinkedIn without permission may violate their terms of service.
