# my basic info
from js import document

def generate_message(e):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById ("school").value
    document.getElementById("output").innerText = f"{name}\'s age is {age} and {name}\'s school is {school}."