file = open ("atomtest04.txt", "r")

sentences = []
keysets = []

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for line in file:
    sentences.append(line.strip())

#print(sentences)
file.close()

copy_sentences = sentences.copy()
edited_sentences = sentences.copy()

jointindicator = "dagNode {"
jointnames = []

#print(sentences[(sentences.index("dagNode {") + 1)]) # Index of the First Joint

for i in copy_sentences: # Find Joints' names
    if jointindicator in copy_sentences:
        #print([(copy_sentences.index(jointindicator) + 1)])
        jointnames.append((copy_sentences.index(jointindicator) + 1))
        copy_sentences[copy_sentences.index(jointindicator)] = "replaced"

keysindicator = 'keys {'
keyendindicator = "}"

for i in copy_sentences: #Find keys of each joint
    if keysindicator in copy_sentences:
        key_index = copy_sentences.index(keysindicator) + 1 #first key's index -1
        keyend_index = copy_sentences[key_index:].index(keyendindicator) + key_index
        #print(key_index)
        #print(keyend_index)
        jointkeystrings = sentences[key_index:keyend_index]
        keysets.append(jointkeystrings)
        #print(jointkeystrings)
        copy_sentences[copy_sentences.index(keysindicator)] = "replaced"

print(keysets)
#print(jointnames)

print(keysets[0])



for i in jointnames:
    print("\n")
    print(sentences[i])
    a = jointnames.index(i)
    #print(keysets[a])
    for x in keysets[a]:
        #print(find_nth(x, " ", 2))

        secondspace = find_nth(x, " ", 2)
        x = x[0 : secondspace : ]

        #x.replace()
        print(x)


#print(sentences)
#print(sentences.index("dagNode {"))

#print(sentences[9:])

#joint1 = sentences[10]
#print(joint1)

