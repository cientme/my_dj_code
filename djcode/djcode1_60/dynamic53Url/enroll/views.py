from django.shortcuts import render

# Create your views here.

def home(request, check):
    return render(request, 'enroll/home.html', {'check': check})

# def show_details(request, my_id):
#     student = {'id':my_id}
#     return render(request, 'enroll/show.html', student)


def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id':my_id, 'name': 'naufil'}
        
    if my_id == 2:
        student = {'id':my_id, 'name': 'hemi'}

    if my_id == 3:
        student = {'id':my_id, 'name': 'bilal'}

    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id':my_id, 'name': 'naufil', 'info': 'sub detail'}
        
    if my_id == 2 and my_subid == 6:
        student = {'id':my_id, 'name': 'hemi', 'info': 'subdetail'}

    if my_id == 3 and my_subid == 7:
        student = {'id':my_id, 'name': 'bilal', 'info': 'subdetail'}

    return render(request, 'enroll/show.html', student)