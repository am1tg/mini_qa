import sys
import wikipedia
import time
import os

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/")


def fetch(query):                                                    # download data from wikiMedia
    # query = input("Enter search terms :")
    result_set = wikipedia.search(query)
    for term in range(len(result_set)):
            page = wikipedia.page(result_set[term])
            page_title = page.title
            page_title = page_title.replace(" ", "_")
            page_content = page.content
            try:
                os.chdir(path)
                files = [f for f in os.listdir(".") if f.endswith(".txt")]
                for f in files:
                    os.remove(f)
                name = page_title+"."+"txt"
                file = open(name, 'a')
                file.write(page_content)
                file.close()
            except:
                print("Error Occurred")
                sys.exit(0)

'''
def isClear():                                                          # boolean function to verify
    flag = input("Wish to delete data files...<y/n>").strip()
    if flag == 'y':
        return True
    else:
        return False


def clear_directory():                                                   # This function is kept for testing purpose
    if isClear():
        os.chdir(path)
        files = [f for f in os.listdir(".") if f.endswith(".txt")]
        for f in files:
            os.remove(f)
    else:
        print("Files are kept!")
# clear_directory()

start_time = time.time()
print('Now downloading data...')
# fetch()
end_time = time.time()
print("Total time :", end_time - start_time)
'''