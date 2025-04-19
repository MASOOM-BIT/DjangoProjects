from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField(default=0.0)
    email = models.EmailField(max_length=50, unique=True)


# python manage.py shell-------------
# from empApp.models import Employee -> import Employee
# qs=Employee.objects.all() -> get all Employee objects

# <class 'django.db.models.query.QuerySet'> -> <class 'empApp.models.Employee'>
# emp=Employee.objects.get(id=1) -> get Employee object with id=1
# print(emp.firstName) -> print firstName of Employee object
# print(qs.query) -> print query of Employee objects

# -------filtering the data------------------
# emps=Employee.objects.filter(salary__gt=5000) -> filter Employee objects with salary greater than 5000

# emps=Employee.objects.filter(salary__gte=5000) -> filter Employee objects with salary greater than or equal to 5000

# emps=Employee.objects.get(firstName__contains='Mas') -> get Employee object with firstName contains 'Mas'

# emps=Employee.objects.get(firstName__icontains='Mas') -> get Employee object with firstName contains 'Mas' (case insensitive)

# emps=Employee.objects.filter(id__in=[1,2]) -> filter Employee objects with id in [1,2]

# It,Ite,startswith,endswith

# filter -> AND & , OR | , NOT ------------------

# | -> from django.db.models import Q

# In [19]: emps=Employee.objects.filter(Q(firstName__startswith='Mas')|Q(lastName__starts 
    # ...: with='xy')) -> filter Employee objects with firstName starts with 'Mas' or lastName starts with 'xy'

# emps=Employee.objects.exclude(salary__gt=5000) -> exclude Employee objects with salary greater than 5000
# emps=Employee.objects.all().values_list('firstName','salary') -> get all Employee objects with firstName and salary
# Value
# only

#Aggregrate functions ----------------------------
#from django.db.models import Avg, Max, Min, Count, Sum
# Employee.objects.aggregate(Avg('salary')) -> get average salary of Employee objects
# Employee.objects.aggregate(Max('salary')) -> get maximum salary of Employee objects
# Employee.objects.aggregate(Min('salary')) -> get minimum salary of Employee objects
# Employee.objects.aggregate(Count('salary')) -> get count of Employee objects with salary

# --------count object-----------------
# Employee.objects.count() -> get count of Employee objects
# Employee.objects.filter(salary__gt=5000).count() -> get count of Employee objects with salary greater than 5000

# create and bulk create---------------
# Employee.objects.create(firstName='Mas',lastName='xy',salary=5000,

# bulk=-> Employee.objects.bulk_create([Employee(firstName='Mas',lastName='xy',salary=5000,
# ------------delete-------
# Employee.objects.filter(id=1).delete() -> delete Employee object with id=1
# -----------update------------
# Employee.objects.filter(id=1).update(salary=6000) -> update salary of Employee object with id=1 to 6000
# Employee.objects.filter(id=1).update(salary=F('salary')+1000) -> update salary of Employee object with id=1 to salary+1000
# ----------------order by ------------
# Employee.objects.all().order_by('salary') -> order Employee objects by salary in ascending order
# Employee.objects.all().order_by('-salary') -> order Employee objects by salary in descending order