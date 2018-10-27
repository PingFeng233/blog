from django.shortcuts import render, HttpResponse
from userview.utils import change_player_info


# Create your views here.
def search(request, **kwargs):
    change_player_info(request)
    v_url = None
    if request.method == "POST":
        v_url = request.POST.get('video', None)
        line = request.POST.get('line', '1')
        if line == '1':
            pre_url = "http://api.xfsub.com/index.php?url="
        elif line == '2':
            pre_url = "http://app.baiyug.cn:2019/vip/index.php?url="
        elif line == '3':
            pre_url = "https://jx.618g.com/?url="
    return render(request, 'videoplayer/videoplayer.html', locals())
