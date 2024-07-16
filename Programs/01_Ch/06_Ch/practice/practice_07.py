# Write a program to find out whether a given post is talking about “Harry” or not

# post = "Hey Harry !, How are you brother. "
post = input(" Enter your name : ")

if ("harsh" in post.lower()): # jo bhi post mein name likhenge lower krdega after that compare hoga
    print("Name is present is the post")

else:
    print("Not present")