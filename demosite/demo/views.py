from django.shortcuts import render
from .models import Adult, AdultCFk_3, AdultCFk_4, AdultCFk_5, LIMEexp, Survey_Comments, neighbor
from .forms import RateListForm, attentionform
import random
import pickle
from django.http import HttpResponseRedirect
import uuid


# Create your views here.
test_num = 3
random_idx = random.randint(1, 200)
testidx = list(range((random_idx - 1) * 5, (random_idx - 1) * 5 + test_num))
workid = 0
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
        elif -0.7 >= num > -1.0:
            return "#007bb3"
    return "#00000"

def cat2num(cata):
    if cata == 'HS-grad':
        return 12.5
    elif cata == 'Private' or cata =='Assoc':
        return 25
    elif cata == 'Divorced':
        return 20
    elif cata == 'Blue-Collar':
        return 16.7
    elif cata == 'Self-Employed' or cata == 'Bachelors' or cata == 'Other/Unknown' or cata == 'White' or cata == 'Male':
        return 50
    elif cata == 'Doctorate':
        return 37.5
    elif cata == 'Married':
        return 40
    elif cata == 'Professional':
        return 33.3
    elif cata == 'Separated':
        return 60
    elif cata == 'Sales':
        return 66.7
    elif cata == 'Prof-school':
        return 62.5
    elif cata == 'Government' or cata == 'Masters':
        return 75
    elif cata == 'Single':
        return 80
    elif cata == 'White-Collar':
        return 83.3
    elif cata == 'School':
        return 87.5
    elif cata == 'Other/Unknown' or cata == 'Some-college' or cata == 'Widowed' or cata == 'Service' or cata == 'Other' or cata == 'Female':
        return 100
    else:
        return 0


def welcome(request):
    global workid
    workerid = workid
    workid = workerid+1
    return render(request, "demo/welcome.html", {'workid': workerid})
def attention(request):
    if request.method == "POST":
        att_form = attentionform(request.POST)
        if att_form.is_valid():
            a = att_form.cleaned_data['choice1']
            b = att_form.cleaned_data['choice2']
            if a == 'True' and b=='False':
                return HttpResponseRedirect('/Example_1')
            else:
                return HttpResponseRedirect('/exit')
    else:
        att_form = attentionform()
    return render(request, "demo/attention_check.html", {'att':att_form, 'workid': workid-1})

def exit(request):
    return render(request, "demo/exit.html", {'workid': workid-1})
def demo_table1(request, testnum):
    testnum = int(testnum)
    template = "demo/Example_1.html"
    db_adult = Adult.objects.all()[:200]
    dbo = db_adult[random_idx - 1:random_idx]
    # print(cat2num(dbo[0].workclass))
    neighboradult = neighbor.objects.all()
    testadults = [list(enumerate(neighboradult))[i] for i in testidx]
    db = AdultCFk_3.objects.all()
    db = db[(random_idx - 1) * 3:(random_idx - 1) * 3 + 3]
    originalnum = [cat2num(dbo[0].workclass), cat2num(dbo[0].education), cat2num(dbo[0].marital_status),
                   cat2num(dbo[0].occupation), cat2num(dbo[0].race), cat2num(dbo[0].gender)]
    dice1 = [cat2num(db[0].workclass), cat2num(db[0].education), cat2num(db[0].marital_status),
             cat2num(db[0].occupation), cat2num(db[0].race), cat2num(db[0].gender)]
    dice2 = [cat2num(db[1].workclass), cat2num(db[1].education), cat2num(db[1].marital_status),
             cat2num(db[1].occupation), cat2num(db[1].race), cat2num(db[1].gender)]
    dice3 = [cat2num(db[2].workclass), cat2num(db[2].education), cat2num(db[2].marital_status),
             cat2num(db[2].occupation), cat2num(db[2].race), cat2num(db[2].gender)]
    test1 = [cat2num(testadults[testnum][1].workclass), cat2num(testadults[testnum][1].education),
             cat2num(testadults[testnum][1].marital_status), cat2num(testadults[testnum][1].occupation),
             cat2num(testadults[testnum][1].race), cat2num(testadults[testnum][1].gender)]
    if testnum < test_num-1:
        context = {'nextpage': 'Example_1/'+str(testnum+1),'testcase':testnum+1, 'testnum': testnum, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'ori': originalnum, 'dice1': dice1, 'dice2': dice2,
                   'dice3': dice3, 'test1': test1}
    else:
        context = {'nextpage': 'Survey', 'testcase':testnum+1, 'testnum': testnum, 'db_adult': db_adult, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'ori': originalnum, 'dice1': dice1, 'dice2': dice2,
                   'dice3': dice3, 'test1': test1}
    if request.method == "POST":
        return render(request, template,context)
    else:
        return render(request, template,context)
def survey(request):
    if request.method == "POST":
        rating_form = RateListForm(request.POST)
        if rating_form.is_valid():
            new_rate = rating_form.save()
            new_rate.save()
        if request.POST.get('content'):
            com = Survey_Comments()
            com.comments = request.POST.get("content")
            com.save()
        return render(request, "demo/Survey.html",
                      {'rating_form': rating_form, 'workid': workid-1})

    else:
        rating_form = RateListForm()
        return render(request, "demo/Survey.html",
                      {'rating_form': rating_form, 'workid': workid-1})

def demo_table2(request, testnum):
    template = "demo/Example_2.html"
    testnum = int(testnum)
    db_adult = Adult.objects.all()[:200]
    dbo = db_adult[random_idx - 1:random_idx]
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

    neighboradult = neighbor.objects.all()
    testadults = [list(enumerate(neighboradult))[i] for i in testidx]
    if testnum < test_num-1:
        context = {'nextpage': 'Example_2/'+str(testnum+1),'testcase':testnum+1, 'testnum': testnum, 'db_adult': db_adult, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'dbl':dbl, 'style':style }
    else:
        context = {'nextpage': 'Survey', 'testcase':testnum+1, 'testnum': testnum, 'db_adult': db_adult, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'dbl':dbl, 'style':style}
    if request.method == "POST":
        return render(request, template,context)
    else:
        return render(request, template,context)

def demo_table3(request, testnum):
    template = "demo/Example_3.html"
    testnum = int(testnum)
    db_adult = Adult.objects.all()[:200]
    dbo = db_adult[random_idx - 1:random_idx]
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

    neighboradult = neighbor.objects.all()
    testadults = [list(enumerate(neighboradult))[i] for i in testidx]
    if testnum < test_num-1:
        context = {'nextpage': 'Example_3/'+str(testnum+1),'testcase':testnum+1, 'testnum': testnum, 'db_adult': db_adult, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'dbl':dbl, 'style':style }
    else:
        context = {'nextpage': 'Survey', 'testcase':testnum+1, 'testnum': testnum, 'db_adult': db_adult, 'db': db, 'dbo': dbo,
                   'testadults': testadults[testnum][1], 'workid': workid - 1, 'dbl':dbl, 'style':style}
    if request.method == "POST":
        return render(request, template,context)
    else:
        return render(request, template,context)
