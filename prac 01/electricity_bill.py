# Electricity bill estimator (v1) and (v2 with tariffs)

# ---------- v1 ----------
print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
bill = (cents_per_kwh / 100) * daily_use_kwh * days
print(f"Estimated bill: ${bill:.2f}")

# ---------- v2 (tariffs) ----------
print("\nElectricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = input("Which tariff? 11 or 31: ").strip()
while tariff not in {"11", "31"}:
    print("Invalid tariff")
    tariff = input("Which tariff? 11 or 31: ").strip()

rate = TARIFF_11 if tariff == "11" else TARIFF_31
daily_use_kwh = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
bill = rate * daily_use_kwh * days
print(f"Estimated bill: ${bill:.2f}")

# Pseudocode:
# display "Electricity bill estimator"
# get cents_per_kwh
# get daily_use_kwh
# get number_of_days
# bill = (cents_per_kwh / 100) * daily_use_kwh * number_of_days
# display bill
#
# display "Electricity bill estimator 2.0"
# set TARIFF_11 = 0.244618
# set TARIFF_31 = 0.136928
# get tariff (11 or 31)
# while tariff is not valid
#     display error
#     get tariff again
# if tariff == 11
#     rate = TARIFF_11
# else
#     rate = TARIFF_31
# get daily_use_kwh
# get number_of_days
# bill = rate * daily_use_kwh * number_of_days
# display bill
