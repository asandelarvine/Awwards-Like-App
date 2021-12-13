## PROJECT NAME 
*Awwards-Like-App*


## AUTHOR 
Asande Larvine


## DESCRIPTION 
This is a professional web design and development competition body where Developers can submit to.



## Features


As a user of the application you will be able to:


1. A user can log in.
2. A user can sign up.
3. View projects. 
4. A user can submit his or her own projects.
5. A user can upvote or downvote on a project.
6. A user is also able to change his or her profile,add bio .
7. A user can also comment on other people's project. 



## Behavior Driven Development

| __Behavior__  | __Input example__ | __Output example__ |
| ------------- | ----------------- | ------------------ |
| The user should see the landing page on first sight | "http://127.0.0.1:8000/"   | Home  |
| The application should provide an option to register or login to the app | login/register | true  |
| The application should authenticate Users base on details the user provides   | password/username |  access or no access |
| The user should be redirected to home page once logged in | access | home page |
| The user should view different views or post or images from different people | --- | photos |
| The application should be able to restrict unauthorized users from accessing some parts of the application | view | true/false |
| The user should be able to update his/her profile any time | profile update | True |
| The user should be able to follow other users in the application | follow | True |
| The user should be able to comment and like Posts  | like/comment | True |
| The user should be able to logout at will | logout | True |



## Admin Dashboard

[Admin Dashboard Login]()  with credentials

    username : `Awwards`

    password : `awwardspassword`
### Installation and setup instructions

1. Clone this repo: git clone https://github.com/asandelarvine/Instagram_Clone
2. The repo comes in a zipped or compressed format. Extract to your preferred location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database instagram using the command below.


       CREATE DATABASE instagram;
5. Migrate the database using the command below


       python3.8 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## TECHNOLOGIES USED 
* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface

## Known Bugs

* One of my projects "Pitch~Zone" site can not be viewed, yet to be resolved.


## CONTACTS
asandelarvine@gmail.com

## LIVE LINK
https://larv-awwards-2021.herokuapp.com/

