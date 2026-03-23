#Quadratic Time:-
#2n square + 3n + 5 = O(n)square 

#Time Complexity (if this is for DSA exam)
#Nested loop → O(n × m)
#Last loop → O(n)
#Overall complexity → O(nm)
#code:-
n = 5
m = 10

print(n + m)

for i in range(0, n):
    for j in range(0, m):
        print("Hello")

for k in range(0, n):
    print("Welcome")