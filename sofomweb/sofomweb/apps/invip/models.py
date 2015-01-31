from django.db import models

# Create your models here.
class inv(models.Model):

	name 			= models.CharField(max_length=300) 
	ip				= models.CharField(max_length=20)
	puerto			= models.CharField(max_length=10)
	nameuser		= models.CharField(max_length=100)
	passworduser	= models.CharField(max_length=100) 
	os 				= models.CharField(max_length=100) 
	antivirus 		= models.CharField(max_length=200)
	back 			= models.CharField(max_length=500)
	comment			= models.TextField(max_length=500)
	status			= models.BooleanField(default=True)	


	def __unicode__(self): 
		nameservers = "%s %s" % (self.name,self.ip)
		return nameservers
			