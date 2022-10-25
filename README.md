It is my private sample Django project with JSON, based on https://absolutecodeworks.com/python-django-crud-sample-with-json-data 
 
This application allows you to create a database of cars and perform simple data operations

In this READEME.md you will find each step to crete such project. Lets begin:



In repository: 

1. Create virtual environment 

2. pip install cx_Oracle

3. pip install django

4. pip freeze ( check if everything is ok)



5. CREATE PROJECT + APP 
    5.1 django-admin startproject  <project name> np:  CarSalesProject .  "." dot is important if you dont want to create a subfolder with the same name and thus not change the structure during publication

        5.1.1. python manage.py runserver (check if everything is ok)

    5.2 python manage.py startapp  <project name> np:   CarSales

    5.3  Include app to our project  > For this, in settings.py, add our new app CarSales (case sensitive) to INSTALLED_APPS list as below. 



6 Loading First HTML Page
    6.1 < CarSales folder > Html files should be placed within a folder named templates. Create this folder in our CarSales app. 

    6.2  < CarSales folder > Add a new html file carslist.html, inside templates folder. 

    6.3 < CarSales  and CarSalesProject folder > We should have 2 urls.py, one inside project folder and one inside app folder. If not available, create these files. urls.py in project folder adds a reference to the app urls.py.

    6.4 < CarSales folder > In app (CarSales) urls.py we define the urlpatterns for this module.

    6.5 < CarSalesProject folder > In project (CarSalesProject) urls.py - 
        +  add "include" to import 
        +  add path('', include('CarSales.urls')), to urlpatterns               ## urls.py in project folder adds a reference to the app urls.py.

    6.6 < CarSales folder > In views.py we define the htmls to render for each route. 

7. Setting up data 
7.1 Create a folder named json-data inside CarSales app and place a file carslist.json in this folder. 
7.2. Add data to JSON manually

 [
    {"id":"1", "name":"Toyota Camry", "year":"2018", "price":"2000"},
    {"id":"2", "name":"Honda Civic", "year":"2019", "price":"2200"},
    {"id":"3", "name":"Chevrolet Silverado", "year":"2017", "price":"1800"},
    {"id":"4", "name":"Ford F-150", "year":"2020", "price":"2500"},
    {"id":"5", "name":"Nissan Altima", "year":"2021", "price":"3000"}
]

8 List 
8.1 carslist.html is going to hold the list of cars available for sale. To list the items, add below code in the body of html. Here, we using a for loop to bind the data to a table.

CRUD

9 Create
9,1 Add a new url pattern for addcar in the app urls.py. 
9,2 Add new html file addcar.html in templates folder and place new code.
9,3 Html uses forms. To handle forms in Django we need a form class. Add an new file forms.py in the CarSales app folder and include the form details.
9,4 Then add new code in view.py as the second function below carslist function. 
9,5 Also import the form class and redirect in view.py


