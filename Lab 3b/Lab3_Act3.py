
"""
(Enter a name)
(Enter a country)
(Enter a verb ending in ing)
(Enter a mode of transportation)
(Enter an animal)
(Enter a number)
(Enter a sport)
"""
name = input("Enter a name: ")
country = input("Enter a country: ")
verb = input("Enter a verb: ")
transport = input("Enter a mode of transportation: ")
animal = input("Enter an animal: ")
number = float(input("Enter a number: "))
sport = input("Enter a sport: ")

print()
print("Once upon a time, there lived a girl named Nisha. Nisha enjoyed" , verb , "and" , sport , ". However, she was not the best player in the national" , sport , "team. That made her very sad.\n")
print(country , "was going to host a" , sport , "compeition in" , number , "days. However, because of a storm, the competion got postponed by 6 weeks. Now, Nisha had" , number+42 , "extra days to train! She was elated. Nisha decided she would make the best of this opportunity and began training harder than she had ever trained before. She was feeling very confident. \"You can do this!\"" + ", she told herself.\n")
print("After", number+42 , "days of training, Nisha went to competition by a" , transport , "and won first place! Her countrymen were very proud of her and rewarded her with a pet" , animal + ". Nisha decided to name the" , animal , name , ".\n\nNisha had learnt a very important lesson - hard work really does pay off!\n\nThe end.")
