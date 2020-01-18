from django.shortcuts import render



# Create your views here.
def homepage(requests):

	context = {}

	if('hold' in requests.POST):
		label = 'hold'
	elif('reject' in requests.POST):
		label = 'reject'
	elif('select' in requests.POST):
		label = 'select'
	else:
		label = False

	if(label):
		name = requests.POST.get('fname', False)
		email = requests.POST.get('email', False)
		contact = requests.POST.get('contact', False)
		dob = requests.POST.get('dob', False)
		context = {'name':name, 'email':email, 'contact':contact, 'dob':dob,'label':label}

	if('save' in requests.POST):
		total = requests.POST.get('total', False)
		if(total):
			context['total'] = total
	return render(requests, 'mainapp/homepage.html', context)

def history(requests):
	import pandas as pd
	path = '/users/husainshaikh/Documents/BE_project/selected.csv'
	data = pd.read_csv(path)
	data_html = data.to_html()
	context = {'loaded_data': data_html}
	return render(requests, 'mainapp/history.html', context)

def instructions(requests):
	return render(requests, 'mainapp/instructions.html',{})

	
def visualise(requests):
	return render(requests, 'mainapp/visualise.html',{})