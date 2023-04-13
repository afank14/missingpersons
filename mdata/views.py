from django.shortcuts import render
from .models import Statistics

# Create your views here.
def indexPageView(request) :
    return render(request, 'mdata/index.html')

def aboutPageView(request) :
    return render(request, 'mdata/about.html')

def statsPageView(request) :
    db_statistics = Statistics.objects.all()

    context = {
        "data" : db_statistics
    } 

    return render(request, 'mdata/stats.html', context)

def displayPersonPageView(request, id) :
    person = Statistics.objects.get(id=id)

    context = {
        "data" : person
    }

    return render(request, 'mdata/displayPerson.html', context)


