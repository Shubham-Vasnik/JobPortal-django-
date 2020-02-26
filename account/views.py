from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import RegistrationForm, AccountAuthenticationForm, EmployeeUpdateForm,CompanyUpdateForm
from blog.models import JobPost 
from account.models import Account



def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def employee_registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db() 
			user.is_employee=True
			user.last_name = request.POST['last_name']
			user.register_id=None
			
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			user.save()
			
			login(request, account)

			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register_employee.html', context)

def company_registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db() 
			user.is_employee=False
			register_id=request.POST['register_id']
			user.last_name=None
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user.register_id = register_id
			account = authenticate(email=email, password=raw_password)
			print(register_id)
			user.save()
			login(request, account)

			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/company_register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/home')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def employee_account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = EmployeeUpdateForm(request.POST, request.FILES or None, instance=request.user)
		if form.is_valid():
			print(request.FILES)
			print(request.FILES.get('image'))
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
					"last_name":request.POST['last_name'],
					"image":request.user.image
					
					
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = EmployeeUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
					"last_name":request.user.last_name,
					"image":request.user.image,
				}
			)

	context['account_form'] = form

	return render(request, "account/employee_update_form.html", context)

def company_account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = CompanyUpdateForm(request.POST, request.FILES or None, instance=request.user)
		if form.is_valid():
			
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
					"register_id":request.POST['register_id'],
					"image":request.FILES['image']
					
					
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = CompanyUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
					"register_id":request.user.register_id,
					"image":request.user.image
				}
			)

	context['account_form'] = form

	blog_posts = JobPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, "account/company_update_form.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})


def register_option_view(request):
	return render(request,'account/register_option.html')

def company_redirect_view(request):
	return render(request,'account/company_redirect.html')

def employee_redirect_view(request):
	return render(request,'account/employee_redirect.html')