
import utils



# utils.html_output()

# utils.apply_template()

#2.5
import sys
print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    utils.html_output()
    utils.apply_template()
elif command == "new":
    page_name =input("what is the page name?")
    new_page = 'content/' + page_name + '.html'
    open(new_page, "w+").write("some new content")
else:
    print("Please specify ’build’ or ’new’")