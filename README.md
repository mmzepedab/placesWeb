# placesWeb with Django Framework and Google Appengine Infrasctructure

Using Django project [Django](https://www.djangoproject.com/)
with Google App Engine Flexible Environment. It uses the
[Writing your first Django app](https://docs.djangoproject.com/en/1.9/intro/tutorial01/) as the 
example app to deploy.


# Template
This uses the django App Engine Standard enviroment as a template[Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.

# App Engine instance
Google Cloud SQL instance: polls-instance

#command to run on linode server environment using uwsgi
uwsgi --http :8080 --home /home/django/Env/places/ --chdir /home/django/placesWeb/ --module mysite.wsgi

#Kill process running with uwsgi
kill `pidof uwsgi`

#Activate  Virtual enviroment inside project
source ./bin/activate

#Deactivate
deactivate

#All dependencies should be installed on Env virtual environment
#Dependencies needed so far

pip install --upgrade django-crispy-forms
pip install djangorestframework
pip install markdown
pip install django-filter
pip install MySQL-python



