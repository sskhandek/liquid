from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from intranet.member_manager.models import Member
from intranet.member_manager.forms import MemberForm

# Create your views here.
def main(request):
  return render_to_response('intranet/member_manager/main.html',{"section":"intranet","page":'members'})
  
def new(request):
  c = {}
  c.update(csrf(request))
  if request.method == 'POST': # If the form has been submitted...
      form = MemberForm(request.POST) # A form bound to the POST data
      if form.is_valid(): # All validation rules pass
          form.save()
          return HttpResponseRedirect('/') # Redirect after POST
  else:
      form = MemberForm() # An unbound form

  return render_to_response('intranet/member_manager/form.html',{
      'form': form,
      "section":"intranet",
      "page":'members',
      "page_title":"Create new Member"
      },context_instance=RequestContext(request))
    