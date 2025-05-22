from bs4 import BeautifulSoup
import requests
import csv

def rappler_data_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return

    response_html=BeautifulSoup(response.text,"html.parser")
    main_article_rappler = response_html.find("div",class_="article-main-section")

    article_title = response_html.find("h1",class_="post-single__title").get_text(strip=True)
    article_tags = main_article_rappler.find_all(['h5', 'p', 'li'])
    article_text = [tag.get_text(strip=True) for tag in article_tags][12:-4]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def inq_op_data_scraper(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article_inq = response_html.find("article",class_="amp-wp-article")
    article_title = response_html.find("h1",class_="amp-wp-title").get_text(strip=True)

    article_tags = main_article_inq.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def inq_data_scraper(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article_inq = response_html.find("article",id="article_level_wrap")
    article_title = response_html.find("h1",class_="entry-title").get_text(strip=True)

    article_tags = main_article_inq.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags][:-5]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def phil_data_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article_phil = response_html.find("div",class_="article__writeup")
    article_title_cont = response_html.find("div",class_="article__title")
    article_title = article_title_cont.find("h1").get_text(strip=True)

    article_tags = main_article_phil.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def gma_data_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article_gma = response_html.find("div",class_="upper_article")
    article_title = main_article_gma.find("h1",class_="story_links").get_text(strip=True)

    article_tags = main_article_gma.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")
urls = [
#     {
#         "link":"https://www.rappler.com/newsbreak/explainers/things-to-know-budget-process-philippines/",
#         "media_cat": "Rappler"
#     },
#     {
#         "link":"https://www.rappler.com/newsbreak/data-documents/philippine-budget-2025-blanks-adjustments-after-ratification/",
#         "media_cat": "Rappler"
#     },
#     {
#         "link":"https://opinion.inquirer.net/180508/claims-of-blank-items-in-2025-budget-bicam-report-misleading/amp",
#         "media_cat": "Inquirer-Opinion"
#     },
#     {
#         "link":"https://newsinfo.inquirer.net/1996770/senate-receives-general-appropriations-bill-from-house",
#         "media_cat": "Inquirer"
#     },
#     {
#         "link":"https://newsinfo.inquirer.net/2016000/makabayan-wants-bicam-to-convene-again-to-address-budget-issues",
#         "media_cat": "Inquirer"
#     },
#     {
#         "link":"https://newsinfo.inquirer.net/2026756/i-dont-believe-ex-president-dutertes-claims-vs-2025-budget",
#         "media_cat": "Inquirer"
#     },
#     {
#         "link":"https://opinion.inquirer.net/180352/bigger-problems-in-2025-budget",
#         "media_cat": "Inquirer"
#     },
#     # {
#     #     "link":"https://www.philstar.com/headlines/2025/01/22/2414670/explainer-how-executive-branch-coping-budget-cuts/amp/",
#     #     "media_cat": "Philstar"
#     # },
#     {
#         "link":"https://www.philstar.com/opinion/2025/01/15/2414208/overhauling-2025-gaa",
#         "media_cat": "Philstar"
#     },
#     {
#         "link":"https://www.philstar.com/business/2025/03/15/2428412/p423-trillion-released-2025-budget",
#         "media_cat": "Philstar"
#     },
#     {
#         "link":"https://www.philstar.com/headlines/2024/11/07/2398381/senate-must-have-safeguard-vs-unconstitutional-items-2025-budget-says-lawmaker",
#         "media_cat": "Philstar"
#     },
#     {
#         "link":"https://www.philstar.com/pang-masa/police-metro/2025/01/25/2416751/isyu-sa-blangkong-line-items-sa-bicam-report-sa-2025-budget-wag-isisi-sa-palasyo",
#         "media_cat": "Philstar"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/934185/quimbo-p6-325-trillion-budget-legal-bicam-report-contained-correction/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/934241/quimbo-confirms-blanks-in-budget-bicam-report-but-says-funding-already-identified/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/927519/marcos-proposed-2025-budget-urgent/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/924784/house-2025-gab-senate/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/932100/marcos-wants-critical-projects-in-nep-be-restored-in-2025-budget/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/money/economy/915118/dbm-submits-p6-3-trillion-2025-national-expenditure-program-to-senate/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/933644/3-senators-deny-there-were-blank-entries-in-2025-budget-bicam-report/story/",
#         "media_cat": "GMA"
#     },
#     {
#         "link":"https://www.gmanetwork.com/news/topstories/nation/933695/hontiveros-blank-entries-2025-budget-wala-akong-nakita/story/",
#         "media_cat": "GMA"
#     },
#     # {
#     #     "link":"https://www.gmanetwork.com/news/topstories/nation/933946/bersamin-on-supposed-blank-items-in-2025-budget-hindi-kami-ang-mananagot-diyan/story/",
#     #     "media_cat": "GMA"
#     # },
#     # {
#     #     "link":"https://www.gmanetwork.com/news/video/24oras/697654/kopya-ng-bicam-report-ng-2025-nat-l-budget-na-may-blangko-pero-niratipikahan-ng-kongreso-ipinakita-ni-rep-manuel/video/",
#     #     "media_cat": "GMA"
#     # },
]

# for url in urls:
#     link = url["link"]
#     media_site = url["media_cat"]

#     match media_site:
#         case "Rappler":
#             rappler_data_scraper(link)
#         case "Inquirer-Opinion":
#             inq_op_data_scraper(link)
#         case "Inquirer":
#             inq_data_scraper(link)
#         case "Philstar":
#             phil_data_scraper(link)
#         case "GMA":
#             gma_data_scraper(link)

def gov1_data_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article = response_html.find("div",class_="entry-content")

    article_title = main_article.find("p",class_="has-text-align-center has-large-font-size").get_text(strip=True)
    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags][:-2]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def pna_data_scraper(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article = response_html.find("div",id="article-view")

    article_title = main_article.find("h1",class_="mb-6 text-3xl font-semibold md:text-publishable-title").get_text(strip=True)
    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags][:-4]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def senate_data_scraper(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return

    response_html=BeautifulSoup(response.text,"html.parser")
    article_title = response_html.find_all("p")[40:][0].get_text(strip=True)
    article_tags = response_html.find_all("p")[40:]
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def dbm_data_scraper(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
        return
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article = response_html.find("div",class_="com-content-article__body")
    article_title = response_html.find("h2").get_text(strip=True)

    article_content = main_article.find("div",class_="article-ct")
    article_tags = article_content.find_all("div", style="text-align: justify;")
    article = " ".join(p.get_text(strip=True) for p in article_tags if p.get_text(strip=True))

    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def dof_data_scraper(url):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")

    response_html=BeautifulSoup(response.text,"html.parser")
    main_article = response_html.find("div",class_="entry-content clr")
    article_title = response_html.find("h2",class_="single-post-title entry-title").get_text(strip=True)
    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags][:-1]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def pids_data_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
    response_html=BeautifulSoup(response.text,"html.parser")
    main_article = response_html.find("div",class_="container-content")
    article_title = response_html.find("h1",class_="page-title").get_text(strip=True)

    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def politiko_data_scraper(url):
    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
    response_html=BeautifulSoup(response.text,"html.parser")
    article_title = response_html.find("h1",class_="elementor-heading-title elementor-size-default").get_text(strip=True)

    article_tags = response_html.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags][1:-50]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def vera_data_scraper(url):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
    response_html=BeautifulSoup(response.text,"html.parser")
    article_title = response_html.find("h1").get_text(strip=True)
    main_article = response_html.find("div",class_="is-fact-check entry-content space-y-6")

    article_tags = main_article.find_all(["h2","blockquote","p"])
    article_text = [text for text in [tag.get_text(strip=True) for tag in article_tags] if text!=""]

    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def tribu_data_scraper(url):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
    response_html=BeautifulSoup(response.text,"html.parser")
    article_title = response_html.find("h1").get_text(strip=True)
    main_article = response_html.find("div",class_="arr--story-page-card-wrapper")

    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]

    save_data(article_title,article_text,url)
    
def save_data(article_title,article_text,url):
    article = " ".join(article_text)
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")

def bwo_data_scraper(url):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Link Has Successfully Been Accessed!")
    else:
        print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
    response_html=BeautifulSoup(response.text,"html.parser")
    article_title = response_html.find("h1",class_="entry-title").get_text(strip=True)
    main_article = response_html.find("div",class_="td-post-content td-pb-padding-side")

    article_tags = main_article.find_all("p")
    article_text = [tag.get_text(strip=True) for tag in article_tags]
    save_data(article_title,article_text,url)

url = "https://businessmirror.com.ph/2025/01/29/taxpayers-suit-challenges-gaa-2025-constitutionality/"

headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Link Has Successfully Been Accessed!")
else:
    print(f"Your Link Is Not Accessible!\nError: {response.status_code}")
response_html=BeautifulSoup(response.text,"html.parser")
article_title = response_html.find("h1",class_="entry-title").get_text(strip=True)
main_article = response_html.find("section",class_="entry-content")

article_tags = main_article.find_all("p")
article_text = [tag.get_text(strip=True) for tag in article_tags][:-5]

print(article_title)
# save_data(article_title,article_text,url)

