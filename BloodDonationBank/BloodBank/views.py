from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Donor,Hospital,UserDetail
import time
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User



def index(request):
    context = {
        "Donor" : Donor.objects.all()
    }
    return render(request,"BloodBank/index.html",context)

def search(request):
    context = {
        "searchResult" :Hospital.objects.filter(Blood_Grp=request.POST.get('select')),
        "donorResult" :Donor.objects.filter(Blood_Grp=request.POST.get('select'))

    }
    return render(request,"BloodBank/beforeSearch.html",context)
def beforeSearch(request):
    return render(request,"BloodBank/beforeSearch.html")

def staff(request):
    return render(request,"BloodBank/staff.html")

def insertStock(request):
    return render(request,"BloodBank/insertStock.html")

def donorInfo(request):
    return render(request,"BloodBank/donorInfo.html")

def stockInfo(request):
    validation = []
    grp = request.GET['grp']
    stock = int(request.GET['stock'])
    code = request.GET['code']
    validation.append(grp)
    validation.append(stock)
    validation.append(code)
    if '' in validation:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

    try:
        try:
            user = User.objects.get(username=request.user.get_username)
            data = UserDetail.objects.get(Hos_Code=code,User_Name= user)
        except Exception as e:
            message="Check the Enter data"
            return HttpResponse(message)
        if data:
            insertResult=Hospital.objects.filter(Blood_Grp=grp,Hospital_Code=code)
            w = insertResult.first()
            w.stock = stock + w.stock
            w.save()
            message = 'Succeffull'
            context = {
            "result" : Hospital.objects.filter(Hospital_Code=code)
            }

            return render(request,"BloodBank/insertStock.html",context)
    except AttributeError as e:
        message = "Check entered data"
        return HttpResponse(message)

def getDonorInfo(request):
    donorBloodGrp = request.GET['donorBloodGrp']
    if 'donorBloodGrp' in request.GET:
        context = {
            "donorResult" :Donor.objects.filter(Blood_Grp=request.GET['donorBloodGrp']),
            "donorBloodGrp":donorBloodGrp

        }
        return render(request,"BloodBank/donorInfo.html",context)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def newUser(request):
    joinedDate = str(request.user.date_joined)
    first = joinedDate.split(" ")
    time1 = first[1].split(":")

    join_date = str(first[0])
    join_time = int(time1[0])*60 + int(time1[1])
    pc_time = time.ctime().split(" ")[3].split(":")

    pc1_time = int(pc_time[0])*60 + int(pc_time[1])
    pc1_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))

    active = request.user.is_active
    staff = request.user.is_staff

    user = User.objects.get(username=request.user.get_username)
    if not staff:
        if(join_date == pc1_date):
            if (join_time <= pc1_time):
                return render(request,"BloodBank/newUser.html")
    else:
        return render(request,"BloodBank/staff.html")

def getNewUserInfo(request):
    C = request.POST["Hospital_Code"]
    N = request.POST["Hos_Name"]

    G1 = request.POST["1"]
    S1 = request.POST["Stock1"]

    G2 = request.POST["2"]
    S2 = request.POST["Stock2"]

    G3 = request.POST["3"]
    S3 = request.POST["Stock3"]

    G4 = request.POST["4"]
    S4 = request.POST["Stock4"]

    G5 = request.POST["5"]
    S5 = request.POST["Stock5"]

    G6 = request.POST["6"]
    S6 = request.POST["Stock6"]

    G7 = request.POST["7"]
    S7 = request.POST["Stock7"]

    G8 = request.POST["8"]
    S8 = request.POST["Stock8"]

    A = request.POST["Hos_Address"]
    P = request.POST["Hos_PhoneNo"]
    E = request.POST["Hos_Email"]

    user = User.objects.get(username=request.user.get_username)
    try:
        o = UserDetail.objects.create(Hos_Code=C,User_Name=user)
    except IntegrityError:
        message = "Hospital Code already present"
        return HttpResponse(message)
    try:
        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G1 ,stock=S1 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)
        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G2 ,stock=S2 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)

        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G3 ,stock=S3 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)
        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G4 ,stock=S4 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)

        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G5 ,stock=S5 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)
        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G6 ,stock=S6 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)

        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G7 ,stock=S7 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)
        insertResult=Hospital.objects.create(Hospital_Code=C ,Hos_Name=N ,Blood_Grp=G8 ,stock=S8 ,Hos_Address=A ,Hos_PhoneNo=P ,Hos_Email=E)

        message = 'Succeffull'
        user = User.objects.get(username=request.user.get_username)
        user.is_staff = True
        user.save()
        context = {
        "thank":"Thank You",
        "result":"Insert New User Successfully "

        }
        return render(request,"BloodBank/newUser.html",context)
    except AttributeError as e:
        message = "Check entered data"
        return HttpResponse(message)


def donorRegistration(request):
    n=[]
    for i in range(17,71):
        n.append(i)
    context = {
    "n":n
    }
    return render(request,"BloodBank/donorRegistration.html",context)

def getDonorRegInfo(request):
    N = request.POST["Reg_Name"]
    A = request.POST.get("Reg_Age")

    G = request.POST.get("Reg_Gender")
    Grp = request.POST.get("Reg_grp")

    C = request.POST["Reg_PhoneNo"]

    n=[]
    for i in range(17,71):
        n.append(i)
    try:
        insertResult=Donor.objects.create(Name=N, Age=A, Gender=G, Blood_Grp=Grp, PhoneNo=C )
        context = {
        "Result":"Your Donation Save Life.",
        "thank" :"Thank You",
        "n":n
        }
        return render(request,"BloodBank/donorRegistration.html",context)
    except AttributeError as e:
        message = "Check entered data"
        return HttpResponse(message)
