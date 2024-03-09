from django.shortcuts import render,HttpResponse
from bouti.models import *
from django.core.files.storage import FileSystemStorage
import datetime
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def forgot_password(request):
    if request.method=="POST":
        fname=request.POST['fname']
        q=login.objects.filter(username=fname)
        if q:
            lid=q[0].id
            eid=q[0].username
            ut=q[0].usertype
            if ut=="user":
                qq=user.objects.filter(login_id=lid)
                if qq:
                    emails=qq[0].email
            elif ut=="pending":
                    return HttpResponse("<script>alert('YOUR ACCOUNT IS NOT VERIFIED !!!!!PLEASE CHECK YOUR MAIL TO VERIFY YOUR ACCOUNT');window.location='/forgot_password'</script>" )


            return HttpResponse("<script>alert('your username verified successfully');window.location='/set_password/%s/%s/%s'</script>" %(lid,eid,emails))
        else:
            return HttpResponse("<script>alert('Enter your correct username to verify');window.location='/forgot_password'</script>" )
    return render(request,'forgot_password.html')


def set_password(request,id,eid,emails):
    if request.method=="POST":
        cpwd=request.POST['cpwd']
        # confirm_encryptedpassword=make_password(cpwd)
        # print(confirm_encryptedpassword)
        q=login.objects.get(id=id)
        if q:
            q.password=cpwd
            q.save()
            subject = 'CHANGE PASSWORD'
            message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/login>click to login here</a>"
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emails]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("<script>alert('your password changed successfully');window.location='/login'</script>")


    return render(request,'set_password.html')






def index(request):
 
    q1=design.objects.all().order_by('-id')[:6]
    print('new arrivals',q1)
    return render(request,'index.html',{'q1':q1})

