from os import system,getcwd,environ
from sys import exit
import re

def run_cli_commands(commands):
    for command in commands:
        print(f"\nExecuting command: {command}")
        system(command)
def add_to_tabulate(arr):
    for key,val in arr:
        TABULATE[key] = val

def check_run_permission():
    global RUN_PERMISSION
    if RUN_PERMISSION == 'n':
        RUN_PERMISSION = input("\n would you like to change a value or end the process entirely?[y,n]: ")
        while not RUN_PERMISSION:
            RUN_PERMISSION = input("\nPlease enter 'y' for yes or 'n' for no: ").strip()
        options = [option for option in TABULATE]
        while RUN_PERMISSION == 'y':
            for choice in NAME_CHOICES:
                print(f"\n{NAME_CHOICES[choice]} or {choice}")
            
            value_to_change = input("\nWhich one yould you like to change : ").strip().upper().replace(" ", "_")
            while value_to_change not in options and value_to_change not in NAME_CHOICES:
                value_to_change = input("\nPlease input the a value based on these:\n").strip().upper()
            if value_to_change in NAME_CHOICES:
                value_to_change = NAME_CHOICES[value_to_change]
            new_value = input(f"{value_to_change} = ").strip().replace(" ", "_")
            while not new_value:
                new_value(f"This can't be left blank \n{value_to_change} =  ")
            while True:
                if value_to_change in ["RUNSERVER_PERMISSION","DATABASE_READY"]:
                    new_value = new_value.lower()
                    if new_value not in ['y','n','yes','no']:
                        new_value = input(f"The only values for {value_to_change} is 'y' or 'n'")
                        continue
                    if new_value in ['y','n']:
                        new_value = CHOICES[new_value]
                    break
                if value_to_change == "STYLES_CHOICE":
                    new_value = new_value.lower()
                    if new_value not in ['t','b','c']:
                        new_value = input(f"The only values for {value_to_change} is 't' or 'b' or 'c' ")
                        continue
                    new_value = CHOICES[new_value]
                    break
                break
            TABULATE[value_to_change] = new_value
            print(tabulate(list(TABULATE.items()), tablefmt="grid"))
            RUN_PERMISSION = input("\nWould you like to change another value (y,n): ").strip()
            while not RUN_PERMISSION:
                RUN_PERMISSION = input("\nPlease enter 'y' for yes or 'n' for no: ").strip()
            if RUN_PERMISSION == "y":
                continue

            RUN_PERMISSION = input("\nWould you like to complete the setup with this information provided: ").strip()
            while not RUN_PERMISSION:
                RUN_PERMISSION = input("\nPlease enter 'y' for yes or 'n' for no: ").strip()
            if RUN_PERMISSION == 'y':
                TABULATE["RUNSERVER_PERMISSION"] = CHOICES[TABULATE["RUNSERVER_PERMISSION"]]
                TABULATE["DATABASE_READY"] = CHOICES[TABULATE["DATABASE_READY"]]
                TABULATE["STYLES_CHOICE"] = CHOICES[TABULATE["STYLES_CHOICE"]]
                return
            check_run_permission() 
        print("please look through your information before running")
        exit(1)

if not environ.get('VIRTUAL_ENV'):
    system("python -m venv my_venv")
    print("\nYou are not in a virtual environment. Please activate your virtual environment before running this script.")
    print('\nTo activate your virtual environment, run the following command: \n\nFor CMD: \n             my_venv\\Scripts\\activate\n\nFor BASH: \n             source my_venv/scripts/activate\n')
    print("\nAfter activating your virtual environment, run setup.py again.")
    exit(1)

system("pip install tabulate")
from tabulate import tabulate
CURRENT_DIRECTORY = getcwd()
CURRENT_FOLDER = re.search(r".*[\\|/](.*)",CURRENT_DIRECTORY).group(1)
IMPORTS = {
    'SETTINGS':[
        '\nload_dotenv()',
        '\nfrom dotenv import load_dotenv',
        '\nimport dj_database_url',
        '\nimport os',
        
    ],
}
CHOICES = {
    't':"TAILWIND_CSS",
    'b':"BOOTSTRAP",
    'c':"CSS",
    'y':"yes",
    'n':"no",
    "yes":'y',
    "no":'n',
    "TAILWIND_CSS":'t',
    "BOOTSTRAP":'b',
    "CSS":'c',
}

