from django.contrib import admin
<<<<<<< HEAD
from .models import Tweet, TweetLike
# Register your models here.

class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content','user__username', 'user__email']
    class Meta:
        model = Tweet
=======
>>>>>>> parent of 67de47e... user added

# Register your models here.
