# Ex.05 Design a Website for Server Side Processing
## Date:07/10/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMI Calculator</title>
    <style>
        body {
            background-color:dark green; 
        }
        .box {
            background-color:green; 
            width: 400px;
            margin-left: 100px;  
            margin-right: 50px;  
            border: 3px dotted #fca311; 
            padding: 20px;
            color:black ;
            border-radius: 12px;
        }

        .formelt {
            color: wight;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }

        h1 {
            color:black; 
            text-align: center;
            padding-top: 20px;
        }

        input[type="text"] {
            width: 120px;
            padding: 4px;
            text-align: center;
        }

        input[type="submit"] {
            background-color:dark green;
            color:green;
            border: none;
            padding: 6px 12px;
            cursor: pointer;
            border-radius: 5px;
            font-weight: bold;
        }

        input[type="submit"]:hover {
            background-color:dark green;
        }
    </style>
</head>
<body>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <div class="edge">
        <div class="box">
            <h1>Body Mass Index (BMI) Calculator</h1>
           <form method="POST">
  {% csrf_token %}
  <label>Height (cm):</label>
  <input type="text" name="height"><br>
  <label>Weight (kg):</label>

  <input type="text" name="weight"><br>

  <button type="submit">Calculate</button>
                <div class="formelt">
                    BMI : <input type="text" name="bmi" value="{{bmi}}"><br/>
                </div>
            </form>
        </div>
    </div>
</body>
</html>

views.py

from django.shortcuts import render

def calculate_bmi(request):
    bmi = None
    height_cm = None
    weight_kg = None

    if request.method == "POST":
        try:
            height_cm = float(request.POST.get("height"))
            weight_kg = float(request.POST.get("weight"))
            height_m = height_cm / 100  # convert cm to meters
            bmi = round(weight_kg / (height_m * height_m), 2)

            # Print all three values to the terminal
            print(f"Height (cm): {height_cm}")
            print(f"Weight (kg): {weight_kg}")
            print(f"Calculated BMI: {bmi}")

        except (TypeError, ValueError, ZeroDivisionError):
            bmi = None

    return render(request, "mathapp/math.html", {"bmi": bmi})

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate_bmi, name='calculate_bmi'),
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-07 205420-1.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-07 205319-1.png>)

## RESULT:
The program for performing server side processing is completed successfully.
