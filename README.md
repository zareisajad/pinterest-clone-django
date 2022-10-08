# Django Pinterest Clone
![Screenshot 2022-02-02 at 10-21-38 Pinterest-min](https://user-images.githubusercontent.com/71011395/152303215-f1b256c4-505c-4c4a-8ad6-eb044df43398.png)
A pinterest clone:
user can create a board and save pins on that board.  
similar pins are also shown below each pin in pin-detail page.  
the algorithm is very simple: when user goes to the pin-detail page, we look for all boards in database that may contain this particular pin,
then we show all pins in that boards.

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
- [ ] in pin-detail page, show the board name in form if the pin is saved already
