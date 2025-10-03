from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    movie_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Petition for {self.movie_name}"
    
    @property
    def yes_votes(self):
        return self.vote_set.filter(vote_type='yes').count()
    
    @property
    def no_votes(self):
        return self.vote_set.filter(vote_type='no').count()

class Vote(models.Model):
    VOTE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=3, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('petition', 'user')  # One vote per user per petition
    
    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.petition.movie_name}"
