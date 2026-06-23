import json
student = {
    "name": "Aiswarya",
    "age": 22,
    "course": "Python"
}
with open("student.json","w")as file:
    json.dump(student,file,indent=4)
    print("Data written to student.json")
with open("student.json","r")as file:
    data=json.load(file)
    print("\n data read from json file:")
    print(data)