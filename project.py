import tkinter as tk  # Import the tkinter library

# Function to calculate the sum
def calculate_sum():
    # Get input from entry boxes
    num1 = entry1.get()
    num2 = entry2.get()
    try:
        # Calculate the sum
        result = float(num1) + float(num2)
        # Update the result label
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")  # Set the title of the app
root.geometry("300x200")  # Set the size of the app window

# Add input fields for numbers
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Add a button to calculate the sum
tk.Button(root, text="Calculate", command=calculate_sum).pack()

# Add a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the tkinter event loop
root.mainloop()
