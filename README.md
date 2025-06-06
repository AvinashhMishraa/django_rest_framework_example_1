https://www.django-rest-framework.org/#quickstart <br>
https://www.geeksforgeeks.org/django-rest-framework-adding-additional-field-to-modelserializer/
<br><br>
First you need to install Python. <br>
After installation, you can cheeck where Python is installed by executing <code>where python</code> command in your **command prompt**.
<br><br>
Create a project folder <code>company_api</code>  <br>
Go into it through a terminal either using <code>cmd</code> , <code>powershell</code>, <code>gitbash</code> or any <code>code editior</code>  <br>
<code>py --version</code> &nbsp;&nbsp;--------------------------------------------&nbsp;&nbsp; to see the python version  <br>
<code>py</code> &nbsp;&nbsp;--------------------------------------------------------&nbsp;&nbsp; to start a python terminal. If you want to exit, use <code>exit()</code>  <br>
<code>cls</code> &nbsp;&nbsp;-------------------------------------------------------&nbsp;&nbsp; to clear the terminal  <br>
<code>pip install --upgrade pip</code> &nbsp;&nbsp;-----------------------------&nbsp;&nbsp; <code>python.exe -m pip install --upgrade pip</code> &nbsp;&nbsp;➜&nbsp;&nbsp; to upgrade **pip**  <br>
<code>pip list</code> &nbsp;&nbsp;-------------------------------------------------&nbsp;&nbsp; to show all the packages we already have in the global scope of the system   <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; to show all the packages we already have in the global scope of the system   <br>
<code>py -m venv env</code> &nbsp;&nbsp;------------------------------------------&nbsp;&nbsp; to create an **environment** to keep only necessary packages required for the project  <br>
<code>./env/Scripts/activate</code> &nbsp;&nbsp;---------------------------------&nbsp;&nbsp; to activate the virtual environment in **Windows** <br>
<code>deactivate</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; to deactivate the virtual environment  <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; nothing in the virtual environement as of now  <br>
<code>pip install django</code>  &nbsp;&nbsp;--------------------------------------&nbsp;&nbsp;  to install Django  <br>
<code>pip freeze</code> &nbsp;&nbsp;-----------------------------------------------&nbsp;&nbsp; to check what all dependencies got installed alomng with Django  <br>
<code>django-admin startproject company_drf_api .</code> &nbsp;&nbsp;---------&nbsp;&nbsp; use **dot** in the end to create files at the **root folder**   <br>
<code>py manage.py runserver</code> &nbsp; <code>py ./manage.py runserver</code> &nbsp;&nbsp;-&nbsp;&nbsp; <code>http://127.0.0.1:8000/</code>  &nbsp;&nbsp;or&nbsp;&nbsp;  <code>http://localhost:8000/</code>

<br>

> create a file called <code>company_api/company_drf_api/views.py</code>
> ```
> from django.http import HttpResponse
>
> def home_page(request):
>	  print("home page requested")
>	  return HttpResponse("This is homepage") 		# return HttpResponse("This is homepage")
> ```

<br>

> <code>company_api/company_drf_api/urls.py</code>
> ```
> from .views import home_page
> 
> urlpatterns = [
>	  path('home', home_page)
> ]
> ```

<br>

>
> Now open the home page of the app &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; http://localhost:8000/home/
>

<br>

In **Django**, we render a **HTML template** through a function to feed the data in a context. <br>
Whereas in **Django Rest Framework**, we directly dump data into a **JSON response** as an **API** for the frontend to consume.

<br>

> To install Django REST Framework
> ```
> pip install djangorestframework                                 
> ```

<br>

> <code>company_api/company_drf_api/settings.py</code>
> ```
> INSTALLED_APPS = [
>	  ...,
>	  'rest_framework',
> ]
> ```

<br>

> To create a **REST API** called "api"
> ```
> py manage.py startapp api
> ```
> It will not create a separate <code>settings.py</code> file. Rather it will consider the already created <code>settings.py</code> file in the <code>company_drf_api</code> folder.
																
<br>

> <code>company_api/api/model.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **model** called <code>Company</code>
> ```
> from django.db import models
>
> # Company model
> class Company(models.Model):
>    id = models.IntegerField(primary_key=True)
>    name = models.CharField(max_length=50)
>    location = models.CharField(max_length=50)
>    about = models.TextField()
>    type = models.CharField(max_length=100,
>                            choices = (
>                                ('IT', 'IT'),
>                                ('Finance', 'Finance'),
>                                ('E-Commerce', 'E-Commerce')
>                           )
>                  )
>    added_date = models.DateTimeField(auto_now=True)
>    active = models.BooleanField(default=True)
>    ceo = models.CharField(max_length=100, null=True, blank=True
> ```

