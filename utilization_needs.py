import pandas as pd
import matplotlib.pyplot as plt

# Data extraction
data = {
    "New Albany Early Learning Center": {
        "Program Capacity": 562,
        "22-23 Enrollment": 505,
        "22-23 Utilization": 0.90,
        "Active & Planned Developments": 12,
        "Utilization + Developments (1-5 Years)": 0.92,
        "Future Developments (1-5 Years)": 12,
        "Utilization + Developments (5-10 Years)": 0.94,
        "Future Developments (5-10 Years)": 59,
        "Utilization + Developments (>10 Years)": 1.05,
        "Developments from Vacant Land (>10 Years)": 141,
        "Utilization + Developments": 1.30
    },
    "New Albany Primary School": {
        "Program Capacity": 1080,
        "22-23 Enrollment": 1060,
        "22-23 Utilization": 0.98,
        "Active & Planned Developments": 47,
        "Utilization + Developments (1-5 Years)": 1.02,
        "Future Developments (1-5 Years)": 46,
        "Utilization + Developments (5-10 Years)": 1.07,
        "Future Developments (5-10 Years)": 221,
        "Utilization + Developments (>10 Years)": 1.27,
        "Developments from Vacant Land (>10 Years)": 533,
        "Utilization + Developments": 1.76
    },
    "New Albany Intermediate School": {
        "Program Capacity": 1248,
        "22-23 Enrollment": 1122,
        "22-23 Utilization": 0.90,
        "Active & Planned Developments": 50,
        "Utilization + Developments (1-5 Years)": 0.94,
        "Future Developments (1-5 Years)": 49,
        "Utilization + Developments (5-10 Years)": 0.98,
        "Future Developments (5-10 Years)": 235,
        "Utilization + Developments (>10 Years)": 1.17,
        "Developments from Vacant Land (>10 Years)": 568,
        "Utilization + Developments": 1.62
    },
    "New Albany Middle School": {
        "Program Capacity": 1121,
        "22-23 Enrollment": 783,
        "22-23 Utilization": 0.70,
        "Active & Planned Developments": 35,
        "Utilization + Developments (1-5 Years)": 0.73,
        "Future Developments (1-5 Years)": 34,
        "Utilization + Developments (5-10 Years)": 0.76,
        "Future Developments (5-10 Years)": 164,
        "Utilization + Developments (>10 Years)": 0.91,
        "Developments from Vacant Land (>10 Years)": 397,
        "Utilization + Developments": 1.26
    },
    "New Albany High School": {
        "Program Capacity": 1990,
        "22-23 Enrollment": 1594,
        "22-23 Utilization": 0.80,
        "Active & Planned Developments": 72,
        "Utilization + Developments (1-5 Years)": 0.84,
        "Future Developments (1-5 Years)": 71,
        "Utilization + Developments (5-10 Years)": 0.87,
        "Future Developments (5-10 Years)": 341,
        "Utilization + Developments (>10 Years)": 1.04,
        "Developments from Vacant Land (>10 Years)": 823,
        "Utilization + Developments": 1.46
    },
    "TOTAL": {
        "Program Capacity": 6001,
        "22-23 Enrollment": 5064,
        "22-23 Utilization": 0.84,
        "Active & Planned Developments": 216,
        "Utilization + Developments (1-5 Years)": 0.88,
        "Future Developments (1-5 Years)": 213,
        "Utilization + Developments (5-10 Years)": 0.92,
        "Future Developments (5-10 Years)": 1020,
        "Utilization + Developments (>10 Years)": 1.50,
        "Developments from Vacant Land (>10 Years)": 2462,
        "Utilization + Developments": 1.50
    }
}

# Extract total data for plotting
total_data = data["TOTAL"]
years = ["22-23", "1-5 Years", "5-10 Years", ">10 Years"]
students = [
    total_data["22-23 Enrollment"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"] + total_data["Future Developments (5-10 Years)"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"] + total_data["Future Developments (5-10 Years)"] + total_data["Developments from Vacant Land (>10 Years)"]
]

# Calculate the required capacity for ideal utilization
ideal_capacity_lower = [s / 0.85 for s in students]
ideal_capacity_upper = [s / 0.75 for s in students]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(years, ideal_capacity_lower, label="Ideal Capacity Lower Bound (85%)", marker='o', linestyle='-', color='green')
plt.plot(years, ideal_capacity_upper, label="Ideal Capacity Upper Bound (75%)", marker='o', linestyle='-', color='blue')

# Annotate the required capacity
for i, txt in enumerate(ideal_capacity_lower):
    plt.annotate(int(txt), (years[i], ideal_capacity_lower[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(ideal_capacity_upper):
    plt.annotate(int(txt), (years[i], ideal_capacity_upper[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel("Time Period")
plt.ylabel("Required Capacity")
plt.title("Projected Required Capacity for Ideal Utilization in New Albany Schools")
plt.legend()
plt.grid(True)
plt.ylim(0, max(ideal_capacity_upper) * 1.1)
plt.show()
