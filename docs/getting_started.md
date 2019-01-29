# Iron-Skillet CNC Quick Start

The steps below are used to set up the cnc environment and step through
basic config template options.

More details about template contents can be found at:

[Iron Skillet Template Docs](https://iron-skillet.readthedocs.io)


# Activating the CNC Environment

* Click on the lock image (upper right corner)

* Enter the master passphrase

**NOTE:** when the system prompts for the passphrase initially and no passphrase
has been created, it will use that value to create the passphrase. This
passphrase is unique to the local system.

* If an existing environment, choose ```Load``` to activate

### Creating a New Environment

* Choose an existing Environment and select ```Clone```

* Enter a name and description

* Edit values by adding the existing Key name and associcated Value

* Submit and new the updated secrets list for the Key value

* When all values updated, you can ```Load``` as an active enviroment


### Viewing the Environments

* Click on the username (upper right of window)

* Select ```Environments```

* Configure or Load as required


# Loading a Configuration

* Activate the CNC environment to define which device is used for configuration

* Choose the menu option

    - Panorama xml API options

        * v8.0 or v8.1 software version

        * complete or device-group and template stack only

        * shared or non-shared device-group elements

    - Panorama SET commands without API interactions

    - Firewall/PAN-OS options by software version

    - Firewall SET commands without API interactions


* Enter form values and step through the config panels

* Submit of the environment API config device will initiate an API config push

