# String Indexing
place = "Marina Bay"

print(len(place))
print(place[0])
print(place[len(place) - 1])
print(place[-1]) # negative indexing


# String Slicing - to extract a substring
print(place[0:6:2])

print(place[::-1]) # reverse a string

place2 = "Clarke-Quay"
print(place2[-7:-10:-1])

# ClQu
print(place2[0:2:1] + place2[7:9:1])

# Upper and Lower Case Conversion
print(place2.upper())
print(place2.lower())

# CLARKE-quay
print(place2[0:6:1].upper() + place2[6::1].lower())


# Build a function that converts all vowels in any strings into upper case while consonants into lower case
def vowels_upper(anyString):
    vowels = "aeiouAEIOU"
    result = ""

    for c in anyString:
        if c in vowels:
            result = result + c.upper()
        else:
            result = result + c.lower()

    anyString = result
    print(anyString)


vowels_upper("apple")
vowels_upper("orange")




