<br>

> <code>company_api/api/serializers.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Company Serializer** <code>CompanySerializer()</code>
> ```
> from rest_framework import serializers
> from api.models import Company
>
> # Company serializer
> class CompanySerializer(serializers.HyperlinkedModelSerializer):
>    class Meta:
>        model = Company
>        fields = "__all__"
> ```																 

<br>

> <code>company_api/api/views.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Company view**  called <code>CompanyViewSet()</code>
> ```
> from django.shortcuts import render
> from rest_framework import viewsets
> from api.models import Company
> from api.serializers import CompanySerializer
>
> # Company view
> class CompanyViewSet(viewsets.ModelViewSet):
>    queryset = Company.objects.all()
>    serializer_class = CompanySerializer
> ```

<br>

> <code>company_api/api/urls.py</code> 
> ```
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
> ```

<br>

> <code>company_api/company_drf_api/settings.py</code> 
> ```
> INSTALLED_APPS = [
>	  ...,
>	  'api'
> ]
> ```																

<br>

> <code>company_api/company_drf_api/urls.py</code>
> ```
> from django.urls import include	
> url_patterns = [
>	  ...,
>	  path("api/v1/",include('api.urls'))
> ]
> ```

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
> ```
> class CompanySerializer(serializers.HyperlinkedModelSerializer):
>    id = serializers.ReadOnlyField()
> ```

<br>

> To see a **table structure** & it's **definition**, use the following query in the DB browser for **SQLite** :
>
> ```
> PRAGMA table_info('api_company');
> ```
>
> ```
> SELECT sql 
> FROM sqlite_master 
> WHERE type = 'table' AND name = 'api_company';
> ```

<br>														

> ⭐ &nbsp;**Migrations**
> > How to add a new column <code>ceo</code> to an already existing model <code>Company</code> ?
> >
> > <code>company_api/api/models.py</code>
> > ```
> > class Company(models.Model):
> >	    ceo = models.CharField(max_length=100, null=True, blank=True) 		# new column
> > ```
> >
> > <code>py manage.py makemigrations</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp; <code>py manage.py makemigrations --name <migration_file_name></code> <br>
> > ```
> > class Migration(migrations.Migration):
> >    operations = [
> >        migrations.AddField(
> >            model_name='company',
> >            name='ceo',
> >            field=models.CharField(blank=True, max_length=100, null=True),
> >        ),
> >    ]
> > ```
> > <code>py manage.py migrate</code>
>
> <br>
>
> > To delete a model let say <code>Company</code> : 
> > - First comment out the <code>Company()</code> model code in the <code>company_api/api/models.py</code> file
> > - Then create a migration file using <code>py manage.py makemigrations</code> <br>
> You can use <code>py manage.py makemigrations --empty</code> in case you didn't comment out the code regarding <code>Company()</code> **model**
> > - And finally in the migration file, just do the following :
> > ```
> > class Migration(migrations.Migration):
> >    operations = [
> >        migrations.DeleteModel(
> >            name='Company',
> >        ),
> >    ]
> > ```
>
> <br>
>
> > **Note &nbsp;:** <br>
> >
> > ∎ &nbsp; In case you want to delete the models and re-run the migrations : <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py migrate api --fake</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py migrate api --fake-initial</code>  <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now add all the records from the begining. <br>
> > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; However it's important to backup data before we drop a column or a table.
> >
> > ∎ &nbsp; To generate an empty migration &nbsp;&nbsp;&nbsp;&nbsp; ➜ &nbsp;&nbsp;&nbsp;&nbsp; <code>py manage.py makemigrations api --empty</code>
> >
> > ∎ &nbsp; To show all migrations &nbsp;&nbsp;&nbsp;&nbsp; ➜ &nbsp;&nbsp;&nbsp;&nbsp; <code>py ./manage.py showmigrations</code>
> > 
> > ∎ &nbsp; To open Django ORM &nbsp;&nbsp;&nbsp;&nbsp; ➜ &nbsp;&nbsp;&nbsp;&nbsp; <code>py ./manage.py shell</code>
> >
> > ∎ &nbsp; To update the migration file name on DB Browser for SQLite :
> > ```
> > UPDATE django_migrations
> > SET name = 'new_name'
> > WHERE app = 'api' AND name = 'old_name';
> > ```

<br>

---

**Optional Implementation** &nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp; add a new column <code>company_id</code> to the <code>Company</code> model, and <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;copy the primary key <code>id</code> to it such that it becomes <code>Bharat_{id}</code>

<br>

> <code>company_api/api/models.py</code>
> ```
> class Company(models.Model):
>    company_id = models.CharField(max_length=100, null=True, blank=True) 		# new column
> ```

