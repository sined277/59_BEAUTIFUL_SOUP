# Importing the necessary libraries
from bs4 import BeautifulSoup
import requests

# Sending a GET request to the webpage and getting the HTML content
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

# Creating a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Creating empty lists to store the article titles, links, and upvotes
article_titles = []
article_links = []
article_upvotes = []

# Finding all the article titles on the webpage and extracting their text and links
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

# Finding the upvotes for each article and storing them in a list
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        # If there are no upvotes, append 0 to the list
        article_upvotes.append(0)
    else:
        # Otherwise, extract the number of upvotes from the HTML and convert to an integer
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# Finding the index of the article with the most upvotes
max_points_index = article_upvotes.index(max(article_upvotes))

# Printing the title, upvotes, and link of the article with the most upvotes
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)
