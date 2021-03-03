# The Django Test

[IMakeCodes](https://github.com/imakecodes) challenge me to take a Django Test from a job interview to test my programming skills. \
Since i love challenges i accepted it, this is the result of my work

## The Challenge

An API that consumes a GeoCODE API to list the Geolocalization of every customer on\
a spreedsheet that contains 1000 customers. 

The information given from every customer on the spreedsheet is:

- Name
- Last Name
- Email
- Gender
- Company
- City
- Title

## 

## Prerequisites

- [Python](https://www.python.org/): ^3.8

## How to run server

- Git clone the project
- On terminal type: python manage.py runserver
- Search for "localhost:8080/customers"
- Talk to yourself: "Why there is no customers info?"
- Again go for terminal and type: python manage.py parsedata --path {CSV File's path} --gkey {Positions Stack's GeocodeKey}
- And again run: python manage.py runserver
- Be marveled, all customers info will be shown on json format, included latitude and longitude

