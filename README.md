# my-django-boilerplate
homegrown starter kit for web projects by using django

Django is an open-source web software based on Python that enable fast creation and deployment of web applications.Its scalable,secure and easy to implement.

- MVC Architectural
- Models to manage data
- Design a universal resource locator
- Combining HTML&Python;Overriding boilerplate/hardcoded code with dynamic data from the database
- Customizing templates
- Static files
- SQLite Database API

ADVANCED FEATURES

- Combining Python & PDF to create statistics files
- Download data from the Internet,PDF format automatically
- Data visualization and Analyzation with python

Why Python and Django
- Python connects with a larger field of scientific computing


Documentation
- easy_install django
- django-admin --version
- pipenv install

- pipenv lock --clear
- pipenv clear

### Create a virtual environment within a project
- pipenv shell
- pipenv install Django===2.2.1

- Change your models (in models.py).
- python manage.py makemigrations [appname] - to create migrations for those changes
- python manage.py migrate - migrate to apply those changes to the database.
- python manage.py createsuperuser


### Admin/Customization
- admin.site.unregister()
- admin.site.site_header = 'New Header'

Class SnippetAdmin(admin.ModelAdmin):
    #specify fields to hide
    exclude = ('title')
    #specify fields to show
    fields = ('title', 'created')
    #
    list_display = ('title','created')
    #
    list_filter = ('created')


### Flow
- Create models
- Register models in Admin