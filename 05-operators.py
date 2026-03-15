# Arithmetic Operators

x = 2
y = 4

total = x + y
print(total)

total = y - x
print(total)

total = x * y 
print(total)

total = y / x 
print(total)

total = y % x
print(total)

total = y ** x
print(total)

print("-----------------------------")
# ---------------------------------------------
# Comparison Operators

a = 5
b = 10

out = a < b
print(out)

out = a > b
print(out)
    
out = a <= b
print(out)

out = a >= b
print(out)

out = a == b
print(out)

out = a != b
print(out)  


print("-----------------------------") 
# ---------------------------------------------
# Assignment Operators

c = 0
d = 1

c += d  # c = c + d
print(c)

c -= d  # c = c - d
print(c)

c *= d  # c = c * d
print(c)

c /= d  # c = c / d
print(c)

c %= d  # c = c % d
print(c)    

c **= d  # c = c ** d
print(c)


print("-----------------------------") 
# ---------------------------------------------
# Logical Operators

a = 40
b = 60

x = 2
y = 3

out = (a > b) and (x < y)  # and operator => both conditions must be true
print(out)

out = (a > b) or (x < y)   # or  operator => at least one condition must be true
print(out)

out = not (a > b)          # not operator => negates the condition 
print(out)


print("-----------------------------") 
# ---------------------------------------------
# Membership Operators

skills = ["Python", "Java", "C++", "Docker", "Kubernetes"]
ans = "Python" in skills
print(ans)

ans = "Docker" not in skills
print(ans) 

ans = "Ansible" in skills
print(ans)

ans = "DevOps" not in skills
print(ans)


print("-----------------------------") 
# ---------------------------------------------
# Identity Operators

a = 12
b = 12

resuls = a is b
print(resuls) 

resuls = a is not b
print(resuls)


print("-----------------------------") 
# ---------------------------------------------
