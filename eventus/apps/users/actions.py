from django.db.models import Model
from django.db.models.fields.files import FieldFile
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Usermodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("User")
    
    row_num = 0
    
    columns = [
        (u"ID", 2000),
        (u"username", 6000),
        (u"first_name", 8000),
        (u"last_name", 8000),
        (u"email", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.username,
            obj.first_name,
            obj.last_name,
            obj.email
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response
    
export_xls.short_description = u"Export XLS"