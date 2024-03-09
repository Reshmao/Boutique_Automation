from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)



class user(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    
class category(models.Model):
    category=models.CharField(max_length=225)

class design(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    design=models.CharField(max_length=225)
    dqty=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)
    image=models.CharField(max_length=1000)
    details=models.CharField(max_length=2000)
    size_details=models.CharField(max_length=2000)

class sizechart(models.Model):
    design=models.ForeignKey(design,on_delete=models.CASCADE)
    size=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class booking(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    sizechart=models.ForeignKey(sizechart,on_delete=models.CASCADE)
    total=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class bchild(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    design=models.ForeignKey(design,on_delete=models.CASCADE)
    qty=models.CharField(max_length=225)
    bamt=models.CharField(max_length=225)

class payment(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225) 
    date=models.CharField(max_length=225) 

class customised_design(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=225)
    cd_name=models.CharField(max_length=225)
    details=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)
    date=models.CharField(max_length=1000)
    status=models.CharField(max_length=2000)
    orderid=models.CharField(max_length=2000)


class cpayment(models.Model):
    customised_design=models.ForeignKey(customised_design,on_delete=models.CASCADE)
    camount=models.CharField(max_length=225) 
    cdate=models.CharField(max_length=225) 


class purchase(models.Model):
    design=models.ForeignKey(design,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)
    date=models.CharField(max_length=1000)
    details=models.CharField(max_length=2000)



class chat(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    chat=models.CharField(max_length=225)
    reply=models.CharField(max_length=225)
    date=models.CharField(max_length=1000)



class feedback(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=225)
    date=models.CharField(max_length=225)    

class refer_no(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    refer_no=models.CharField(max_length=225)
    date=models.CharField(max_length=225)    

class wishlist(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    design=models.ForeignKey(design,on_delete=models.CASCADE)    