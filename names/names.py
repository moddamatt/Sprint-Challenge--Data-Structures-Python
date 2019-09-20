import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Since both files are read into a list i'm going to use a set type.

# Python Docs:
# intersection(*others)
# set & other & ...
# Return a new set with elements common to the set and all others.

# So duplicates will be set to the common intersection of the names list
# Oh wait nevermind I can't use this hmm
# duplicates = set(names_1).intersection(names_2)

# Maybe I'll try differnt for loop configurations
# Declare dups
duplicates = [name for name in names_1 if name in names_2] # maybe I can use a comprehension

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

