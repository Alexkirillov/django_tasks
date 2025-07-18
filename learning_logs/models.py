from django.db import models

# Create your models here.
class Topic(models.Model):
    """a topic the user is talking about"""
    text = models.CharField(max_length = 200)
    data_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """something specific learned about a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= "entries"

    def __str__(self):
        """return a simple string representing the entry"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"