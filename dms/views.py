from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout 
from donation .models import *
from datetime import date
from django.contrib import messages





def all_login(request):
        return render(request, 'all_login.html')


def index(request):
        return render(request, 'index.html')

def donor_login(request):
        if request.method == 'POST':
              u=request.POST['emailid']
              p=request.POST['pwd']
              user = authenticate(username=u,password=p)
              if user:
                    login(request,user)
                    error="no"
              else:
                    error="yes"
        return render(request,'donor_login.html',locals())       

def admin_login(request):
        if request.method == 'POST':
              u=request.POST['username']
              p=request.POST['pwd']
              user = authenticate(username=u,password=p)
              try:
                  if user.is_staff:
                    login(request,user)
                    error="no"
                  else:
                    error="yes"
              except:
                error="yes"        
        return render(request,'admin_login.html',locals())             

 
def volunteer_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"  
    return render(request, 'volunteer_login.html', {'error': error})


def donor_reg(request):
    error = ""
    if request.method == 'POST':
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        contact=request.POST['contact']
        pwd=request.POST['pwd']
        userpic=request.FILES['userpic']
        address=request.POST['firstname']

        try:
             user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
             Donor.objects.create(user=user,contact=contact,userpic=userpic,address=address)   
             error="no" 
        except:
              error="yes"    
    return render(request, 'donor_reg.html',locals())




def donor_home(request):
    if not request.user.is_authenticated:
         return redirect(request,'donor_login')
    return render(request,'donor_home.html')


def volunteer_home(request):
    if not request.user.is_authenticated:
         return redirect(request,'volunteer_login')
    return render(request,'volunteer_home.html')



def admin_home(request):
    if not request.user.is_authenticated:
         return redirect(request,'admin_login')
    return render(request,'admin_home.html')

def Logout(request):
      logout(request)
      return redirect('index')


def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method == 'POST':
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        try:
             Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,collectionloc=collectionloc,description=description,status="pending")
             error="no"      
        except:
               error="yes"          
    return render(request, 'donate_now.html',locals())
    



def donation_history(request):
        if not request.user.is_authenticated:
          return render(request, 'donor_login')
        user=request.user
        donor= Donor.objects.get(user=user)
        donation = Donation.objects.filter(donor=donor)
        return render(request, 'donation_history.html',locals())


