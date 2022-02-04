import os, codecs
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
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
from . import models

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
from resume import forms as cv_forms
from resume.models import  Education, PersonalInfo, JobAccomplishment

from django.conf import settings
from django.core.files.storage import FileSystemStorage


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
    personal_info = PersonalInfo.objects.get(pk=perso_id)
    overview = Overview.objects.get(personal=perso_id)
    education = Education.objects.filter(personal=perso_id).exclude(name__istartswith='Formation')
    formations = Education.objects.filter(personal=perso_id, name__istartswith='Formation')
    jobaccomplishment = JobAccomplishment.objects.filter(personal=perso_id)

    job_list = Job.objects.filter(personal=perso_id)
    skillset = Skill.objects.filter(personal=perso_id)
    progarea = ProgrammingArea.objects.all()
    proglan = ProgrammingLanguage.objects.filter()
    languages = models.MesLanguages.objects.filter(personal=perso_id)
    projtype = ProjectType.objects.all()

    project = Project.objects.filter(personal=perso_id)

    achievement = Achievement.objects.filter(personal=perso_id)
    publication = Publication.objects.filter(personal=perso_id)

    return render(request, 'resume/dev_resume.html', {
        'site_name': site_name,
        'pinfo': personal_info,
        'overview' : overview,
        'educations' : education,
        'formations': formations,
        'languages' : languages,
        'job_list' : job_list,
        'skills' : skillset,
        'progarea' : progarea,
        'proglan' : proglan,
        'projtype' : projtype,
        'projects' : project,
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

     #This part will Miscellaneous projects involving InterSystems' technologycreate the pdf.
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
        pdf = render_to_pdf('resume/dev_resume.html', context)

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
    PDF_DIR             = os.path.join(BASE_DIR, 'resume/out')


    # je cheche le cv enregiestre par id envoyé
    try :
        perso_id = 2
        """
        site_name = RequestSite(request).domain
        """
        pinfo = PersonalInfo.objects.get(pk=perso_id)
        
        overview = Overview.objects.get(personal=perso_id)
        educations = Education.objects.filter(personal=perso_id).exclude(name__istartswith='Formation')
        formations = Education.objects.filter(personal=perso_id, name__istartswith='Formation')
        jobaccomplishment = JobAccomplishment.objects.filter(personal=perso_id)
        
        job_list = Job.objects.filter(personal=perso_id)
        skills = Skill.objects.filter(personal=perso_id)
        progarea = ProgrammingArea.objects.all()
        proglan = ProgrammingLanguage.objects.filter()
        languages = models.MesLanguages.objects.filter(personal=perso_id)
        projtype = ProjectType.objects.all()

        projects = Project.objects.filter(personal=perso_id)

        job_list = Job.objects.filter(personal=perso_id)
        skillset = Skillset.objects.all().order_by("name")
        ##
        mes_skills = {}
        for sks in skillset :
            mes_skills[sks.name] = sks.mes_skills.all().filter(personal=perso_id)

        project = Project.objects.filter(personal=perso_id)
        
        achievement = Achievement.objects.filter(personal=perso_id)
        publication = Publication.objects.filter(personal=perso_id)

    except Exception as message:
        messages.success(request, " pb de dans lecture de donnée ! %s ... " % str(message))
        return HttpResponseRedirect("/")

    # ecrire en fichier

    with  codecs.open("resume/out/cv_moderne_%s.html" % perso_id, 'w', 'utf-8') as fd_out :
        content = render_to_string( "resume/dev_resume.html", locals())
        #content = render_to_string( "resume/html_cv.html", locals())
        fd_out.write(content)


     # save en pdf
    # wkhtmltopdf
    try :
        os.system("wkhtmltopdf  {1}/cv_moderne_{0}.html {1}/cv_moderne_{0}.pdf".format(perso_id, PDF_DIR))
    except (TypeError, ValueError) as err:
        messages.success(request, "oups erreur ! %s ... " % str(err))
    except Exception as err:
        messages.success(request, "oups Exception ! %s ... " % str(err))

    return render(request, "resume/dev_resume.html", locals())



class Resume_Forms(SessionWizardView):
    #template_name = "resume/cv_form_1.html"
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))


    TEMPLATES={
        "step1":"resume/cv_form_1.html",
        "step2":"resume/cv_form_12.html",
        "step3":"resume/cv_form_2.html",
        "step4":"resume/cv_form_3.html",
        "step5":"resume/cv_form_4.html",
        "step6":"resume/cv_form_5.html",
    }

    form_list = [
        ("step1", cv_forms.BookFormset1),
        ("step2", cv_forms.BookFormset12),
        ("step3", cv_forms.BookFormset2),
        ("step4", cv_forms.BookFormset3),
        ("step5", cv_forms.BookFormset4),
        ("step6", cv_forms.ProjectForm),
    ]

    def get_context_data(self, form, **kwargs):
        # messages.add_message(self.request, messages.INFO, "self.steps.current = {}".format(self.steps.current))
        context = super(Resume_Forms, self).get_context_data(form=form, **kwargs)
        #if self.steps.current == 'step1':
        context.update(self.storage.extra_data)
        context['STEP_NUMBER'] = self.steps.current
        # update form instance
        """
        form.initial.update({
            'user' : self.request.user,
        })
        """

        context['wizard'].update( {
            'form': form,
            'steps': self.steps,
        })


        return context

    def get_template_names(self):
        return[self.TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict,  **kwargs):
        step1,step2, step3, step4, step5, step6 = form_list
        # identite
        if step1.is_valid():
            school_data=[]
            for form in step1:

                try :
                    # user = form_dict['step1']['user']
                    # save personal
                    #personal = form_dict['step1'].save()
                    personal = form.save()
                    # save un overview
                    apercu = form_dict['step1'][0]['apercu'].data
                    Overview.objects.create(personal=personal, text=apercu)
                except Exception as err:
                    messages.add_message(self.request, messages.INFO,
                                        'Error : form is not valide in step1  err={}'.format( err))
                    return HttpResponseRedirect('/')

        # identite Suite
        if step2.is_valid():
            #--
            for form in step2:
                try :

                    personal.email = form_dict['step2'][0]['email'].data
                    personal.linkedin = form_dict['step2'][0]['linkedin'].data
                    personal.facebook = form_dict['step2'][0]['facebook'].data
                    ## add language
                    languages = form_dict['step2'][0]['language'].data
                    ##  personal.language =['14', '12', '13']
                    for lang_id in languages :
                        models.MesLanguages.objects.create(language_id=lang_id, personal=personal)

                    messages.add_message(self.request, messages.INFO,
                                        'identite plus : personal.language ={}'.format(languages))

                    # save personal
                    personal.save()

                except Exception as err:
                    messages.add_message(self.request, messages.INFO,
                                        'Error identite plus : form is not valide in step2  err={}'.format( err))
                    return HttpResponseRedirect('/')

        ## EDUCATION - FORMATION
        if step3.is_valid():
            for form in step3:
                try :
                    education = form.save(commit=False)
                    education.personal_id=personal.id
                    education.save()

                except Exception as err:
                    messages.add_message(self.request, messages.INFO,
                                'Erreur Education form2 in step3 form={} err={}'.format([form.cleaned_data for form in form_list], err))
                    return HttpResponseRedirect('/')

        ## EXPERIENCES -
        if step4.is_valid():
            accomplishement = "VIDE"

            for form in step4:
                try :
                    job = form.save(commit=False)
                    job.personal_id=personal.id
                    job.save()
                    # insert accomplissements :
                    accomplissement = form_dict['step4'][0]['accomplishement1'].data
                    if accomplishement :
                        JobAccomplishment.objects.create(personal=personal, job=job, description=accomplissement)
                    # 2
                    accomplishement = form_dict['step4'][0]['accomplishement2'].data
                    if accomplishement:
                        JobAccomplishment.objects.create(personal=personal, job=job, description=accomplissement)
                    # 3
                    accomplishement = form_dict['step4'][0]['accomplishement3'].data
                    if accomplishement :
                        JobAccomplishment.objects.create(personal=personal, job=job, description=accomplissement)



                except Exception as err:
                    messages.add_message(self.request, messages.INFO,
                                'Erreur Job  err={} accomplissement={}'.format(err, form_dict['step4']['accomplishement1']))
                    return HttpResponseRedirect('/')

        ##  - SKILL
        if step5.is_valid():
            for form in step5:
                try :
                    # messages.add_message(self.request, messages.INFO,
                    #'Erreur Job form {} '.format( form.cleaned_data ))
                    skill = form.save(commit=False)
                    skill.personal_id=personal.id
                    skill.save()
                except Exception as err:
                    messages.add_message(self.request, messages.INFO,
                                'Erreur Job  err={}'.format( err))
                    return HttpResponseRedirect('/')
                    #--

        ## les projets de carrieres
        #if step6.is_valid():
        if form_dict['step6'].is_valid():
            try :
                form = form_dict['step6']
                project = form.save(commit=False)
                project.personal_id=personal.id

                """
                if self.request.FILES['photo']:
                    myfile = self.request.FILES['photo']
                    fs = FileSystemStorage()
                    myfile = request.FILES['photo']
                    filename = fs.save(myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)
                """
                project.save()

            except Exception as err:
                messages.add_message(self.request, messages.INFO,
                            'FILES = {}, Erreur Projects  err={}'.format(self.request.FILES, err))
                return HttpResponseRedirect('/')

            return HttpResponseRedirect('/cv/pdf/{}'.format(personal.id))




