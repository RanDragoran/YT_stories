from django.db import models
from embed_video.fields import EmbedVideoField

class Youtube_Entry(models.Model):
    youtubeVideo = EmbedVideoField(unique=True)
    videoTitle = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return self.videoTitle

class CommentStories(models.Model):
    commentUser = models.CharField(max_length=100, blank=False)
    commentContent = models.TextField(blank=False)
    commentDate = models.DateTimeField()
    commentChannel = models.URLField(null=True)
    commentKey = models.ForeignKey(Youtube_Entry, on_delete=models.CASCADE, related_name='stories')

    def __str__(self):
        return str(self.commentKey) + ' ' + self.commentUser
