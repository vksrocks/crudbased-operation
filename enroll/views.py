from django.shortcuts import render
from . form import studentregistration
from . models import user
from django.http  import HttpResponseRedirect 

# Create your views here.
def add_show(request):
	if request.method=='POST':
		fm=studentregistration(request.POST)
		if fm.is_valid():
			nm=fm.cleaned_data['name']
			em=fm.cleaned_data['email']
			ps=fm.cleaned_data['password']
			reg=user(name=nm,email=em,password=ps)
			reg.save()
			fm=studentregistration()


	else:

		fm=studentregistration()
	
	stud=user.objects.all()

	return render(request,'enroll/addandshow.html',{'form': fm ,'stu':stud})

# This is for the deletion

def deletion(request,id):
	if request.method=='POST':
		pi=user.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')

# This is for updation
def updation(request,id):
	if request.method=='POST':
		pi=user.objects.get(pk=id)
		fm=studentregistration(request.POST,instance=pi)
		if fm.is_valid():
			fm.save()
			fm=studentregistration()
	else:
		pi=user.objects.get(pk=id)
		fm=studentregistration(instance=pi)

	return render(request,'enroll/updatestudent.html',{'fk':fm})
