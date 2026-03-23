# Cubic Time
#1️⃣ Outer loop (i) → n times chalega
#2️⃣ Middle loop (j) → har i ke liye n times chalega
#3️⃣ Inner loop (k) → har j ke liye n times chalega

n = 3

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)