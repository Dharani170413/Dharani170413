#find whether a string is anagram of given string
str1=input("enter a string1:")
str2=input("enter a string2:")
k1=' '.join(sorted(str1))
k2=' '.join(sorted(str2))
if(k1==k2):
	print("anagram")
else:
	print("not a anagram")
