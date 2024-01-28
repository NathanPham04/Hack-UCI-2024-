from django.http import HttpResponse
from django.template import loader
import pandas as pd
# Create your views here.

def get_all_majors():
    data_path = 'data/major_data.csv'
    data = pd.read_csv(data_path)
    return list(data['major_name'])

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
        'classes' : get_all_majors()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

if __name__ == '__main__':
    print(get_all_majors())