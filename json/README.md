# JSON Processing
JSON is a data interchange format used widely on the internet and supported by most programming languages in wide use today.

## Encoding python objects in JSON
We can create a python dictionary and then encode it using JSON and write it to a file:
```
course_films = {}
course_films['Jack Goes Boating'] = 'Java: Might We Be Friends Project'
...
with open('course_films.json', 'w') as film_file:
    film_file.write(json.dumps(course_films))
```
