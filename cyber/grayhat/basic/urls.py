from django.urls import path
from .views import (
                HomeView,
                NewProgram,
                BugBounty,
                PenetrationTesting,
                LiveHacking,
                ProgramList,
                About,
                Partner,
                Contact
)


app_name = 'basic'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('new-program', NewProgram.as_view(), name = 'new-program'),
    path('bug-b-solution', BugBounty.as_view(), name = 'bug-b-solution'),
    path('penetration-testing', PenetrationTesting.as_view(), name = 'penetration-testing'),
    path('live-hacking', LiveHacking.as_view(), name = 'live-hacking'),
    path('program-list', ProgramList.as_view(), name = 'program-list'),
    path('about', About.as_view(), name = 'about'),
    path('partners', Partner.as_view(), name = 'partners'),
    path('contact', Contact.as_view(), name = 'contact'),
]
