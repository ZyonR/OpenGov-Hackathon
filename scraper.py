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
    print(article)
    print("\n")
    is_data_good_to_go = input("Is the data good to go? (Press Y for Yes or N for No)")

    match is_data_good_to_go:
        case "Y":
            data = [
                {"title": article_title, "content": article, "link": url}
            ]
            with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
                writer.writerows(data)
                print(f"{article_title} has been Successfully Recorded!")
        case "N":
            print("Kindly change the indexes or the code itself to have a better data!")
        case _:
            print("Invalid Input! Only use Y or N Please :)")

url = "https://www.rappler.com/newsbreak/explainers/things-to-know-budget-process-philippines/?fbclid=IwZXh0bgNhZW0CMTEAAR7G72KMZWqByYELpzWWonAdcLKBtPhuXtNLhwXIrFuiJRNejOKIQJkZHJeykg_aem_nCk0q1otfk_Ugsml5wDGzQ"
rappler_data_scraper(url) 