<br>

> <code>py manage.py makemigrations --name add_company_id_to_company_model_and_populate_it</code> <br>

<br>

> Open the migration file created &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; <code>company_api/api/XXXX_add_company_id_to_company_model_and_populate_it.py</code> <br>
>
> ```
> from django.db import migrations
>
> def copy_ids(apps, schema_editor):
>    Company = apps.get_model('api', 'Company')
>    for company in Company.objects.all():
>        company.company_id = "Bharat_" + company.id 		# copy id to company_id
>        company.save()
>
> class Migration(migrations.Migration):
>    operations = [
>        migrations.AddField(
>            model_name='company',
>            name='company_id',
>            field=models.CharField(blank=True, max_length=100, null=True),
>        ),
>        migrations.RunPython(copy_ids)
>    ]
> ```

<br>

> <code>py manage.py migrate</code>

---

<br>

> **Custom Field** &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; How to add an additional field to a ModelSerializer _without actually adding it in the Model_ ?
> ```
> class CompanySerializer(serializers.HyperlinkedModelSerializer):
>
>    summary = serializers.SerializerMethodField()
>
>    class Meta:
>        	model = Company
>        	fields = ["url", "id", "name", "location", "about", "type", "added_date", "active", "summary"]
> 
>    def get_summary(self, obj):         
>        	return f"{obj.name} is a {obj.location} based {obj.type} company"
> ```
		
<br>

> Now let's create another model called <code>Employee</code> such that a **company** can have many **employees**. So, it's a **One-to-Many** relationship.
> ```
> # Employee model
> class Employee(models.Model):
>     name = models.CharField(max_length=100)
>     email = models.CharField(max_length=50)
>     address = models.CharField(max_length=200)
>     phone = models.CharField(max_length=10)
>     about = models.TextField()
>     position = models.CharField(max_length=50, 
>                                 choices=(
>                                     ('Manager', 'MGR'),
>                                     ('Software Developer', 'SD'),
>                                     ('Project Leader', 'PL')
>                                )
>               	      )
>     company = models.ForeignKey(Company, on_delete=models.CASCADE) 		# company_id = Foreign Key
> ```
> 
> <code>py .manage.py makemigrations --name create_employee_model</code>
>
> <code>py manage.py migrate</code>

<br>

> <code>company_api/api/serializers.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Employee Serializer** <code>EmployeeSerializer()</code>
> ```
> from api.models import Employee
>
> # Employee serializer
> class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
>
>    id = serializers.ReadOnlyField()
>
>    class Meta:
>        model = Employee
>        fields = "__all__"
> ```																	 

<br>

> <code>company_api/api/views.py</code> &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; create a **Company view**  called <code>CompanyViewSet()</code>
> ```
> from api.models import Employee
> from api.serializers import EmployeeSerializer
>
> # Employee view
> class EmployeeViewSet(viewsets.ModelViewSet):
>    queryset = Employee.objects.all()
>    serializer_class = EmployeeSerializer
> ```

<br>

> <code>company_api/api/urls.py</code> 
> ```
> from api.views import EmployeeViewSet
>
> router.register(r'employees', EmployeeViewSet)
> ```

<br>

<code>http://localhost:8000/api/v1/companies/</code> &nbsp;&nbsp; has all the APIs for companies <br><code>http://localhost:8000/api/v1/employees/</code> &nbsp;&nbsp; has all the APIs for employees

So now that you have seen how to create **root URLs**, let's see how to create a **custom URL** :

<br>

