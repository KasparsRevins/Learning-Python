#A simple nested loop example that sums the even and odd numbers between 1 and 11 and prints out the computation.
for even_num in range(2,11,2):
    for odd_num in range(1,11,2):
        val = even_num + odd_num
        print(even_num, "+", odd_num, "=" ,val)