import os
from django.shortcuts import render
from jobs.keras_first_go import KerasFirstGoModel
from jobslink.models import JobDesc

# Create your views here.


def train_model():
	global first_go_model
	print("Train the model")
	first_go_model = KerasFirstGoModel()


def my_jobs(request):
	return render(request,'jobs/index.html')



def result(request):
	if request.method == 'POST':
		result = request.POST['Job']
		#result = request.form.getlist('Job')
		train_model()
		processed_text = first_go_model.prediction(result[0])
		result = {'Job': processed_text}
		print(processed_text)
	
		result["result_query"]=JobDesc.objects.filter(category__icontains=processed_text)
		print(result)
		return render(request,"jobs/result.html",result)


