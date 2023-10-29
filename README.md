# Budget Tracker App

### The Budget Tracker is a web-based application designed to help users keep track of their finances. By allowing them to add and manage their income and expenses, the application provides a quick and easy way to monitor spending habits and identify areas where savings can be made.

- What does it do?  
   The Budget Tracker is a web-based application that allows users to add and manage their income and expenses, providing a quick and easy way to monitor spending habits and identify areas where savings can be made.

- What is the "new feature" which you have implemented that we haven't seen before?  
   The latest version of the Budget Tracker includes the ability to perform CRUD operations on both income resources and expenses, allowing users to manage their finances more effectively. Additionally, the dynamic clock provides a convenient way to stay up-to-date with the current time.

## Prerequisites
<!-- 
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)?
List those here (if any). -->

- I used json-server to run the database for this app so you need to install json-server and run it.
- Follow those commands:
  Open terminal in root directory of the project and enter this command:

```
npm install json-server
```

- When It's installed, enter this command:

```
json-server --watch data.json
```
- To start the project, run this command in root direcory of the project:
```
python -m flask --app main.py run
```

<!-- ## Project Checklist

- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
      Please provide the name of the module you are using in your app.
  - Module name: datetime, json
- [x] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name: main.py
  - Line number(s): **line 21 & line 125**
  - Name of two properties: **resource, amount, date**
  - Name of two methods: **create, update, delete**
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to a file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
      one example of a conditional statement in your code.
  - File name: **static/script.js**
  - Line number(s): **line 8**
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
      one example of a loop in your code.
  - File name: **main.py**
  - Line number(s): **line 155**
- [x] It lets the user enter a value in a text box at some point.
      This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code.
      In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository. -->
