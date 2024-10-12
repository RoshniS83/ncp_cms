from django.urls import path
from ncpforpeople.views import PeopleAPI

urlpatterns = [
    path('allPeople/', PeopleAPI.as_view({'get': 'list'})),
    path('Details/<int:pk>/', PeopleAPI.as_view({'get': 'retrieve'})),
    path('createPeopleIssue/', PeopleAPI.as_view({'post': 'create'})),
    path('updatePeopleIssue/<int:pk>', PeopleAPI.as_view({'put': 'update'})),
    path('partialupdatePeopleIssue/<int:pk>/', PeopleAPI.as_view({'patch': 'partial_update'})),
    path('deletePeopleIssue/<int:pk>/', PeopleAPI.as_view({'delete': 'destroy'})),

]