# so encode into one string, then decode use splitting up type of method
## learned that .join() is gonna make a list into a string
##might need to use slicing

##"Hello", "World" --> "5#Hello5#World"

#encoding:
#need to read length of each item in list, store that to be in front followed by a # and repeat

#decoding, so must read first element = k that is numeric before #
#and then take the k + 1 next elements as the string to parse then continue loop

##decode:
#for each element in the one string, take first element and convert to  k
##then from i + 2  till stop at k + 1 i take that and add it to a list as a string?

class Solution:

    def encode(self, strs: List[str]) -> str:
        newlist = []
        for i in strs:
            length_count = str(len(i)) ##string numeric like 5
            newlist.append(length_count + "#" + i)
            ##continues for each element in strs
        return "".join(newlist)


    def decode(self, s: str) -> List[str]:
        newlist = []
        i = 0 #index pointer till #
        starting = 0

        while i < len(s): #"5#Hello5#World"
            while s[i] != "#":
                i += 1
            ##so now we reached '#'
            ##need next i characters stored in a string that is added to newlist
            ###*******SLICING
            string_length = int(s[starting:i]) ###like 5 
            newlist.append(s[i + 1:i + 1 + string_length])
            i = i + 1 + string_length
            starting = i
        return newlist










