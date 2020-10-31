from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

class NewProgram(TemplateView):
    template_name = 'new-program.html'

class BugBounty(TemplateView):
    template_name = 'bug-b-solutions.html'

class PenetrationTesting(TemplateView):
    template_name = 'penetration-testing.html'

class LiveHacking(TemplateView):
    template_name = 'live-hacking.html'

class ProgramList(TemplateView):
    template_name = 'program-list.html'

class About(TemplateView):
    template_name = 'about.html'

class Partner(TemplateView):
    template_name = 'partners.html'

class Contact(TemplateView):
    template_name = 'contact.html'    
