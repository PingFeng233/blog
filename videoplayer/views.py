from django.shortcuts import render, HttpResponse


# Create your views here.
def search(request, **kwargs):
    v_url = None
    if request.method == "POST":
        v_url = request.POST.get('video', None)
    return render(request, 'videoplayer/videoplayer.html', locals())
