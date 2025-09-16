
#creating models
#step 1 create the models in models.py
#step 2 run python manage.py makemigrations in the terminal
#step 3 run python manage.py migrate in the terminal
#step 4 register the models in the admin.py file in the app folder
#step 5 update or creat function usual requires updating the html file the function in the views.py file
#and updating the urls.py file in the app folderfrom django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name