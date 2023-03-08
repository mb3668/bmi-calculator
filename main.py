import tkinter as tk


def calculate_bmi(height, weight):
    """
    Calculate user bmi

    :param height:
    height in inches
    :param weight:
    weight in pounds

    :return:
    User bmi category
    """
    bmi = (weight / (height*0.025)**2)
    print(bmi)
    if 18.5 <= bmi < 25:
        result = "Normal"
        return result, bmi
    elif 25 <= bmi < 30:
        result = "Overweight"
        return result, bmi
    elif bmi >= 30:
        result = "Obese"
        return result, bmi
    else:
        result = "Underweight"
        return result, bmi


def on_click():
    # Set height and get inches
    height = height_entry.get()
    inches = inches_entry.get()

    # Set int
    height_int = int(height)
    inches_int = int(inches)

    # Set output labels
    info_output = tk.Label(window, text="")
    bmi_output = tk.Label(window, text="")

    if inches_int > 12 or inches_int < 0:
        # Hide labels
        info_output.grid_forget()
        bmi_output.grid_forget()

        # Place error message
        info_output.config(text="")
        info_output.grid(row=4, column=0, columnspan=2, sticky="nsew")
        bmi_output.config(text="Enter a valid height!")
        bmi_output.grid(row=5, column=0, columnspan=2, sticky="nsew")

    else:
        # Get total inches
        total_inches = (height_int*12)+inches_int

        # Set weight and integer
        weight = weight_entry.get()
        metric_weight_int = int(weight) * .45

        bmi_result, bmi = calculate_bmi(total_inches, metric_weight_int)

        print("Your height: ", height, "'", inches, " and weight: ", weight)  # Show input height and weight
        print(bmi_result)  # Print the bmi category

        info_output.config(text=f"Your height: {height}'{inches} and weight {weight}")
        info_output.grid(row=4, column=0, columnspan=2)

        bmi_output.config(text=f"BMI: {round(bmi,2)}\nBMI Range: {bmi_result}")
        bmi_output.grid(row=5, column=0, columnspan=2, sticky="nsew")


if __name__ == '__main__':
    window = tk.Tk()  # Create tk window

    # Set window title
    window.title("Calculate BMI!")

    # Ask for height
    height_label = tk.Label(window, text="Feet: ")
    height_label.grid(row=0, column=0)

    # Set height entry
    height_entry = tk.Entry(window)
    height_entry.grid(row=0, column=1)

    # Ask for inches
    inches_label = tk.Label(window, text="Inches: ")
    inches_label.grid(row=1, column=0)

    # Set inches entry
    inches_entry = tk.Entry(window)
    inches_entry.grid(row=1, column=1)

    # Ask for weight
    weight_label = tk.Label(window, text="Enter your Weight(in Pounds): ")
    weight_label.grid(row=2, column=0)

    # Set weight
    weight_entry = tk.Entry(window)
    weight_entry.grid(row=2, column=1)

    # Set button
    button = tk.Button(window, text="Calculate BMI!", command=on_click)
    button.grid(row=3, column=0, columnspan=2, sticky="nsew")

    window.mainloop()

