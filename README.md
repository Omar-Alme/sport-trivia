![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Features


## Data model

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Technologies Used
 - [ASCII art generator](https://patorjk.com/software/taag/#p=testall&f=Graceful&t=Sport%20Trivia%20) was used to transform the text to ascii art for the terminal.
 - [Open Trivia Database](https://opentdb.com/) a free to use, user contributed trivia question database used to generate the API documentation for the quiz.
 - [Python] is the programming language used.
 - [VScode] Integrated development environement and rich text editor.
 - [Heroku] is the cloud application platform used to create and host apps.
 - [Github] for version control.
 - [PEP8CI] was used to validate Python code.
 - [Node.js] 
 
 
## Testing

### Manual Testing

### Bugs

## Validator Testing

## Deployment
 The program was deployed in Heroku.

  - Steps for deployment:
     1. Log in to Heroku and go to dashboard
     2. Click on "New" button and create a new app
     3. Name the app and click create app.
     4. Go to the app's settings, click "Reveal Config Vars.
     5. Create a Configuration variable "PORT" with value "8000".
     6. Scroll down to "Buildpacks" and add Python first then Node.js. The order of the dependencies is important!
     7. Navigate to "Deploy".
     8. Choose Github as the deplyment method and connect your Heroku to Github, then select the repository you wish to deply.
     9. Enable Automatic Deploy.
     10. Manually Deploy the Project .


## Credits
  - [How to build a multiple Choice quiz in Python](https://www.youtube.com/watch?v=SgQhwtIoQ7o&list=PLLAZ4kZ9dFpMMs5lskzBApYXn0bl7emsW&index=33) similar code used but changed to be original.
  - [Python object oriented programming for beginners](https://www.youtube.com/watch?v=JeznW_7DlB0) tutorial by Tech with Tim helped understand concept of OOP.
  - [W3school](https://www.w3schools.com/python/gloss_python_class_init.asp) documentation for the initialisation function.
  - [TypeError](https://www.learndatasci.com/solutions/python-typeerror-list-indices-must-be-integers-or-slices-not-str/) helped fix a bug when picking data from dictionaries.
