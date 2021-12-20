def picnic_planner(weather_list):
    good_days = []
    for day in weather_list:
        if day["cloudiness"] == 'sunny':
            comfort = day["temperature"] - day["wind"] * 1.5 + 5
        else:
            comfort = day["temperature"] - day["wind"] * 1.5
        if comfort >= 15 and day["cloudiness"] != 'rainy':
            good_days.append({'day': day['day'], 'comfort': comfort})
    return good_days


weather = [{"day": 1, "cloudiness": 'rainy', "wind": 3, "temperature": 17},
           {"day": 2, "cloudiness": 'sunny', "wind": 7, "temperature": 33},
           {"day": 3, "cloudiness": 'sunny', "wind": 1, "temperature": 21},
           {"day": 4, "cloudiness": 'cloudy', "wind": 8, "temperature": 22},
           {"day": 5, "cloudiness": 'rainy', "wind": 2, "temperature": 12},
           {"day": 6, "cloudiness": 'cloudy', "wind": 0, "temperature": 3},
           {"day": 7, "cloudiness": 'sunny', "wind": 2, "temperature": 12},
           {"day": 8, "cloudiness": 'sunny', "wind": 1, "temperature": 15}]

print(picnic_planner(weather))
