from django.shortcuts import render, redirect

from employeeapp.forms import EmployeeForm
from employeeapp.models import Employee


# Create your views here.
def add(request):
    employee1=Employee.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        mobileno=request.POST.get('mobileno')
        designation=request.POST.get('designation')
        employee=Employee(name=name,dob=dob,mobileno=mobileno,designation=designation)
        employee.save()
    return render(request,'base.html',{'employee1':employee1})
def delete(request,id):
    if request.method=='POST':
        employee=Employee.objects.get(id=id)
        employee.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST or None,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})