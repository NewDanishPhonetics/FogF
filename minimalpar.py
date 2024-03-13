# Dette script sammenligner alle ord i en ordliste for at se hvor forskellige ordene er fra hinanden.
# Scriptet bruger funktioner fra difflib.

import difflib

input = open("ordliste.txt", "r", encoding="utf8") #encoding utf-8 sørger for at IPA-tegn genkendes
text = input.read()
ordliste = text.split()

d = {}
i = 0
for a in ordliste:
   i += 1
   for b in ordliste[i:]: #evaluer hvert ordpar en gang
       pair = a + " " + b
       for x,s in enumerate(difflib.ndiff(a, b)): #evaluerer det mindste antal gange man skal tilføje eller fjerne et tegn før de to ord er ens
           if s[0]==' ': continue
           else:
               if pair in d:
                   d[pair] += 1
               else:
                   d[pair] = 1

print("Der er følgende minimalpar i ordlisten:")
for ord in d:
    if d[ord] == 2: #print kun ordpar der adskiller sig med 2 (NB! Ikke alle ord der adskiller sig med 2, er minimalpar. Kan raffineres.)
        print(ord)