# AWWWARDS-REPLICA
#### By Charles Okunzo, June 15, 2022
### This application is a clone of the awwwards app.
## Table of Contents
+ [Description](#description)
+ [Installation Requirements](#installation)
+ [Technologies Used](#technology)
+ [Lisence](#lisence)
+ [Authors Info](#author)

## Description
This application is a clone of the popular app-awwwards.

- Users  can view listed projects.
- Users can login to rate on posted projects.
- Users can interact with the Api used to build the project through DRF.
- Users login to the platform and post projects to be rated.
...
```
Landing Page
```
<img src="static/images/Screenshot from 2022-05-16 09-03-06.png">
<img src="static/images/Screenshot from 2022-06-15 13-56-20.png">

```
Sign Up
```

<img src="static/images/Screenshot from 2022-06-15 13-57-05.png">

```
Log In
```

<img src="static/images/Screenshot from 2022-06-15 13-56-54.png">


[Go Back to the top](#awwwards-replica)

## Getting Started

To clone the repository, run:

    git clone https://github.com/charles-okunzo/awwwards-replica

Then navigating to the cloned directory:

    cd awwwards-replica


### Prerequisite
This awwards Clone project requires a prerequisite understanding of the following:
- Django Framework
- Django REST API Framework
- Python3.8
- Postgres
- Python pipenv
- Makefile


## Setup and installation

###  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `pipenv shell`
####  Install dependancies
Install dependancies that will create an environment for the app to run from `Pipfile`
####  Create the Database
    - psql
    - CREATE DATABASE awwards;
####  .env file
Create .env file and paste the following, filling where appropriate:

    SECRET_KEY = '<secret_key>'
    DB_NAME = '<db_name>'
    DB_USER = '<username>'
    DB_PASSWORD = '<password>'

#### Run initial Migration
    make migrate
    
#### Run the app
    make run or make
    
    Open terminal on localhost:

[Go Back to the top](#awwwards-replica)
    
## Deployment

The application is deployed on Heroku and is live on this link:

[https://awwwards-replica.herokuapp.com/](https://awwwards-replica.herokuapp.com/)

## Technologies Used

  - [Django Rest Framework](https://www.django-rest-framework.org/) - For developing an API
  - [Django 4.0.5](https://docs.djangoproject.com/en/4.0/releases/4.0.4/) - Backend logic of the application.
  - [Bootstrap](https://getbootstrap.com/) - Used for overall design and responsive site


## Known Bugs
No known bugs.


## Licence

copyright (c) 2022 MIT License. [View License Here](LICENSE)

[Go Back to the top](#awwwards-replica)

## Authors Info

* Slack Profile - [Charles Okunzo](https://app.slack.com/client/T0101L740P4/C010GLANY3A/user_profile/U02TTFQ0VJR)
* Email address - [Charles Okunzo](charles.okunzo@student.moringaschool.com)