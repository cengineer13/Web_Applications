import requests
from bs4 import BeautifulSoup
import time

print("Some skills that you are not familiar with")
unfamiliar_skill = input('Write down:')
print(f"Filtiring out {unfamiliar_skill}")


def find_jobs():

    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from"
                            "=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(" ",'')
            skills = job.find('span', class_ = 'srp-skills').text.replace(" ","")
            more_info = job.header.h2.a['href']


            if unfamiliar_skill not in skills:

                with open(f"jobs/{index}.txt", 'w') as file:

                    file.write(f"Company name:{company_name.strip()}\n")
                    file.write(f"Required skills:{skills.strip()}\n")
                    file.write(f"Link to job:{more_info}\n")

                print(f"File saved: {index}")



if __name__ == '__main__':
    while True:
        min = 10
        find_jobs()
        time.sleep(min * 60)


