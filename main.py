print("Generation Identifier")

year = int(input("What year were you Born?"))
if year >= 1883 and year <= 1900:
  print("Lost Generation")
  print("Probably the worst generation")
elif year >=1901 and year <= 1927:
  print("Greatest Generation")
  print("The best generation")
elif year >=1928 and year <= 1945:
  print("Silent Generation")
  print("The worst generation")
elif year >=1946 and year <= 1964:
  print("Baby Boomers")
  print("The worst generation, Lotta Kids")
elif year >=1965 and year <= 1980:
  print("Generation X")
  print("The worst generation, X-men")
elif year >=1981 and year <= 1996:
  print("Millenials")
  print("Millenials are the best generation, It's a right not a privilege")
elif year >=1997 and year <= 2012:
  print("Generation Z")
  print("The worst generation")
elif year >=2013 and year <= 2024:
  print("Generation Alpha")
  print("The worst generation")    
else:
  print("Dude, you must be an Alien!")
