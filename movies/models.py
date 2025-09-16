#creating models
#step 1 create the models in models.py
#step 2 run python manage.py makemigrations in the terminal
#step 3 run python manage.py migrate in the terminal
#step 4 register the models in the admin.py file in the app folder
#step 5 update or creat function usual requires updating the html file the function in the views.py file
#and updating the urls.py file in the app folder
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    stock = models.IntegerField(default=0)  # Add this line

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name