https://www.django-rest-framework.org/#quickstart <br>
https://www.geeksforgeeks.org/django-rest-framework-adding-additional-field-to-modelserializer/
<br><br>
Create a project folder <code>company_api</code>                                                                                                                                   <br>
Go into it through a terminal either using <code>cmd</code> , <code>powershell</code>, <code>gitbash</code> or any <code>code editior</code>                                       <br>
<code>py --version</code> &nbsp;&nbsp;--------------------------------------------&nbsp;&nbsp; to see the python version                                                               <br>
<code>py</code> &nbsp;&nbsp;--------------------------------------------------------&nbsp;&nbsp; to start a python terminal. If you want to exit, use <code>exit()</code>              <br>
<code>pip install --upgrade pip</code> &nbsp;&nbsp;-----------------------------&nbsp;&nbsp; to upgrade **pip**                                                                        <br>
<code>pip list</code> &nbsp;&nbsp;-------------------------------------------------&nbsp;&nbsp; to show all the packages we already have in the global scope of the system             <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; to show all the packages we already have in the global scope of the system             <br>
<code>py -m venv env</code> &nbsp;&nbsp;------------------------------------------&nbsp;&nbsp; to create an **environment** to keep only necessary packages required for the project <br>
<code>./env/Scripts/activate</code> &nbsp;&nbsp;---------------------------------&nbsp;&nbsp; to activate the virtual environment in **Windows**  <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; nothing in the virtual environement as of now <br>
<code>pip install django</code>  &nbsp;&nbsp;--------------------------------------&nbsp;&nbsp;  to install Django <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; to check what all dependencies got installed alomng with Django <br>
<code>django-admin startproject company_drf_api</code> &nbsp;&nbsp;-----------&nbsp;&nbsp; use **dot** to create the files at the **root folder**   <br>
<code>py manage.py runserver</code> &nbsp; <code>py ./manage.py runserver</code> &nbsp;&nbsp;-&nbsp;&nbsp; <code>http://127.0.0.1:8000/</code>  &nbsp;&nbsp;or&nbsp;&nbsp;  <code>http://localhost:8000/</code>

<br>

> create a file called <code>company_api/company_drf_api/views.py</code>
> <pre>
> from django.http import HttpResponse
>
> def home_page(request):
>	  print("home page requested")
>	  return HttpResponse("This is homepage")           # return HttpResponse("This is homepage")
> </pre>

<br>

> <code>company_api/company_drf_api/urls.py</code>
> <pre>
> from .views import home_page
> 
> urlpatterns = [
>	  path('home', home_page)
> ]
> </pre>

<br>

>
> Now open the home page of the app &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; <code>http://localhost:8000/home/</code>
>

<br>

> To install Django REST Framework
> <pre>
> pip install djangorestframework                                 
> </pre>

<br>

> <code>company_api/company_drf_api/settings.py</code>
> <pre>
> INSTALLED_APPS = [
>	  ...,
>	  'rest_framework',
> ]
> </pre>

<br>

> To create a REST API called <code>api</code>
> <pre>
> py manage.py startapp api
> </pre>
> It will not create a separate <code>settings.py</code> file. Rather it will consider the already created <code>settings.py</code> file in the <code>company_drf_api</code> folder.
																
<br>

