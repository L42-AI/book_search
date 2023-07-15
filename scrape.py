import requests
from bs4 import BeautifulSoup

def scrape_book_info(book_name):
    # Format the book name for the URL
    formatted_book_name = book_name.replace(' ', '+')

    # Construct the search URL
    url = f'https://www.bol.com/nl/nl/l/{formatted_book_name}'

    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract book information
        title = soup.find('h1', class_='product-title').text.strip()
        author = soup.find('a', class_='product-subtitel').text.strip()
        price = soup.find('div', class_='promo-price').text.strip()
        description = soup.find('span', class_='long-description').text.strip()
        
        # Additional information you may want to extract:
        # - ISBN
        # - Publisher
        # - Publication date
        # - Book cover image URL

        # Print the extracted information
        print('Title:', title)
        print('Author:', author)
        print('Price:', price)
        print('Description:', description)

        # Add code to update your Notion database with the extracted information
        # You'll need to use the Notion API or the unofficial Python client for Notion

    else:
        print('Failed to fetch book information.')

# Example usage
book_name = input('Enter the name of the book: ')
scrape_book_info(book_name)
