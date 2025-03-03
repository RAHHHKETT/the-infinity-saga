from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import render


class Image(models.Model):
    key = models.CharField(max_length=100, help_text="The public id of the uploaded file")
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100, help_text='The original name of the uploaded image')
    created_at = models.DateTimeField(auto_now_add=True)
    
def upload_media(request):
    return render(request, 'upload_media.html')

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(max_length=200, blank=True, null=True)
    image_link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title} - {self.stars} stars"
