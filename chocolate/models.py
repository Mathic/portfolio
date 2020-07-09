from django.db import models

#"Company","Bar_Name","REF","Review_Date","Cocoa_Percent","Company_Location","Rating","Bean_Type","Origin"

# Create your models here.
class ChocolateBar(models.Model):
    company = models.CharField(max_length=40)
    bar_name = models.CharField(max_length=50)
    ref = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    date = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    company_location = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    bean_type = models.CharField(max_length=30, blank=True, null=True)
    bean_origin = models.CharField(max_length=30)

    def __str__(self):
        return str(self.rating) + ' ' + str(self.bean_origin) + ' ' + str(self.bean_type)
