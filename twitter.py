users = {}        # usernames will go here
posts = []        # every post you create gets added here
post_id = 1       # each post gets its own number

def createaccount():
    while True:
        username = input("Your username here: ")
        if username in users:
            print("Username already exists. Please try again.")
            continue
        else:
            break
    bio = input("Your bio here: ")
    users[username] = {"bio": bio, "followers": 0}
    #I know it wasn't part of the requirements, but I wanted to have something that added a password.
    print("Add a password? (Enter 'yes' to add one. Otherwize, enter anything else.)")
    if input().lower().strip() == "yes":
        password = input("Your password here: ")
        users[username]["password"] = password
    print("Account created.")
    return users
def login():
    #I made a login feature because logging in was repetitive.
    while True:
        signedin = input("Your username: ")
        if signedin not in users:
            print("Invalid username. Please try again.")
            continue
        elif "password" in users[signedin]:
            while True:
                signpass = input("Your password: ")
                if users[signedin]["password"] == signpass:
                    print("Welcome,", signedin)
                    break
                else:
                    print("Invalid password. Please try again.")
                    continue
            break
        else:
            print("Welcome,", signedin)
            break
    return signedin
def post():
    #using global was a bug fix
    global post_id
    print("Log in before creating a post.")
    signedin = login()
    posts.append({"id": post_id, "user": signedin, "text": input("Write your post: "), "likes": 0})
    post_id = post_id + 1
def viewfeed():
    print("-                               PYTHONX: FEED                               -")
    print("")
    print("")
    print("Press ENTER/RETURN to see a new post")
    #I added a "like" feature in the feed to create something more like an actual social media algorithm.
    print("Write 'L' to like a post.")
    print("")
    print("")
    goes = 0
    while True:
        for p in posts:
            print(p["user"], "says:")
            print(p["text"])
            print("Likes:", p["likes"])
            print("ID number", p["id"])
            goes = goes + 1
            nxt = input()
            #Personalized feed system where if you like a post, it shows you another post from that user.
            if nxt.upper().strip() == "L":
                p["likes"] = p["likes"] + 1
                print("Post liked.")
                for q in posts:
                    if q["user"] == p["user"]:
                        print(q["user"], "says:")
                        print(q["text"])
                        print("Likes:", q["likes"])
                        print("ID number", q["id"])
                        goes = goes + 1
                        nxt = input()
                        if nxt.upper().strip() == "L":
                            q["likes"] = q["likes"] + 1
                            print("Post liked.")
                            print("")
                            print("(advertisement)")
                            print("If you love posts by", p["user"], "you'll LOVE StateFarm's new insurance plan. Try it today!")
                            placeholder = input()
                        else:
                            break
        print("")
        print("You've seen", goes, "post(s). Leave the feed?")
        if input().lower().strip() == "yes":
            print("Leaving feed.")
            print("")
            break
        else:
            continue
def like():
    while True:
        liked = False
        try:
            idfind = int(input("Enter the post's id: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        for p in posts:
            if p["id"] == idfind:
                p["likes"] = p["likes"] + 1
                liked = True
                print("Post liked.")
        if not liked:
            print("Invalid input. Please try again.")
            continue
        else:
            break
def editbio():
    print("Sign in to edit your bio.")
    signedin = login()
    users[signedin]["bio"] = input("New bio here: ")
    print("Done.")
def delpost():
    print("Sign in to delete a post.")
    signedin = login()
    while True:
        deleted = False
        try:
            idfind = int(input("Enter the post's id: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        for p in posts:
            if p["id"] == idfind:
                if p["user"] == signedin:
                    posts.remove(p)
                    deleted = True
                    print("Post deleted.")
        if not deleted:
            print("Invalid input. Please try again.")
            continue
        else:
            break
        
    
  


#Here's the main thing:

print("-                  PYTHONX (FORMERLY X (FORMERLY TWITTER))                  -")
print("")
print("")
print("")
print("")
while True:
    print("Select the corresponding number of a choice.")
    print("1. Create a user")
    print("2. Write a post (account needed)")
    print("3. View the feed")
    print("4. Like a post")
    print("5. Exit")
    print("6. Extra features (account needed)")
    number = input().strip()
    if number == "1":
        users = createaccount()
        continue
    elif number == "2":
        if not users:
            print("Create an account to access this feature.")
        else:
            post()
        continue
    elif number == "3":
        if not posts:
            print("No posts yet. Try another feature:")
            continue
        else:
            viewfeed()
            continue
    elif number == "4":
        if not posts:
            print("No posts yet. Try another feature:")
            continue
        else:
            like()
            continue
    elif number == "5":
        break
    elif number == "6":
        if not users:
            print("Create an account to access these features.")
            continue
        else:
            print("Select the corresponding number of a choice.")
            print("1. Edit bio")
            print("2. Delete a post")
            extranumber = input()
            if extranumber == "1":
                editbio()
                continue
            elif extranumber == "2":
                if not posts:
                    print("No posts yet. Try another feature:")
                    continue
                else:
                    delpost()
                    continue
    else:
        print("That didn't work. Enter something else:")
        continue
quit()
