# personlib

personlib is a library which offers useful methods for storing data about persons

## Installation

- Clone the repository
```
git clone https://github.com/DerIch69420/personlib.git
```

- Create a venv and install the library
```
python -m venv venv
source venv/bin/activate
pip install -e personlib
```

## Documentation

- Import the library
```py
import personlib
```

- Choose the directory to save the person data
```py
personlib.DB_DIR = "db"
```

- Choose the indent which is used in the json files
```py
personlib.JSON_INDENT = 4
```

- Create a new person
```py
p = personlib.Person("Name")
```

- Change the any attributes of the person
```py
p.name = "John"

from datetime import date
p.birth_date = date(2010, 6, 16)
```

- Get the attributes of the person
```py
name: str = p.name # string representing the name
age: int = p.age # integer representing the years which have passed since the date of birth
birth_date: date = p.birth_date # datetime.date representing the date of birth
```
