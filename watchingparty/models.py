from django.db import models


class Profile(models.Model):
    interests = models.TextField(
        default="This is a default interest. Please edit this in the profile settings if you want"
                " people to see your interests.")
    userName = models.CharField(max_length=200, default="")
    firstFavoriteMovie = models.CharField(max_length=200, default="")
    secondFavoriteMovie = models.CharField(max_length=200, default="")
    thirdFavoriteMovie = models.CharField(max_length=200, default="")
    fourthFavoriteMovie = models.CharField(max_length=200, default="")
    fifthFavoriteMovie = models.CharField(max_length=200, default="")
    firstFavoriteTVShow = models.CharField(max_length=200, default="")
    secondFavoriteTVShow = models.CharField(max_length=200, default="")
    thirdFavoriteTVShow = models.CharField(max_length=200, default="")
    fourthFavoriteTVShow = models.CharField(max_length=200, default="")
    fifthFavoriteTVShow = models.CharField(max_length=200, default="")
    reviews = models.TextField(default="This is a default review.")

    def __str__(self):
        return self.firstFavoriteMovie


class Meeting(models.Model):
    link = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=20, default="")
    movieTitle = models.CharField(max_length=200, default="")


class Event(models.Model):
    DEFAULT_PROFILE_ID = 1
    mediaTitle = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    # if the creator of an event deletes their account, don't delete the event
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='creator_profile',
                                default=DEFAULT_PROFILE_ID)
    eventDate = models.DateTimeField('date published')
    platform = models.CharField(max_length=200)  # for image files
    address = models.CharField(max_length=200, default="375 Merchant Walk Sq")
    city = models.CharField(max_length=200, default="Charlottesville")
    # has attributes year, month, day, hour, minute, second, tzinfo
    description = models.CharField(max_length=200)
    # an event can have multiple participants
    participant = models.ManyToManyField(Profile)

    def __str__(self):
        return self.mediaTitle + " with " + self.username
