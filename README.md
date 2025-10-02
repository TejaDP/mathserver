# Ex.05 Design a Website for Server Side Processing
# Date:2.10.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
views.py
from django.shortcuts import render
def physics(request):
    power = ''
    intensity=''
    resistance=''

    if request.method == 'POST':
        intensity = float(request.POST.get('intensity'))
        resistance = float(request.POST.get('resistance'))
        power = (intensity ** 2) * resistance 
    return render(request, 'power.html', {'power': power, 'intensity':intensity, 'resistance':resistance,
})

url.py
from django.contrib import admin
from django.urls import path
from powerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.physics)
]

templates
<html>
<head>
    <title>Power Calculator</title>
</head>
<style>
    body{
        background-image: url(https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0yMjItbWluZC0xNl8xLmpwZw.jpg
        ); background-position: center; background-size: cover; align-items: center;
        justify-content: center; height: 100vh; place-items:center;
    }
    h1{ text-align: center ; -webkit-text-fill-color: darkblue; background-color: aliceblue;
    font-style: bold; font-size: xx-large;}
   .me{  justify-content: center; text-align: center;
       background: white;
      padding: 40px;
      border-radius: 15px;
      height: 40%; width: 50%; 
      text-align: center;
      width: 400px;}
    label{ align-items: center; font-size: x-large; 
         -webkit-text-fill-color:royalblue; 
      }
   button{
    background-color:rgb(23, 120, 247); width: 100px; height: 50px; margin: 3px;;
   }
   </style>
<body>
    <br>
    <br>
    <h1>Power Calculator</h1>
    <br>
    <br>
    <br>
    <br>
    <br>
     <div class="me" > 
    <form method="post">
        {% csrf_token %}
        <label>Intensity : </label>
        <input type="number"  name="intensity"required  value="{{intensity}}">(w/m^2)<br><br>
        <label>Resistance : </label>
        <input type="number"  name="resistance"required value="{{resistance}}" > (ohm)<br><br>
         <button type="submit">Calculate Power</button>
    </form>
     <pre> <h1>    Power: {{ power }} watts </h> </pre>
    </div>
</body>
</html>
```

# SERVER SIDE PROCESSING:
# HOMEPAGE:
![alt text](<Screenshot (46).png>)
![alt text](<Screenshot (47).png>)
# RESULT:
The program for performing server side processing is completed successfully.
