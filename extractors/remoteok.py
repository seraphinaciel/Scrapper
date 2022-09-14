import requests
from bs4 import BeautifulSoup


def extract_remote_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            anchors = job.find("td", class_="source").find("a")
            link = anchors['href']
      
            if company:
                company = company.string.strip()
            if location:
                location = location.string.strip()
            if position:
                position = position.string.strip()

            if company and position and location:
                job_data = {
                    'link': f"https://remoteok.com/{link}",
                    'company': company,
                    'location': location,
                    'position': position
                }
                results.append(job_data)
    else:
        print("Can't get jobs.")
    return results

                
