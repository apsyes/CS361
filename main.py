import random

def check_all_microservice():
    pass

def microservice_call_curr(city):
    print(f"\n Contacting current weather microservice for {city}")

    tempval = random.choice([True, False])
    
    if tempval:
        print(f"{city} responded with weather data!")

    else:
        print(f"Failed to retrieve data for {city}.")


def microservice_call_5(city):
    print(f"\n Contacting 5 day forcast microservice for {city}")

    tempval = random.choice([True, False])
    
    if tempval:
        print(f"{city} responded with weather data!")
    else:
        print(f"Failed to retrieve data for {city}.")


def microservice_call_day(city):
    print(f"\n Contacting full day weather microservice for {city}")

    tempval = random.choice([True, False])
    
    if tempval:
        print(f"{city} responded with weather data!")
    else:
        print(f"Failed to retrieve data for {city}.")


def main():
    print("~~~Weather App~~~")
    city = input("Enter city and state (ex. Las Vegas NV): ").strip()

    while True:
        print(f"\nWeather location: {city}")
        print("What would you like to do?")
        print("[1] Check current weather status")
        print("[2] Check 5 day forcast")
        print("[3] Look at the weather for the rest of the day")
        print("[4] Change location")
        print("[5] Exit")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            microservice_call_curr(city)
        elif choice == "2":
            microservice_call_5(city)
        elif choice == "3":
            microservice_call_day(city)
        elif choice == "4":
            city = input("Enter new city and state: ").strip()
        elif choice == "5":
            print("Thank you for using Weather App")

            break
        else:
            print("Not a valid choice. Please type the number you want to select")

if __name__ == "__main__":
    main()
