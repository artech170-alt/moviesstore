from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Petition, Vote

@login_required
def index(request):
    petitions = Petition.objects.all().order_by('-created_at')
    template_data = {
        'title': 'Movie Petitions',
        'petitions': petitions
    }
    return render(request, 'petitions/index.html', {'template_data': template_data})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        movie_name = request.POST.get('movie_name')
        
        petition = Petition.objects.create(
            title=title,
            description=description,
            movie_name=movie_name,
            created_by=request.user
        )
        messages.success(request, 'Petition created successfully!')
        return redirect('petitions.index')
    
    template_data = {
        'title': 'Create Petition'
    }
    return render(request, 'petitions/create.html', {'template_data': template_data})

@login_required
def vote(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)
    vote_type = request.POST.get('vote_type')
    
    if vote_type not in ['yes', 'no']:
        messages.error(request, 'Invalid vote type.')
        return redirect('petitions.index')
    
    # Check if user already voted
    existing_vote = Vote.objects.filter(petition=petition, user=request.user).first()
    
    if existing_vote:
        # Update existing vote
        existing_vote.vote_type = vote_type
        existing_vote.save()
        messages.success(request, 'Your vote has been updated!')
    else:
        # Create new vote
        Vote.objects.create(
            petition=petition,
            user=request.user,
            vote_type=vote_type
        )
        messages.success(request, 'Your vote has been recorded!')
    
    return redirect('petitions.index')
