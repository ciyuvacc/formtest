#coding:utf8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from mysite import models,forms

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


def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    html = template.render(locals())

    return HttpResponse(html)



def posting(request):
    template = get_template('posting.html')
    moods = models.Mood.objects.all()
    message = '如果要张贴信息,那么没一个字段都要填...'



    request_context = RequestContext(request)
    request_context.push(locals())

    html = template.render(request_context)

    return HttpResponse(html)



def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感谢您的来信.'
      
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school  = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']


        else:
            message = '请检查您的输入信息是否正确!'
    else:
        form = forms.ContactForm()
    template = get_template('contact.html')

    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)



def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "你的信息已存储,要等管理员启用后才能看到."
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如果要张贴信息,那么没一个字段都要填...'
    else:
        post_form = forms.PostForm()
        message = '如果要张贴信息,那么没一个字段都要填...'

    template = get_template('post2db.html')

    request_context = RequestContext(request)
    request_context.push(locals())

    html = template.render(request_context)

    return HttpResponse(html)

