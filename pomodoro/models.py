from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name='activity name')
    due_date = models.DateField(verbose_name='activity due date')
    estimated_pomos = models.IntegerField()
    pomos_completed = models.IntegerField()
    seconds_completed = models.IntegerField(verbose_name='seconds completed current pomodoro')
    status = models.IntegerField(verbose_name='activity status')
    priority = models.IntegerField(verbose_name='activity priority')

    def __unicode__(self):
        return self.name
