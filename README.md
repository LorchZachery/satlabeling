# **Satellite Labeling Project**  
creating a tool to label satillite images similar to labelme yet focused on more than just the rgb bands  
  
  
## running the flask app and accessing it  
* flask run   
* then go to ***localhost*** in browser (firefox works best but all are good)  
  
## getting the stuff to azure  
* docker build -t satlabeling:<version> .  
* docker run --env-file ./env.list -d -p 80:80 satlabeling:<version> 
* docker tag satlabeling:tag satlabeling.azurecr.io/zlorch/sat_labeling:<version>  
* az login  
* az acr login -n satlabeling  
* docker push satlabeling.azurecr.io/zlorch/sat_labeling:<version>  
## docker
to create the docker container, it is suggested to move the docker files into another folder in order to   
not build the container with legacy and dev. 
## Authors
Zachery J Lorch, USAFA  
Alexis Shirley, USAFA  
