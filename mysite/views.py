#coding:utf8
from django.template.loader import get_template
from django.http import HttpResponse
from mysite import models

def index1(request):
    template = get_template('index.html')
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None
    if urid != None and urpass == '1234':
        verified = True
    else:
        verified = False
    
    #years = range(1990,2017)
    #urfcolor = request.GET.getlist('fcolor')
    #year = request.GET['byear']

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    #print verified
    html = template.render(locals())

    return HttpResponse(html)

def index(request,pid=None,del_pass=None):
    template = get_template('index.html')

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如果要张贴信息,那么每个字段都要填...'
    
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功"
            else:
                message = "密码错误"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood,nickname=user_id,del_pass=user_pass,message=user_post)
        post.save()
        message = '成功存储!请记住编辑的密码[{}]!,信息须审查后才会显示.'.format(user_pass)
     
    html = template.render(locals())

    return HttpResponse(html)
