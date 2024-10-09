import bs4

print("-----------------")

exampleFile = open('./Chapter12/Project2/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
elems = exampleSoup.select('#author')
print(elems)

print(type(elems))

print(len(elems))

print(type(elems[0]))

print(elems[0].getText())

print(elems[0].attrs)

print("-----------------")

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())