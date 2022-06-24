f = open("msg.txt","r")
text = f.read()

#find frequency of each character?
freq = {}
for char in text:
	if char in freq:
		freq[char] +=1
	else:
		freq[char] = 1
res = ""
for key,value in freq.items():
	print(f"Key : {key}\t Frequency : {value}")
	res += chr(value)

print(res)
f.close()