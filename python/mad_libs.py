def blank1(place):
	print("I went to the " + place)

places = ["store", "beach", "ice cream parlor", "microbrewery"]

for place in places:
	blank1(place)

def blank2(companion):
    print("I was with " + companion + ".")

companions = ["Viola", "Jette", "Frank"]

for companion in companions:
    blank2(companion)
    blank1()
