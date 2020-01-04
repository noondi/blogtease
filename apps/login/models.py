from __future__ import unicode_literals

from django.db import models

import bcrypt

import re

class UserManager(models.Manager):
	# function to create the user, two parameters self and user posted data
	def creator(self, postData): 
		user = self.create(
		first_name = postData['first_name'],
		last_name = postData['last_name'],
		email = postData['email'],
		password = bcrypt.hashpw(            # Hashing passwd with bcrypt
			postData['password'].encode(),   
			bcrypt.gensalt()),               # Salting passwd with bcrypt
		)
		return user # optional return

	# function to validate user posted data, two parameters self and user posted data
	def validate(self, postData):
		# print postData # Check if Data is reaching
		results = { 
			'status': True,
			'errors':[]
		}
		#first name validations
		if len(postData['first_name']) < 3:
			results['errors'].append('last name must not be less than 3 characters!!!!')
			results['status'] = False
		#last name validations
		if len(postData['last_name']) < 3:
			results['errors'].append('last name must not be less than 3 characters!!')
			results['status'] = False

		# email validations        
		if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
			results['errors'].append('Your email is invalid!!')
			results['status'] = False

		# password validations
		if len(postData['password']) < 3:
			results['errors'].append('Your password not less than 3 characters!!!!')
			results['status'] = False
		# password match validations    
		if postData['password'] != postData['confpw']:
			results['errors'].append('Your passwords do not match!!')
			results['status'] = False
		# user non-existing validations  
		if len(self.filter(email = postData['email'])) > 0:
			results['errors'].append('The user already exists')  
			results['status'] = False  
		return results

		# function to create a logging-in user, two parameters self and user posted data
	def loginValidator(self, postData):
		# print 'Testing login function ************************'
		results = {'status': True,'errors': [], 'user': None}
		users = self.filter(email = postData['email']) # check if email exists in db
		if len(users) < 1: # if user not in db
			results['status'] = False
		else: # otherwise encrypt this pw with bcrypt
			if bcrypt.checkpw(
				postData['password'].encode(), 
				users[0].password.encode()
				):
				results['user'] = users[0] # compare with database user pwd hash
			else:
				results['status'] = False # if no match 
		return results

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	objects = UserManager()


