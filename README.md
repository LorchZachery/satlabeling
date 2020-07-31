# **Satellite Labeling Project**  
creating a tool to label satillite images similar to labelme yet focused on more than just the rgb bands  
  
  
## running the flask app and accessing it  
* python app.py  
* then go to ***localhost*** in browser (firefox works best but all are good)  
  
## getting the stuff to azure  
* docker new container added   
* docker pull satlabeling.azurecr.io/zlorch/satlabeling  
* ***do the shit*** 
* docker build -t satlabeling:<version> .  
* docker run --env-file ./env.list -d -p 80:80 satlabeling:<version> 
* docker tag satlabeling:tag satlabeling.azurecr.io/zlorch/sat_labeling:<version>  
* az login  
* az acr login -n satlabeling  
* docker push satlabeling.azurecr.io/zlorch/sat_labeling:<version>  
