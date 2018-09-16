# First, get the template files
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/homepage1.html').read()

# Combine template HTML code with content HTML code
homepage_html = top_template + content + bottom_template
open('homepage.html', 'w+').write(homepage_html)

