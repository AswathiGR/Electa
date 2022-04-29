from django.shortcuts import render
from voters_list.forms import VotersForm  
from voters_list.models import Voters_list  
# Create your views here.
def emp(request):  
    if request.method == "POST":  
        form = VotersForm()(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = VotersForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    voters = Voters_list().objects.all()  
    return render(request,"show.html",{'voters_list':voters_list})  
def edit(request, id):  
    voters_list = Voters_list().objects.get(id=id)  
    return render(request,'edit.html', {'voters_list':voters_list})  
def update(request, id):  
    voters_list = Voters_list().objects.get(id=id)  
    form =VotersForm()(request.POST, instance = voters_list) 

    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'voters_list': voters_list})
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  