class Resume_Forms2(SessionWizardView):
    template_name = "resume/cv_form_1.html"


    TEMPLATES={
        "step1":"resume/cv_form_1.html",
        "step2":"resume/cv_form_2.html",
    }

    form_list = [
        ("step1", cv_forms.ProfileInfoForm),
        ("step2", cv_forms.EducationForm),
    ]

    def get_context_data(self, form, **kwargs):
        messages.add_message(self.request, messages.INFO, "self.steps.current = {}".format(self.steps.current))
        context = super(Resume_Forms2, self).get_context_data(form=form, **kwargs)
        #if self.steps.current == 'step1':
        # update form instance
        form.initial.update({
            'step1-user' : self.request.user,
            'step1-title' : "XXXXXXXXXXXXXXXXXXXXXXX",
        })

        context.update(self.storage.extra_data)
        context['wizard'] = {
            'form': form,
            'steps': self.steps,

            'management_form': ManagementForm(prefix=self.prefix, initial={
                'current_step': self.steps.current,
            }),
        }
        context['current_step'] = self.steps.current
        return context

    def get_template_names(self):
        self.get_context_data(args, kwargs)
        messages.add_message(self.request, messages.INFO, "get =...".format(kwargs))

        return[self.TEMPLATES[self.steps.current]]


    def post__(self, *args, **kwargs):
        perso_id = self.request.POST.get('step1-user')

        if PersonalInfo.objects.filter(id=perso_id).exists() :
            messages.add_message(self.request, messages.INFO, "perso_id = {}".format(perso_id))

            return HttpResponseRedirect('/cv/pdf/{}'.format(perso_id))
        ##--
        return super(Resume_Forms, self).post(*args, **kwargs)



    def get(self, request, *args, **kwargs):

        try:
            self.storage.reset()
            # reset the current step to the first step.
            self.storage.current_step = self.steps.first
            return self.render(self.get_form())

        except KeyError:
            return super().get(request, *args, **kwargs)


class UpdateCvWizard(SessionWizardView):
    template_name = "resume/cv_form.html"

    TEMPLATES__={
        "step1":"resume/formpart_1.html",
        "step2":"resume/formpart_2.html",
    }

    form_list = [
        ("step1", cv_forms.ProfileInfoForm),
        ("step2", cv_forms.EducationForm),
    ]

    def get_form_instance(self, step):
        # step 0: user form
        if 'Personal_pk' in self.kwargs and step == '0':
            Personal_pk = self.kwargs['personal_id']
            profil = models.PersonalInfo.objects.get(user_id=Personal_pk)
            user = profil.user
            return user
        # step 1: Cv form
        elif 'Personal_pk' in self.kwargs and step == '1':
            Personal_pk = self.kwargs['personal_id']
            Cv = models.Cv.objects.get(pk=Personal_pk)
            return Cv
        # The default implementation
        return self.instance_dict.get(step, None)
