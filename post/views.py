import json
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from django.db import connection
from .models import Post, PostInfo
from .forms import PostForm, PostInfoForm
from post.common.views import scanPost, dictfetchall


def list(request):
    with connection.cursor() as cursor:
        sql = '''
            select  id,
                    title,
                    content,
                    regist_date,
                    ifnull(total_cnt, 0) as total_cnt
            from post x
            left join (
            	select post_id, count(*) as total_cnt
            	from post_info
            	group by post_id
            ) y
            on x.id = y.post_id
            where x.delete_yn = 'N'
            order by id desc
        '''
        cursor.execute(sql)
        post = dictfetchall(cursor)
    context = {}
    context['post'] = post
    return render(request, 'post/list.html', context)


def post(request, id):
    p = Post.objects.get(id=id)
    pf = PostForm(instance=p)
    context = {}
    context['form'] = pf
    context['id'] = id
    return render(request, 'post/post.html', context)


def regist(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        result = scanPost(content)
        p = Post(
            title = title,
            content = content,
            regist_date = datetime.datetime.now()
        )
        p.save()
        for n in result:
            hanja = n['hanja']
            hiragana = n['hiragana']
            hangul = n['hangul']
            PostInfo(
                post_id = p.id,
                hanja = hanja,
                hiragana = hiragana,
                hangul = hangul,
                regist_date = datetime.datetime.now()
            ).save()
        return JsonResponse({'result': 200})
    else:
        pf = PostForm()
        context = {}
        context['form'] = pf
        return render(request, 'post/regist.html', context)


def report(request):
    with connection.cursor() as cursor:
        sql = '''
            select 	@rownum := @rownum + 1 AS ranking,
            		hanja,
            		hiragana,
            		hangul,
            		total_cnt
            from (
            	select 	hanja,
            			hiragana,
            			hangul,
            			count(*) as total_cnt
            	from post_info
            	group by hanja, hiragana, hangul
                order by total_cnt desc
            ) w
            JOIN (SELECT @rownum := 0) r
        '''
        cursor.execute(sql)
        report = dictfetchall(cursor)
    context = {}
    context['report'] = report
    return render(request, 'post/report.html', context)


def delete(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        x = Post.objects.get(id=post_id)
        x.delete_yn = 'Y'
        x.delete_date = datetime.datetime.now()
        x.save()
        return JsonResponse({'result': 200})
