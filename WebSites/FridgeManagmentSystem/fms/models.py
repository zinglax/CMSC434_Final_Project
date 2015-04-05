from django.db import models

class Item(models.Model):

    # from barcode site
    status = models.CharField(max_length=150, blank=True, null=True) 
    lastModifiedUTC = models.CharField(max_length=150, blank=True, null=True) 
    description = models.CharField(max_length=150, blank=True, null=True) 
    noCacheAfterUTC = models.CharField(max_length=150, blank=True, null=True) 
    ean = models.CharField(max_length=150, blank=True, null=True) 
    upce = models.CharField(max_length=150, blank=True, null=True) 
    upc = models.CharField(max_length=150, blank=True, null=True) 
    pendingUpdates = models.CharField(max_length=150, blank=True, null=True) 
    found = models.CharField(max_length=150, blank=True, null=True) 
    message = models.CharField(max_length=150, blank=True, null=True) 
    size = models.CharField(max_length=150, blank=True, null=True) 
    issuerCountry = models.CharField(max_length=150, blank=True, null=True) 
    issuerCountryCode = models.CharField(max_length=150, blank=True, null=True) 
    
    # FMS fields
    quantity = models.CharField(max_length=150, blank=True, null=True) 
    expiration_date = models.CharField(max_length=150, blank=True, null=True) 
    
    # Hangers
    hung_on = models.ForeignKey('Hanger', blank=True, null=True,on_delete=models.SET_NULL, )
        
    def __unicode__(self):        
        return self.data 

# Create your models here.
####################################################
## Hangers: Objects that store only one type of django data field
##
## Example: String_Hanger class contains a CharField(max_length=150) and a pointer to 
## a Hanger
class Hanger(models.Model):
    
    # Name of Hanger (ex. Images)
    name = models.CharField(max_length=150, blank=True, null=True) 
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('self', blank=True, null=True,on_delete=models.SET_NULL, )
    
        
    def __unicode__(self):        
        return self.name  
    
    
####################################################
## String_Hanger: Can hang a string on a hanger
class Str_Hanger(models.Model):
    # String (ex. hello)
    data = models.CharField(max_length=500, blank=True, null=True) 
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('Hanger', blank=True, null=True,on_delete=models.SET_NULL, )
        
    def __unicode__(self):        
        return self.data  

####################################################
## Int_Hanger: Can hang a integer on a hanger
class Int_Hanger(models.Model):
    # int (ex. hello)
    data = models.IntegerField(blank=True, null=True)
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('Hanger', blank=True, null=True,on_delete=models.SET_NULL, )
      
    def __unicode__(self):        
        return self.data          
    
    
####################################################
## Boolean_Hanger: Can hang a boolean on a hanger
class Boolean_Hanger(models.Model):
    # Boolean Value (ex. True)
    data = models.NullBooleanField(blank=True, null=True)
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('Hanger', blank=True, null=True,on_delete=models.SET_NULL, )
      
    def __unicode__(self):        
        return self.data      
    
####################################################
## Email_Hanger: Can hang a email address on a hanger
class Email_Hanger(models.Model):
    # Boolean Value (ex. True)
    data = models.EmailField(blank=True, null=True)
    
    # Where is this Hanger Hung
    hung_on = models.ForeignKey('Hanger', blank=True, null=True,on_delete=models.SET_NULL, )
      
    def __unicode__(self):        
        return self.data     