NAME_CHOICES = {
    'PN':'PROJECT_NAME',
    'AN':'APP_NAME',
    'IF':'INDEX_FUNC',
    'IH':'INDEX_HTML',
    'SC':'STYLES_CHOICE',
    'DN':'DATABASE_NAME',
    'DO':'DATABASE_OWNER',
    'DP':'DATABASE_PASSWORD',
    'CCN':'CLOUDINARY_CLOUD_NAME',
    'CAK':'CLOUDINARY_API_KEY',
    'CAS':'CLOUDINARY_API_SECRET',
    'DR':'DATABASE_READY',
    'RP':'RUNSERVER_PERMISSION',
}
INDEX_FUNC = None
INDEX_HTML = None
STYLES_CHOICE = None
DATABASE_NAME = None
DATABASE_OWNER = None
DATABASE_PASSWORD = None
CLOUDINARY_CLOUD_NAME = None
CLOUDINARY_API_KEY = None
CLOUDINARY_API_SECRET = None
SETTINGS_LINES = None
SECRET_KEY = None
TABULATE = {}

PROJECT_NAME = input(f"\nEnter the name of your Django project (leave blank for '{CURRENT_FOLDER}'): ").replace(" ", "_").lower()
PROJECT_NAME = CURRENT_FOLDER if not PROJECT_NAME else PROJECT_NAME
add_to_tabulate([["PROJECT_NAME",PROJECT_NAME]])
APP_NAME = input("\nEnter the name of your Django app (leave blank for 'my_app'): ").replace(" ", "_").lower()
APP_NAME = "my_app" if not APP_NAME else APP_NAME
add_to_tabulate([["APP_NAME",APP_NAME]])

## permissions
TEMPLATE_PERMISSION ='y'
DATABASE_PERMISSIONS = 'y'

DATABASE_READY = input("\n Is you PostgreSQL database ready to make migrations? (y/n): ").strip().lower()
while DATABASE_READY not in ['y', 'n']:
    DATABASE_READY = input("\nPlease enter 'y' for yes or 'n' for no: ").strip().lower()

CLOUDINARY_PERMISSIONS = input("\nDo you want to set up Cloudinary for media storage? (y/n): ").strip().lower()
while CLOUDINARY_PERMISSIONS not in ['y', 'n']: 
    CLOUDINARY_PERMISSIONS = input("\nPlease enter 'y' for yes or 'n' for no: ").strip().lower()

RUNSERVER_PERMISSION = input("\nDo you want to run the Django development server after setup? (y/n): ").strip().lower()
while RUNSERVER_PERMISSION not in ['y', 'n']:
    RUNSERVER_PERMISSION = input("\nPlease enter 'y' for yes or 'n' for no: ").strip().lower()

add_to_tabulate([["DATABASE_READY",CHOICES[DATABASE_READY]],["RUNSERVER_PERMISSION",CHOICES[RUNSERVER_PERMISSION]]])

# congigurations based on accepted template permissions
if TEMPLATE_PERMISSION == "y":
    INDEX_FUNC = input("\nEnter the name of the index function in views.py (leave blank for 'home'): ").replace(" ", "_").lower()
    INDEX_FUNC = "home" if not INDEX_FUNC else INDEX_FUNC
    INDEX_HTML = input("\nEnter the name of the HTML file for the index view (leave blank for 'index.html'): ").replace(" ", "_").replace(r"\..*", "").lower()
    INDEX_HTML = "index" if not INDEX_HTML else INDEX_HTML
    STYLES_CHOICE = input("\nDo you want to use Tailwind CSS, Bootstrap or CSS? (T/B/C): ").strip().lower()
    while STYLES_CHOICE not in ['t', 'b', 'c']:
        STYLES_CHOICE = input("\nPlease enter 'T' for Tailwind CSS, 'B' for Bootstrap or 'C' for CSS: ").strip().lower()
    add_to_tabulate([["INDEX_FUNC",INDEX_FUNC],["INDEX_HTML",INDEX_HTML],["STYLES_CHOICE",CHOICES[STYLES_CHOICE]]])

