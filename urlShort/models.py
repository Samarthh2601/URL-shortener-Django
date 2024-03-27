from django.db import models
import string
import random

class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url
    
    def generate_shortened_url(self, original_url: str) -> str:
        check_original = Url.objects.filter(long_url=original_url)
        if check_original.exists():
            short_url = check_original.first().short_url
            new_object = False
        else:
            characters = string.ascii_letters + string.digits
            short_url = ''.join(random.choices(characters, k=7))
            check = Url.objects.filter(short_url=short_url)
            if check.exists():
                return self.generate_shortened_url()
            new_object = True
        self.short_url = short_url
        return (short_url, new_object,)