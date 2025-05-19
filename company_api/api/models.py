from django.db import models


# Company model
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            choices = (
                                ('IT', 'IT'),
                                ('Finance', 'Finance'),
                                ('E-Commerce', 'E-Commerce')
                            ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    ceo = models.CharField(max_length=100, null=True, blank=True)        # new column

    def __str__(self):
        return self.name + ', ' + self.location


# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, 
                                choices=(
                                    ('Manager', 'MGR'),
                                    ('Software Developer', 'SD'),
                                    ('Project Leader', 'PL')
                                ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)        # company_id = Foreign Key
