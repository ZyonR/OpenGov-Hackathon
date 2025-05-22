from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os

url ="https://www.dbm.gov.ph/index.php/budget?fbclid=IwY2xjawKZpwxleHRuA2FlbQIxMQABHndjbIU6m6J4U3PD0xVxKXrBc_diAwQDVcrl4XTg2PDsuN6ETmK2qS6IXg6v_aem_B4SU2pXFiJh_88_UPdQM5A"
response = requests.get(url)
if response.status_code == 200:
    print("Link Has Successfully Been Accessed!")
else:
    print(f"Your Link Is Not Accessible!\nError: {response.status_code}")

response_html=BeautifulSoup(response.text,"html.parser")
card_years = response_html.find_all("ul",class_="nav navbar-nav")[3]
all_download_links = card_years.find_all("a")

links = [a.get("href") for a in all_download_links if a.get("href") and a.get("href") != "#"]

folder_path = "pdf_data"
os.makedirs(folder_path, exist_ok=True)

for link in links:
    visiting_url = urljoin(url, link)
    print("Visiting:", visiting_url)
    visit_response = requests.get(visiting_url)

    subpage_soup = BeautifulSoup(visit_response.text, "html.parser")
    download_links = subpage_soup.find_all("a")

    pdf_links = [
        urljoin(visiting_url, a.get("href"))
        for a in download_links
        if a.get("href") and a.get("href").endswith(".pdf")
    ]

    for pdf_url in pdf_links:
        print("Found PDF:", pdf_url)
        filename = pdf_url.split("/")[-1]
        full_path = os.path.join(folder_path, filename)

        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            with open(full_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f"PDF downloaded successfully as '{full_path}'")
        else:
            print(f"Failed to download PDF: {pdf_url} (Status: {pdf_response.status_code})")