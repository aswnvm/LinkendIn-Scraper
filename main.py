import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas as pd
import csv

jobs = []


def main():
    for i in range(0, 5):
        res = requests.get(
            f"https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum={i}"
        )
        soup = BeautifulSoup(res.text, "html.parser")
        job_class = soup.select(".base-card")

        for job in job_class:
            job_company = job.select_one(".base-search-card__subtitle").get_text(
                strip=True
            )
            job_title = job.select_one(".base-search-card__title").get_text(strip=True)
            job_location = job.select_one(".job-search-card__location").get_text(
                strip=True
            )
            job_href = job.select_one(".base-card__full-link").get("href")

            res2 = requests.get(job_href)
            soup = BeautifulSoup(res2.text, "html.parser")
            job_description_section = soup.select_one(".show-more-less-html__markup")
            job_desc = []
            if job_description_section:
                job_description = "\n".join(
                    [
                        li.get_text(strip=True)
                        for li in job_description_section.find_all("li")
                    ]
                )
                job_desc.append(job_description)
            else:
                print("Job description not found")

            jobs.append(
                {
                    "Company": job_company,
                    "Title": job_title,
                    "Location": job_location,
                    "URL": job_href,
                    "Description": job_desc,
                }
            )

    df = pd.DataFrame(jobs)

    df.to_excel("./linkedin_jobs.xlsx", index=False)
    # jobs_json = json.dumps(jobs, indent=4)
    # pprint.pprint(jobs)


if __name__ == "__main__":
    main()
