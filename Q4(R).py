import datetime

def read_temperature_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    measurements = []
    for i in range(0, len(lines), 2):
        time_str = lines[i].strip()
        temperature = float(lines[i+1].strip())
        measurements.append((time_str, temperature))
    
    return measurements

def calculate_daily_average(measurements):
    total_temperature = 0
    num_measurements = len(measurements)
    for _, temperature in measurements:
        total_temperature += temperature
    return round(total_temperature / num_measurements, 3)

def calculate_time_range_average(measurements, start_hour, end_hour):
    total_temperature = 0
    num_measurements = 0
    for time_str, temperature in measurements:
        time = datetime.datetime.strptime(time_str, '%d-%m-%Y %H:%M:%S')
        if start_hour <= time.hour <= end_hour:
            total_temperature += temperature
            num_measurements += 1
    if num_measurements == 0:
        return 0
    return round(total_temperature / num_measurements, 3)

def main():
    filename = 'temp.txt'
    measurements = read_temperature_data(filename)
    
    daily_average = calculate_daily_average(measurements)
    morning_average = calculate_time_range_average(measurements, 5, 15)
    evening_average = calculate_time_range_average(measurements, 16, 21)
    
    print("Daily Average Temperature:", daily_average)
    print("Morning Average Temperature (5:00 - 15:59:59):", morning_average)
    print("Evening Average Temperature (16:00 - 21:59:59):", evening_average)

if __name__ == "__main__":
    main()
