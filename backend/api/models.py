from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=10, null=True)
    civil_status = models.CharField(max_length=20, null=True)
    height = models.FloatField(default=1.70)
    weight = models.FloatField(default=70.0)
    blood_type = models.CharField(max_length=3, null=True)
    gsis_id_no = models.CharField(max_length=20, null=True)
    pagibig_id_no = models.CharField(max_length=20, null=True)
    philhealth_no = models.CharField(max_length=20, null=True)
    sss_no = models.CharField(max_length=20, null=True)
    tin_no = models.CharField(max_length=20, null=True)
    agency_employee_no = models.CharField(max_length=20, null=True)
    citizenship = models.CharField(max_length=50, null=True)
    residential_address = models.CharField(max_length=255, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    permanent_address = models.CharField(max_length=255, null=True)
    telephone_no = models.CharField(max_length=20, null=True)
    mobile_no = models.CharField(max_length=20, null=True)
    email_address = models.EmailField(null=True)
    fathers_name = models.CharField(max_length=100, null=True)
    mothers_name = models.CharField(max_length=100, null=True)

    def str(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"
