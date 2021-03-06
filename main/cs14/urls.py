from django.urls import path
from cs14 import views


app_name = 'cs14'

urlpatterns = [
	path('', views.index, name='index'),
	path('code/<int:id>/', views.codingPage, name='code'),
	path('sendCode', views.sendCode, name='sendCode'),
	path('codingPageCookie', views.codingPageCookie, name='codingPageCookie'),
	path('register/', views.register, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('profile/', views.profile, name='profile'),
	path('results/', views.results, name='results'),
	path('myresults/', views.cresults, name='cresults'),
	path('codereview/<int:id>/', views.creview, name='creview'),
	path('testCode', views.testCode, name='testCode'),
	path('rhistory', views.rhistory, name='rhistory'),
	path('getresultsession', views.getresultsession, name='getresultsession'),
	path('updateTemplate', views.updateTemplate, name='updateTemplate')
]

