"""
Concept: Web Scraping with BeautifulSoup

BeautifulSoup is a library for parsing HTML and XML documents. It creates a
parse tree that you can navigate, search, and modify.

Key concepts:
- `BeautifulSoup(html, 'html.parser')` - Create a soup object from HTML
- `soup.title` - Access the <title> tag directly
- `soup.title.string` - Get the text content of the title tag
- `soup.find('tag')` or `soup.tag` - Find the first matching tag
- `soup.find_all('tag')` - Find all matching tags (returns a list)
- `tag['attribute']` - Access an attribute of a tag (e.g., href)

Example:
    soup = BeautifulSoup('<p class="intro">Hello</p>', 'html.parser')
    paragraph = soup.find('p')
    print(paragraph.string)  # "Hello"
    print(paragraph['class'])  # ['intro']

Task: Parse the provided HTML to:
      1. Extract the title text (without the <title> tags)
      2. Find the first <a> (anchor/link) tag
"""

from bs4 import BeautifulSoup


def main():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    </body></html>
    """

    soup = BeautifulSoup(html_doc, "html.parser")

    # TODO: Get the title string (the text inside <title> tags, without the tags)
    # Hint: Access soup.title to get the tag, then .string to get the text
    title = ""

    # Verification for title
    if title == "":
        raise Exception("title is empty! Use soup.title.string to get the title text")

    if title != "The Dormouse's story":
        raise Exception(f'Expected title "The Dormouse\'s story", got "{title}"')

    # TODO: Find the first <a> tag in the document
    # Hint: You can use soup.find('a') or simply soup.a
    first_link = None

    # Verification for link
    if first_link is None:
        raise Exception(
            "first_link is None! Use soup.find('a') or soup.a to find the first link"
        )

    if first_link.name != "a":
        raise Exception(f"Expected an <a> tag, got <{first_link.name}>")

    print("Web scraping successful!")
    print(f"Title: {title}")
    print(f"First link text: {first_link.string}")
    print(f"First link href: {first_link['href']}")


if __name__ == "__main__":
    main()
