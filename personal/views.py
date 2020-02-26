from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_job_post_queryset
from blog.models import JobPost

def first_page_view(request):
	return render(request,'index.html')

JOB_POSTS_PER_PAGE = 10

def home_screen_view(request, *args, **kwargs):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	job_posts = sorted(get_job_post_queryset(query), key=attrgetter('contact_email'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
	job_posts_paginator = Paginator(job_posts, JOB_POSTS_PER_PAGE)
	try:
		job_posts = job_posts_paginator.page(page)
	except PageNotAnInteger:
		job_posts = job_posts_paginator.page(JOB_POSTS_PER_PAGE)
	except EmptyPage:
		job_posts = job_posts_paginator.page(job_posts_paginator.num_pages)

	context['blog_posts'] = job_posts

	return render(request, "personal/home.html", context)



