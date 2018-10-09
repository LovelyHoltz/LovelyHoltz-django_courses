from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'surveyform_app/index.html')

def show(request):
    print (request.method)
    return render(request, 'surveyform_app/new_user.html')

def new_user(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    print (request.method)
    if request.method == "POST":
        print ('*' * 50)
        print (request.POST)
        print ('*' * 50)
        request.session['user_name'] = request.POST['user_name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['fav_language'] = request.POST['fav_language']
        request.session['user_comment'] = request.POST['user_comment']
        return render(request, 'surveyform_app/new_user.html')
    else:
        return redirect('/')

def back(request):
    return render(request, 'surveyform_app/index.html')
