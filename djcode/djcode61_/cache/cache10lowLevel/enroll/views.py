from ensurepip import version
from functools import cache
from django.shortcuts import render
from django.core.cache import cache

# Create your views here.

# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The Social Network', 30)
#         mv = cache.get('movie')
#     return render(request, 'enroll/course.html', {'mv': mv})


# def home(request):
#     mv = cache.get_or_set('fees', 5000, 30, version=2)
#     return render(request, 'enroll/course.html', {'mv': mv})


# def home(request):
#     data = {'name': 'Hemi', 'roll': 101}
#     cache.set_many(data, 30)
#     sv = cache.get_many(data)
#     return render(request, 'enroll/course.html', {'stu': sv})

# def home(request):
#     cache.delete('fees', version=2)
#     return render(request, 'enroll/course.html')





# def home(request):
#    cache.set('roll', 60, 5)
#    dv = cache.get('roll')
#    print(dv)
#    return render(request, 'enroll/course.html', {'stu':dv})


# def home(request):
#    # cache.set('roll', 60)
#    dv = cache.decr('roll', delta=2)
#    # dv = cache.incr('roll', delta=1)
#    print(dv)
#    return render(request, 'enroll/course.html', {'stu':dv})

def home(request):
   cache.clear()
   return render(request, 'enroll/course.html')

