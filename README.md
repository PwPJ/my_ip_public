# My Public IP

"My Public IP" is a python 3.x library which you can use to find your IP.You can build this library on your system by using the instructions below:

## Requirments
 1)You will need ```setuptools``` for installing setup.py. In case you don't have this library you can use the commands below:

	```pip install setuptools``` or ```pip3 install setuptools```

 2)You have to have your project directory open while you are doing the steps below.

## Installation
 Step1:Make sure your project directory is open.
 Step2:Type the command below in your terminal:

 	```make install```
    *Note*:you may need to use your root account by using the command below  ```sudo make install```  or if you are on windows you can see [```this```](https://superuser.com/a/808818)

 Step3: Whenever you need this project in your program, just import it:

    ```import my_ip_public```
 Step4:You can call these three functions to get your public IP from 3 diffrent providers

 * [```my_ip_public.ipify_org()```](https://ipify.org)
 * [```my_ip_public.my_ip_com()```](https://myip.com)
 * [```my_ip_public.my_ip_io()```](https://my-ip.io)

 step5:Type ```make clean``` at the command line to get rid of your object and executable files but make sure that project directory is still open.

## Usage
 This is a script that you can read to understand how to use this library:

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

### Acknowledgments
You can also use the links below for more help:

* [init.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
* [Python Library Structure](https://docs.python-guide.org/writing/structure/)
* [Python Json Library](https://docs.python.org/3/library/json.html)
* [Http Library in python](https://docs.python.org/2/library/httplib.html)
* [Http](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

#### To Contribute

If you think you can make this file better so please make a *pull request* [here](https://www.atlassian.com/git/tutorials/making-a-pull-request)
