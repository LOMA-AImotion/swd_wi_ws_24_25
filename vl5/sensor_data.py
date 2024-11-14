# Lies Sensordaten
# Nimm bis zur ersten Hälfte nur jeden zweiten Wert
sensor_data = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
subsample = sensor_data[0: len(sensor_data) // 2  + 1 : 2]

print(sensor_data)
print(subsample)