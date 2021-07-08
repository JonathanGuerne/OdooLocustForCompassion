# OdooLocust for compassion CH

this code uses locust to stress test a running "compassion odoo" instance trough Http and RPC

## Dependencies

This repo relies on OdooLocust by Odoo

## Installation

Make sure to run this code in its own virtual environment. Some of the dependencies shared by locust and odoo don't use the same 
version and thus could not be run in the same environment

```bash
>>> pip install -r requirements.txt
```
## configuration

Even before launching locust you should specify the session's configuration. The recommended way to do so is to use a `locust.conf` file. You'll find an example of such file in the repo. 

You can configure locust with any of the parameters mentionned in [its documentation](https://docs.locust.io/en/stable/configuration.html). 

A couple of custom parameters have been added via this repo. You should always pay attention to specify them otherwise locust won't be able to connect to Odoo. 

| Added custom parameters        | Description           |
| ------------- |:-------------:|
| login| login of the user you want to use to connect to odoo |
| password      | password of the above mentionned user      |
| database | specify on which database you want to execute your query      |

## Launching a stress test session

To start locust simply run the following command :

``` 
locust -f locust.py
```

This will setup the test process but not yet start it. After only a few seconds you should see a link in the command line to open the web interface. 

```bash 
[...] Starting web interface at http://0.0.0.0:8089
```

Once connected to the web interface you'll have the ability to start testing. 




