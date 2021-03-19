from django.db import models
from accounts.models import UserProfile
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class PublicPoll(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True) 
    time_duration = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.now)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        strtime = "".join(str(timezone.now).split("."))
        string = "%s-%s" % (strtime[7:], self.title)
        self.slug = slugify(string)
        super(PublicPoll, self).save()

    def __str__(self):
        return self.title


class PrivatePoll(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)  
    password = models.CharField(max_length=20, unique=True)
    time_duration = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.now)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        strtime = "".join(str(timezone.now).split("."))
        string = "%s-%s" % (strtime[7:], self.title)
        self.slug = slugify(string)
        super(PrivatePoll, self).save()

    def __str__(self):
        return self.title


class PublicPollOption(models.Model):
    option = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    publicpoll = models.ForeignKey(PublicPoll, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        strtime = "".join(str(timezone.now).split("."))
        string = "%s-%s" % (strtime[7:], self.publicpoll.title)
        self.slug = slugify(string)
        super(PublicPollOption, self).save()

    def __str__(self):
        return self.publicpoll.title


class PublicPollResult(models.Model):
    permission = models.BooleanField(default=True)
    publicpoll_option = models.ForeignKey(PublicPollOption, on_delete=models.CASCADE)
    publicpoll = models.ForeignKey(PublicPoll, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.publicpoll.title


class PrivatePollOption(models.Model):
    option = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    privatepoll = models.ForeignKey(PrivatePoll, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        strtime = "".join(str(timezone.now).split("."))
        string = "%s-%s" % (strtime[7:], self.privatepoll.title)
        self.slug = slugify(string)
        super(PrivatePollOption, self).save()

    def __str__(self):
        return self.privatepoll.title


class PrivatePollResult(models.Model):
    permission = models.BooleanField(default=True)
    privatepoll_option = models.ForeignKey(PrivatePollOption, on_delete=models.CASCADE)
    privatepoll = models.ForeignKey(PrivatePoll, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.privatepoll.title
