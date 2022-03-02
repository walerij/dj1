from django.shortcuts import render


def adv_list(request, *args, **kwargs):
    #ip = request.META.get('REMOTE_ADDR')
    adv = ['Мастер на час', 'Экскурсия по Пензе','Выведение из запоя',"Сдача квартиры","Карты Таро"]
    return render(request,'adv/adv_list.html',{'advs':adv})

