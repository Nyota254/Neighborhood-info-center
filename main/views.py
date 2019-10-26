from django.shortcuts import render

def index_view(request):
    '''
    Main home page view
    '''
    title = "home"
    context = {
        "title":title
    }
    return render(request,"main/index.html",context)
