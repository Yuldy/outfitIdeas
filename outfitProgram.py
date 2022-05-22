#Outfit Ideas // Created by Christian Phan 3/30/22
#imports:
from maleOutfitPictures import maleSunny, maleCloudy

"""
NOTE: The pictures used for this program are not my own images, as I am using this to create a program that
provides outfit ideas to fellow users of the program. I am not using these online photos for this program to profit
or make a revenue off of, as this is served for educational purposes, including myself.
"""

def main():

    print("Welcome to Outfit Ideas! Created by Christian Phan")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
    

    genderChoice = genderIdentity()

def genderIdentity():
    
    print("Would you like to see outfits for Men or Women? ")
    gender = input('Please enter: \n "M" for Male: \n "F" for Female: \n')
    gender = gender.lower()

    if gender == "m":
        print("You selected outfits for Men.")
        
        maleOutfit = male()
        

    elif gender == "f":
        print("You selected outfits for Female.")

        femaleOutfit = female()

    else:
        print("Invalid response! Please enter either one of the two options listed below: ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
        repeatGenderQuestion = genderIdentity()


"""    [MALE OUTFITS:]      """
def male():

    print()
    outfitBased = input('Would you like outfit inspiration based on weather or season or style/category? \n Please enter: \n "W" for based on weather: \n "S" for season \n "C" for style/category \n')
    outfitBased = outfitBased.lower()


    if outfitBased == "w":
        weather = input('What is the weather outside? \n Please enter \n - - - - - \n  "S" for Sunny: \n  "C" for Cloudy: \n  "R" for Rainy \n  "W" for Windy \n  "SN" for Snowy \n ')
        weather = weather.lower()

        if weather == "s":
            print("The weather is sunny! \n Here are some outfits that complement sunny weather: ")

        elif weather == "c":
            print("The weather is cloudy! \n Here are some outfits that complement cloudy weather:")

        elif weather == "r":
            print("The weather is rainy! \n Here are some outfits that complement rainy weather:")

        elif weather == "w":
            print("The weather is windy! \n Here are some outfits that complement windy weather:")

        elif weather == "sn":
            print("The weather is snowy! \n Here are some outfits that complement snowy weather:")

        

    elif outfitBased == "s":
        season = input('What season is it? \n Please enter: \n - - - - - \n "F" for Fall: \n "W" for Winter: \n "SP" for Spring: \n "SU" for Summer: \n ')
        season = season.lower()

        if season == "f":
            print("The season is fall! \n Here are some outfits that complement the fall season: ")

        elif season == "w":
            print("The season is winter! \n Here are some outfits that complement the winter season: ")

        elif season == "sp":
            print("The season is spring! \n Here are some outfits that complement the spring season: ")

        elif season == "su":
            print("The season is summer! \n Here are some outfits that complement the summer season: ")


    elif outfitBased == "c":
        print("What category or look do you want outfit inspiration from?")
        print("- - - - - - - - - - -")
        category = input("1. Vintage \n 2. Casual \n 3. Business Casual \n 4. Athelisure \n 5. Streetwear \n 6. Minimal \n 7. Eboy \n 8. Formal \n 9. Soft Boy \n ")
        category = category.lower()

        if category == 1:
            print('You have chosen the "Vintage Style" \n Here are some outfits:')

        elif category == 2:
            print('You have chosen the "Casual Style" \n Here are some outfits:')

        elif category == 3:
            print('You have chosen the "Business Casual Style" \n Here are some outfits:')

        elif category == 4:
            print('You have chosen the "Athelisure Style" \n Here are some outfits:')

        elif category == 5:
            print('You have chosen the "Streetwear Style" \n Here are some outfits:')

        elif category == 6:
            print('You have chosen the "Minimal Style" \n Here are some outfits:')

        elif category == 7:
            print('You have chosen the "Eboy Style" \n Here are some outfits:')

        elif category == 8:
            print('You have chosen the "Formal Style" \n Here are some outfits:')

        elif category == 9:
            print('You have chosen the "Soft Boy Style" \n Here are some outfits:')


    else:
        print("Invalid response! Please enter either one of the three options listed below: ")
        repeatMale = male()


"""    [FEMALE OUTFITS:]      """
def female():
    
    print()
    outfitBased = input('Would you like outfit inspiration based on weather or season or style/category? \n Please enter: \n "W" for based on weather: \n "S" for season \n "C" for style/category \n')
    outfitBased = outfitBased.lower()


    if outfitBased == "w":
        weather = input('What is the weather outside? \n Please enter \n - - - - - \n  "S" for Sunny: \n  "C" for Cloudy: \n  "R" for Rainy \n  "W" for Windy \n  "SN" for Snowy \n ')
        weather = weather.lower()

        if weather == "s":
            print("The weather is sunny! \n Here are some outfits that complement sunny weather: ")

        elif weather == "c":
            print("The weather is cloudy! \n Here are some outfits that complement cloudy weather:")

        elif weather == "r":
            print("The weather is rainy! \n Here are some outfits that complement rainy weather:")

        elif weather == "w":
            print("The weather is windy! \n Here are some outfits that complement windy weather:")

        elif weather == "sn":
            print("The weather is snowy! \n Here are some outfits that complement snowy weather:")

        

    elif outfitBased == "s":
        season = input('What season is it? \n Please enter: \n - - - - - \n  "F" for Fall: \n "W" for Winter: \n "SP" for Spring: \n "SU" for Summer: \n ')
        season = season.lower()

        if season == "f":
            print("The season is fall! \n Here are some outfits that complement the fall season: ")

        elif season == "w":
            print("The season is winter! \n Here are some outfits that complement the winter season: ")

        elif season == "sp":
            print("The season is spring! \n Here are some outfits that complement the spring season: ")

        elif season == "su":
            print("The season is summer! \n Here are some outfits that complement the summer season: ")


    elif outfitBased == "c":
        print("What category or look do you want outfit inspiration from?")
        print("- - - - - - - - - - -")
        category = input("1. Vintage \n 2. Casual \n 3. Business Casual \n 4. Athelisure \n 5. Streetwear \n 6. Minimal \n 7. Sexy Fashion \n 8. Formal \n 9. Elegant Fashion \n ")
        category = category.lower()

        if category == 1:
            print('You have chosen the "Vintage Style" \n Here are some outfits:')

        elif category == 2:
            print('You have chosen the "Casual Style" \n Here are some outfits:')

        elif category == 3:
            print('You have chosen the "Business Casual Style" \n Here are some outfits:')

        elif category == 4:
            print('You have chosen the "Athleisure Style" \n Here are some outfits:')

        elif category == 5:
            print('You have chosen the "Streetwear Style" \n Here are some outfits:')

        elif category == 6:
            print('You have chosen the "Minimal Style" \n Here are some outfits:')

        elif category == 7:
            print('You have chosen the "Sexy Fashion Style" \n Here are some outfits:')

        elif category == 8:
            print('You have chosen the "Formal Style" \n Here are some outfits:')

        elif category == 9:
            print('You have chosen the "Elegant Fashion Style" \n Here are some outfits:')


    else:
        print("Invalid response! Please enter either one of the three options listed below: ")
        repeatFemale = female()

main()













