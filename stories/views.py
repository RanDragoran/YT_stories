from django.shortcuts import render, get_object_or_404
from .models import CommentStories, Youtube_Entry
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'stories/home.html', {'navBar': 'home'})

def content(request, content_id):
    video = get_object_or_404(Youtube_Entry, pk=content_id)
    vidContent = CommentStories.objects.filter(commentKey=content_id).order_by('-commentDate')
    contentParameters = {'video' : video, 'contents':vidContent}
    return render(request, 'stories/content.html', contentParameters )

def all_stories(request):
    stories = CommentStories.objects.all().order_by('-commentDate')
    video = Youtube_Entry.objects.all()

    paginator = Paginator(stories, 15)
    page = request.GET.get('page')
    stories = paginator.get_page(page)

    storiesParameter = {'videos': video, 'stories': stories, 'navBar':'updates'}

    return render(request, 'stories/stories.html', storiesParameter)

def one_story(request, story_id):
    story = get_object_or_404(CommentStories, pk=story_id)
    count = CommentStories.objects.filter(commentKey=story.commentKey).count()
    oneStory = {'story': story, 'count':count}
    return render(request, 'stories/view_one.html', oneStory)

def archive(request):
    videos = Youtube_Entry.objects.all().order_by('videoTitle')
    stories = CommentStories.objects.all()
    videoCount = videos.count()

    paginator = Paginator(videos, 30)
    page = request.GET.get('page')
    videos = paginator.get_page(page)

    dictionary = {'videos': videos, 'stories': stories, 'navBar':'archive', 'videoCount':videoCount}

    return render(request, 'stories/archive.html', dictionary)
