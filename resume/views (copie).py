import os, codecs
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.views.generic import View, ListView
from django.contrib import messages

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

from django.http import HttpResponse
from django.template.loader import get_template

#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.

from xhtml2pdf import pisa
#difine render_to_pdf() function

#importing get_template from loader
from django.template.loader import get_template
from django_xhtml2pdf.utils import pdf_decorator
from formtools.wizard.views import SessionWizardView
from resume.forms import BookFormset0, BookFormset1, Education, ProfileInfo

"""
3 solutions :
    * xhtml2pdf PIZA
    * Reportlab
    * weasyprint
    * easypdf
    * sudo apt-get install wkhtmltopdf
    http://localhost:8000/media/static/resume/img/profile_Haib9iq.jpg
    Or nodejs
    use NodeJS html-pdf npm package (see GitHub, install via: npm install -g html-pdf) as suggested in the comment. Usage:
    html-pdf http://example.com/ example.pdf

"""

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



def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()

     #This part will create the pdf.
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        personal_info = PersonalInfo.objects.filter(pk=2)
        context = {
              'personal_info': personal_info,
              }

        #getting the template
        #pdf = render_to_pdf('resume/pdf_cv.html', context)
        pdf = render_to_pdf('resume/cv_ckely.html', context)

         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


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


# ou avec l"executable


#-----------------------------------
# on genere le cv au format html
#-----------------------------------
def genereCvHtml2pdf(request, perso_id):

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    STATIC_ROOT         = os.path.join(BASE_DIR, 'resume/static')
    TEMPLATE_ROOT       = os.path.join(BASE_DIR, 'resume/templates/resume')


    # je cheche le cv enregiestre par id envoyé
    try :
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

    except Exception as message:
        messages.success(request, " pb de %s ... " % str(message))
        return HttpResponseRedirect("/")

    # ecrire en fichier

    with  codecs.open("resume/out/cv_moderne_%s.html" % perso_id, 'w', 'utf-8') as fd_out :
        content = render_to_string( "resume/pdf_cv.html", locals())
        fd_out.write(content)


     # save en pdf
    # wkhtmltopdf
    try :
        os.system("wkhtmltopdf  http://localhost:8000/ resume/out/cv_moderne_%s.pdf" % (perso_id))
    except (TypeError, ValueError) as err:
        messages.success(request, "oups erreur ! %s ... " % str(err))
    except Exception as err:
        messages.success(request, "oups erreur ! %s ... " % str(err))

    return render(request, "resume/resume.html", locals())




class Resume_Forms(SessionWizardView):
    template_name = "resume/cv_form.html"

    TEMPLATES__={
        "step1":"resume/formpart_1.html",
        "step2":"resume/formpart_2.html",
    }

    form_list = [
        ("step1", ProfileInfo),
        ("step2",Education),
    ]

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):

        step1,step2 = form_list

        if step1.is_valid():
            for form in step1:
                firstname = form.cleaned_data["FirstName"]
                lastname = form.cleaned_data["LastName"]
                 
        else:
            message(request, "Step-1-Error")

        if step2.is_valid():
            school_data=[]
            for form0 in step2:
                title = form0.cleaned_data["title"]
                schoolname = form0.cleaned_data["schclgname"]
                yearstart = form0.cleaned_data["yearStart"]
                yearEnd = form0.cleaned_data["yearEnd"]

                school_data.append({
                    "title":title,
                    "schoolname":schoolname,
                    "yearstart":yearstart,
                    "yearEnd":yearEnd
                })

        else:
            message(request, "Step-2-Error")


        return  render(self.request,"Resume-{}.html".format(self.kwargs['pk']),
                       context = { 'form_data': [form.cleaned_data for form in form_list],
                                  })
