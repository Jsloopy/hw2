
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()
content = open('content/homepage1.html').read()
homepage_html = top_template + content + bottom_template
open('docs/homepage.html', 'w+').write(homepage_html)


top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()
content = open('content/bio1.html').read()
bio_html = top_template + content + bottom_template
open('docs/bio.html', 'w+').write(bio_html)

top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()
content = open('content/resume1.html').read()
bio_html = top_template + content + bottom_template
open('docs/resume.html', 'w+').write(bio_html)