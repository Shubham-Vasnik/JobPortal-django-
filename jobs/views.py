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
		context={}
		result = request.POST['Job']
		#result = request.form.getlist('Job')
		result=list([result])
		#print(type(result))
		print('____________________________')

		print(result[0])
		print('________________________________--')
		train_model()
		processed_text = first_go_model.prediction(result[0])
		context = {'Job': processed_text}
		print('###########################')
		print(processed_text)
		print('###########################')

		split_data=processed_text.split()
		for data in split_data:
			context["result_query"]=JobDesc.objects.filter(category__icontains=data)


	

		return render(request,"jobs/result.html",context)


