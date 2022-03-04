# My Public IP

## About The Project
This library will give you, your **Public IP** using different online tools.

### Built With
* Python 3.x

## Getting Started
Go to the Project Directory

### Prerequisites
For installing setup.py you need ```setuptools``` python library.

If you don't have this library on your system, try one of the commands below:

```pip install setuptools```

or

```pip3 install setuptools```

### Installation
1. While you're in **Project Directory**, write the message below in the terminal

```bash
make install
```


   *Note* : You may need to use ```sudo make install```  or if you are on windows you can use see [```this```](https://superuser.com/a/808818)
4. Whenever you need this project in your program, just import it 
```bash
import my_ip_public
```
5. You can call these three functions to get your public IP from 3 diffrent providers

* [```my_ip_public.ipify_org()```](https://ipify.org)
* [```my_ip_public.my_ip_com()```](https://myip.com)
* [```my_ip_public.my_ip_io()```](https://my-ip.io)

4. You can always clean this, by ```make clean``` command while you are in the **Project Directory**

### Usage
This is the example of how to use them
```
.../my_ip_public$ python3
Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import my_ip_public
>>> my_ip_public.ipify_org()
(True, 'Your Public IP')
>>> my_ip_public.my_ip_com()
(True, 'Your Public IP')
>>> my_ip_public.my_ip_io()
(True, b'Your Public IP')
>>> 
```

## Screenshot

<img alt="App Screenshot" height="500" src="https://s6.uupload.ir/files/photo_2022-01-27_17-25-13_0ob9.jpg" width="600"/>

## Acknowledgments
Some links that you may find helpful

* [init.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
* [Python Library Structure](https://docs.python-guide.org/writing/structure/)
* [Python Json Library](https://docs.python.org/3/library/json.html)
* [Http Library in python](https://docs.python.org/2/library/httplib.html)
* [Http](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
