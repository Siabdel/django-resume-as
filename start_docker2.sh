# commandes creation docker avec l'appli djangoresume "cvmoderne"

### Lister les images docker du register local
sudo docker images

### Creer le docker web a partir de l'image cvmoderne a l'ecoute sur port=8020 avec volume mounté sur /home/django/mount/data
```
sudo docker run --name web  -v /home/django/mount/data:/opt/app/djangoresume/data  -ti -p 8020:8020 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=grutil001 -e DJANGO_SUPERUSER_EMAIL=admin@example.com  cvmoderne
```
#
### stoper le container web
sudo docker stop web
### redemarer le docker
sudo docker start web
## lister les docker en ligne
sudo docker ps -a
## Supprimer un docker 
sudo docker rm -f web
## supprimer une image 
sudo docker rmi cvmoderne
