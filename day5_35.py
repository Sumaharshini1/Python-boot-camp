vowels="aeiou"
consonant="bcdfghjklmnpqrstvwxy"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)