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
utilization = [
    total_data["22-23 Utilization"] * 100,
    total_data["Utilization + Developments (1-5 Years)"] * 100,
    total_data["Utilization + Developments (5-10 Years)"] * 100,
    total_data["Utilization + Developments (>10 Years)"] * 100,
]
students = [
    total_data["22-23 Enrollment"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"] + total_data["Future Developments (5-10 Years)"],
    total_data["22-23 Enrollment"] + total_data["Active & Planned Developments"] + total_data["Future Developments (1-5 Years)"] + total_data["Future Developments (5-10 Years)"] + total_data["Developments from Vacant Land (>10 Years)"]
]

ideal_utilization_lower = [75] * len(years)
ideal_utilization_upper = [85] * len(years)
over_utilization = [150] * len(years)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(years, utilization, label="Utilization", marker='o')
plt.plot(years, ideal_utilization_lower, label="Ideal Utilization Lower Bound (75%)", linestyle='--', color='green')
plt.plot(years, ideal_utilization_upper, label="Ideal Utilization Upper Bound (85%)", linestyle='--', color='green')
plt.plot(years, over_utilization, label="Over Utilization (150%)", linestyle='--', color='red')

# Annotate the number of students
for i, txt in enumerate(students):
    plt.annotate(txt, (years[i], utilization[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel("Time Period")
plt.ylabel("Utilization (%)")
plt.title("Projected Utilization of New Albany Schools with Student Numbers")
plt.legend()
plt.grid(True)
plt.ylim(0, 160)
plt.show()
