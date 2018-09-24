#2.1-2.2
pages = [
    {
        "filename" : "content/homepage1.html",
        "output" : "docs/homepage.html",
        "title" : "My Homepage",
    },
    {
        "filename" : "content/bio1.html",
        "output" : "docs/bio.html",
        "title" : "Bio",
    },
    {
        "filename" : "content/resume1.html",
        "output" : "docs/resume.html",
        "title" : "Resume",
    },
    {
       "filename" : "content/contact1.html",
        "output" : "docs/contact.html",
        "title" : "Contact Me", 
    },
]
def main():
    for value in pages:
        top_template = open('templates/top.html').read()
        bottom_template = open('templates/bottom.html').read()
        content = open(value["filename"]).read()
        homepage_html = top_template + content + bottom_template
        open(value["output"], 'w+').write(homepage_html)



if __name__ == "__main__":
    main()

#2.3 string replacement 
def meain():
    for value in pages:
        template = open("templates/base.html").read()
        content = open(value["filename"]).read()
        homepage_html= template.replace("{{content}}", content)
        open(value["output"], 'w+').write(homepage_html)