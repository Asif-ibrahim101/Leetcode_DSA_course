#Given a string s, return the first character to appear twice. 
# It is guaranteed that the input will have a duplicate character.

def repeatedCharacter(s: str) -> str:
   #using an setmap
   seen = set()

   for c in s:
      if c in seen:
         return c
      
      seen.add(c)

