from django.shortcuts import render
from .models import Adult, AdultCFk_3, AdultCFk_4, AdultCFk_5, LIMEexp, Comments
from .forms import RateListForm
import random


# Create your views here.
def choosecolor(num):
    if num >= 0:
        if num < 0.05:
            return "#FFC5B9"
        elif 0.05 <= num < 0.1:
            return "#FFA591"
        elif 0.1 <= num < 0.5:
            return "#FF8469"
        elif 0.5 <= num < 0.7:
            return "#FF5A36"
        elif 0.7 <= num <= 1.0:
            return "#FF3F16"
    else:
        if num > -0.05:
            return "#A9E1Fb"
        elif -0.05 >= num > -0.1:
            return "#82D8FF"
        elif -0.1 >= num > -0.5:
            return "#43C4FF"
        elif -0.5 >= num > -0.7:
            return "#00AFFF"
    return "#00000"


def Dataset(request):
    db = Adult.objects.all()
    db = db[:200]
    return render(request, "demo/dataset.html", {'db': db})


def demo_table1(request):
    dbo = Adult.objects.all()
    dbo = dbo[:200]
    random_idx = random.randint(1, 200)
    dbo = dbo[random_idx - 1:random_idx]
    db = AdultCFk_3.objects.all()
    db = db[(random_idx - 1) * 3:(random_idx - 1) * 3 + 3]
    dbl = LIMEexp.objects.all()
    dbl = dbl[random_idx - 1:random_idx]
    style = [0]*8
    style[0] = choosecolor(dbl[0].age)
    style[1] = choosecolor(dbl[0].workclass)
    style[2] = choosecolor(dbl[0].education)
    style[3] = choosecolor(dbl[0].marital_status)
    style[4] = choosecolor(dbl[0].occupation)
    style[5] = choosecolor(dbl[0].race)
    style[6] = choosecolor(dbl[0].gender)
    style[7] = choosecolor(dbl[0].hours_per_week)
    if request.method == "POST":
        rating_form = RateListForm(request.POST)
        if rating_form.is_valid():
            new_rate = rating_form.save()
            new_rate.save()
        if request.POST.get('content'):
            com = Comments()
            com.comments = request.POST.get("content")
            com.save()
        return render(request, "demo/Example_1.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})

    else:

        rating_form = RateListForm()
        return render(request, "demo/Example_1.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})


def demo_table2(request):
    dbo = Adult.objects.all()
    dbo = dbo[:200]
    random_idx = random.randint(1, 200)
    dbo = dbo[random_idx - 1:random_idx]
    db = AdultCFk_4.objects.all()
    db = db[(random_idx - 1) * 4:(random_idx - 1) * 4 + 4]
    dbl = LIMEexp.objects.all()
    dbl = dbl[random_idx - 1:random_idx]
    style = [0]*8
    style[0] = choosecolor(dbl[0].age)
    style[1] = choosecolor(dbl[0].workclass)
    style[2] = choosecolor(dbl[0].education)
    style[3] = choosecolor(dbl[0].marital_status)
    style[4] = choosecolor(dbl[0].occupation)
    style[5] = choosecolor(dbl[0].race)
    style[6] = choosecolor(dbl[0].gender)
    style[7] = choosecolor(dbl[0].hours_per_week)
    if request.method == "POST":
        rating_form = RateListForm(request.POST)
        if rating_form.is_valid():
            new_rate = rating_form.save()
            new_rate.save()
        if request.POST.get('content'):
            com = Comments()
            com.comments = request.POST.get("content")
            com.save()
        return render(request, "demo/Example_2.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})

    else:

        rating_form = RateListForm()
        return render(request, "demo/Example_2.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})

def demo_table3(request):
    dbo = Adult.objects.all()
    dbo = dbo[:200]
    random_idx = random.randint(1, 200)
    dbo = dbo[random_idx - 1:random_idx]
    db = AdultCFk_5.objects.all()
    db = db[(random_idx - 1) * 5:(random_idx - 1) * 5 + 5]
    dbl = LIMEexp.objects.all()
    dbl = dbl[random_idx - 1:random_idx]
    style = [0] * 8
    style[0] = choosecolor(dbl[0].age)
    style[1] = choosecolor(dbl[0].workclass)
    style[2] = choosecolor(dbl[0].education)
    style[3] = choosecolor(dbl[0].marital_status)
    style[4] = choosecolor(dbl[0].occupation)
    style[5] = choosecolor(dbl[0].race)
    style[6] = choosecolor(dbl[0].gender)
    style[7] = choosecolor(dbl[0].hours_per_week)
    if request.method == "POST":
        rating_form = RateListForm(request.POST)
        if rating_form.is_valid():
            new_rate = rating_form.save()
            new_rate.save()
        if request.POST.get('content'):
            com = Comments()
            com.comments = request.POST.get("content")
            com.save()
        return render(request, "demo/Example_3.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})

    else:

        rating_form = RateListForm()
        return render(request, "demo/Example_3.html",
                      {'db': db, 'dbo': dbo, 'dbl': dbl, 'rating_form': rating_form, 'style': style})