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


def height_inches(height):
    """
    Calculate height in feet and inches to inches
    :param
    height: input height(feet'inches)
    :return:
    total_inches: height(inches)
    """
    if "'" in height:
        feet, inches = height.split("'")
        total_inches = int(feet) * 12 + int(inches.strip('"'))
    # If only feet input
    else:
        total_inches = int(height) * 12
    return total_inches


def on_click():
    # Set height and get inches
    height = height_entry.get()
    inches = height_inches(height)

    # Set weight and integer
    weight = weight_entry.get()
    weight_int = int(weight)

    print("Your height: ", height, " and weight: ", weight)  # Show input height and weight
    print(calculate_bmi(inches, weight_int))  # Print the bmi category


if __name__ == '__main__':
    window = tk.Tk()  # Create tk window

    # Set window title
    window.title("Calculate BMI!")

    # Ask for height
    height_label = tk.Label(window, text="Enter your Height(Feet and Inches): ")
    height_label.pack()

    # Set height entry
    height_entry = tk.Entry(window)
    height_entry.pack()

    # Ask for weight
    weight_label = tk.Label(window, text="Enter your Weight(in Pounds): ")
    weight_label.pack()

    # Set weight
    weight_entry = tk.Entry(window)
    weight_entry.pack()

    # Set button
    button = tk.Button(window, text="Calculate BMI!", command=on_click)
    button.pack()

    window.mainloop()

