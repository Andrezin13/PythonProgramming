
location = input("Where should I look?\n")

if location == "In the bedroom":
     sublocation = input("Where in the bedroom should I look?\n")
     if sublocation == "under the bed":
         print("Found some shoes but no phone")
     else:
         print("Found some mess but no phone")


elif location == "in the bathroom":
     sublocation = input("Where in the bathroom should I look?\n")
     if sublocation == "In the bathtub":
         print("Found a rubber duck but no phone")
     else:
         print("Found bathroom stuff but no phone")

elif location == "in the living room":
     sublocation = input("Where in the living room should I look?\n")
     if sublocation == "On the table":
         print("Yes! I found my phone")
     else:
         print("Found some stuff but no phone")

else:
     print("I do not know where that is but I will keep looking.")
