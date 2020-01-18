from django.shortcuts import render

# Create your views here.
def account_homepage(requests):
	return render(requests, 'accounts/account_homepage.html')


def account_signup(requests):
	return render(requests, 'accounts/account_signup.html')


def account_login(requests):
	return render(requests, 'accounts/account_login.html')