from django.shortcuts import render, redirect

from . models import User

def index(request):
	if request.method == "POST":
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		return redirect('/users')
	else:
		context = {
			"all_users": User.objects.all()
		}
		return render(request, 'semirest_app/index.html', context)

def new(request):
	return render(request, 'semirest_app/new.html')

def show_update(request, user_id):
	if request.method == "POST":
		user = User.objects.filter(id=user_id)
		user.update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'] )
		return redirect('/users')
	else:
		user = User.objects.get(id=user_id)
		context = {
			"user": user
		}
		return render(request, 'semirest_app/show.html', context)

def edit(request, user_id):
	user = User.objects.get(id=user_id)
	context = {
		"user": user
	}
	return render(request, 'semirest_app/edit.html', context)

def delete(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/users')
