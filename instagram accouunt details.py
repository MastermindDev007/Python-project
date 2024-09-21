# Import instaloader package
import instaloader
import os

# creating an Instaloader() object
ig = instaloader.Instaloader()

# Create a main directory named 'insta account detail' if it doesn't exist
main_directory = "insta account detail"
if not os.path.exists(main_directory):
    os.makedirs(main_directory)

# Taking the Instagram username as input from the user
usrname = input("Enter username: ")

# Fetching the details of the provided username using the Instaloader object
profile = instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username + " has " + str(profile.followers) + ' followers.')
print(profile.username + " is following " + str(profile.followees) + ' people.')
print("Bio: ", profile.biography)

# Setting the download directory to the main directory 'insta account detail'
ig.dirname_pattern = os.path.join(main_directory, "{profile}")

# Downloading the profile picture only and storing it in the desired directory
ig.download_profile(usrname, profile_pic_only=True)
