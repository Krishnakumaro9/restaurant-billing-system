import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Krishna's Restaurant Billing System")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Menu items and prices
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Fries": 100,
    "Coke": 50
}
# Heading
tk.Label(root, text="Krishna's Restaurant Billing Menu", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)
# Dictionary to hold entry widgets
entry_dict = {}
# Create input fields for each item
for item, price in menu.items():
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=5)
    tk.Label(frame, text=f"{item} (₹={price})", font=("Arial", 12), width=20, anchor="w", bg="#f0f0f0").pack(side="left")
    entry = tk.Entry(frame, width=5)
    entry.pack(side="left")
    entry.insert(0, "0")
    entry_dict[item] = entry

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", justify="left", fg="blue")
result_label.pack(pady=10)

# Function to calculate total
def calculate_total():
    total = 0
    bill_details = ""
    for item, price in menu.items():
        qty = int(entry_dict[item].get())
        if qty > 0:
            item_total = price * qty
            total += item_total
            bill_details += f"{item} x {qty} = ₹{item_total}\n"
    tax = round(total * 0.05, 2)
    grand_total = total + tax
    bill_details += f"\nSubtotal: ₹{total}\nTax (5%): ₹{tax}\nGrand Total: ₹{grand_total}"
    result_label.config(text=bill_details)

# Function to clear all entries
def clear_all():
    for entry in entry_dict.values():
        entry.delete(0, tk.END)
        entry.insert(0, "0")
    result_label.config(text="")

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate Bill", command=calculate_total, bg="green", fg="white", width=15).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear_all, bg="orange", fg="white", width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Exit", command=root.destroy, bg="red", fg="white", width=10).pack(side="left", padx=5)

# Run the app
root.mainloop()