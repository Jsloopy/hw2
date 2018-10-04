
import utils

# utils.html_output()

# utils.apply_template()


import sys
print("This is argv:", sys.argv)
command = sys.argv[1]
if command == "build":
    utils.html_output()
    utils.apply_template()
elif command == "new":
    page_name =input("What is the page name?")
    new_page = 'content/' + page_name + '.html'
    open(new_page, "w+").write("Import new content")
else:
    print("Please specify ’build’ or ’new’")