> ⭐ **Custom URL**
> <br>
> <br>
> <code>http://localhost:8000/api/v1/companies/1/employees</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; All employee of company 1 &nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;&nbsp; Page not found (404) <br>
> <code>http://localhost:8000/api/v1/companies/{company_id}/employees</code> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; how to get all employees of a particular company ?
> <br><br>
>
> > <code>company_api/api/views.py</code>
> > ```
> > from rest_framework.decorators import action
> > from rest_framework.response import Response
> >						
> > @action(detail=True, methods=['get'])
> > def employees(self, request, pk=None):
> >    # print('get employess of company ', pk) 		# to check if this method is called by http://localhost:8000/api/v1/companies/1/employees
> >    company = Company.objects.get(pk=pk)
> >    emps = Employee.objects.filter(company=company)
> >    emps_serializer = EmployeeSerializer(emps, many=True, context={'request' : request})
> >    return Response(emps_serializer.data)
> > ```
> <br>
>
> Suppose you have created 3 companies with id = 1, 2, 3 respectively.  <br>
> And if you want, you may create some employees too.                   <br>
> Now let's check the following APIs :                                  <br>
> http://localhost:8000/api/v1/companies/1/employees/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; now works for company 1 because it exists
> http://localhost:8000/api/v1/companies/2/employees/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; now works for company 2 because it exists
> http://localhost:8000/api/v1/companies/3/employees/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; now works for company 3 because it exists
> http://localhost:8000/api/v1/companies/4/employees/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; does not work for company 4 because it may not exist
> <br><br>
>
> > So put it in a **Try-Exception** block like below :
> > ```
> > def employees(self, request, pk=None):
> >    try:
> >        company = Company.objects.get(pk=pk)
> >        emps = Employee.objects.filter(company=company)
> >        emps_serializer = EmployeeSerializer(emps, many=True, context={'request' : request})
> >        return Response(emps_serializer.data)
> >    except Exception as e:
> >        print(e)
> >        return Response({
> >            'message' : 'Company might not exist !! ERROR'
> >        })
> > ```
> <br>
> 
> http://localhost:8000/api/v1/companies/4/employees/ &nbsp;➜&nbsp; does not throw error for company 4 even if it does not exist <br>
> http://localhost:8000/api/v1/companies/5/employees/ &nbsp;➜&nbsp; now works even when there is no company 5

<br>

> > Now if you want to allow only the <code>READ</code> operation on a browser so that the <code>CREATE</code>, <code>UPDATE</code> & <code>DELETE</code> operations can only be done through the **Application Backend**, you will have to **disable the permissions** accordingly for unauthenticated users like following :
> >
> > <code>company_api/company_drf_api/settings.py</code>
> > ```
> > REST_FRAMEWORK = {
> >    # Use Django's standard `django.contrib.auth` permissions, or allow read-only access for unauthenticated users
> >    'DEFAULT_PERMISSION_CLASSES': [
> >        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
> >    ]
> > }
> > ```
> <br>
> 
> > Now go to both the root urls and you will see there is no form to create a record :
> > ```
> > {
> >    "companies": "http://localhost:8000/api/v1/companies/",
> >    "employees": "http://localhost:8000/api/v1/employees/"
> > }
> > ```
> <br>
>
> > Now let's try to **create**, **update** or **delete** a company or an employee through **Postman** and see what happens :
> >
> > <code>http://localhost:8000/api/v1/companies/</code> &nbsp;&nbsp;&nbsp;&nbsp;===>&nbsp;&nbsp;&nbsp;&nbsp; **ERROR - 403 Forbidden :**&nbsp; _Authentication credentials were not provided_.
> >
> > Similarly try to delete or update a companyor an employee, you will get the same **403 Forbidden Error**.
> <br>
>
> > Similarly, to completely disable the browsable API i.e, to disable even the <code>READ</code> (<code>**GET**</code>) operation on a browser, <br>
> > you need to pass <code>JSONRenderer</code> to your <code>Default_Renderer_Classes</code> like the following :
> >
> > ```
> > REST_FRAMEWORK = {
> >    'DEFAULT_RENDERER_CLASSES': [
> >        'rest_framework.renderers.JSONRenderer'
> >    ]
> > }
> > ```

<br>

Now let's handle the things as **admin** :

<br>

> **Admin**
>
> > For that we need to first register our models at &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; <code>company_api/api/admin.py</code>
> > ```
> > from api.models import Company, Employee
> > admin.site.register(Company)
> > admin.site.register(Employee)
> > ```
>
> <code>http://localhost:8000/admin/</code> &nbsp;&nbsp;&nbsp;&nbsp; <code>http://localhost:8000/admin/login/?next=/admin/</code>
>
> You will not be able to login because you have not created a superuser yet.
>
> <code>python manage.py createsuperuser</code> &nbsp;&nbsp;&nbsp;&nbsp;# To create a superuser for admin access
>
> > To delete a user, open the **ORM** using the command <code>python manage.py shell</code> and then execute the following command :
> > ```
> > user = User.objects.get(username='admin')
> > user.delete()
> > ```

<br>

> To **customize** the Django Admin &nbsp;&nbsp;&nbsp;&nbsp;➜&nbsp;&nbsp;&nbsp;&nbsp; <code>company_api/api/admin.py</code>
> ```
> class CompanyAdmin(admin.ModelAdmin):
>    list_display = ('name', 'location', 'type', 'active')
>    search_fields = ('name',)
>
> class EmployeeAdmin(admin.ModelAdmin):
>    list_display = ('name', 'email', 'company', 'position')
>    search_fields = ('name', 'email',)                          #  search_fields = ('name', 'email', 'company',) will throw foreign key error
>    list_filter = ('company',)                                  #  to filter employees based on company filter
> ```
