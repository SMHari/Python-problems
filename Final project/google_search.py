class Gsearch:
    def __init__(self, name_search):
        self.name = name_search

    def Gsearch(self):
        global search
        count = 0
        try:
            from googlesearch import search
        except ImportError:
            print("There seems a problem with the import: No Module named 'google' Found")
        for i in search(query=self.name, tld='com', lang='en', num=50, stop=30, pause=2):
            count += 1
            print("Result no:",count)
            print(i + '\n')


if __name__ == '__main__':

    while True:
        Query_str = input("Enter your Query to search: [Type quit to exit]  \n")
        print("connecting and searching.......")
        if Query_str.lower() != 'quit':
            search = Gsearch(Query_str)
            search.Gsearch()

        else:
            print("Thanks for using my script to Google via commandline")
            break
