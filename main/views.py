from django.shortcuts import render
from .models import CsvLoyalty2
from .models import CsvLoyalty
from .forms import Upload_Form
# Create your views here.

def uploadtest(request):
    if request.method == 'POST':
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['filespec']
            uploaded_file2 = "media/uploads/loyaltycodes/test.csv"
            filename = "media/uploads/loyaltycodes/%s" % uploaded_file.name
            fout = open(filename, 'wb+')
            for chunk in uploaded_file.chunks():
                fout.write(chunk)
            fout.close()
            # CsvLoyalty2.import_from_file(open(filename))
            CsvLoyalty.import_data(data=open(filename))
    else:
        form = Upload_Form()
    return render(request , 'main/upload_test.html', {'form': form})