> <code>company_api/api/model.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **model** called <code>Company</code>
> <pre>
> from django.db import models
>
> # Company model
> class Company(models.Model):
>      id = models.IntegerField(primary_key=True)
>      name = models.CharField(max_length=50)
>      location = models.CharField(max_length=50)
>      about = models.TextField()
>      type = models.CharField(max_length=100,
>                              choices = (
>                                ('IT', 'IT'),
>                                ('Finance', 'Finance'),
>                                ('E-Commerce', 'E-Commerce')
>                              ))
>      added_date = models.DateTimeField(auto_now=True)
>      active = models.BooleanField(default=True)
>      ceo = models.CharField(max_length=100, null=True, blank=True
</pre>

<br>

> <code>company_api/api/serializers.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Company Serializer** <code>CompanySerializer()</code>
> <pre>
> from rest_framework import serializers
> from api.models import Company
>
> # Company serializer
> class CompanySerializer(serializers.HyperlinkedModelSerializer):
>    class Meta:
>	     model = Company
>	     fields = "__all__
> </pre>																	 

<br>

> <code>company_api/api/views.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Company view**  called <code>CompanyViewSet()</code>
> <pre>
> from django.shortcuts import render
> from rest_framework import viewsets
> from api.models import Company
> from api.serializers import CompanySerializer
>
> # Company view
> class CompanyViewSet(viewsets.ModelViewSet):
>     queryset = Company.objects.all()
>     serializer_class = CompanySerializer
> </pre>

<br>

> <code>company_api/api/urls.py</code> 
> <pre>
> from django.contrib import admin
> from django.urls import path, include
> from api.views import CompanyViewSet
> from rest_framework import routers
>
> router = routers.DefaultRouter()
> router.register(r'companies', CompanyViewSet)
>
> urlpatterns = [
>	  path('', include(router.urls))
> ]
</pre>

<br>

> <code>company_api/company_drf_api/settings.py</code> 
> <pre>
> INSTALLED_APPS = [
>	  ...,
>	  'api'
> ]
> </pre>																	

<br>

> <code>company_api/company_drf_api/urls.py</code>
> <pre>
> from django.urls import include	
> url_patterns = [
>	  ...,
>	  path("api/v1/",include('api.urls'))
> ]
</pre>

<br>

> <code>py ./manage.py makemigrations</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; to make migrations for models <br>
> <code>py ./manage.py migrate</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; to migrate

<br>

> <code>py ./manage.py runserver</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; http://localhost:8000/api/v1/ &nbsp;&nbsp;&nbsp;&nbsp;&&nbsp;&nbsp;&nbsp;&nbsp;           http://localhost:8000/api/v1/companies/

<br>

> ∎ &nbsp;Now create a couple of companies &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; http://localhost:8000/api/v1/companies/ <br>
> ∎ &nbsp;Also check if tables created are being reflected in the DB browser for **SQLite** <br>
> ∎ &nbsp;Install **Postman** app and play with it.

<br>

> <code>company_api/api/serializers.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; to expose the <code>id</code> of the companies in the JSON output, just add the following line :
> <pre>
> class CompanySerializer(serializers.HyperlinkedModelSerializer):
>     id = serializers.ReadOnlyField()
> </pre>

<br>																	

⭐ &nbsp;**Migrations**
> > How to add a new column <code>ceo</code> to an already existing model <code>Company</code> ?
> >
> > <code>company_api/api/models.py</code>
> > <pre>
> > class Company(models.Model):
> >	    ceo = models.CharField(max_length=100, null=True, blank=True)              # new column
> > </pre>
> >
> > <code>py manage.py makemigrations</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp; <code>py manage.py makemigrations --name <migration_file_name></code> <br>
> > <pre>
> > class Migration(migrations.Migration):
> >    operations = [
> >        migrations.AddField(
> >		    model_name='company',
> >		    name='ceo',
> >		    field=models.CharField(blank=True, max_length=100, null=True),
> >        ),
> >    ]
> > </pre>
> > <code>py manage.py migrate</code>
>
> <br>
>
> > To delete a model let say <code>Company</code> : 
> > - First comment out the <code>Company()</code> model code in the <code>company_api/api/models.py</code> file
> > - Then create a migration file using <code>py manage.py makemigrations</code> <br>
> You can use <code>py manage.py makemigrations --empty</code> in case you didn't comment out the code regarding <code>Company()</code> **model**
> > - And finally in the migration file, just do the following :
> > <pre>
> > class Migration(migrations.Migration):
> >    operations = [
> >        migrations.DeleteModel(
> >            name='Company',
> >        ),
> >    ]
> > </pre>
>
> <br>
>
> > **Note &nbsp;:** <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∎ &nbsp; In case you want to delete the models and re-run the migrations : <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py migrate api --fake</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py migrate api --fake-initial</code>  <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now add all the records from the begining. <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; However it's important to backup data before we drop a column or a table.
> >
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∎ &nbsp; To generate an empty migration &nbsp;&nbsp;&nbsp;&nbsp; ➜ &nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py makemigrations api --empty</code>
> >
> > To show all migrations &nbsp;&nbsp;&nbsp;&nbsp; ➜ &nbsp;&nbsp;&nbsp;&nbsp; <code>py ./manage.py showmigrations</code>

<br>

---

**Optional Implementation** &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp; add a new column <code>company_id</code> to the <code>Company</code> model, and <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;copy the primary key <code>id</code> to it such that it becomes <code>Bharat_{id}</code>

<br>

> <code>company_api/api/models.py</code>
> <pre>
> class Company(models.Model):
>      company_id = models.CharField(max_length=100, null=True, blank=True)              # new column
> </pre>

<br>

> <code>py manage.py makemigrations --name add_company_id_to_company_model_and_populate_it</code> <br>

<br>

> Open the migration file created &nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;&nbsp; <code>company_api/api/XXXX_add_company_id_to_company_model_and_populate_it.py</code> <br>
>
> <pre>
> from django.db import migrations
>
> def copy_ids(apps, schema_editor):
>      Company = apps.get_model('api', 'Company')
>      for company in Company.objects.all():
>           company.company_id = "Bharat_" + company.id               # copy id to company_id
>           company.save()
>
> class Migration(migrations.Migration):
>    operations = [
>        migrations.AddField(
>		    model_name='company',
>		    name='company_id',
>		    field=models.CharField(blank=True, max_length=100, null=True),
>        ),
>        migrations.RunPython(copy_ids)
>    ]
> </pre>

<br>

> <code>py manage.py migrate</code>

---

<br>

Now what if we want to correct the spelling mistake of a column "compnay_id" in the Company TABLE?
	STEP-1: Copy all the data from the field "compnay_id
	STEP-2: Create a new migration to add a new column called "company_id"
	STEP-3. Remove the column "compnay_id" by making a new migration
	
	
company_api/api/model.py                                         ----------> add a new field in the Company model like the follwoing :
										                                     company_id = models.IntegerField(null=True)

py manage.py makemigrations
py manage.py migrate

py manage.py makemigrations api --empty                          ----------> python manage.py makemigrations your_app_name --empty        # to generate an empty migration

python manage.py makemigrations --name add_user_profile          ----------> to give a name to a migration file

																			
py ./manage.py showmigrations                                    ----------> to show all migrations


UPDATE django_migrations
SET name = '0001_create_company_model'
WHERE app = 'api' AND name = '0001_initial';


py ./manage.py shell                                              ---------> to open Django ORM

from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("""
        UPDATE django_migrations
        SET name = '0001_create_company_model'
        WHERE app = 'api' AND name = '0001_initial';
    """)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PRAGMA table_info('api_company');

SELECT sql 
FROM sqlite_master 
WHERE type = 'table' AND name = 'api_company';


Views are of 2 types :
	1) Function based view
	2) Class based view

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To add an additional field to ModelSerializer without adding it in the Model :

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    summary = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = ["url", "id", "name", "location", "about", "type", "added_date", "active", "summary"]
    def get_summary(self, obj):         
        return f"{obj.name} is a {obj.location} based {obj.type} company"
		
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

