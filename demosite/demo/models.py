from django.db import models
from django import forms


# Create your models here.

class Adult(models.Model):
    Adultid = models.AutoField(auto_created=True, primary_key=True)
    age = models.FloatField(blank=True, default=None, null=True)
    workclass = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    hours_per_week = models.FloatField(blank=True, default=None, null=True)
    income = models.FloatField(blank=True, default=None, null=True)

    class Meta:
        db_table = "adult"


class AdultCFk_3(models.Model):
    Adultid = models.AutoField(auto_created=True, primary_key=True)
    age = models.FloatField(blank=True, default=None, null=True)
    workclass = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    hours_per_week = models.FloatField(blank=True, default=None, null=True)
    income = models.FloatField(blank=True, default=None, null=True)

    class Meta:
        db_table = 'adultcfk_3'


class AdultCFk_4(models.Model):
    Adultid = models.AutoField(auto_created=True, primary_key=True)
    age = models.FloatField(blank=True, default=None, null=True)
    workclass = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    hours_per_week = models.FloatField(blank=True, default=None, null=True)
    income = models.FloatField(blank=True, default=None, null=True)

    class Meta:
        db_table = 'adultcfk_4'


class AdultCFk_5(models.Model):
    Adultid = models.AutoField(auto_created=True, primary_key=True)
    age = models.FloatField(blank=True, default=None, null=True)
    workclass = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    hours_per_week = models.FloatField(blank=True, default=None, null=True)
    income = models.FloatField(blank=True, default=None, null=True)

    class Meta:
        db_table = 'adultcfk_5'


class LIMEexp(models.Model):
    Adultid = models.AutoField(auto_created=True, primary_key=True)
    age = models.FloatField(blank=True, default=None, null=True)
    workclass = models.FloatField(blank=True, default=None, null=True)
    education = models.FloatField(blank=True, default=None, null=True)
    marital_status = models.FloatField(blank=True, default=None, null=True)
    occupation = models.FloatField(blank=True, default=None, null=True)
    race = models.FloatField(blank=True, default=None, null=True)
    gender = models.FloatField(blank=True, default=None, null=True)
    hours_per_week = models.FloatField(blank=True, default=None, null=True)


class Rates(models.Model):
    options = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, ''),
    )
    rate_choice1 = models.PositiveSmallIntegerField(choices=options)
    rate_choice2 = models.PositiveSmallIntegerField(choices=options)
    rate_choice3 = models.PositiveSmallIntegerField(choices=options)
    rate_choice4 = models.PositiveSmallIntegerField(choices=options)
    rate_choice5 = models.PositiveSmallIntegerField(choices=options)


class Comments(models.Model):
    comments = models.CharField(max_length=1000, blank=True, null=True)
