import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.views.generic import View, ListView

from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingArea, ProgrammingLanguage, Language
from .models import ProjectType, Project
from .models import Achievement, Publication


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from io import BytesIO #A stream implementation using an in-memory bytes buffer
                       # It inherits BufferIOBase

from django.http import HttpResponse
from django.template.loader import get_template

from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin
##
import reportlab
from django.http import FileResponse
from reportlab.pdfgen import canvas

"""
3 solutions :
    * xhtml2pdf PIZA
    * Reportlab
    * weasyprint
    * easypdf
    * sudo apt-get install wkhtmltopdf
"""

def reportpdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def index(request):
    perso_id = 2
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.filter(pk=perso_id)
    overview = Overview.objects.filter(personal=perso_id)[:1]
    education = Education.objects.filter(personal=perso_id)
    jobaccomplishment = JobAccomplishment.objects.filter(personal=perso_id)

    job_list = Job.objects.filter(personal=perso_id)
    skillset = Skillset.objects.filter(personal=perso_id)
    progarea = ProgrammingArea.objects.all()
    proglan = ProgrammingLanguage.objects.filter(personal=perso_id)
    language = Language.objects.filter(personal=perso_id)
    projtype = ProjectType.objects.all()

    project = Project.objects.filter(personal=perso_id)

    achievement = Achievement.objects.filter(personal=perso_id)
    publication = Publication.objects.filter(personal=perso_id)

    return render(request, 'resume/resume.html', {
        'site_name': site_name,
        'personal_info': personal_info,
        'overview' : overview,
        'education' : education,
        'language' : language,
        'job_list' : job_list,
        'skillset' : skillset,
        'progarea' : progarea,
        'proglan' : proglan,
        'projtype' : projtype,
        'project' : project,
        'achievement' : achievement,
        'publication' : publication,
    })


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def conv2pdf(request):
    ##
    return render(request, "resume/resume.html", locals())


# pip install django-xhtml2pdf
class ProductPdfView(PdfMixin, DetailView):
    model = PersonalInfo
    template_name = "resume/resume.html"


from django_xhtml2pdf.utils import pdf_decorator

@pdf_decorator
def myviewpdf(request):
    perso_id = 2
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.filter(pk=perso_id)
    return render(request, "resume/pdf_cv.html",
                  {
                      'site_name': site_name,
                      'personal_info': personal_info,
                  })


from django.http import HttpResponse
from django.template.loader import get_template

#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.

from xhtml2pdf import pisa
#difine render_to_pdf() function

def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()

     #This part will create the pdf.
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


#importing get_template from loader
from django.template.loader import get_template

#import render_to_pdf from util.py

#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        personal_info = PersonalInfo.objects.filter(pk=2)
        context = {
              'personal_info': personal_info,
              }

        #getting the template
        pdf = render_to_pdf('resume/pdf_cv.html', context)

         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
