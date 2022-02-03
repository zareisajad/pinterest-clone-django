# Django Pinterest Clone
A pinterest clone created by django rest-framework, the idea in this program is about pins and boards. Users can create a board in their profile and save the pins on the board. Related/similar pins are also shown below each pin. The algorithm for the related/similar pins is very simple: when the user goes to the "PIN Details" page, we look for all the boards that may contain the particular "pin", then we also show all the other pins on that board.

## Features:
- public profile include bio, photo, webiste link, etc..
- create pin, image or video
- create boards, public or private (only you can see it)
- edit board cover, name, etc..
- edit pin's board, title, desc or delete it
- follow/unfollow
- add comment
- save pins to your own board
- etc..

## Used in this app:
- python3
- django 
- bootstrap
- sqlite3 database
- vanila javascript

## How to run this app:
1. clone or download the project.
2. change directory to ``` pinterest-clone-django```
3. make sure you have ``python3``, ```pip``` and ```virtualenv``` installed in your machine.
4. create virtualenv: ```python3 -m venv venv```
5. active virtualenv: Mac & Linux os: ```source venv/bin/activate```, windows os: ```venv\scripts\activate```
6. install app requirements: ```pip install -r requirements.txt```
7. databse migrate: ```python manage.py migrate```
8. run the server: ```python manage.py runserver```
9. you should be able to open this address now: http://127.0.0.1:8000/

## To-Do:
- [ ] in pin-detail page, show the board in form if the pin is saved alerady
