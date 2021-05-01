from django.db import models


# Create your models here.
class onlineuser(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);


class dataset(models.Model):
	v1=models.CharField(max_length=10);
	v2=models.CharField(max_length=10);
	v3=models.CharField(max_length=10);
	v4=models.CharField(max_length=10);
	v5=models.CharField(max_length=10);
	v6=models.CharField(max_length=10);
	v7=models.CharField(max_length=10);
	v8=models.CharField(max_length=10);
	v9=models.CharField(max_length=10);
	v10=models.CharField(max_length=10);
	v11=models.CharField(max_length=10);
	v12=models.CharField(max_length=10);
	v13=models.CharField(max_length=10);
	v14=models.CharField(max_length=10);
	v15=models.CharField(max_length=10);
	v16=models.CharField(max_length=10);
	v17=models.CharField(max_length=10);
	res=models.CharField(max_length=10);


class graph(models.Model):
	naive=models.FloatField(max_length=1000)
	nn=models.FloatField(max_length=1000)
	

