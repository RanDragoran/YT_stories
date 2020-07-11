from django.shortcuts import render, get_object_or_404
from .models import CommentStories, Youtube_Entry

# Create your views here.
def home(request):
    return render(request, 'stories/home.html')

def content(request, content_id):
    video = get_object_or_404(Youtube_Entry, pk=content_id)
    vidContent = CommentStories.objects.filter(commentKey=content_id).order_by('-commentDate')
    contentParameters = {'video' : video, 'contents':vidContent}
    return render(request, 'stories/content.html', contentParameters )

def all_stories(request):
    stories = CommentStories.objects.all().order_by('-commentDate')
    video = Youtube_Entry.objects.all()
    storiesParameter = {'videos': video, 'stories': stories}
    return render(request, 'stories/stories.html', storiesParameter)