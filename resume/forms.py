from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms.models import inlineformset_factory

from django import forms
from django.forms import  formset_factory
from resume import  models


## form load Files
class BootstrapForm(forms.Form) :

    def __init__(self,  *args, **kwargs):
        # appel a la class mère
        super(BootstrapForm, self).__init__(*args, **kwargs)
        # set the user_id as an attribute of the form
        #self.fields['semaine'].initial = 33

        # charger la class bootstrap
        for key, field in self.fields.items():
            if field:
                if field.label:
                    field.label = ugettext(field.label)  # traduire le label
                # les input

                if type(field.widget) in (forms.TextInput,  forms.EmailField, forms.EmailInput):
                    field.widget.attrs['class'] = 'form-field-input form-control form-control-lg'
                    field.widget.attrs['size'] = 20
                    # charger place holder
                    if  field.label :
                        field.widget.attrs['placeholder'] = 'Saisissez ' + str(field.label)
                    else :
                        field.widget.attrs['placeholder'] = 'Saisissez '

                elif type(field.widget) in (forms.Select, forms.SelectMultiple ):
                    field.widget.attrs['class'] = 'form-control input-lg'

                elif type(field ) in  (forms.DateTimeInput, ) :
                    field.widget.attrs['class'] = 'form-control input-lg'

                elif type(field.widget) in  ( forms.DateTimeInput, ) :
                    field.widget.attrs['class'] = 'form-control input-lg'
                else :
                    field.widget.attrs['class'] = 'form-control input-lg'


## form load Files
class BootstrapModelForm(forms.ModelForm) :

    def __init__(self,  *args, **kwargs):
        # appel a la class mère
        super(BootstrapModelForm, self).__init__(*args, **kwargs)

        # charger la class bootstrap
        for key, field in self.fields.items():
            if field:
                if field.label:
                    field.label = ugettext(field.label)  # traduire le label
                # les input

                if type(field.widget) in (forms.TextInput,  forms.EmailField, forms.EmailInput):
                    field.widget.attrs['class'] = 'form-field-input form-control form-control-lg'
                    field.widget.attrs['size'] = 20
                    # charger place holder
                    if  field.label :
                        field.widget.attrs['placeholder'] = 'Saisissez ' + str(field.label)
                    else :
                        field.widget.attrs['placeholder'] = 'Saisissez '

                elif type(field.widget) in (forms.Select, forms.SelectMultiple ):
                    field.widget.attrs['class'] = 'form-control input-lg'

                elif type(field ) in  (forms.DateTimeInput, ) :
                    field.widget.attrs['class'] = 'form-control input-lg'

                elif type(field.widget) in  ( forms.DateTimeInput, ) :
                    field.widget.attrs['class'] = 'form-control input-lg'
                else :
                    field.widget.attrs['class'] = 'form-control input-lg'


        def clean__(self, *args, **kwargs):
            data = super(DocumentForm, self).clean(*args, **kwargs)
            filename = os.path.splitext(data)
            data.name = unicode(data.name)
            if len(filename[1]):
                data.name += u'.'+slugify(filename[1])
            return data


class ProfileInfoForm(BootstrapModelForm):
    """
    img_field=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form_profile_image",
                "id":"dec_sec_profile",
                 "type":"Hidden"


            }
        )
    )
    """
    # un Aperçu de mes compètences
    apercu =  forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"step1-0-apercu"}))

    class Meta:
        model = models.PersonalInfo
        fields = ('user', 'last_name', 'first_name', 'title', 'image', )
        exclude = ( 'cv_pdf', 'suffix', 'locality', 'region',  )

class PersonalLanguageForm(BootstrapForm):

    def __init__(self,  *args, **kwargs):
        # appel a la class mère
        super(PersonalLanguageForm, self).__init__(*args, **kwargs)
        query_societe = models.Language.objects.all().values_list( 'id', 'name' ).order_by('name')
        languages_choice  = [ (id, name[:20]) for ( id, name) in query_societe.iterator() ]
        self.fields['language'].widget.choices = languages_choice

    email = forms.EmailField(label="Saisir votre email")

    linkedin = forms.CharField(label="Saisir votre linkedin", widget=forms.TextInput(
                                                      attrs={"class":"form-contruiere=Falseol",
                                                             "id":"step2-0-linkedin",
                                                             }))

    facebook = forms.CharField(label="Saisir votre facebook", widget=forms.TextInput(attrs={"class":"form-control",
                                                              "id":"step2-0-facebook",
                                                              }))
    #language = forms.CharField(label="Saisir votre language", required=False, widget=forms.CheckboxSelectMultiple)
    language = forms.CharField(label="Saisir votre language", required=False, widget=forms.SelectMultiple)

    class Meta:
        fields = ( 'language', 'email', 'linkedin', 'facebook',)


class ProjectForm(BootstrapModelForm):

    def __init__(self,  *args, **kwargs):
        # appel a la class mère
        super(ProjectForm, self).__init__(*args, **kwargs)
        query_techno = models.ProgrammingLanguage.objects.all().values_list( 'id', 'name' ).order_by('name')
        languages_choice  = [ (id, name[:20]) for ( id, name) in query_techno.iterator() ]
        self.fields['programminglanguage'].widget.choices = languages_choice


    #language = forms.CharField(label="Saisir votre language", required=False, widget=forms.CheckboxSelectMultiple)
    programminglanguage = forms.CharField(label="Saisir votre language de programmation", required=False, widget=forms.SelectMultiple)
    programmingarea = forms.CharField(label="Saisir votre programming area", required=False, widget=forms.CheckboxSelectMultiple)
    image = forms.Field(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = models.Project
        fields = ('projtype',  'programminglanguage', 'image','short_description','long_description', )


class EducationForm(BootstrapModelForm):
    #

    class Meta :
        model = models.Education
        fields = ('name', 'location',  'start_date', 'end_date', )
        exclude = ('name2', 'location2',  'schoolurl2', 'degree', 'description', 'schoolurl')

class ExperienceForm(BootstrapModelForm):

    accomplishement1 = forms.CharField(max_length=500)
    accomplishement2 = forms.CharField(max_length=500)
    accomplishement3 = forms.CharField(max_length=500)

    class Meta :
        model = models.Job
        fields = ('company', 'location', 'title', 'description', 'start_date', 'end_date',
                   'accomplishement1', 'accomplishement2', 'accomplishement3')
        exclude = ('name2',  'is_current', 'is_public')

class SkillForm(BootstrapModelForm):

     class Meta :
         model = models.Skill
         fields = ('text', 'order', 'skillset')
         #exclude = ('personal')


BookFormset1=formset_factory(ProfileInfoForm,extra=1)
BookFormset12=formset_factory(PersonalLanguageForm,extra=1)
BookFormset2=formset_factory(EducationForm, extra=1)
BookFormset3=formset_factory(ExperienceForm, extra=1)
BookFormset4=formset_factory(SkillForm, extra=1)
