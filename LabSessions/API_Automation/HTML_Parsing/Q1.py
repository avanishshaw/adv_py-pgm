# Install and import BeautifulSoup from the bs4 module.
# Write a simple program to parse a small HTML string.
# Given this HTML:
# Extract the title text.
# Extract the <h1> text.
# Extract the paragraph text.
# Write a program to:
# Find the first <a> tag.
# Print its href attribute.
# Use .prettify() to format parsed HTML.
# What is the difference between:
# find()
# find_all()
# <html>
#   <head><title>Test Page</title></head>
#   <body>
#     <h1>Welcome</h1>
#     <p>This is a paragraph.</p>
#   </body></html>


from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
"""

# Parse HTML
soup = BeautifulSoup(html_doc, "html.parser")

# Extract title text
title_text = soup.title.text
print("Title:", title_text)

# Extract <h1> text
h1_text = soup.h1.text
print("H1:", h1_text)

# Extract paragraph text
p_text = soup.p.text
print("Paragraph:", p_text)

# Extract first <a> tag
first_link = soup.find("a")
print("First link:", first_link)

# Print format HTML
print("\nFormatted HTML:")
print(soup.prettify())