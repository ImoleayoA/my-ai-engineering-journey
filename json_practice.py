import json

profile = { "name" : "CiA", "age" : 18, "skills" : ["Trading", "Video Editing", "Photography"], "learning" : True}

#Convert to Json

json_string = json.dumps(profile, indent=4)
print(json_string)

json_string = '{"city":"Lagos", "population":1500000,"country":"Nigeria"}'

converted = json.loads(json_string)
print(converted)
print(converted["city"])

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    loaded = json.load(file)


print(loaded)
print(type(loaded))

company = {"name" : "TechCorp", "employees" : [{"name" : "CiA", "role" : "Ai Engineer"}, {"name" : "CiA", "role" : "AI Operator"}], "location": {"city" : "Lagos", "country" : "Nigeria"}}

with open("company.json", "w") as file:
    json.dump(company, file, indent=4)

with open("company.json", "r") as file:
    reading = json.load(file)

print(reading["employees"][1]["name"])
print(reading["location"]["city"])

bad_json = '{"name" : "CiA", "age" : }'

try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
