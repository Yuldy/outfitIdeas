"""
NOTE: The pictures used for this program are not my own images, as I am using this to create a program that
provides outfit ideas to fellow users of the program. I am not using these online photos for this program to profit
or make a revenue off of, as this is served for educational purposes, including myself.
"""

"""
This folder contains all of the coded images for MALE outfits:
"""
import cv2
from PIL import Image
from matplotlib import pyplot as plt


"""    [WEATHER]      """
def maleSunny():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Sunny/MaleSun1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Sunny/MaleSun2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Sunny/MaleSun3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Sunny/MaleSun4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")


def maleCloudy():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Cloudy/MaleClo1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Cloudy/MaleClo2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Cloudy/MaleClo3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Cloudy/MaleClo4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")


def maleRainy():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Rainy/MaleRain1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Rainy/MaleRain2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Rainy/MaleRain3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Rainy/MaleRain4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")

def maleWindy():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Windy/MaleWind1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Windy/MaleWind2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Windy/MaleWind3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Windy/MaleWind4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")

def maleSnowy():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")



"""    [SEASON]      """
def maleFall():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Fall/GuyFall1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Fall/GuyFall2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Fall/GuyFall3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Fall/GuyFall4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")

def maleWinter():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Winter/GuyWinter1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Winter/GuyWinter2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Winter/GuyWinter3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Winter/GuyWinter4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")


def maleSpring():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Spring/GuySpring1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Spring/GuySpring2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Spring/GuySpring3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Season/Male/Spring/GuySpring4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")


def maleSummer():

    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Weather/Male/Snowy/MaleSnow1.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")




"""    [CATEGORY]      """
def maleVintage():
 
    fig =  plt.figure(figsize = (10, 7))

    rows = 2
    columns = 2

    #reading images
    img1 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Style:Category/Male/Vintage/GuyVin1.jpeg')[:,:,::-1]
    img2 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Style:Category/Male/Vintage/GuyVin2.jpeg')[:,:,::-1]
    img3 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Style:Category/Male/Vintage/GuyVin3.jpeg')[:,:,::-1]
    img4 = cv2.imread('/Users/christianphan/Documents/VSCode/OutfitIdeas/assets/Style:Category/Male/Vintage/GuyVin4.jpeg')[:,:,::-1]
    

    fig.add_subplot(rows, columns, 1)
    
    # showing image
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Outfit 1")
    
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Outfit 2")
    
    fig.add_subplot(rows, columns, 3)
    
    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Outfit 3")
    

    fig.add_subplot(rows, columns, 4)
    
    plt.imshow(img4)
    plt.axis('off')
    plt.title("Outfit 4")











