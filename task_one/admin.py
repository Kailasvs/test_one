from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin
from .models import Hospital, Doctors

class DoctorsResource(resources.ModelResource):
    # specify custom widget for foreign key field
    fk_hospital = fields.Field(
        column_name='fk_hospital',
        attribute='fk_hospital',
        widget=widgets.ForeignKeyWidget(Hospital)
    )

    class Meta:
        model = Doctors
        fields = ('id', 'name', 'fk_hospital', 'experience','biography','education')

    def before_import_row(self, row, **kwargs):
        # check for duplicates and skip importing row if necessary
        if Doctors.objects.filter(name=row['name']).exists():
            return None

@admin.register(Doctors)
class Doctorsadmin(ImportExportModelAdmin):
    resource_class = DoctorsResource