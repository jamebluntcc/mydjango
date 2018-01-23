from django.shortcuts import render
from django.http import HttpResponse
from .models import Character
# Create your views here.

# base
def index(request):
    return HttpResponse('<p>my west</p>')

# connect database
def staff(request):
    Character.objects.all().delete()
    staffs = [Character(name='cc'), Character(name='haha')]
    # save
    for staff in staffs:
        staff.save()
    # get all
    all_staffs = Character.objects.all()
    staff_name = map(lambda x: getattr(x, 'name'), all_staffs)
    return HttpResponse('<p>' + ','.join(staff_name) + '</p>')

# with template
def templay(request):
    context = {}
    context['label'] = 'hello, django templates'
    return render(request, 'index.html', context)

# use get or post
def form(request):
    if request.method == 'POST':
        user = request.POST.get('username', '')
        if user:
            return HttpResponse('<p>hello, {}</p>'.format(user))
    return render(request, 'form.html')

