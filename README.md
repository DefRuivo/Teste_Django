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
- Well that obvious, there is no database, we will fill it with the customers info and request theirs Geolocalization with [Position Stack](https://https://positionstack.com/)'s API
- Again go for terminal and type: python manage.py parsedata --path {CSV File's path} --gkey {Positions Stack's GeocodeKey} \
  Ex.: ```python manage.py parsedata /some/folder/customers.csv --gkey Th1Sm1gHtB34K3y```
- And again run: python manage.py runserver
- Be marveled, all customers info will be shown on json format, included latitude and longitude

## How it works

The most import part is the command part ```parsedata.py```

We will use 2 arguments one for the CSV File path to parse the data stored in the spreedsheet \
And another argument to use the Position Stacks API Geocode Key for security measures

The primary function command is:

```
with open(file_path, 'r') as f:
  reader = csv.reader(f)
  for i, row in enumerate(reader):
  if i == 0:
    continue
```

This code will access the CSV file and jump the first row since it is a header but we only want the customers info

The nested function will get the city data and send a request to Position Stack API while storing the json response on cache:

```
@functools.lru_cache(maxsize=60)
def position_stack(address):

    params = f"forward?access_key={key}&query={address}&country=US"

    req = requests.get(f"http://api.positionstack.com/v1/{params}")

    try:
        latitude_req = req.json()["data"][0]["latitude"]
        longitude_req = req.json()["data"][0]["longitude"]
        endereco = latitude_req, longitude_req
        print(endereco)
    except TypeError:
        endereco = (0, 0)
```  

with that json response we will store it on mysql db:

```
with open(file_path, 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue

        latitude, longitude = position_stack(row[6])

        Customers.objects.update_or_create(
            first_name=row[1],
            last_name=row[2],
            email=row[3],
            gender=row[4],
            company=row[5],
            city=row[6],
            title=row[7],
            longitude=longitude,
            latitude=latitude,
        )
```

## Special Thanks