How to add a column to a model in Django Rest Framework ?

class Company(models.Model):
	ceo = models.CharField(max_length=100, null=True, blank=True)        # new column

py manage.py makemigrations

py manage.py migrate                           --->  I am getting the error while trying to add "ceo" column to the company model :

django.db.utils.OperationalError: table "api_company" already exists     ------     likely because the migration history and actual database schema are out of sync
                                                                                    This happens because :
																					    - You deleted migration files manually.
																					    - You dropped or recreated the database table outside of Django.
																					    - You’re starting fresh but the migration state is corrupted.

py manage.py migrate api --fake-initial         # it will delete the model along with it's migrations             <py manage.py migrate api --fake>

Now add all the records from the begining

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

How to create a Custom URL ? 

http://localhost:8000/api/v1/companies/      has all the APIs for companies
http://localhost:8000/api/v1/employees/      has all the APIs for employees

http://localhost:8000/api/v1/companies/{company_id}/employees       -      how to get all employees of a particular company?

http://localhost:8000/api/v1/companies/1/employees                  -      Page not found (404)

api/views.py    ------>     from rest_framework.decorators import action
							from rest_framework.response import Response
						
							@action(detail=True, methods=['get'])
							def employees(self, request, pk=None):
								# print('get employess of company ', pk)           			# to check if the method is called by http://localhost:8000/api/v1/companies/1/employees
								company = Company.objects.get(pk=pk)
								emps = Employee.objects.filter(company=company)
								emps_serializer = EmployeeSerializer(emps, many=True, context={'request' : request})
								return Response(emps_serializer.data)
								
