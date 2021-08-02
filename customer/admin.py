from django.contrib import admin
from .models import(
    Personal_Information,
    Document,
    Apply_Loan
)

# Register your models here.
@admin.register(Personal_Information)
class Personal_info_Admin(admin.ModelAdmin):
    list_display = ['id','Full_Name','Mother_Name','DOB','Age','Pin_code','Work_Type','Address_Type',
        'Aadhar_Card_Number','Pan_Card_Number'
    ]


@admin.register(Document)
class Document_Admin(admin.ModelAdmin):
    list_display = ['id','Front_Upload_Aadhar','Back_Upload_Aadhar',
        'Upload_Pancard','Upload_Image','Upload_Income_Proof','Upload_Residence_Proof'

    ]

@admin.register(Apply_Loan)
class loan_apply(admin.ModelAdmin):
    list_display = ['id','Company_Name','Salary','Amount_Need','Tenure','Rate']
