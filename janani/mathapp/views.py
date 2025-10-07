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


