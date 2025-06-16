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

- Create a new person
```py
p = personlib.Person("Name")
```

- Change the any attributes of the person
```py
p.name = "John"
p.age = 15

from datetime import date
p.birth_date = date(2010, 6, 16)
```

- Get the attributes of the person
```py
name = p.name
age = p.age
birth_date = p.birth_date
```
