A small Python 3 module that parses currency

[![Code Health](https://landscape.io/github/Fuchida/purrency/master/landscape.svg?style=flat)](https://landscape.io/github/Fuchida/purrency/master)

```Bash
>> pip install purrency
```

```Python
from purrency import Purrency

prcy = Purrency('$200')

prcy.parse()

>> {'amount': Decimal(200.0), 'currency': '$'}

```


### Testing:
--------------
``` bash
git clone https://github.com/Fuchida/purrency.git

virtualenv --distribute --no-site-packages purrency -p /path/to/your/python3

. bin/activate

pip install -r test-requirements.txt

nosetests -v src/test_parser.py

```