# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

weather = "rainy", "sunny", "windy", "neutral"
time_of_day = "day", "night" 
cow_milking_status = True or False  # need milking, don't need milking
location_of_the_cows = "pasture", "cowshed"
season = "winter", "spring", "summer", "fall"
slurry_tank = True or False    #full, not full
grass_status = True or False   #long, short

def farm_action (weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
#action 1:  
  
    if (location_of_the_cows=="pasture" and time_of_day=="night") or weather=="rainy": 
        return "take cows to cowshed" 

#action 2:
    elif cow_milking_status==True:
        if location_of_the_cows =="cowshed":
            return "milk_cows"
        if location_of_the_cows == "pasture":
            return "take cows to cowshed\nmilk cows\ntake cows back to pasture"

#action 3:   
    elif slurry_tank == True:
        if location_of_the_cows=="cowshed" and weather!="sunny" or weather !="windy":
            return "fertilize_pasture"
        if location_of_the_cows == "pasture" and weather != "windy" or weather != "sunny":
            return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"

#action 4: 
    elif grass_status==True and season=="spring" and weather=="sunny":
        if  location_of_the_cows!="pasture":
            return "mow_gras"
    elif grass_status == True and weather == 'sunny' and season == 'spring':
        if location_of_the_cows != 'cowshed':
            return 'take cows to cowshed\nmow grass\ntake cows back to the pasture'

#action 5:
    else: 
        return "wait" 

print (farm_action ("rainy", "night", True, "pasture", "Winter", True, True))
print (farm_action ("sunny", "day", True, "cowshed", "spring", False, True)) 
print (farm_action ("neutral", "day", False, "cowshed", "spring", True, True))
print (farm_action ("sunny", "day", False, "cowshed", "spring", False, True))
print (farm_action ("windy", "night", False, "cowshed", "winter", False, False))
