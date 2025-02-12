# @TODO: Your code here

my_info = {"name": "Rex",
            "occupation": "dog",
            "age": 21,
            "hobbies": ["barking", "eating", "sleeping", "loving my owner"],
            "wake-up": {"Mon":5, "friday": 5, "saturday": 10, "sunday": 9}}

# print out results that are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["saturday"]}')
