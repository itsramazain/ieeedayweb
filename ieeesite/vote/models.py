from django.db import models

# Create your models here.
class Poll(models.Model):
    question=models.TextField()
    option_one=models.CharField(max_length=200)
    option_two=models.CharField(max_length=200)
    option_three=models.CharField(max_length=200)
    option_four=models.CharField(max_length=200)
    option_five=models.CharField(max_length=200)
    option_six=models.CharField(max_length=200)
    option_two_count=models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    option_five_count=models.IntegerField(default=0)
    option_six_count=models.IntegerField(default=0)
    option_one_count=models.IntegerField(default=0)
    def total(self):
        return self.option_one_count+self.option_two_count+self.option_three_count+self.option_four_count+self.option_five_count+self.option_six_count
