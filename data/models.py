from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(blank = False, max_length=150)
    email = models.EmailField(blank = False, unique=True)
    password = models.CharField(blank = False, max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(blank = False, max_length=20)
    #list_subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Subject(models.Model):
    user = models.ForeignKey(User)
    # action = models.ForeignKey(Action)
    # transfer = models.ForeignKey(Transfer)
    # binnacle = models.ForeignKey(Binnacle)
    # checkpoint = models.ForeignKey(Checkpoint)

class Action(models.Model):
    description = models.TextField()
    type = models.SmallIntegerField()
    critical = models.CharField(max_length=1)
    num_day = models.IntegerField()
    day_week = models.SmallIntegerField()
    time = models.TimeField(default=timezone.now)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #binnacle = models.ForeignKey(Binnacle)

    def __unicode__(self):
        return "%s - %s" % (self.type, self.description)

class SensorData(models.Model):
    accel_x = models.FloatField()
    accel_y = models.FloatField()
    accel_z = models.FloatField()
    compass = models.FloatField()
    #transfer = models.ForeignKey(Transfer)

    def __unicode__(self):
        return "(%s, %s, %s)" % (self.accel_x, self.accel_y, self.accel_z)

class Transfer(models.Model):
    sensor_data = models.OneToOneField(SensorData, primary_key=True)
    time = models.DateTimeField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    velocity = models.FloatField()
    course = models.FloatField()
    provider = models.TextField()
    time_gps = models.DateTimeField()
    gps = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #type_event = models.ForeignKey(TypeEvent)

    def __str__(self):
        return self.time

    def __unicode__(self):
        return "%s - %s" % (self.time, self.provider)

class Binnacle(models.Model):
    time = models.TimeField(default=timezone.now)
    accomplished = models.TextField()
    key = models.TextField()
    againstkey = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    def __unicode__(self):
        return "%s - %s" % (self.time, self.accomplished)

class Checkpoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    action = models.SmallIntegerField()
    time = models.TimeField()
    num_day = models.IntegerField()
    day_week = models.SmallIntegerField()
    day_month = models.SmallIntegerField()
    num_month = models.SmallIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __unicode__(self):
        return "%s - (%s, %s, %s)" % (self.time, self.x, self.y, self.z)

    def __unicode__(self):
        return self.user






