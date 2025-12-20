#tuple
tuple1=(1,2,'abc',34.90,'mst')
tuple2=('est','cst')

#updation
tup=(1,2,3)
even=(2,4,6)
even=tup
print(even)

#Addition
add=tuple1+tuple2
print("Addition",add)

#replication
print("Repitition:",tuple2*3)

#slicing
print(tuple2[1:1])
print(tuple1[2:-1])
print(tuple1[::-1])
print(tuple1[-3:-1])
print(tuple1[3:-1])

#tuple deletion
#del tuple2
#print(tuple2) 

#Functions
#1.min()
tup3=(10,20,30,20,20)
print("min element of tuple:",min(tup3))

#2. max()
print("max element of tuple:",max(tup3))

#3.len()
print("length of tuple:",len(tup3))

#4.tuple()

#5.count()
print(tup3)
a=tup3.count(20)
print(a)
