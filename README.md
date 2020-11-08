## Approach
This application has been developed using Python and Django framework.

## Minimum requirement
- pipenv
- Python 3.8
- Django
- Requests

## Installation Steps
- Install python 3.8
- Install pipenv package manager (if already installed, skip this step) 
```sh
pip install pipenv
```
- Create virtual environment in a preferred location 
```sh
pipenv shell
```
- Clone the repository
- Install all the dependencies
```sh
pipenv install
```
- run the application
cd support_desk and run following command in the terminal
```sh
python manage.py runserver
```
- visit http://127.0.0.1:8000/ to browse the application
- To run the test cases
cd support_desk run following command in the terminal
```sh
./manage.py test tickets/
```
- Settings can be changed in /support_desk/support_desk/settings.py
```
END_POINT = '' # Zendesk api endpoint
AUTH_USER = '' # Zendesk account email
AUTH_PASS = '' # Zendesk account password
PER_PAGE = 25  # Records per page
```
Note: The tha above command should be executed in the pipenv shell that is created when running pipenv shell


