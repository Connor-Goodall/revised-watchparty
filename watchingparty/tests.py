from django.test import TestCase
from .models import Profile, Meeting, Event
from datetime import datetime
from django.db.models import Q
# Create your tests here.
class watchpartyTest(TestCase):
    def test_site_one(self):
        test = "This is a Test"
        self.assertEqual(test, "This is a Test")

#creates a profile object based on parameters.
def createProfile(interest,firstmovie,secondmovie,thirdmovie,fourthmovie,fifthmovie,firstshow,secondshow,thirdshow,fourthshow,fifthshow,username):
    return Profile.objects.create(interests = interest,firstFavoriteMovie=firstmovie,secondFavoriteMovie=secondmovie,thirdFavoriteMovie=thirdmovie,fourthFavoriteMovie=fourthmovie,fifthFavoriteMovie=fifthmovie,firstFavoriteTVShow=firstshow,secondFavoriteTVShow=secondshow,thirdFavoriteTVShow=thirdshow,fourthFavoriteTVShow=fourthshow,fifthFavoriteTVShow=fifthshow,userName=username)

class ProfileTest(TestCase):
    def test_profile_interest(self):
        profile = createProfile(interest="Im interested in cars.",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profileInterest = Profile.objects.filter(interests="Im interested in cars.")
        self.assertQuerysetEqual(profileInterest, [profile])

    def test_profile_firstmovie(self):
        profile = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilefirstmovie = Profile.objects.filter(firstFavoriteMovie="Cars")
        self.assertQuerysetEqual(profilefirstmovie, [profile])

    def test_profile_secondmovie(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="Cars",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilesecondmovie = Profile.objects.filter(secondFavoriteMovie="Cars")
        self.assertQuerysetEqual(profilesecondmovie, [profile])

    def test_profile_thirdmovie(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "Cars",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilethirdmovie = Profile.objects.filter(thirdFavoriteMovie="Cars")
        self.assertQuerysetEqual(profilethirdmovie, [profile])

    def test_profile_fourthmovie(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="Cars",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilefourthmovie = Profile.objects.filter(fourthFavoriteMovie="Cars")
        self.assertQuerysetEqual(profilefourthmovie, [profile])

    def test_profile_fifthmovie(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="Cars",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilefifthmovie = Profile.objects.filter(fifthFavoriteMovie="Cars")
        self.assertQuerysetEqual(profilefifthmovie, [profile])

    def test_profile_firstshow(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="Cars",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilefirstshow = Profile.objects.filter(firstFavoriteTVShow="Cars")
        self.assertQuerysetEqual(profilefirstshow, [profile])

    def test_profile_secondshow(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="Cars",thirdshow="",
                                fourthshow="",fifthshow="",username="")
        profilesecondshow = Profile.objects.filter(secondFavoriteTVShow="Cars")
        self.assertQuerysetEqual(profilesecondshow, [profile])

    def test_profile_thirdshow(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="Cars",
                                fourthshow="",fifthshow="",username="")
        profilethirdshow = Profile.objects.filter(thirdFavoriteTVShow="Cars")
        self.assertQuerysetEqual(profilethirdshow, [profile])

    def test_profile_fourthshow(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="Cars",fifthshow="",username="")
        profilefourthshow = Profile.objects.filter(fourthFavoriteTVShow="Cars")
        self.assertQuerysetEqual(profilefourthshow, [profile])

    def test_profile_fifthshow(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="Cars",username="")
        profilefifthshow = Profile.objects.filter(fifthFavoriteTVShow="Cars")
        self.assertQuerysetEqual(profilefifthshow, [profile])

    def test_profile_username(self):
        profile = createProfile(interest="",firstmovie="",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="John Doe")
        profileUserName = Profile.objects.filter(userName="John Doe")
        self.assertQuerysetEqual(profileUserName, [profile])

    def test_profile_username2(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        profile2 = createProfile(interest="", firstmovie="Cars", secondmovie="",
                                 thirdmovie="", fourthmovie="", fifthmovie="",
                                 firstshow="", secondshow="", thirdshow="",
                                 fourthshow="", fifthshow="", username="John Doe")

        profile1person = Profile.objects.filter(firstFavoriteMovie="Cars", userName="Jane Smith")
        profile2person = Profile.objects.filter(firstFavoriteMovie="Cars", userName="John Doe")
        self.assertFalse(profile1person == profile2person)

def createMeeting(link, password, username, movieTitle):
    return Meeting.objects.create(link=link, password=password, username=username,movieTitle=movieTitle)

class ZoomTest(TestCase):
    def test_one_movie_with_one_user(self):
        meeting = createMeeting(link="default", password="default", username="cag3dmr", movieTitle="The Batman")
        zoomMeeting = Meeting.objects.all()
        self.assertQuerysetEqual(zoomMeeting, [meeting])
    def test_one_movie_with_two_users(self):
        meeting1 = createMeeting(link="default", password="default", username="cag3dmr", movieTitle="The Batman")
        meeting2 = createMeeting(link="default", password="default", username="burningshock83", movieTitle="The Batman")
        zoomMeeting1 = Meeting.objects.filter(username="cag3dmr")
        zoomMeeting2 = Meeting.objects.filter(username="burningshock83")
        self.assertFalse(zoomMeeting1 == zoomMeeting2)
    def test_two_movies_with_one_user(self):
        meeting1 = createMeeting(link="default", password="default", username="cag3dmr", movieTitle="The Batman")
        meeting2 = createMeeting(link="default", password="default", username="cag3dmr", movieTitle="Finding Nemo")
        zoomMeeting1 = Meeting.objects.filter(movieTitle="The Batman")
        zoomMeeting2 = Meeting.objects.filter(movieTitle="Finding Nemo")
        self.assertFalse(zoomMeeting1 == zoomMeeting2)
    def test_two_movies_with_two_users(self):
        meeting1 = createMeeting(link="default", password="default", username="cag3dmr", movieTitle="The Batman")
        meeting2 = createMeeting(link="default", password="default", username="burningshock83", movieTitle="Finding Nemo")
        zoomMeeting1 = Meeting.objects.filter(username="cag3dmr", movieTitle="The Batman")
        zoomMeeting2 = Meeting.objects.filter(username="burningshock83", movieTitle="Finding Nemo")
        self.assertFalse(zoomMeeting1 == zoomMeeting2)

def createMovie(creator, title, description, date, platform):
    return Event.objects.create(creator=creator, mediaTitle=title, description=description, eventDate=date, platform=platform)

class MovieEventTest(TestCase):
    def test_arbitrary_movie(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        batMovie = Event.objects.all()
        self.assertQuerysetEqual(batMovie, [movie])

    def test_two_movie_with_one_users(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        movie2 = createMovie(creator=profile1, title="Madagascar", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        self.assertFalse([movie2] == [movie])

    def test_one_movie_with_two_users(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        profile2 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jack Briles")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        movie2 = createMovie(creator=profile2, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        self.assertFalse([movie2] == [movie])

    def test_two_movies_with_two_user(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        profile2 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jack Briles")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        movie2 = createMovie(creator=profile2, title="Madagascar", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        self.assertFalse([movie2] == [movie])


class AttendeeTest(TestCase):
    def test_one_attendee(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        profile2 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Doc Brown")
        Event.objects.get(creator=profile1, mediaTitle="The Batman", description="A good movie.", eventDate="2020-08-23 03:23:02", platform="movieStock.jpeg").participant.add(profile2)
        test = Event.objects.get(creator=profile1, mediaTitle="The Batman", description="A good movie.", eventDate="2020-08-23 03:23:02", platform="movieStock.jpeg").participant.all()
        self.assertQuerysetEqual(test, [profile2])

    def test_multiple_attendees(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        profile2 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Doc Brown")
        profile3 = createProfile(interest="",firstmovie="Cars",secondmovie="example",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Junior")
        profile4 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="example",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Alexander")
        
        Event.objects.get(creator=profile1, mediaTitle="The Batman", description="A good movie.", eventDate="2020-08-23 03:23:02", platform="movieStock.jpeg").participant.add(profile2, profile3, profile4)
        test = Event.objects.get(creator=profile1, mediaTitle="The Batman", description="A good movie.", eventDate="2020-08-23 03:23:02", platform="movieStock.jpeg").participant.all().order_by('userName')
        self.assertQuerysetEqual(test, [profile4, profile2, profile3])

    def test_no_attendees(self):
        profile1 = createProfile(interest="",firstmovie="Cars",secondmovie="",
                                thirdmovie = "",fourthmovie="",fifthmovie="",
                                firstshow="",secondshow="",thirdshow="",
                                fourthshow="",fifthshow="",username="Jane Smith")
        movie = createMovie(creator=profile1, title="The Batman", description="A good movie.", date="2020-08-23 03:23:02", platform="movieStock.jpeg")
        test = Event.objects.get(creator=profile1, mediaTitle="The Batman", description="A good movie.", eventDate="2020-08-23 03:23:02", platform="movieStock.jpeg").participant.all()
        self.assertQuerysetEqual(test, [])
class SearchTest(TestCase):
    def test_search(self):
        profile = createProfile(interest="", firstmovie="", secondmovie="",
                                thirdmovie="", fourthmovie="", fifthmovie="",
                                firstshow="", secondshow="", thirdshow="",
                                fourthshow="", fifthshow="", username="John Doe")
        cars = Event.objects.create(mediaTitle="Cars 2", username="", creator=profile, eventDate=datetime.now(),
                                    platform="default", address="default", city="default", description="test")
        #cats = Event.objects.create(mediaTitle="Cats", username="", creator=profile, eventDate=datetime.now(),
        #                            platform="default", address="default", city="default", description="test")

        self.assertQuerysetEqual(Event.objects.filter(mediaTitle__icontains="Ca"), [cars])

    def test_search_empty(self):
        profile = createProfile(interest="", firstmovie="", secondmovie="",
                                thirdmovie="", fourthmovie="", fifthmovie="",
                                firstshow="", secondshow="", thirdshow="",
                                fourthshow="", fifthshow="", username="John Doe")
        cars = Event.objects.create(mediaTitle="Cars 2", username="", creator=profile, eventDate=datetime.now(),
                                    platform="default", address="default", city="default", description="test")
        #cats = Event.objects.create(mediaTitle="Cats", username="", creator=profile, eventDate=datetime.now(),
        #                            platform="default", address="default", city="default", description="test")

        self.assertQuerysetEqual(Event.objects.filter(mediaTitle__icontains=""), [cars])

    def test_search_no_match(self):
        profile = createProfile(interest="", firstmovie="", secondmovie="",
                                thirdmovie="", fourthmovie="", fifthmovie="",
                                firstshow="", secondshow="", thirdshow="",
                                fourthshow="", fifthshow="", username="John Doe")
        cars = Event.objects.create(mediaTitle="Cars 2", username="", creator=profile, eventDate=datetime.now(),
                                    platform="default", address="default", city="default", description="test")
        #cats = Event.objects.create(mediaTitle="Cats", username="", creator=profile, eventDate=datetime.now(),
        #                            platform="default", address="default", city="default", description="test")

        self.assertQuerysetEqual(Event.objects.filter(mediaTitle__icontains="Cat"), [])

    def test_search_username(self):
        profile = createProfile(interest="", firstmovie="", secondmovie="",
                                thirdmovie="", fourthmovie="", fifthmovie="",
                                firstshow="", secondshow="", thirdshow="",
                                fourthshow="", fifthshow="", username="John Doe")
        cars = Event.objects.create(mediaTitle="Cars 2", username="nexus", creator=profile, eventDate=datetime.now(),
                                    platform="default", address="default", city="default", description="test")
        #cats = Event.objects.create(mediaTitle="Cats", username="", creator=profile, eventDate=datetime.now(),
        #                            platform="default", address="default", city="default", description="test")

        self.assertQuerysetEqual(Event.objects.filter(username__icontains="ne"), [cars])
    
