# Stock-Crawler
A simple script to get company data from idx.com


When importing use this to silence get_company_data()
```
import io
import contextlib
import sys

@contextlib.contextmanager
def no_stdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

...

with no_stdout():
    ...
```
