from django.db import models
import json


class Videos(models.Model):
    # list_videos = models.JSONField(json.JSONEncoder, json.JSONDecoder)
    list_videos = models.CharField(max_length=2, default='FRESHMAN')
