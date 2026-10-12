course = "python programming "
print(course.title())
print(course.upper())
print(course.lower())
print(course.capitalize())

#string spaces
print(course.strip())
print(course.lstrip())
print(course.rstrip())

#replace text
text = "Python is a popular programming language."
print(text.replace("Python", "Java"))

data = "john,25,Huye"
array_data = data.split(",")
print(array_data)
print(text[4:])

print(text.count("python"))
print(text.find("python"))
print("Python" in text)
print("Java" not in text)