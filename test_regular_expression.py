import re
# 0964 308 308

# regex = r"([a-zA-Z]+) (\d+)"

# if re.search(regex, "June 24"):
# 	match = re.search(regex, "June 24")
# 	print("%s, %s" % (match.start(), match.end()))
# 	print("%s" % (match.group(0)))
# 	print("%s" % (match.group(1)))
# 	print("%s" % (match.group(2)))


# matches = re.findall(regex,"June 24, Aug9, Dec 12")
# for match in matches:
# 	print(match)

# print(re.sub(regex, r"\2 of \1", "June 24, Aug9, Dec 12" ))

# regex = r"([a-zA-Z]+) \d+"
# matches = re.findall(regex, "June 24, Aug9, Dec 12")
# for match in matches:
# 	print(match)

# matches = re.finditer(regex, "June 24, Aug9, Dec 12")
# for match in matches:
# 	print(match.start(), match.end())


# regex = re.compile(r"(\w+) World")
# result = regex.search("Hello World isthe easies")
# if result:
# 	print(result.start(), result.end())

# for result in regex.findall("Hello World, Bonjour"):
# 	print(result)

# print(regex.sub(r"\1 Earth", "hello World"))

# r = re.compile('[0-9]+')
# string_list = ["123", "a", "467", "a2_2", "322"]
# o = filter(r.match, string_list)
# print(o)

# files = [ '/a/b/c/la_seg_x005_y003.png',
#           '/a/b/c/la_seg_x005_y003.npy',
#           '/a/b/c/la_seg_x004_y003.png',
#           '/a/b/c/la_seg_x004_y003.npy',
#           '/a/b/c/la_seg_x003_y003.png',
#           '/a/b/c/la_seg_x003_y003.npy', ]

# regex = re.compile(r'_x\d+_y\d+\.npy')

# selected_files = filter(regex.search, files)
# selected_files = filter(lambda x: x.endswith('.npy'), files)
# print(selected_files)

# strlst = ['aaaaaa', '1234', 'bbbbb', '------', '.+/4-3', 'a1b2c3']
# rexlst = [re.compile(x) for x in [r'^[a-z]+$', r'^\d+$']]

# outlst = filter(lambda x: any([True if r.match(x) else False for r in rexlst]), strlst)
# print(outlst)

# print(set(strlst))

# t = "A fat cat doesn't eat oat but a rat eats bats."
# mo = re.findall("[force]at", t)
# print(mo)

# items = re.findall("[0-9]+.*: .*", "Customer number: 234234, Data: Feb 12, 2012")
# print(items)

# str = "The destination is Londonn."
# mo = re.search(r"destination.*(London|Paris|Lon|on)", str)
# if mo:
# 	print(mo.group())

# regex = r"[A-z]{1,2}[0-9R][0-9A-Z] [0-9][ABD-HJLNP-UW-Z]{2}"
# address = "BBC News Centre, London, W12 7RJ"
# compiled_re = re.compile(regex)
# res = compiled_re.search(address)
# # print(filter(compiled_re.search, address))
# print(dir(res))
# print(res.string)
# print(res.start(), res.end())

# metamorphoses = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"

# a = re.split("\W+", metamorphoses)
# print(a)

# lines = ["surname: Obama, prename: Barack, profession: president", "surname: Merkel, prename: Angela, profession: chancellor"]

# for line in lines:
# 	print(re.split(",* *\w*: ", line))
# 	print(re.split(",* *\w*: ", line)[1:])

# str = "yes I sad yes I will Yes"
# res = re.sub("[yY]es", "no", str)
# print(res)

# import re
# s1 = "Mayer is a very common Name"
# s2 = "He is called Meyer but he isn't German."
# print re.search(r"^M[ae][iy]er", s1)
# print re.search(r"^M[ae][iy]er", s2)
# s = s2 + "\n" + s1

# print re.search(r"^M[ae][iy]er", s, re.M)

# fh = ["<composer>Wolfgang Amadeus Mozart</composer>","<author>Samuel Beckett</author>", "<city>London</city>"]
# for i in fh:
# 	res = re.search(r"<([a-z]+)>(.*)</\1>", i)
# 	print(res.group(1) + ": " + res.group(2))

# l = ["555-8396 Neu, Allison", 
#      "Burns, C. Montgomery", 
#      "555-5299 Putz, Lionel",
#      "555-7334 Simpson, Homer Jay"]

# for i in l:
# 	res = re.search(r'([0-9-]*)\s*([A-Za-z]+),\s(.*)', i)
# 	print(res.group(1))
# 	print(res.group(3) + " " + res.group(2) + " " + res.group(1))

# string = "Python123@#$@$ 213djagno"
# words = re.split('\W+', string)
# result = [] 
# for word in words:
# 	a = re.findall(r'\w+', word)
# 	result += a
# print(result)

# regex = r'[a-zA-Z]+'
# result = re.findall(regex, string)
# print(result)

string = "Ruby Programming - 1.1 - Komodo IDE"
regex = r'ruby|gram|modoasdf'
print(re.findall(regex, string, re.I))