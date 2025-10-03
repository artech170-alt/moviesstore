from django.contrib import admin
from .models import Petition, Vote

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'title', 'created_by', 'created_at', 'yes_votes', 'no_votes']
    list_filter = ['created_at']
    search_fields = ['movie_name', 'title']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['petition', 'user', 'vote_type', 'created_at']
    list_filter = ['vote_type', 'created_at']
#User story: As a user, I'd like to post a "include movie petition" (on a separate page) in the movie store so that all users can vote on whether they want to see the admin add a certain movie to the catalog.

#Completion steps: 

#1. Log in or register an account.

#2. Navigate to the Petition's page (or whatever you have named this separate page).

#3. Create a new petition. 

#4. Log out and log in/register into a second account.

#5. Access the Petition's page and vote affirmatively on the previously made petition.

#6. Log in/register into another account and verify that the petition affirmative vote was recorded --> the 'yes' count increased.