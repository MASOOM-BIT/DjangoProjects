from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    mydict={'name':'Masoom Raza'}
    return render(request,'templateApp/firstTemplate.html',context=mydict)

def renderEmployee(request):
    mydict={'name':'Masoom Raza','age':23,'salary':100000}
    return render(request,'templateApp/employeeTemplate.html',mydict)