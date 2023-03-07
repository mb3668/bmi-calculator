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
    bmi = (weight / (height*height) * 703)
    print(bmi)
    if 18.5 <= bmi < 25:
        result = "Normal"
        return result
    elif 25 <= bmi < 30:
        result = "Overweight"
        return result
    elif bmi >= 30:
        result = "Obese"
        return result
    else:
        result = "Underweight"
        return result


def on_click():
    # Set height and get inches
    height = height_entry.get()
    inches = inches_entry.get()

    # Set int
    height_int = int(height)
    inches_int = int(inches)

    if inches_int > 12 or inches_int < 0:
        error_output = tk.Label(window, text="Enter a valid input!")
        error_output.grid(row=4, column=0)

    else:
        # Get total inches
        total_inches = (height_int*12)+inches_int

        # Set weight and integer
        weight = weight_entry.get()
        weight_int = int(weight)

        print("Your height: ", height, "'", inches, " and weight: ", weight)  # Show input height and weight
        print(calculate_bmi(total_inches, weight_int))  # Print the bmi category

        info_output = tk.Label(window, text=f"Your height: {height}'{inches} and weight {weight}")
        info_output.grid(row=4, column=0, columnspan=2)

        bmi_output = tk.Label(window, text=f"{calculate_bmi(total_inches, weight_int)}")
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

