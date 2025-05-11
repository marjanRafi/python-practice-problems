# Function to check if the image is in landscape or portrait mode
def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

width = 1200
height = 800

result = isLandscape(width, height)
print(f"The image is in {result} mode.")
