import os
import webbrowser

def create_directory_file():
    # create directory with the name bkmarks 
    # if a directory with name bkmarks doesn't exist
    if not(os.path.isdir("bkmarks")):
        try:
            os.mkdir("./bkmarks")
            # create the file to store urls
            urls_in_file = open("bkmarks/" + "url_list.txt", "w")
            urls_in_file.write("www.google.com")
        except OSError as error: 
            print(error) 
        urls_in_file.close()

def open_urls():
    try:
        # open the file containing the urls
        urls_in_file = open("bkmarks/" + "url_list.txt")
    except OSError() as e:
        print(e)
    else:
        # open the urls on browser
        for i in urls_in_file.readlines():
            print("yo")
            webbrowser.open_new_tab(i)
    urls_in_file.close()

def main():
    create_directory_file()
    open_urls()

if __name__ == "__main__":
    main()