# configurations based on accepted dababase permissions
if DATABASE_PERMISSIONS == 'y':
    print("\nConfiguring PostgreSQL database settings...")
    DATABASE_NAME = input("\nEnter the name of your PostgreSQL database: ").strip()
    while not DATABASE_NAME:
        DATABASE_NAME = input("\nDatabase name cannot be empty. Please enter a valid PostgreSQL database name: ").strip()
    DATABASE_OWNER = input("\nEnter your PostgreSQL username: ").strip()
    while not DATABASE_OWNER:
        DATABASE_OWNER = input("\nUsername cannot be empty. Please enter a valid PostgreSQL username: ").strip()
    DATABASE_PASSWORD = input("\nEnter your PostgreSQL password: ").strip()
    while not DATABASE_PASSWORD:
        DATABASE_PASSWORD = input("\nPassword cannot be empty. Please enter a valid PostgreSQL password: ").strip()
    add_to_tabulate([["DATABASE_NAME",DATABASE_NAME],["DATABASE_OWNER",DATABASE_OWNER],["DATABASE_PASSWORD",DATABASE_PASSWORD]])

# congigurations based on accepted cloudinary permissions
if CLOUDINARY_PERMISSIONS == 'y':
    IMPORTS['SETTINGS'].extend([
        "\nimport cloudinary.api",
        "\nimport cloudinary.uploader",
        "\nimport cloudinary",
    ])
    CLOUDINARY_CLOUD_NAME = input("\nEnter your Cloudinary cloud name: ").strip()
    while not CLOUDINARY_CLOUD_NAME:
        CLOUDINARY_CLOUD_NAME = input("\nCloud name cannot be empty. Please enter a valid Cloudinary cloud name: ").strip()
    CLOUDINARY_API_KEY = input("\nEnter your Cloudinary API key: ").strip()
    while not CLOUDINARY_API_KEY:
        CLOUDINARY_API_KEY = input("\nAPI key cannot be empty. Please enter a valid Cloudinary API key: ").strip()
    CLOUDINARY_API_SECRET = input("\nEnter your Cloudinary API secret: ").strip()
    while not CLOUDINARY_API_SECRET:
        CLOUDINARY_API_SECRET = input("\nAPI secret cannot be empty. Please enter a valid Cloudinary API secret: ").strip()
    add_to_tabulate([["CLOUDINARY_CLOUD_NAME",CLOUDINARY_CLOUD_NAME],["CLOUDINARY_API_KEY",CLOUDINARY_API_KEY],["CLOUDINARY_API_SECRET",CLOUDINARY_API_SECRET]])

print(tabulate(list(TABULATE.items()), tablefmt="grid"))
RUN_PERMISSION = input("\nWould you like to complete the setup with this information provided: ").strip()
while not RUN_PERMISSION:
    RUN_PERMISSION = input("\nPlease enter 'y' for yes or 'n' for no: ").strip()
check_run_permission()

INDEX_FUNC = TABULATE['INDEX_FUNC']
INDEX_HTML = TABULATE['INDEX_HTML']
STYLES_CHOICE = TABULATE['STYLES_CHOICE']
DATABASE_NAME = TABULATE['DATABASE_NAME']
DATABASE_OWNER = TABULATE['DATABASE_OWNER']
DATABASE_PASSWORD = TABULATE['DATABASE_PASSWORD']
CLOUDINARY_CLOUD_NAME = TABULATE['CLOUDINARY_CLOUD_NAME']
CLOUDINARY_API_KEY = TABULATE['CLOUDINARY_API_KEY']
CLOUDINARY_API_SECRET = TABULATE['CLOUDINARY_API_SECRET']
DATABASE_READY = TABULATE['DATABASE_READY']
RUNSERVER_PERMISSION = TABULATE['RUNSERVER_PERMISSION']

