from django.shortcuts import render, redirect
from . forms import EmployeeForm
from . models import Employee

# Create your views here.


def employeeAdd(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = EmployeeForm()

    return render(request, 'employee_registry/employee_form.html', {'form':form})

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request, 'employee_registry/employee_list.html', context)


def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {'form':form}
    return render(request, 'employee_registry/employee_form.html', context)



def employeeView(request, id):
    employee = Employee.objects.get(id=id)

    context={'employee':employee}
    return render(request, 'employee_registry/employee.html', context)


def employeeDelete(request, id):
    employee =Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')

    context = {'employee':employee}
    return render(request, 'employee_registry/delete.html', context)


def search_Employee(request):
    if request.method == 'POST':
        q = request.POST['q']
        employees = Employee.objects.filter(name__icontains=q)
        
        return render(request, 'employee_registry/search_employee.html', {'q':q, 'employees':employees})

    else:
        return render(request, 'employee_registry/search_employee.html', {})


