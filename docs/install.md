# Installing and Running Iron Skillet CNC


The easiest way to run the mssp application is to pull the docker container:

    docker run -p 8888:80 scotchoaf/ironskillet_cnc_v80 (or v81)

**Note**: The intial release of ironskillet cnc is PAN-OS version specific

Then access the UI via http://localhost:8888

The default username and password is: `skillet` and `skillet`

**Note**: The example uses port 8888 to run and access the application. Modify to an open port as needed


Building PanHandler
-------------------

If you want to build ironskillet_cnc from source (which is not recommended). You will need to update the git submodules,
install the pip python requirements for both the app and also CNC, create the local db, and create a local user.


    git submodule init
    git submodule update
    pip install -r requirements.txt
    pip install -r cnc/requirements.txt
    ./cnc/manage.py migrate
    ./cnc/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('skillet', 'admin@example.com', 'skillet')"