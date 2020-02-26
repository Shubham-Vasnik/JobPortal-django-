from django.shortcuts import render
from scholarship_blog.models import ScholarShip
# Create your views here.


def scholarship_blog_view(requests):
	context={}
	scholarships =ScholarShip.objects.all()
	print(scholarships)
	context['scholarships']=scholarships
	return render(requests,'scholarship_blog/scholarship.html',context)