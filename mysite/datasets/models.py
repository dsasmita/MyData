from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    def __str__(self):
        return self.name

class Dataset(models.Model):
    category = models.ManyToManyField(Category, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    periode = models.CharField(max_length=256, null=True, blank=True)
    source = models.CharField(max_length=256, null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    total_rows = models.IntegerField(default=0, null=True, blank=True)
    download_count = models.IntegerField(default=0, null=True, blank=True)
    seen_count = models.IntegerField(default=0, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def update_counter_seen(self):
        self.seen_count = self.seen_count + 1
        self.save()

    def update_counter_download(self):
        self.download_count = self.download_count + 1
        self.save()
