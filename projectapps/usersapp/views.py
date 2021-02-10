import pytz
from django.utils import timezone

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import IncidentForm
from .models import Incident, Post
from django.views.decorators.http import require_POST
from .filters import ResponsesFilter
from django.contrib.messages.views import SuccessMessageMixin


#from django.views.generic.edit import CreateView 
from django.views import generic

# Create your views here.

# add a new view function called incident_create
#PostList will become the home page instead of the function home 
'''
def  home (request): 
    #incident = Incident.objects.get(pk=1)
    return render(request,'index.html')
'''
def aboutus (request):
    return render(request, 'aboutus.html')

def incident_create(request):
    if request.method == 'POST':

       # lastvideo= Incident.objects.last()
        
        #videofile= lastvideo.videofile

        #form = IncidentForm(request.POST)
        userform = IncidentForm(request.POST, request.FILES)

        #if form.is_valid():
        if userform.is_valid():

            #form.save()
            userform.save()
            
            print('form submitted')
            messages.info(request, 'Thank you for reporting')
            return redirect('incident_create')
    else:
        print('Unable to submit')

        #form = IncidentForm()
        userform = IncidentForm()
    
    return render(request,
    'incident_create.html',
    {
        #'videofile': videofile,
        #'form': form
        'form': userform
    })


#this function generates users' report responses into a single table
def responder(request):
    #detail=Incident.objects.all().filter(accident_location__exact='Adamawa')
    detail=Incident.objects.all()
    return render(request,
    'responder.html',
    {
        'detail': detail
    })

'''
#getting responders timezone when searching users responses 

def convert_to_localtime(utctime):
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz
'''

#writing a function that would filter fields in ResponsesFilter in filters.py
def search_responses(request):
    responses = Incident.objects.all()
    response_filter = ResponsesFilter(request.GET, queryset=responses)
   # has_filter = any(field in request.GET for field in set(response_filter.get_fields()))
    return render(request, 
    'search_responses.html', 
    {'filter': response_filter
    })


class PostCreate(SuccessMessageMixin, generic.CreateView):
    # specify the model for create view 
    model = Post 
  
    # specify the template to be displayed 
    template_name = 'post_create.html' 
    success_message =  'Your post has been submitted'

    # specify the fields to be displayed 
  
    fields = ['accident_location', 'local_government_area', 'address_or_nearest_landmark', 'content', 'imagefile']
    def get_success_url(self):
        #return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})
        return reverse('post_create')


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model= Post
    template_name = 'post_detail.html'
