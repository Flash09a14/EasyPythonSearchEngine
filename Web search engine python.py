import webbrowser
while True:
    try:
        user_input = input("\nDo you want to search terms on google or do you want to search for a web address (type 1 for a term, else, type 2) ")
        if user_input.upper() == "2":
            user = input("\nEnter address or search: ")
            webbrowser.open(user)
        elif user_input.upper() == "1":
            search_term = input("\nEnter what you want to search instead of an address: ")
            webbrowser.open("https://google.com/search?q={}".format(search_term))
        else:
            print("Invalid Input")
    except:
        print("Unable to open browser link, check internet connection\n")