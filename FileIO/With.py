import pickle

# file read/write without .close()
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))