from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    context = {
        # Days of the week
        'days' : ['Mon', 'Tues', 'Wed', 'Thur', 'Fri'],
        # Weeks in the calendar
        'hours' : ['7am', 
                   '8am', 
                   '9am', 
                   '10am', 
                   '11am', 
                   '12am', 
                   '1pm',
                   '2pm',
                   '3pm',
                   '4pm',
                   '5pm',
                   '6pm',
                   '7pm',
                   '8pm',
                   '9pm',
                   '10pm'],
        'classes' : ['Political Science', 
                     'Business Administration', 
                     'Mechanical Engineering',
                     'Biomedical Engineering']
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))