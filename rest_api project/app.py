from flask import Flask,request,jsonify

app = Flask(__name__)

Practice={"3136e3cd-c90c-48bb-b9a9-60ca68382ad7":{"title": "Say hello with python",
    "problem": "Print hello world in Python using print",
    "point": 1,
    "level": "beginner",
    "language": "python",
    "input": "",
    "expected_output": "Hello World"},
    "1ff26d62-e748-4907-bccf-cf2eec4ec06b":{
    "title": "Arithmetic Operators - Sum",
    "problem": "Sum two numbers",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "5,6",
    "expected_output": "11"},
    "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f":
    {"title": "Loops",
    "problem": "Print the square of each number in the loop step",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "4",
    "expected_output": "0,1,4,9"}}
@app.route('/')
def rest_api():
    return Practice["3136e3cd-c90c-48bb-b9a9-60ca68382ad7"]["title"] #istenilen kullanıcının idsi yazılarak bilgiler sorgulanabilir


if __name__ == '__main__':
    app.run()
