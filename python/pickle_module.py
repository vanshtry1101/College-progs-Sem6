import pickle

snacks=('bread toast','fruit salad')

file=input('enter your file name:')

with open(file,"wb+") as f:
    pickle.dump(snacks, f)

    print("dumped")

    print("File contents:")

    f.seek(0)
    data=pickle.load(f)
    print(data)