http://localhost:8000/api/v1/companies/1/employees/   ----->   now works for company 1 because it exists
http://localhost:8000/api/v1/companies/2/employees/   ----->   now works for company 2 because it exists
http://localhost:8000/api/v1/companies/3/employees/   ----->   now works for company 3 because it exists
http://localhost:8000/api/v1/companies/4/employees/   ----->   does not work for company 4 because it may not exist

So put it in Try-Exception block like below:

							def employees(self, request, pk=None):
								try:
									company = Company.objects.get(pk=pk)
									emps = Employee.objects.filter(company=company)
									emps_serializer = EmployeeSerializer(emps, many=True, context={'request' : request})
									return Response(emps_serializer.data)
								except Exception as e:
									print(e)
									return Response({
										'message' : 'Company might not exist !! ERROR'
									})
								
http://localhost:8000/api/v1/companies/4/employees/   ----->   now works and does not throw error for company 4 even when it does not exist
http://localhost:8000/api/v1/companies/5/employees/   ----->   now works even there is no company with id = 5


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now if you want to allow only the READ operation on the browser so that the CREATE, UPDATE & DELETE operations can only be done through Application backend, you will have to disable the permissions accordingly for unauthenticated user like the foolowing :

company_api/company_drf_api/settings.py       ----->     

															REST_FRAMEWORK = {
																# Use Django's standard `django.contrib.auth` permissions,
																# or allow read-only access for unauthenticated users.
																'DEFAULT_PERMISSION_CLASSES': [
																	'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
																]
															}


Now go to both the root urls and you will see there is no form to create a record:
															{
																"companies": "http://localhost:8000/api/v1/companies/",
																"employees": "http://localhost:8000/api/v1/employees/"
															}
												
												
Now let's try to create, delete or update a company or an employee through Postman and see what happens :

POST  ==>  http://localhost:8000/api/v1/companies/      =======>  ERROR - 403 Forbidden : Authentication credentials were not provided.
{
    "name": "Bharat LLM",
    "location": "Hyderabad",
    "about": "It is an AI company working on India's own indegenious large language model.",
    "type": "IT",
    "active": true,
    "ceo": "Bechan Mishra"
}

Similarly try to delete or update a companyor an employee, you will get the same 403 Forbidden Error.

Now similarly to disable even the browsable API i.e, to disable even the read (GET) operation on browser, you need to pass JSONRenderer to your Default_Renderer_Classes like the following :

															REST_FRAMEWORK = {
																'DEFAULT_RENDERER_CLASSES': [
																	'rest_framework.renderers.JSONRenderer'
																]
															}
															

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now let's handle the things as admin :

For that we need to first register our models at 	-----   api/admin.py

															from api.models import Company, Employee
															admin.site.register(Company)
															admin.site.register(Employee)


http://localhost:8000/admin/    --------    http://localhost:8000/admin/login/?next=/admin/

python manage.py createsuperuser


To delete a user :       Open the ORM using the command     ----    <python manage.py shell>

																	user = User.objects.get(username='admin')
																	user.delete()


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To customize the Django Admin :                             api/admin.py
						
															class CompanyAdmin(admin.ModelAdmin):
																list_display = ('name', 'location', 'type', 'active')
																    search_fields = ('name',)
															
															class EmployeeAdmin(admin.ModelAdmin):
																list_display = ('name', 'email', 'company', 'position')
																search_fields = ('name', 'email',)       #  search_fields = ('name', 'email', 'company',) will throw foreign key error
																list_filter = ('company',)               #  to filter employees based on company filter
																
																

															admin.site.register(Company, CompanyAdmin)
															admin.site.register(Employee, EmployeeAdmin)
															
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

