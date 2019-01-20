from django.db import models

class EField(models.Field):
	def __init__(self, val, *args, **kwargs):
		self.val = val

		super().__init__(*args, **kwargs)
		# kwargs['val'] = self.val

	def db_type(self, connection):
		return 'ENUM(%s)' % self.val

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		kwargs['val'] = self.val
		return name, path, args, kwargs
    
class receiveCalls(models.Model):
	test_bet = EField(val = "hi,wor", default='hi')
