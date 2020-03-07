from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from blog.models import JobPost
from blog.forms import CreateJobPostForm, UpdateJobPostForm
from account.models import Account


def create_blog_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('company_redirect')



	form = CreateJobPostForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		context['success']="Successfully Updated"
		form = CreateJobPostForm()

	context['form'] = form

	return render(request, "blog/create_blog.html", context)


def detail_blog_view(request, slug):

	context = {}

	job_post = get_object_or_404(JobPost, slug=slug)
	context['job_post'] = job_post

	return render(request, 'blog/detail_blog.html', context)



def edit_blog_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("company_redirect")

	job_post = get_object_or_404(JobPost, slug=slug)

	if job_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form = UpdateJobPostForm(request.POST or None, instance=job_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			job_post = obj

	form = UpdateJobPostForm(
			initial = {
					"job_title": job_post.job_title,
					"job_type": job_post.job_type,
					"job_description": job_post.job_description,
					"url":job_post.url,
					"location":job_post.location,
					"position":job_post.position,
					"job_description":job_post.job_description,

			}
		)

	context['form'] = form
	return render(request, 'blog/edit_blog.html', context)


def get_job_post_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = JobPost.objects.filter(
				Q(job_title__icontains=q) | 
				Q(job_description__icontains=q)|
				Q(job_type__icontains=q)|
				Q(location__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	
