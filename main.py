import math
s = input()
s = s.split()
a, b, c = int(s[0]), int(s[1]), int(s[2])
for i in range(3):
    s[i] = int (s[i])    
if b*b-4*a*c > 0:
    print(f"Two different roots. x1 = {int((-b+math.sqrt(b*b-4*a*c))/2*a)}, x2 = {int((-b-math.sqrt(b*b-4*a*c))/2*a)}")
elif b*b-4*a*c < 0:
    print("No real root")
elif b*b-4*a*c == 0:
    print(f"Two same roots. x = {int((-b+math.sqrt(b*b-4*a*c))/2*a)}")