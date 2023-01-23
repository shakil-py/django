from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Information


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

    millrate=cal()

    def masage():
        if millrate > 14:
            return "Your millrate is to high"
        else:
            return "Great job Maneger Continue"


    millrate = {"millrate":millrate, "masage": masage()}
    if request.method == "post":
        return render(request, "resultindex.html", millrate)
    return render(request, "resultindex.html", millrate)