SETUP_CLI_COMMANDS =[
    'python -m pip install --upgrade pip',
    "pip install django",
    f"\ndjango-admin startproject {PROJECT_NAME}",
    f"ren {PROJECT_NAME} {PROJECT_NAME}_backup",
    f"move {PROJECT_NAME}_backup\\manage.py {CURRENT_DIRECTORY}",
    f"move {PROJECT_NAME}_backup/{PROJECT_NAME} {CURRENT_DIRECTORY}",
    f"rmdir {PROJECT_NAME}_backup",
    f"\npython manage.py startapp {APP_NAME}",
    f"type nul > urls.py",
    f"move urls.py {APP_NAME}",
    "pip install psycopg2",
    "pip install psycopg2-binary",
    "pip install gunicorn",
    "pip install decouple",
    "pip install dj-database-url",
    "pip install djangorestframework",
    "pip install python-dotenv",
    "pip freeze > requirements.txt",
]
TEMPLATE_CLI_COMMANDS = [
    "mkdir templates",
    "mkdir static",
    "type nul > styles.css"
    "type nul > scripts.js",
    "mkdir images",
    "move styles.css static",
    "move scripts.js static",
    "move images static",
    f"move templates {APP_NAME}",
    f"move static {APP_NAME}",
    
]
DATABASE_CLI_COMMANDS = [
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py createsuperuser",
]
CLOUDINARY_CLI_COMMANDS = [
    "pip install cloudinary",
]

GIT_CLI_COMMANDS=[
    "git init",
    "git add .",
]

run_cli_commands(SETUP_CLI_COMMANDS)
if CLOUDINARY_PERMISSIONS == 'y':
    run_cli_commands(CLOUDINARY_CLI_COMMANDS)
# modify settings.py to include the app and database configuration
with open('.gitignore', 'w') as file:
    file.write(f"""
.env
*setup.py
my_venv
               """)
with open(f'{PROJECT_NAME}/settings.py', 'r') as file:
    SETTINGS_LINES = file.readlines()
    found_imports = 0
    found_installed_apps = False
    found_database = False
    
    for i, line in enumerate(SETTINGS_LINES):
        if 'DEBUG =' in line:

            SETTINGS_LINES[i] = "DEBUG = os.getenv('DEBUG')"
            
            continue
        if 'SECRET_KEY =' in line:
            match = re.search(r"'(.*)'", line)
            SECRET_KEY = match.group(1)
            SETTINGS_LINES[i] = "SECRET_KEY = os.getenv('SECRET_KEY')"
            
            continue
        if 'ALLOWED_HOSTS =' in line:
            SETTINGS_LINES[i] = "ALLOWED_HOSTS = os.getenv('ALLOWED_HOST', '127.0.0.1').split(',')"
            continue
        if 'STATIC_URL =' in line:
            SETTINGS_LINES.insert(i+1,"STATICFILES_DIRS = [")
            SETTINGS_LINES.insert(i+2,'BASE_DIR / "my_app" / "static",')
            SETTINGS_LINES.insert(i+3,"]")
        
        if 'INSTALLED_APPS' in line:
            found_installed_apps = True
            continue
        if not found_imports and 'import' in line:
            for setting in IMPORTS['SETTINGS']:
                SETTINGS_LINES.insert(i+1,setting)
            found_imports += 1
            continue
        if  line.strip().startswith('DATABASES = {') and DATABASE_PERMISSIONS == 'y':
            found_database = True
            continue
        

        if found_installed_apps and line.strip() == ']':
            SETTINGS_LINES.insert(i, f"    '{APP_NAME}',\n")
            if CLOUDINARY_PERMISSIONS == 'y':
                SETTINGS_LINES.insert(i+1, "    'cloudinary',\n")
            found_installed_apps = False
        if found_database:
            SETTINGS_LINES[i] = ""
            if '}' in line:
                SETTINGS_LINES.insert(i,f"""
    'default': dj_database_url.config(
""")
                SETTINGS_LINES.insert(i+1,f"""
        default=os.getenv('DATABASE_URL'),
""")
                SETTINGS_LINES.insert(i+2,f"""
        conn_max_age=600,
""")
                SETTINGS_LINES.insert(i+3,f"""
    )
""")
                found_database = False
                continue

with open(f'{PROJECT_NAME}/settings.py', 'w') as file:
    file.writelines(SETTINGS_LINES)
if CLOUDINARY_PERMISSIONS == "y":
    with open(f'{PROJECT_NAME}/settings.py', 'a') as file:



            file.write("""
cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET'),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    """)
    

with open(f"{APP_NAME}/views.py", "w") as views_file:
        views_file.write(f"""
from django.shortcuts import render,redirect
from django.http import HttpResponse
                         """)