def pending_donation(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        donation = Donation.objects.filter(status="pending")
        return render(request, 'pending_donation.html',locals())


def accepted_donation(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        donation = Donation.objects.filter(status="accept")
        return render(request, 'accepted_donation.html',locals())



def view_donationdetail(request,pid):
        if not request.user.is_authenticated:
          return render(request,'admin_login')
        donation = Donation.objects.get(id=pid)
        if request.method == "POST":
             status = request.POST['status']
             adminremark=request.POST['adminremark']


             try:
                 donation.adminremark=adminremark
                 donation.status=status
                 donation.updationdate=date.today()
                 donation.save()
                 error="no"
             except:
                 error="yes"    
        return render(request, 'view_donationdetail.html',locals())




def add_area(request):
    if not request.user.is_authenticated:
        return render(request, 'admin_login')
    if request.method == 'POST':
        areaname = request.POST['areaname']
        description = request.POST['description']
        try:
            DonationArea.objects.create(areaname=areaname, description=description)
            error = "no"
        except:
            error = "yes"
    else:
        error = None
    return render(request, 'add_area.html', locals())

    

def manage_area(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        area = DonationArea.objects.all()
        return render(request, 'manage_area.html',locals())



def edit_area(request,pid):
    if not request.user.is_authenticated:
        return render(request, 'admin_login')
    area = DonationArea.objects.get(id=pid)
    if request.method == 'POST':
        areaname = request.POST['areaname']
        description = request.POST['description']
        area.areaname=areaname
        area.description=description
        try:
            area.save()
            error = "no"
        except:
            error = "yes"
    else:
        error = None
    return render(request, 'edit_area.html', locals())


def delete_area(request,pid):
    area = DonationArea.objects.get(id=pid)
    area.delete()
    return redirect('manage_area')




def manage_donor(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        donor = Donor.objects.all()
        return render(request, 'manage_donor.html',locals())



def view_donordetail(request,pid):
    if not request.user.is_authenticated:
        return render(request, 'admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request,'view_donordetail.html', locals())


def delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('manage_donor')



def volunteer_reg(request):
    error = ""
    if request.method == 'POST':
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        contact=request.POST['contact']
        pwd=request.POST['pwd']
        userpic=request.FILES['userpic']
        idpic=request.FILES['idpic']
        address=request.POST['address']
        aboutme=request.POST['aboutme']

        try:
             user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
             Volunteer.objects.create(user=user,contact=contact,userpic=userpic,idpic=idpic,address=address,aboutme=aboutme,status="pending")   
             error="no" 
        except:
             error="yes"    
    return render(request, 'volunteer_reg.html', locals())




def new_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        volunteer = Volunteer.objects.filter(status="pending")
        return render(request, 'new_volunteer.html',locals())




def view_volunteerdetail(request,pid):
        if not request.user.is_authenticated:
          return render(request,'admin_login')
        volunteer = Volunteer.objects.get(id=pid)
        if request.method == "POST":
             status = request.POST['status']
             adminremark=request.POST['adminremark']

             try:
                 volunteer.adminremark=adminremark
                 volunteer.status=status
                 volunteer.updationdate=date.today()
                 volunteer.save()
                 error="no"
             except:
                 error="yes"    
        return render(request, 'view_volunteerdetail.html',locals())



def accepted_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        volunteer = Volunteer.objects.filter(status="accept")
        return render(request, 'accepted_volunteer.html',locals())





def rejected_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        volunteer = Volunteer.objects.filter(status="reject")
        return render(request, 'rejected_volunteer.html',locals())

def all_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'admin_login')
        volunteer = Volunteer.objects.all()
        return render(request, 'all_volunteer.html',locals())





def delete_volunteer(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')


def accepted_donationdetail(request,pid):
        if not request.user.is_authenticated:
          return render(request,'admin_login')
        donation = Donation.objects.get(id=pid)
        donationarea=DonationArea.objects.all()
        volunteer=Volunteer.objects.all()
        if request.method == "POST":
             donationareaid = request.POST['donationareaid']
             volunteerid=request.POST['volunteerid']
             da=DonationArea.objects.get(id=donationareaid)
             v=Volunteer.objects.get(id=volunteerid)

             try:
                 donation.donationarea=da
                 donation.volunteer=v
                 donation.status="Volunteer Allocated"
                 donation.updationdate=date.today()
                 donation.save()
                 error="no"
             except:
                 error="yes"    
        return render(request, 'accepted_donationdetail.html',locals())



def collection_req(request):
        if not request.user.is_authenticated:
          return render(request, 'volunteer_login')
        user=request.user
        volunteer = Volunteer.objects.get(user=user)
        donation  = Donation.objects.filter(volunteer=volunteer,status="Volunteer Allocated")
        return render(request, 'collection_req.html',locals())



def donationcollection_detail(request,pid):
        if not request.user.is_authenticated:
          return render(request,'volunteer_login')
        donation = Donation.objects.get(id=pid)
        if request.method == "POST":
             status=request.POST['status']
             volunteerremark=request.POST['volunteerremark']
             try:
                 donation.status=status
                 donation.volunteerremark=volunteerremark
                 donation.updationdate=date.today()
                 donation.save()
                 error="no"
             except:
                 error="yes"    
        return render(request, 'donationcollection_detail.html',locals())




def donationrec_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'volunteer_login')
        user=request.user
        volunteer = Volunteer.objects.get(user=user)
        donation  = Donation.objects.filter(volunteer=volunteer,status="Donation Received")
        return render(request, 'donationrec_volunteer.html',locals())




def donationrec_detail(request,pid):
        if not request.user.is_authenticated:
          return render(request,'volunteer_login')
        donation = Donation.objects.get(id=pid)
        if request.method == "POST":
             status=request.POST['status']
             deliverypic=request.FILES['deliverypic']
             try:
                 donation.status=status
                 donation.updationdate=date.today()
                 donation.save()
                 Gallery.objects.create(donation=donation,deliverypic=deliverypic,)
                 error="no"
             except:
                 error="yes"    
        return render(request, 'donationrec_detail.html',locals())



def donationnotrec_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'volunteer_login')
        user=request.user
        volunteer = Volunteer.objects.get(user=user)
        donation  = Donation.objects.filter(volunteer=volunteer,status="Donation NotReceived")
        return render(request, 'donationrec_volunteer.html',locals())


def donationdelivered_volunteer(request):
        if not request.user.is_authenticated:
          return render(request, 'volunteer_login')
        user=request.user
        volunteer = Volunteer.objects.get(user=user)
        donation  = Donation.objects.filter(volunteer=volunteer,status="Donation Delivered Successfully")
        return render(request, 'donationdelivered_volunteer.html',locals())



def profile_volunteer(request):   
    if not request.user.is_authenticated:
       return render(request, 'volunteer_login')
    error = ""
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        userpic = request.FILES['userpic'] if 'userpic' in request.FILES else volunteer.userpic
        idpic = request.FILES['idpic'] if 'idpic' in request.FILES else volunteer.idpic
        address = request.POST['address']
        aboutme = request.POST['aboutme']

        try:
            if user.first_name != fn:
                user.first_name = fn
            if user.last_name != ln:
                user.last_name = ln
            if user.username != em:
                user.username = em
            user.save()

            if volunteer.contact != contact:
                volunteer.contact = contact
                volunteer.userpic = userpic
                volunteer.idpic = idpic
            if volunteer.address != address:
                volunteer.address = address
            if volunteer.aboutme != aboutme:
                volunteer.aboutme = aboutme
            volunteer.save()

            error = "no" 
        except:
            error = "yes"    
    return render(request, 'profile_volunteer.html', locals())



def password_volunteer(request):
    error = ""
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if request.user.check_password(old_password):
            if new_password1 == new_password2:
                request.user.set_password(new_password1)
                request.user.save()
                return redirect('volunteer_login')
            else:
                error = "New passwords do not match."
        else:
            error = "Current password is incorrect."

    return render(request, 'password_volunteer.html', {'error': error})
