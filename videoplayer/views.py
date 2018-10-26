from django.shortcuts import render, HttpResponse
from userview.utils import change_player_info


# Create your views here.
def search(request, **kwargs):
    change_player_info(request)
    v_url = None
    if request.method == "POST":
        v_url = request.POST.get('video', None)
    return render(request, 'videoplayer/videoplayer.html', locals())
