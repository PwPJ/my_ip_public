# My Public IP

My Public IP is a Python program that provides you with the possibility of getting your public IP address.

## Prerequisites

Install setuptools befor run setup.py

```bash
pip3 install setuptools
```

## Installation

you can refer to makefile and use bellow commands for install and clean project :

### Install

```bash
python3 setup.py install
```

### Clean

```bash
rm -rf my_ip_public.egg-info dist build my_ip_public/__pycache__ my_ip_public/providers/__pycache__/
```

## Usage

```python
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgements

Whenever you need to use this program, just import it.

```bash
import my_ip_public
```

## License

[Creativecommons](https://creativecommons.org/licenses/by/2.0/)
