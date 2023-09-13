from django.db import models
from django.utils import timezone
from accounts.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    caption = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Account, blank=True, related_name='likes')
    slikes = models.ManyToManyField(Account, blank=True, related_name='slikes')
    

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(Account, blank=True, related_name='comment_likes')
    slikes = models.ManyToManyField(Account, blank=True, related_name='comment_slikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')


   
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on')

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False



class Profile(models.Model):
    user = models.OneToOneField(Account, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null= True)
    dob = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures',  default='uploads/profile_pictures/default.jpeg', blank=True)
    followers = models.ManyToManyField(Account, blank=True, related_name='followers')

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=Account)
    def creat_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

        