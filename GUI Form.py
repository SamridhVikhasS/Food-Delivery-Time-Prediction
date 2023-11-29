import tkinter as tk
from tkinter import ttk,messagebox
import OnTime as ot
import numpy as np

def calculate_delivery_time():
    age = int(age_entry.get())
    ratings = float(ratings_entry.get())
    distance = float(distance_entry.get())
    weather = ot.map_input("weather",weather_combobox.get())
    traffic = ot.map_input("traffic",traffic_combobox.get())
    order = ot.map_input("order",order_type_combobox.get())
    vehicle = ot.map_input("vehicle",vehicle_combobox.get())
    fest = ot.map_input("fest",festival_var.get())
    city = ot.map_input("city",city_var.get())
    
    time = ot.predict_time(age,ratings,distance,weather,traffic,order,vehicle,fest,city)
    time = np.round(time,2)
    
    messagebox.showinfo("Delivery Time", f"The estimated delivery time is {time} minutes.")

# Create the main window
window = tk.Tk()
window.title("OnTime")

# Create and place form elements
ttk.Label(window, text="Delivery Person Age").grid(row=0, column=0)
age_entry = ttk.Entry(window)
age_entry.grid(row=0, column=1)

ttk.Label(window, text="Delivery Person Ratings").grid(row=1, column=0)
ratings_entry = ttk.Entry(window)
ratings_entry.grid(row=1, column=1)

ttk.Label(window, text="Distance").grid(row=2, column=0)
distance_entry = ttk.Entry(window)
distance_entry.grid(row=2, column=1)

ttk.Label(window, text="Weather Conditions").grid(row=3, column=0)
weather_options = ["Sunny", "Stormy", "Sandstorms", "Cloudy", "Fog", "Windy"]
weather_combobox = ttk.Combobox(window, values=weather_options)
weather_combobox.grid(row=3, column=1)

ttk.Label(window, text="Traffic Density").grid(row=4, column=0)
traffic_options = ["Low", "Medium", "High", "Jam"]
traffic_combobox = ttk.Combobox(window, values=traffic_options)
traffic_combobox.grid(row=4, column=1)

ttk.Label(window, text="Type of Order").grid(row=5, column=0)
order_type_options = ["Snack", "Drinks", "Buffet", "Meal"]
order_type_combobox = ttk.Combobox(window, values=order_type_options)
order_type_combobox.grid(row=5, column=1)

ttk.Label(window, text="Vehicle of Delivery Person").grid(row=6, column=0)
vehicle_options = ["Motorcycle", "Scooter", "Electric Scooter", "Bicycle"]
vehicle_combobox = ttk.Combobox(window, values=vehicle_options)
vehicle_combobox.grid(row=6, column=1)

ttk.Label(window, text="Festival Day").grid(row=7, column=0)
festival_var = tk.StringVar()
festival_radiobutton_no = ttk.Radiobutton(window, text="No", variable=festival_var, value="No")
festival_radiobutton_yes = ttk.Radiobutton(window, text="Yes", variable=festival_var, value="Yes")
festival_radiobutton_no.grid(row=7, column=1, sticky="w")
festival_radiobutton_yes.grid(row=7, column=1, sticky="e")

ttk.Label(window, text="City Type").grid(row=8, column=0)
city_var = tk.StringVar()
city_radiobutton_urban = ttk.Radiobutton(window, text="Urban", variable=city_var, value="Urban")
city_radiobutton_metropolitan = ttk.Radiobutton(window, text="Metropolitan", variable=city_var, value="Metropolitan")
city_radiobutton_semi_urban = ttk.Radiobutton(window, text="Semi-Urban", variable=city_var, value="Semi-Urban")
city_radiobutton_urban.grid(row=8, column=1, sticky="w")
city_radiobutton_metropolitan.grid(row=8, column=3)
city_radiobutton_semi_urban.grid(row=8, column=5, sticky="e")

calculate_button = ttk.Button(window, text="When will I get my food?", command=calculate_delivery_time)
calculate_button.grid(row=9, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
