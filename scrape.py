import requests
from bs4 import BeautifulSoup


def scrape_book_info(book_name: str) -> tuple[str, str, str]:
    """
    Scrapes book information from bol.com based on the provided book name.

    Args:
        book_name (str): The name of the book.

    Returns:
        tuple[str, str, str]: A tuple containing the image link, title, and author of the book.
    """
    formatted_book_name = book_name.replace(' ', '+')
    url = f'https://www.bol.com/nl/nl/s/?searchtext={formatted_book_name}'

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('URL error')

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the list item of interest using XPath
    uri = soup.find('ul', {'class': "list-view product-list js_multiple_basket_buttons_page"}).find('li').find('a').get('href')
    url = f'https://www.bol.com{uri}'

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('SUB URL error')

    sub_soup = BeautifulSoup(response.content, 'html.parser')

    img_link = sub_soup.find('div', {'class': 'image-slot'}).find('img').get('src')
    title = sub_soup.find('h1', {'class': "page-heading"}).find('span').text.strip()
    author = sub_soup.find('div', {'class': "pdp-header__meta-item"}).find('a').text.strip()
    return img_link, title, author
