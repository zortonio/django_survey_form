from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "default/index.html")

def process(request):
    if 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    else:
        request.session['count'] = 1

    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    print request.session
    return redirect('/result')

def result(request):
    return render(request, "default/result.html")

def home(request):
    return redirect('/')
