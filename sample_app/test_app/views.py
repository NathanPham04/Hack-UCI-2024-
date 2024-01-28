from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    context = {
        # Days of the week
        'days' : ['Mon', 'Tues', 'Wed', 'Thur', 'Fri'],
        # Weeks in the calendar
        'hours' : ['7 AM', 
                   '8 AM', 
                   '9 AM', 
                   '10 AM', 
                   '11 AM', 
                   '12 PM', 
                   '1 PM',
                   '2 PM',
                   '3 PM',
                   '4 PM',
                   '5 PM',
                   '6 PM',
                   '7 PM',
                   '8 PM',
                   '9 PM',
                   '10 PM']
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))