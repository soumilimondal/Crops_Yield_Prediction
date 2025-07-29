from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from joblib import load


rf = load("mysite/crops_final.joblib")



def home(request):
    return render(request,"a.html")

def pred(request):
    if request.method == "POST":
        try:
            nitrogen = float(request.POST.get('N', 0))
            phosphorus = float(request.POST.get('P', 0))
            potassium = float(request.POST.get('K', 0))
            temperature = float(request.POST.get('Temp', 0))
            humidity = float(request.POST.get('Hum', 0))
            ph = float(request.POST.get('Ph', 0))
            rainfall = float(request.POST.get('Ra', 0))

            ex = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]
            crop = rf.predict(ex)[0]
            return render(request, "pred.html", {'pcrop': crop})
            return JsonResponse({'predicted_crop': crop})

        except ValueError:
            return HttpResponse("Invalid input. Please ensure all fields are filled correctly.", status=400)
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)
