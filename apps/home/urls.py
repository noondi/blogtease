# app level

from django.conf.urls import url
from . import views

def test(request):
	# naruto ascii
  # http://www.ascii-art.de/ascii/ab/anime.txt
	print """




REGister worked ?????!!!!!!
	"""

urlpatterns = [
  url(r'^$', views.home),
  url(r'^vulnhub/jarbas1$', views.jarbas1),
  url(r'^vulnhub/bsides2018vancouver$', views.bsides2018vancouver),
  url(r'^vulnhub/born2root$', views.born2root),
  url(r'^vulnhub/billymadison$', views.billymadison),
  url(r'^vulnhub/spjerome1$', views.spjerome1),
  url(r'^logout$', views.logout),    
]

			
