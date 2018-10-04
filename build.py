from jinja2 import Template
import glob
import os
all_html_files = glob.glob("content/*.html")



pages = []
def html_output():
    for each in all_html_files:
        file_name = os.path.basename(each)
        name_only, extension = os.path.splitext(file_name)
        

        pages.append({
            "filename": each,
            "title": name_only,
            "output": "docs/" + name_only + '.html',
            "link": name_only + '.html',
            
        }) 
    

html_output()


def apply_template():
    for page in pages:
        index_html = open(page['filename']).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        page_output = template.render(
            title=page['title'],
            content=index_html,
            pages=pages,
            )
        open(page["output"], "w+").write(page_output)
        
apply_template()









