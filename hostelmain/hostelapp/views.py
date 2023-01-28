from .models import meal
from django.shortcuts import render, redirect
from operator import getitem
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


# def millsubmit(request):
#     # name = request.POST["Shakil"]
#     # mealvalue = request.POST["value"]
#     # record = Information(name=name, mealvalue=mealvalue)
#     # record.save()

#     shakil_choice = request.POST.get("Shakil")
#     sadik_choice = request.POST.get("Sadik")
#     babu_choice = request.POST.get("Babu")
#     # Do something with the selected values
#     HostelappMillamaount.objects.create(shakil=shakil_choice, sadik=sadik_choice, babu=babu_choice)

#     if request.method == "post":
#         return render(request, "millindex.html")
#     return render(request, "millindex.html")


# def my_view(request):
#     if request.method == "POST":
#         shakil_choice = request.POST.get("Shakil")
#         sadik_choice = request.POST.get("Sadik")
#         babu_choice = request.POST.get("Babu")
#         if shakil_choice and sadik_choice and babu_choice:
#             # Create a new instance of the model
#             my_model_instance = MyModel()
#             my_model_instance.shakil = shakil_choice
#             my_model_instance.sadik = sadik_choice
#             my_model_instance.babu = babu_choice
#             # Save the instance to the database
#             my_model_instance.save()
#             return redirect('success_view')
#         else:
#             return redirect('error_view')
#     return render(request, 'millindex.html')
@csrf_exempt
def mmealview(request):
    # person_1 = request.post.get(redio_btn="redio-btn")

    # record = meal(person_1=person_1,)
    # record.save()
    # if request.method == "post":
    #     name = request.POST.get("")

    #     return redirect("sucess")
    if request.method == 'POST':
        print("ok")
        radio_choice = request.POST.get(
            'radio_button')

        # Save the radio choice to the database
        model_instance = meal(person_1=radio_choice)
        model_instance.save()
        return render(request, 'millindex.html')
    else:
        return render(request, 'millindex.html')
