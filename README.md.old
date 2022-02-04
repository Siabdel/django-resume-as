## Djangoresume
Resume site based on Django. See it live at [aless80.pythonanywhere.com/resume](https://aless80.pythonanywhere.com/resume)
This Django project uses sqlite because it is free on pythonanywhere.com. See my other project [Django-resume-PostgreSQL](https://github.com/aless80/Django-resume-PostgreSQL) 

![Alt Text](https://github.com/aless80/Djangoresume/blob/master/Djangoresume.png)


## Table of Contents
* [Installation](#installation)  
  * [Install the virtual environment](#virtual-environment)
  * [Security settings](#security-settings)
  * [Start Djangoresume](#start-djangoresume)  
* [Models available](#models-available)  

-------------

## Installation
This repository uses a sqlite database. The data for my CV has been dumped to resume/fictures/data.json. 
I suggest setting up a virtual environment for python 3.4, installing sqlite, create a database user, and set up a couple of secret keys and passwords.

#### Virtual environment
<pre>
python3 -m pip3 install --user virtualenv 
cd ~/virtualenv 
virtualenv django_resume
source django_resume/bin/activate
(django_resume)$ pip install -r requirements.txt 
(django_resume)$ python setup.py install  
</pre>

#### Security Settings
Export an environment variable as follows (in linux) before running the server:
```
export SECRET_KEY="*my secret key*"
```

#### Start Djangoresume
To start Djangoresume with the data in my CV run the following: 
```
python3 manage.py loaddata resume/fixtures/data.json
```
To start fresh: 
```
python3 manage.py flush 		#clear all data
python3 manage.py createsuperuser 	#create a superuser
python3 manage.py runserver 		#launch the server
!firefox http://127.0.0.1:8000/admin 	#launch your browser on localhost
```
Then use the UI to manually insert data.

----------

## Models available
The available models are:  
```
Overview  
PersonalInfo  
Education  
Job  
Achievement  
JobAccomplishment  
Skillset  
Skill  
ProgrammingArea  
ProgrammingLanguage  
Language  
Project  
```

## Create data from shell
If you like using objects from shell, create a mock resume with commands similar to the following ones (this is outdated): 

```
python3 manage.py shell

import datetime

from resume.models import PersonalInfo
pi=PersonalInfo.objects.create(email='AlessandroMarin80@gmail.com', region='MA', first_name= 'Alessandro', locality='Boston', last_name='Marin')
pi.title='Wannabe Developer'
pi.linkedin='https://www.linkedin.com/in/alessandromarin80/'
pi.github='https://github.com/aless80'
pi.site='http://www.somesite.com'
pi.save()
pi.__dict__  #print the fields

from resume.models import Overview
over=Overview.objects.create(text='This is a test overview for this CV')
over.save()

from resume.models import Job
j=Job.objects.create(company='MyCompany')
j.start_date=datetime.date(year=2018,month=2,day=19)
j.end_date=datetime.date(year=2018,month=3,day=20)
j.company='Best Co'
j.company_url='https://www.google.com/search?q=best+co'
j.title="CTO"
j.location='Boston, MA'
j.description="Some description of the job which goes here and will be displayed ok you get it"
j.save()

j2=Job.objects.create(company='Booking.com')
j2.start_date=datetime.date(year=2015,month=6,day=19)
j2.end_date=datetime.date(year=2017,month=3,day=20)
j2.company='Booking.com'
j2.company_url='https://www.booking.com'
j2.location='Amsterdam, the Netherlands'
j2.title="Technician"
j2.description="Describe the job here"
j2.save()

from resume.models import JobAccomplishment
acc=JobAccomplishment.objects.create(order=2,job=j)
acc.description="2nd accomplishement"
acc.save()
acc=JobAccomplishment.objects.create(order=3,job=j)
acc.description="my third incomplete accomplishm"
acc.save()
acc=JobAccomplishment.objects.create(order=1,job=j)
acc.description="first accomplishment there"
acc.save()

from resume.models import Achievement
ach1=Achievement.objects.create()
ach1.description="I developed this site. See it on "
ach1.link="https://github.com/aless80/Djangoresume"
ach1.linkname="github"
ach1=Achievement.objects.create()
ach1.save()
ach2=Achievement.objects.create()
ach2.description="Some achievement"
ach2.save()
ach3=Achievement.objects.create()
ach3.description="Some other achievement"
ach3.save()

from resume.models import Education
ed1=Education.objects.create(name='University of Somewhere')
ed1.start_date=datetime.date(year=2010,month=2,day=19)
ed1.end_date=datetime.date(year=2015,month=3,day=1)
ed1.degree="PhD"
ed1.location='Somewhere,FarLand'
ed1.description="Studied spellings"
ed1.save()
ed2=Education.objects.create(name='University of Somewherelse')
ed2.start_date=datetime.date(year=2015,month=4,day=1)
ed2.degree="Hi school"
ed2.location='Boston,MA'
ed2.description="Studied electrodynamics"
ed2.save()

from resume.models import Skillset
from resume.models import Skill
sks=Skillset.objects.create(name='Technical Skills')
s1=Skill.objects.create(text='Data analysis in MATLAB, R, Python',skillset=sks)
s2=Skill.objects.create(text='Experience with relational and NoSQL databases',skillset=sks)
s3=Skill.objects.create(text='UI development in LabView, HTML/Javascript (jQuery, AJAX, D3), LabWindows',skillset=sks)
s1.save()
s2.save()
s3.save()
sks.save()

sks2=Skillset.objects.create(name='Transferable Skills')
s1=Skill.objects.create(name='Troubleshooting: problem solving skills in complex software and hardware problems',skillset=sks2)
s2=Skill.objects.create(name='Strong analytical, multi-tasking and problem solving skills',skillset=sks2)
s1.save()
s2.save()
sks2.save()

from resume.models import ProgrammingLanguage
pl1=ProgrammingLanguage.objects.create(name='Python',description='Proficient',level=5)
pl2=ProgrammingLanguage.objects.create(name='Javascript',description='Intermediate',level=3,order=2)
pl3=ProgrammingLanguage.objects.create(name='C',description='Used in the past',level=2,order=5)
pl4=ProgrammingLanguage.objects.create(name='Django',description='Daily use',level=5,order=4)
pl1.save()
pl2.save()
pl3.save()
pl4.save()

from resume.models import Language
l1=Language.objects.create(language='English',level=4)
l2=Language.objects.create(language='English',level=4)
l3=Language.objects.create(language='Spanish',level=3)
l4=Language.objects.create(language='French',level=3)
l5=Language.objects.create(language='Italian',level=5)
l1.save()
l2.save()
l3.save()
l4.save()
l5.save()

from resume.models import Project
pr1=Project.objects.create(name='Djangoresume', link='https://github.com/aless80', order=2)
pr1.description='Django template for online resumes'
pr1.save()

```

You can print the available fields for each model using:
```
[f.name for f in Overview._meta.get_fields()]
```

## Credits
The initial implementation was based on his [ckelly](https://github.com/ckelly)'s project on this repository: [django-resume](https://github.com/ckelly/django-resume). 
Template based on [BlackrockDigital/startbootstrap-resume](https://github.com/BlackrockDigital/startbootstrap-resume)
