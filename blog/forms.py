from django import forms

from blog.models import JobPost


class CreateJobPostForm(forms.ModelForm):

	class Meta:
		model = JobPost
		fields = ['job_title','job_type','job_description','url','location','position','contact_email']


class UpdateJobPostForm(forms.ModelForm):

	class Meta:
		model = JobPost
		fields = ['job_title','job_type','job_description','url','location','position','contact_email']

	def save(self, commit=True):
		job_post = self.instance
		job_post.job_title = self.cleaned_data['job_title']
		job_post.job_type = self.cleaned_data['job_type']
		job_post.job_description =self.cleaned_data['job_description']
		job_post.url = self.cleaned_data['url']
		job_post.location=self.cleaned_data['location']
		job_post.position=self.cleaned_data['position']
		job_post.contact_email=self.cleaned_data['contact_email']


		if commit:
			blog_post.save()
		return blog_post

