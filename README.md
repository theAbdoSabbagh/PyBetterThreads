# BetterThreads

[![Downloads](https://static.pepy.tech/badge/betterthread)](https://pepy.tech/project/betterthread)
[![PyPi](https://img.shields.io/pypi/v/BetterThreads.svg)](https://pypi.python.org/pypi/BetterThreads)
[![License](https://img.shields.io/github/license/theAbdoSabbagh/BetterThreads.svg?color=black)](https://github.com/theAbdoSabbagh/BetterThreads/main/LICENSE)

BetterThreads is a Python library for adding more features to the threading module in Python. 

BetterThreads makes it possible to return values from threads, and adds a finished signal so that the user can execute a function once the thread is finished. It is still in early development, and more features will be added soon.

## Installation
You can install BetterThreads using pip:
```bash
pip install BetterThreads
```

## Usage
Here is an example of how to use BetterThreads:
```python
from BetterThreads import BetterThread
from time import sleep

def my_function():
    sleep(5)
    return "Hello, World!"

thread = BetterThread(target=my_function)
thread.start()
thread.connect(print)
```
The above code will print "Hello, World!" after 5 seconds, as once the thread is finished, the returned value will passed to the `print` function. The returned value of the thread will be stored in the `value` attribute of the thread.

You can also use the `join` method to wait for the thread to finish and get the returned value, instead of connecting a function to the thread:
```python
from BetterThreads import BetterThread
from time import sleep

def my_function():
    sleep(5)
    return "Hello, World!"

thread = BetterThread(target=my_function)
thread.start()
thread.join()
print(f"The thread returned: {thread.value}")
```
The above code will print "Hello, World!" after 5 seconds, as once the thread is finished, the returned value will be stored in the `value` attribute of the thread.

## Features
- [x] Return values from threads
- [x] Execute a function once the thread is finished
- [ ] More features coming soon!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=theAbdoSabbagh/BetterThreads&type=Date&theme=dark)](https://star-history.com/#theAbdoSabbagh/BetterThreads&Date&theme=dark)