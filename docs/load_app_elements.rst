Load Application Elements into Skeleton
=======================================

The below are quick steps to load submodules and set up the environment for local
usage of the iron skillet cnc app.

Prequisites
-----------

    + clone the skeleton branch

    + active python virtual enviroment (recommended)

Values Used in this Example
---------------------------

    + repo name: ironskillet-cnc

    + repo branch: 81dev

    + pan-cnc submodule directory: cnc

    + Panorama IP address: 192.168.55.7

    + application server port: 9999

Add and prep the pan-cnc submodule
----------------------------------

Start in the repo project root directory


::

    git submodule add -b develop git@github.com:PaloAltoNetworks/pan-cnc.git ./cnc
    cd cnc
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('vistoq', 'admin@example.com', 'vistoq')" (create user account)
    export = PANORAMA_IP=192.168.55.7
    export = PANORAMA_USERNAME=admin
    export = PANORAMA_PASSWORD=admin


Load the iron-skillet submodule
-------------------------------

::

    cd ../src/iron-skillet/snippets
    git submodule add -b 81dev git@github.com:PaloAltoNetworks/iron-skillet.git ./skillet81


Run the app
-----------

::

    cd ../cnc
    ./manage.py runserver 9999



