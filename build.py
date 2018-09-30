#2.1-
# def main():
# #     for value in pages:
# #       top_template = open('templates/top.html').read()
#         bottom_template = open('templates/bottom.html').read()
#         content = open(content/homepage1.html).read()
#         homepage_html = top_template + content + bottom_template
#         open(value["output"], 'w+').write(homepage_html)


# pages = [
#     {
#         "filename" : "content/homepage1.html",
#         "output" : "docs/homepage.html",
#         "title" : "My Homepage",
#     },
#     {
#         "filename" : "content/bio1.html",
#         "output" : "docs/bio.html",
#         "title" : "Bio",
#     },
#     {
#         "filename" : "content/resume1.html",
#         "output" : "docs/resume.html",
#         "title" : "Resume",
#     },
#     {
#        "filename" : "content/contact1.html",
#         "output" : "docs/contact.html",
#         "title" : "Contact Me", 
#     },
# ]

# 2.2
# def main():
#     for value in pages:
#         top_template = open('templates/top.html').read()
#         bottom_template = open('templates/bottom.html').read()
#         content = open(value["filename"]).read()
#         homepage_html = top_template + content + bottom_template
#         open(value["output"], 'w+').write(homepage_html)





# # 2.3 string replacement 
# def main():
#     for value in pages:
#         template = open("templates/base.html").read()
#         content = open(value["filename"]).read()
#         index_html= template.replace("{{content}}", content)
#         open(value["output"], 'w+').write(index_html)




# # # # #2.4 Function refactor

# def apply_template(value):
#     template = open("templates/base.html").read()
#     index_html= template.replace("{{content}}", value)
#     return (index_html)

# def main():
#     for value in pages:
#         content = open(value["filename"]).read()
#         resulting_html_for_index = apply_template(content)
#         open(value["output"], "w+").write(resulting_html_for_index)
    

# # # # # Start of homework 4

# HMWRK4 2.1

#this grabs all of the content files
import glob
import os
all_html_files = glob.glob("content/*.html")
print(all_html_files)

# #this grabs the name only of the output docs. USe for grabbing titles 

file_path = "content/blog.html"


pages = []
def html_output():
    for each in all_html_files:
        print(each)
        file_name = os.path.basename(each)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only)
        output = 'docs/' + name_only + '.html'
        print(output)

        pages.append({
            "filename": each ,
            "title": name_only,
            "output": output,
        }) 
    

html_output()
print(pages)

def apply_template(value, title):
    template = open("templates/base.html").read()
    index_html = template.replace("{{content}}", value)
    title_replace = index_html.replace("{{my_blog}}", title)
    return (title_replace)

def main():
    for value in pages:
        content = open(value["filename"]).read()
        title = value["title"]
        resulting_html_for_index = apply_template(content, title)
        open(value["output"], "w+").write(resulting_html_for_index)




if __name__ == "__main__":
    main()