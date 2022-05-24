# Cars-REST-App

Cars-REST-App is one of the projects that I created during my education in the Python Web Framework (Django) course (March 2022) using Django REST. The app contains the following models: accounts, CarBrand, UserCar, and CarModels . Each user is extended by default Django abstract class and contains a few more columns. Each car object contains relations to the user and CarBrand. Each CarModel contains relation to CarBrand. All models are built with soft delete.

The default Django user class is extended and in addition there are some custom fields. There is login, and register functionality.
