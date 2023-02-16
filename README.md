
# Dental Symptom Checker Api

An API to be able to create, read, update and delete symptoms. And make changes to the symptoms as necessary



## Tech Stack

**Back-end:** Python, Flask

**Database:** Postgresql


## Installation

- Clone this repository
- create a virtual environment
```bash
  $ python3 -m venv venv
  $ source venv/bin/activate
```
- Install dependencies
```bash
  $ pip install -r requirements.txt
```
- Create database
- Create .env file that will hold your database URLs
- Run ```
  $ flask db init```
- After making your first model, update ```app/__init__.py``` to import the model into ```create_app```
- Run the commands ``` flask db migrate```  ```flask db upgrade```
- Check your server by running ```$ flask run```

## Development workflow

- Using Postman to make requests
- Using git as part of the development workflow


