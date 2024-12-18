monuments = {
    "delhi": "Red Fort",
    "agra": "Taj Mahal",
    "jaipur": "Jal Mahal"
}

city = input("Enter a city name: ").lower()

if city in monuments:
    print(f"The monument of {city.capitalize()} is {monuments[city]}.")
else:
    print("Can't Find the Monument")

# Another method
city = input("Enter a city name(delhi,agra,jaipur): ")
city = city.lower()
if (city == 'delhi'):
    print("Delhi Monument is Red Fort")
elif (city == 'agra'):
    print("Agra Monument is Taj Mahal")
elif (city == 'jaipur'):
    print("Jaipur Monument is Jal Mahal")
else:
    print("We dont have information on other cities.")