if DATABASE_PERMISSIONS == 'y':

    with open(f".env" , 'w') as env_file:
        env_file.write(f"""
    DATABASE_URL = "postgresql://{DATABASE_OWNER}:{DATABASE_PASSWORD}@localhost:5432/{DATABASE_NAME}"
    SECRET_KEY = "{SECRET_KEY}"
    """)
        if CLOUDINARY_PERMISSIONS == 'y':
            env_file.write(f"""
    CLOUDINARY_CLOUD_NAME = "{CLOUDINARY_CLOUD_NAME}"
    CLOUDINARY_API_KEY = "{CLOUDINARY_API_KEY}"
    CLOUDINARY_API_SECRET = "{CLOUDINARY_API_SECRET}"
    """)
        env_file.write(f"""
    ALLOWED_HOSTS = localhost, 127.0.0.1
    DEBUG = True
    """)
if TEMPLATE_PERMISSION == 'y':

    run_cli_commands(TEMPLATE_CLI_COMMANDS)



    with open(f"{APP_NAME}/views.py", "a") as views_file:
        views_file.write(f"""
def {INDEX_FUNC}(request):
    return render(request, '{INDEX_HTML}.html')
                        """)

    with open(f"{APP_NAME}/urls.py", "w") as urls_file:
        urls_file.write(f"""
from django.urls import path
from .views import *
urlpatterns = [
    path('', {INDEX_FUNC}, name='{INDEX_FUNC}'),
]
                        """)
        
    with open(f"{PROJECT_NAME}/urls.py", "w") as project_urls_file:
        project_urls_file.write(f"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{APP_NAME}.urls')), 
    path('', include('django.contrib.auth.urls')),
]
                                """)
        
   
    with open(f"{APP_NAME}/templates/layout.html", "w") as index_template:
        index_template.write("""{% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>{%block title%}{%endblock%}</title>\n""")
        if STYLES_CHOICE == 't':
            index_template.write("""
                <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
                                """)
        elif STYLES_CHOICE == 'b':
            index_template.write("""
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                                """)
        else:
            index_template.write("""
            <link rel="stylesheet" href="{% static 'styles.css' %}">
                                """)
            
        index_template.write("""
</head>
    <body>
        {% block content %}{% endblock %}
        <script src="{% static 'scripts.js' %}"></script>
                            """)
        if STYLES_CHOICE == 'b':
            index_template.write(f"""
        {'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q" crossorigin="anonymous"></script>' if STYLES_CHOICE == 'b' else ''}
                            """)
        index_template.write(f"""
    </body>
</html>    
                            """)
    with open(f"{APP_NAME}/templates/{INDEX_HTML}.html", "w") as index_template:
        index_template.write("""
{% extends 'layout.html' %}
{% block title %}
""")
        index_template.write(f"""
                             {APP_NAME}
""")
        index_template.write("""
{% endblock %}
{% block content %}
""")
        index_template.write(f"""
<h1>Welcome to {APP_NAME}!</h1>
""")
        index_template.write("""
{% endblock %}
""")
if DATABASE_PERMISSIONS == 'y':

    with open(f"{APP_NAME}/models.py", "w") as models_file:
        models_file.write(f"""
from django.db import models

# Create your models here.
class {DATABASE_NAME.title()}(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        pass
        """)
    with open(f"{APP_NAME}/admin.py", "w") as admin_file:
        admin_file.write(f"""
from django.contrib import admin
from .models import {DATABASE_NAME.title()}

# Register your models here.
admin.site.register({DATABASE_NAME.title()})
        """)
    with open(f"{APP_NAME}/forms.py", "w") as forms_file:
        forms_file.write(f"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class SignInForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
                         """)
    
if DATABASE_READY in ['y',"yes"]:
        run_cli_commands(DATABASE_CLI_COMMANDS)

    
else:
    print(DATABASE_READY)
    print("\nDatabase setup skipped. You can run migrations later using 'python manage.py makemigrations' and 'python manage.py migrate'.")


run_cli_commands(GIT_CLI_COMMANDS)



if RUNSERVER_PERMISSION == 'y':
    print("\nRunning the Django development server...")
    system("python manage.py runserver")
else:
    print("\nDjango development server not started. You can start it later using 'python manage.py runserver'.")
    print("\nSetup completed successfully!")
    print("\nYou can now start building your Django application!")