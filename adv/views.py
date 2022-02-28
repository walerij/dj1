from django.shortcuts import render

from django.http import HttpResponse


def adv_list(request, *args, **kwargs):
    return render(request,'adv/adv_bs.html',{})

