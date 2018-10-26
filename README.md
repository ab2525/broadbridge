# broadbridge

Broadbridge is a Python3 Flask app designed to make integrating a Broadlink RM2 (or other?) device with IFTTT or any service that can call webhooks.

It provides a framework for defining new commands and the IR or RF codes to send when those commands are called, as well as allowing scenes (chains of multiple commands).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Broadbridge relies on the following python modules. It is recommended to install them via `pip` or your distribution's package manager.

```
flask
broadlink

```

### Installing


Copy the example `scenes.py` and `commands.py` files to their normal place.

```
$ cp scenes.py.example scenes.py
$ cp commands.py.example commands.py
```

Gather your IR codes. The easiest way to do this is from the python shell. There is an example below. The result will be a command packet that you can copy and paste into the commands dictionary, following the formatting from the example ones.

```
>>> import broadlink
>>> device = broadlink.discover(timeout=3)[0]
>>> device.auth()
True
>>> device.enter_learning()
>>> ;;; BEAM IR AT RECEIVER ;;;
>>> device.check_data()
```

Once you have your IR codes in `commands.py`, you can edit `scenes.py` to make chains of commands callable with one URL. (Switch TV input, turn off multiple lights, etc)

Finally, run the server with `run.sh`.


## Deployment

As with all Flask apps, running the development server in production is not recommended - however, due to the low request volume and size these typically receive, it is probably not the end of the world.

Regardless, a proper "production" deployment would be to use one of the standalone WSGI containers for Flask described [here](http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/)

## Built With

* [Flask](http://flask.pocoo.org) - Python web application framework
* [python-broadlink](https://github.com/mjg59/python-broadlink) - Used for discovery and communication with broadlink devices


## Authors

* **Alex Buie** - *Initial work* - [ab2525](https://github.com/ab2525)

See also the list of [contributors](https://github.com/ab2525/broadbridge/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

