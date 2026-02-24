import numpy as np
import matplotlib.pyplot as plt

def draw_user_input_line_chart():

    try:
        num_data = int(input("Enter the number of data points you want to plot: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    y_values = []

    for i in range(num_data):
        while True:
            try:
                value = float(input(f"Enter value for point {i+1}: "))
                y_values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    x_values = np.arange(num_data)

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, marker='o', linestyle='-') 
    plt.xlabel('X-axis (Point Index)')
    plt.ylabel('Y-axis (User Value)')
    plt.title('Line Chart from User Input')
    plt.grid(True) 
    plt.show() 

if __name__ == "__main__":
    draw_user_input_line_chart()