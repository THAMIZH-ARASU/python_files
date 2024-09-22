import pickle

mydb = {'1': 'a', '2': 'b'}
pickle_file = open("pyfile.txt", "wb")
pickle.dump(mydb, pickle_file)
pickle_file = open("pyfile.txt", "rb")
new = pickle.load(pickle_file)

print(new)
