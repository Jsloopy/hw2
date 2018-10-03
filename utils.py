
from jinja2 import Template
import glob
import os
import sys 

all_html_files = glob.glob("content/*.html")

pages = []
def html_output():
    for each in all_html_files:
        # print(each)
        file_name = os.path.basename(each)
        name_only, extension = os.path.splitext(file_name)
        # output = 'docs/' + name_only + '.html'

        pages.append({
            "filename": each,
            "title": name_only,
            # "filename": file_name,
            "output": "docs/" + name_only + '.html',
            "link": name_only + '.html',
            "output_filepath": 'docs/' + name_only + '.html'
        }) 
    



def apply_template():
    for page in pages:
        # print(page) 
        index_html = open(page['filename']).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        # print(template)
        page_output = template.render(
            title=page['title'],
            content=index_html,
            pages=pages,
            )
        open(page["output"], "w+").write(page_output)
        
