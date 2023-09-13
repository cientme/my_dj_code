from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.


# This class Adds New Items And Show All Items.
class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args ,**kwargs)
        form = StudentRegistration()
        stud = User.objects.all()
        context = {'stud': stud, 'form': form}
        return context
    
    def post(self, request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            data = User(name=nm , email=em, password=pwd)
            data.save()
        return HttpResponseRedirect('/')



# This Class will update/edit of Student information.
class EditDataView(View):
    def get(self, request, id):
        data = User.objects.get(pk=id)
        form = StudentRegistration(instance=data)
        context = {'form': form}
        return render(request, 'enroll/updatestudent.html', context)
    
    def post(self, request, id):
        data = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    

# This class will delete.
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


