from .form import RadioButtonForm
from django.shortcuts import render
from operator import getitem
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from hostelapp.models import Information
from hostelapp.models import Meal


# Create your views here.

def hostelapp(request):
    return render(request, 'index.html')


@csrf_exempt
def aftersubmit(request):

    def cal():
        fooditem = request.POST["fooditem"]
        marketcost = request.POST['marketcost']
        member = request.POST['member']
        record = Information(
            fooditem=fooditem, marketcost=marketcost, member=member)
        record.save()
        millrate = int(marketcost)/(int(member)*6)
        return millrate

    millrate = cal()

    def masage():
        if millrate > 14:
            return "Your millrate is to high"
        else:
            return "Great job Maneger Continue"

    millrate = {"millrate": millrate, "masage": masage()}
    if request.method == "post":
        return render(request, "resultindex.html", millrate)
    return render(request, "resultindex.html", millrate)


# @csrf_exempt
# def mealview(request):
#     shakil = request.GET.get("shakil", False)
#     sadik = request.GET.get("sadik", False)
#     babu = request.GET.get("babu", False)

#     if request.method == 'POST':
#         form = RadioButtonForm(request.POST)
#         if form.is_valid():
#             shakil = form.cleaned_data["shakil"]
#             sadik = form.cleaned_data["sadik"]
#             babu = form.cleaned_data["babu"]
#             meal = Meal(person_1=shakil, person_2=sadik, person_3=babu)
#             meal.save()
#             return render(request, 'form.html', {'form': form, 'shakil': shakil, 'sadik': sadik, 'babu': babu})
#     else:
#         form = RadioButtonForm()
#         meal = meal(person_1=shakil, person_2=sadik, person_3=babu)
#         meal.save()
#     return render(request, 'form.html', {'form': form})
@csrf_exempt
def mealview(request):
    if request.method == 'POST':
        form = RadioButtonForm(request.POST)
        if form.is_valid():
            shakil = form.cleaned_data["shakil"]
            sadik = form.cleaned_data["sadik"]
            babu = form.cleaned_data["babu"]
            meal = Meal(person_1=shakil, person_2=sadik, person_3=babu)
            meal.save()
            return render(request, 'form.html', {'form': form, 'shakil': shakil, 'sadik': sadik, 'babu': babu})
    else:
        form = RadioButtonForm()
    return render(request, 'form.html', {'form': form})
