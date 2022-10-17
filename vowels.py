str=input().lower()
vowels=[]
consonant=[]

for f in str:
    if(f in "aeiou"):
        vowels.append(f)
    elif f!=' ':
        consonant.append(f)
print("vowels: ",sep=" ")
print(*vowels,sep=",")
print("consonant: ",sep=" ")
print(*consonant,sep=",")
