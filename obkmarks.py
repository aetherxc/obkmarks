import webbrowser

# create directory with the name bkmarks 
# if a directory with name bkmarks doen't exist

# then make a file in it

stuffinfile = open("bkmarks/" + "url_list.txt")

url = stuffinfile.readline()

# print(url)

# open urls in a webbrowser

webbrowser.open_new_tab(url) 