def logins(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        try:
            q=login.objects.get(username=u,password=p)
            request.session['login_id']=q.pk
            if q.usertype=="admin":
                return HttpResponse("<script>alert('login successfully');window.location='/adminhome'</script>")
            elif q.usertype=="user":            
                return HttpResponse("<script>alert('login successfully');window.location='/user_home'</script>")
        
        except:
            return HttpResponse("<script>alert('login failed');window.location='/login'</script>")


    return render(request, 'login.html')

def user_register(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']        
        g=request.POST['g']
        pincode=request.POST['pincode']
        lg=login.objects.filter(username=f)
        if lg:
            return HttpResponse("<script>alert('Username Already Existed');window.location='/user_register'</script>")
        else:
            le=user.objects.filter(email=e)
            if le:
                return HttpResponse("<script>alert('email already exist!!!Please Try Another Vaild Mail');window.location='/user_register'</script>")
            else:
                ql=login(username=f,password=g,usertype='pending')
                ql.save()
                q=user(fname=a,lname=b,place=c,phone=d,email=e,address=pincode,login=ql)
                q.save()
                subject = 'VERIFICATION'
                message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{ql.id}>verify</a>"
                
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e]
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponse("<script>alert('registered successfuly');alert('THANK YOU FOR REGISTERED WITH US !!!!!!PLEASE CHECK YOUR MAIL FOR ACCOUNT VERIFICATION');window.location='/login'</script>")

    return render(request,'user_register.html')


def acceptcustomer_username(request,id):
    cus=login.objects.get(id=id)
    cus.usertype='user'
    cus.save()
    return HttpResponse("<script>alert('Verified');window.location='/login'</script>")


# ===================================================admin==============================================
def admin_view_feedback(request):
    cus=feedback.objects.all()
    return render(request,'admin_view_feedback.html',{'cus':cus})

def admin_manage_sizechart(request,id):

    qry1=sizechart.objects.filter(design_id=id)

    if request.method=="POST":
        c=request.POST['cat']
        q=sizechart.objects.filter(size=c,design_id=id)
        if q:
            return HttpResponse("<script>alert('This size is Already added ');window.location='/admin_manage_sizechart/%s'</script>"%id)
        else:
            qry=sizechart(size=c,status='active',design_id=id)
            qry.save()
            return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_sizechart/%s'</script>"%id)
    return render(request,'admin_manage_sizechart.html',{'qry1':qry1})

def delete_sizechart(request,did,id):
    qry=sizechart.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_sizechart/%s'</script>"%did)

def size_active(request,did,id):
    q=sizechart.objects.get(id=id)
    q.status='active'
    q.save()
    return HttpResponse("<script>alert('active successfuly');window.location='/admin_manage_sizechart/%s'</script>"%did)

def size_deactive(request,did,id):
    q=sizechart.objects.get(id=id)
    q.status='deactive'
    q.save()
    return HttpResponse("<script>alert('deactive successfuly');window.location='/admin_manage_sizechart/%s'</script>"%did)










def adminhome(request):

    return render(request,'adminhome.html')



def admin_view_user(request):
    cus=user.objects.all()

    # # if request.method=="POST":
    # sname=request.POST['sname']

    return render(request,'admin_view_user.html',{'cus':cus})


def admin_manage_category(request):

    qry1=category.objects.all()

    if request.method=="POST":
        c=request.POST['cat']
        q=category.objects.filter(category=c)
        if q:
            return HttpResponse("<script>alert('This category is Already added ');window.location='/admin_manage_category'</script>")
        else:
            qry=category(category=c)
            qry.save()
            return HttpResponse("<script>alert('added successfully');window.location='/admin_manage_category' ;</script>")
    return render(request,'admin_manage_category.html',{'qry1':qry1})

def delete_category(request,id):
    qry=category.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/admin_manage_category'</script>")



def update_category(request,id):

    qry1=category.objects.all()
    up=category.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST['cat']
        up.category=cat
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_manage_category';</script>")
    return render(request,'admin_manage_category.html',{'up':up,'qry1':qry1})

def admin_manage_design(request):

    q=design.objects.filter()
    if request.method=="POST":
        a=request.POST['a']
        c=request.POST['c']
        b=request.POST['b']
        e=request.POST['e']
        size=request.POST['size']
        sd=request.FILES['sd']
        d=request.FILES['d']
        fs=FileSystemStorage()
        fn=fs.save(d.name,d)

        fss=FileSystemStorage()
        fns=fss.save(sd.name,sd)


        q=design.objects.filter(design=a)
        if q:
            return HttpResponse("<script>alert('This design is Already added ');window.location='/admin_manage_design'</script>")
        else:
            q=design(design=a,dqty=size,amount=b,image=fn,details=e,size_details=fns,category_id=c)
            q.save()
            return HttpResponse("<script>alert('added successfuly');window.location='/admin_manage_design'</script>")
    cat=category.objects.all()
    # result=[]
    # ss=fname
    
        
    return render(request,'admin_manage_design.html',{'q':q,'cat':cat})



def delete_design(request,id):
    q=design.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('deleted successfuly');window.location='/admin_manage_design'</script>")


def update_design(request,id):
    cat=category.objects.all()

    q=design.objects.all()

    up=design.objects.get(id=id)
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        ca=request.POST['ca']
        print(ca)
        d=request.FILES['d']
        e=request.POST['e']
        size=request.POST['size']
        sd=request.FILES['sd']

        fs=FileSystemStorage()
        fn=fs.save(d.name,d)

        fss=FileSystemStorage()
        fns=fss.save(sd.name,sd)
        up.design=a
        up.dqty=size
        up.amount=b
        up.category_id=ca
        up.image=fn
        up.details=e
        up.size_details=fns
        up.save()
        return HttpResponse("<script>alert(' updated successfully');window.location='/admin_manage_design'</script>")
    return render(request,'admin_manage_design.html',{'up':up,'q':q,'cat':cat})




def admin_manage_purchase(request):

    if request.method=="POST":
        a=request.POST['a']
        c=request.POST['c']
        b=request.POST['b']
        des=request.POST['des']
        
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
        q=purchase(design_id=a,quantity=b,amount=c,details=des,date=cdate)
        q.save()
        return HttpResponse("<script>alert('added successfuly');window.location='/admin_manage_purchase'</script>")
    q=design.objects.all()
    qry1=purchase.objects.all()
    # result=[]
    # ss=fname
      
    return render(request,'admin_manage_purchase.html',{'q':q,'qry1':qry1})



def delete_purchase(request,id):
    q=purchase.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('deleted successfuly');window.location='/admin_manage_purchase'</script>")


def update_purchase(request,id):
    qry1=purchase.objects.all()

    q=design.objects.all()

    up=purchase.objects.get(id=id)
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        des=request.POST['des']
        up.details=des
        up.design_id=a
        up.quantity=b
        up.amount=c
        up.save()
        return HttpResponse("<script>alert(' updated successfully');window.location='/admin_manage_purchase'</script>")
    return render(request,'admin_manage_purchase.html',{'up':up,'q':q,'qry1':qry1})




def admin_view_msg(request):
    cus=chat.objects.all()
    return render(request,'admin_view_msg.html',{'cus':cus})

def admin_send_reply(request,id):
    if request.method=="POST":
        a=request.POST['a']
        q=chat.objects.get(id=id)
        q.reply=a
        q.save()
        return HttpResponse("<script>alert('send successfully');window.location='/admin_view_msg';</script>")
    return render(request,'admin_send_reply.html')





def admin_view_bk(request):
    q=booking.objects.filter()
    print(q)
    return render(request,'admin_view_bk.html',{'q':q})

def admin_view_booking_details(request,id):
    q=bchild.objects.filter(booking_id=id)
    print(q)
    return render(request,'admin_view_booking_details.html',{'q':q})

def admin_view_payment(request,id):
    q=payment.objects.filter(booking__user__booking=id)
    print(q)
    return render(request,'admin_view_payment.html',{'q':q})



def admin_dispatch(request,id):
    import datetime
    cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
    if request.method=="POST":
        ref=request.POST['ref']
        q=refer_no(refer_no=ref,date=cdate,booking_id=id)
        q.save()
        return HttpResponse("<script>alert(' added successfully');window.location='/admin_view_bk';</script>")
    return render(request,'admin_dispatch.html')
# def admin_dispatch(request,id):
#     q=booking.objects.get(id=id)
#     q.status='dispatched'
#     q.save()
#     return HttpResponse("<script>alert(' dispatched successfully');window.location='/admin_view_bk';</script>")



def admin_customized_design(request):
    cus=customised_design.objects.all()

    # # if request.method=="POST":
    # sname=request.POST['sname']

    return render(request,'admin_customized_design.html',{'cus':cus})


def admin_accept(request,id):
    q=customised_design.objects.get(id=id)
    q.status='accept'
    q.save()
    return HttpResponse("<script>alert('accepted successfuly');window.location='/admin_customized_design'</script>")

def admin_reject(request,id):
    q=customised_design.objects.get(id=id)
    q.status='reject'
    q.save()
    return HttpResponse("<script>alert('rejected successfuly');window.location='/admin_customized_design'</script>")






def admin_add_amount(request,id):
    if request.method=="POST":
        amt=request.POST['amt']
        q=customised_design.objects.get(id=id)
        q.amount=amt
        q.save()
        return HttpResponse("<script>alert(' amount added successfully');window.location='/admin_customized_design';</script>")
    return render(request,'admin_add_amount.html')


def admin_view_cpayment(request,id):
    q=cpayment.objects.filter(customised_design__user__customised_design=id)
    print(q)
    return render(request,'admin_view_cpayment.html',{'q':q})



def admin_cdispatch(request,id):
    q=customised_design.objects.get(id=id)
    q.status='dispatched'
    q.save()
    return HttpResponse("<script>alert(' dispatched successfully');window.location='/admin_customized_design';</script>")

# =========================user====================================================

def user_view_profile(request):
    lid=request.session['login_id']
    sid=user.objects.filter(login=lid)
    if sid:
        cid=sid[0].id


    up=user.objects.get(id=cid)

    if request.method=="POST":
        fn=request.POST['a']
        ln=request.POST['b']
        place=request.POST['c']
        phone=request.POST['d']
        email=request.POST['e']
        address=request.POST['pincode']
        up.fname=fn
        up.lname=ln
        up.place=place
        up.phone=phone
        up.email=email
        up.address=address
        up.save()
        return HttpResponse("<script>alert('profile updated successfully');window.location='/user_view_profile'</script>")
 
    return render(request,'user_view_profile.html',{'up':up})







def user_add_feedback(request):
    lid=request.session['login_id']
    cid=user.objects.filter(login=lid)
    if cid:
        cus_id=cid[0].id

    import datetime
    cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

    if request.method=="POST":
        feedbacks=request.POST['feedback']
        q=feedback(user_id=cus_id,date=cdate,feedback=feedbacks)
        q.save()
       
        return HttpResponse("<script>alert('send successfully');window.location='/user_add_feedback'</script>")
    return render(request,'user_add_feedback.html')




def user_home(request):
    lid=request.session['login_id']
    cid=user.objects.filter(login=lid)
    if cid:
        cus_id=cid[0].id
        fname=cid[0].fname
        lname=cid[0].lname

    return render(request,'user_home.html',{'fname':fname,'lname':lname})

def user_view_design(request):
    # lid=request.session['login_id']
    # sid=customerr.objects.filter(login=lid)
    # if sid:
    #     cid=sid[0].id
    #     fname=sid[0].fname
    #     print(cid)
    q=design.objects.all()
    if request.method=="POST":
        sname=request.POST['sname']
        # print(q)
    
        q=design.objects.filter(design=sname)
        print(q)
    ss={}
  
    ss['q']=q
    # print(ss)
    return render(request,'user_view_design.html',ss)


def customer_add_cart(request,id,design,amount,image,dqty):
    q=sizechart.objects.filter(design_id=id,status='active')
    import datetime
    lid=request.session['login_id']
    sid=user.objects.filter(login=lid)
    if sid:

        cid=sid[0].id
        fname=sid[0].fname
        print(cid)
    if request.method=="POST":
        tot=request.POST['to']
        rate=request.POST['rate']
        qty=request.POST['qty']
        si=request.POST['si']
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
        q=booking.objects.filter(status='pending',user_id=cid)        
        if q:
            bk_id=q[0].id
            total=q[0].total.split(".")
            print('........',bk_id)
            qqq=bchild.objects.filter(design_id=id,booking_id=bk_id)
            if qqq:
                bc_id=qqq[0].id
                bc_qty=qqq[0].qty
                bc_amt=qqq[0].bamt
                qq=bchild.objects.get(id=bc_id)
                qq.qty=int(qty)+int(bc_qty)
                qq.bamt=int(bc_amt)+int(tot)
                qq.save()
                q2=booking.objects.get(id=bk_id)
                q2.total=int(total[0])+int(tot)
                q2.save()
                # return HttpResponse("<script>alert('Product added to cart');window.location='/customer_view_product/%s'</script>" %id)
                return HttpResponse("<script>alert('Product added to cart');window.location='/user_view_booking'</script>")

            else:
                rates=int(qty)*int(rate)
                qq=bchild(qty=qty,bamt=tot,booking_id=bk_id,design_id=id)
                qq.save()
                q1=booking.objects.get(id=bk_id)
                q1.total=int(total[0])+int(tot)
                q1.save()
                # return HttpResponse("<script>alert('Product added to cart');window.location='/customer_view_product/%s'</script>" %id)
                return HttpResponse("<script>alert('Product added to cart');window.location='/user_view_booking'</script>")

        else:
            rates=int(qty)*int(rate)
            q=booking(total=tot,date=cdate,status='pending',user_id=cid,sizechart_id=si)
            q.save()
            q1=bchild(qty=qty,bamt=tot,booking=q,design_id=id)
            q1.save()
            # return HttpResponse("<script>alert('Product added to cart ');window.location='/customer_view_product/%s'</script>" %id)
            return HttpResponse("<script>alert('Product added to cart');window.location='/user_view_booking'</script>")


    ss={}

    ss['design']=design
    ss['amount']=amount
    ss['image']=image
    ss['dqty']=dqty
    ss['q']=q

    return render(request,'customer_add_cart.html',ss)



def user_view_booking(request):
    lid=request.session['login_id']
    sid=user.objects.filter(login=lid)
    if sid:
        uid=sid[0].id
    q=booking.objects.filter(user_id=uid)
    print(q)
    return render(request,'user_view_booking.html',{'q':q})

def user_view_booking_details(request,id):
    q=bchild.objects.filter(booking_id=id)
    print(q)
    return render(request,'user_view_booking_details.html',{'q':q})

def user_view_reference(request,id):
    q=refer_no.objects.filter(booking_id=id)
    print(q)
    return render(request,'user_view_reference.html',{'q':q})





def rpay(request):
    print("Haiiiiiiiii")
    
    

    # Get the order ID
    order_id = request.GET['order_id']
    order_id = request.GET['order_id']
    print(order_id)
    s=booking.objects.get(id=id)
    if s:
        s.status='Shipped'
        s.order_id=order_id
        s.save() 
    od=booking.objects.filter(booking_id=id)
    print(od)
    if od:
        for i in od:
            pid=i.product_id
            qtys=i.quantity
            print(pid,"....................proid")
            print(qtys,"..................qty")

            pp=design.objects.get(id=pid)
            # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
            if pp:
                pro_qty=pp.stock
                print(pro_qty,"############pro_qty")
                pp.stock=int(pro_qty)-int(qtys)
                pp.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/adminhome';</script>")
   
    return render(request, 'orders.html',context)


def user_payment_completes(request,id):

    # # print(order_id)
    # s=booking.objects.get(id=id)
    # if s:
    #     s.status='paid'
    #     s.save() 

    q1=booking.objects.get(id=id)
    if q1:
        q1.status='paid'
        # q1.orderid=order_id
        q1.save()




    q2=bchild.objects.filter(booking_id=id)
    for i in q2:
        # bid=i.booking_id
        bqty=i.qty
        # print(';;;;;;;;;;;;;-------------------------;;;;;;;;',bid)
        print(';;;;;;;;;;;;;;;;;;;;;',bqty)
        design_id=i.design_id
        print('================',design_id)
        q3=design.objects.get(id=design_id)
        if q3:
            p_qty=q3.dqty
            q3.dqty=int(p_qty)-int(bqty)
            q3.save()
        # q4=purchase.objects.get(design_id=design_id)
        # if q4:
        #     pur_qty=q4.quantity
        #     q4.dqty=int(pur_qty)-int(bqty)
        #     q4.save()

    # q=payment(amount=total,date=cdate,booking_id=id)
    # q.save()
    # q1=booking.objects.get(id=bk_id)
    # q1.status='paid'
    # q1.save()
    # q1=booking.objects.get(id=id)
    # q1.status='paid'
    # q1.orderid=order_id
    # q1.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")


def customer_make_payment(request,id,total):
    lid=request.session['login_id']
    cid=user.objects.filter(login=lid)

    # ss={}
 
    # ss['total']=total
    # ss['ids']=id

    return render(request,'customer_make_payment.html',{'total':total,'ids':id})





# def customer_make_payment(request,id,total):

#     lid=request.session['login_id']
#     cid=user.objects.filter(login=lid)

#     ss={}
 
#     ss['total']=total

#     if request.method=="POST":
#         cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
#         # q=payment(amount=total,date=cdate,booking_id=id)
#         # q.save()
#         amount = total
#         currency="INR"

#             # Create Razorpay client object

#         razorpay_client = Client(auth=("rzp_test_myOF7jDpkIqeD0", "lGAkCY9inaIl4fS1apPqP7Gi"))

#             # Create a payment
#         order = razorpay_client.order.create({
#             "amount": amount,
#             "currency": currency,
#             'receipt': 'receipt_id'
#         })

#         # Get the order ID
#         order_id = order['id']
#         print(order_id)
#         print("AHiiiiiiii")





#         q2=bchild.objects.filter(booking_id=id)
#         for i in q2:
#             # bid=i.booking_id
#             bqty=i.qty
#             # print(';;;;;;;;;;;;;-------------------------;;;;;;;;',bid)
#             print(';;;;;;;;;;;;;;;;;;;;;',bqty)
#             design_id=i.design_id
#             print('================',design_id)
#             q3=design.objects.get(id=design_id)
#             if q3:
#                 p_qty=q3.dqty
#                 q3.dqty=int(p_qty)-int(bqty)
#                 q3.save()
#         # q=payment(amount=total,date=cdate,booking_id=id)
#         # q.save()
#         # q1=booking.objects.get(id=bk_id)
#         # q1.status='paid'
#         # q1.save()
#         q1=booking.objects.get(id=id)
#         q1.status='paid'
#         q1.orderid=order_id
#         q1.save()
#         return HttpResponse("<script>alert('paid successfully');window.location='/user_view_booking'</script>")
#     return render(request,'customer_make_payment.html',ss)




def user_add_cdesgin(request):
    cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

    lid=request.session['login_id']
    cid=user.objects.filter(login=lid)
    if cid:
        uid=cid[0].id
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        # c=request.POST['c']
        des=request.POST['des']
        q=customised_design(quantity=a,cd_name=b,details=des,amount='pending',date=cdate,status='pending',user_id=uid)
        q.save()
        return HttpResponse("<script>alert('added successfuly');window.location='/user_add_cdesgin'</script>")
    q=customised_design.objects.filter(user_id=uid)

    return render(request,'user_add_cdesgin.html',{'q':q})





def user_payment_complete(request,id):

    q1=customised_design.objects.get(id=id)
    q1.status='paid'
    # q1.orderid=order_id
    q1.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")


def customer_make_cpayment(request,id,total):
    from datetime import datetime,date
    today=date.today()
    print(today)
    print(">>>>>>>>>>>>>>>>",total)


       
    ss={}
   
    ss['total']=total
    return render(request,'customer_make_cpayment.html',{'total':total,'ids':id})

















# def customer_make_cpayment(request,id,total):

#     if request.method=="POST":
#         cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
#         # q=cpayment(camount=total,cdate=cdate,customised_design_id=id)
#         # q.save()
#         amount = total
#         currency="INR"

#             # Create Razorpay client object

#         razorpay_client = Client(auth=("rzp_test_myOF7jDpkIqeD0", "lGAkCY9inaIl4fS1apPqP7Gi"))

#             # Create a payment
#         order = razorpay_client.order.create({
#             "amount": amount,
#             "currency": currency,
#             'receipt': 'receipt_id'
#         })

#         # Get the order ID
#         order_id = order['id']
#         print(order_id)
#         print("AHiiiiiiii")
#         q1=customised_design.objects.get(id=id)
#         q1.status='paid'
#         q1.orderid=order_id
#         q1.save()
#         return HttpResponse("<script>alert('paid successfully');window.location='/user_add_cdesgin'</script>")


#     return render(request,'customer_make_cpayment.html',{'total':total})

























def user_send_msg(request):

    lid=request.session['login_id']
    cid=user.objects.filter(login=lid)
    if cid:
        uid=cid[0].id
    if request.method=="POST":
        a=request.POST['cat']
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
        q=chat(user_id=uid,chat=a,reply='pending',date=cdate)
        q.save()
        return HttpResponse("<script>alert('send successfuly');window.location='/user_send_msg'</script>")
    q=chat.objects.filter(user_id=uid)
    # result=[]
    # ss=fname
      
    return render(request,'user_send_msg.html',{'q':q})



def customer_add_wlist(request,id):
    lid=request.session['login_id']
    sid=user.objects.filter(login=lid)
    if sid:
        cid=sid[0].id
    #     fname=sid[0].fname
    #     print(cid)
    q=wishlist.objects.filter(design_id=id,user_id=cid)
    if q:
        return HttpResponse("<script>alert('Product already added to wishlist');window.location='/user_view_design'</script>")
    else:
        q=wishlist(design_id=id,user_id=cid)
        q.save()
        return HttpResponse("<script>alert('Product added to wishlist');window.location='/customer_view_wlist'</script>" )

  
def customer_remove_wlist(request,id):
    q=wishlist.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Product removed to wishlist');window.location='/customer_view_wlist'</script>" )




def customer_view_wlist(request):
    lid=request.session['login_id']
    sid=user.objects.filter(login=lid)
    if sid:
        cid=sid[0].id
    #     fname=sid[0].fname
    #     print(cid)
    q=wishlist.objects.filter(user_id=cid)
    # if request.method=="POST":
    #     sname=request.POST['sname']
    #     # print(q)
    
    #     if int(id)==0:
    #         print("haiiiiii")
    #         q=product.objects.filter(product=sname)
    #     else:
    #         q=product.objects.filter(subcategory_id=id)
    #         print(q)
    ss={}

    ss['q']=q
    # print(ss)
    return render(request,'customer_view_wlist.html',ss)





def user_view_cancel(request,id):

    q2=bchild.objects.filter(booking_id=id)
    for i in q2:
        # bid=i.booking_id
        bqty=i.qty
        # print(';;;;;;;;;;;;;-------------------------;;;;;;;;',bid)
        print(';;;;;;;;;;;;;;;;;;;;;',bqty)
        design_id=i.design_id
        print('================',design_id)
        q3=design.objects.get(id=design_id)
        if q3:
            p_qty=q3.dqty
            q3.dqty=int(p_qty)+int(bqty)
            q3.save()
  
    q1=booking.objects.get(id=id)
    q1.status='cancelled'
    q1.save()

    return HttpResponse("<script>alert('Cancelled Successfully');window.location='/user_view_booking'</script>" )
