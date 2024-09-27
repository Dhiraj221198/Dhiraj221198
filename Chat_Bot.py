import random

def chat_bot():
    print('Hello, I am your chat-bot')

    name = input('What is your name: ')
    print(f'Welcome {name}!')

    while True:
        try:
            age = int(input('Enter your age: '))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError:
            print("Please enter a valid age.")

    if 18 <= age :
        print('You are eligible for using the chat-bot.')
    else:
        print('You are not eligible to use the chat-bot at this time.')
        return  

    print('What is your favorite destination to visit?')
    place = input('Enter your destination: ').capitalize()

    destinations = {
        'Paris': 'The city of love and romance, famous for its art, fashion, and cuisine.',
        'Tokyo': 'A bustling metropolis known for its skyscrapers, shopping, and vibrant culture.',
        'Bali': 'A tropical paradise with stunning beaches, lush rice terraces, and rich cultural heritage.',
        'New York': 'The city that never sleeps, famous for its iconic landmarks, Broadway shows, and diverse neighborhoods.',
        'Rome': 'An ancient city with historic landmarks like the Colosseum, Vatican City, and delicious Italian food.',
        'London': 'A cosmopolitan city known for its historical sites, museums, theater performances, and royal palaces.',
        'Dubai': 'A modern city known for luxury shopping, ultramodern architecture, and lively nightlife.',
        'Sydney': 'A vibrant city with iconic landmarks like the Sydney Opera House and beautiful beaches.',
        'Cairo': 'An ancient city with historic pyramids, museums, and vibrant markets.',
        'Rio de Janeiro': 'A city known for its breathtaking landscapes, Carnival festival, and vibrant culture.',
        'Amsterdam': 'Known for its artistic heritage and elaborate canal system.',
        'Barcelona': 'Famous for its art and architecture, especially Gaudís works.',
        'Santorini': 'A picturesque Greek island with stunning sunsets.',
        'Bangkok': 'A vibrant city known for its ornate temples and bustling street life.',
        'Buenos Aires': 'Known for its European-style architecture and tango culture.',
        'Lisbon': 'Portugal hilly capital known for its colorful buildings.',
        'Hong Kong': 'Known for its skyline and vibrant food scene.',
        'Machu Picchu': 'An ancient Incan city set high in the Andes Mountains.',
    }
    if place in destinations:
        print(f"'{place}', nice choice {name}!")
        if age < 18:
            print(f"You might enjoy visiting {place} with your family.")
        else:
            print(f"If you visit {place} now, you'll have an amazing time exploring {destinations[place]}!")
    else:
        print(f"Sorry, '{place}' is not in our list of recommended destinations. Please try another destination")
        return chat_bot()

    activities = {
        'Paris': ['Visit the Eiffel Tower', 'Explore the Louvre Museum', 'Cruise along the Seine River'],
        'Tokyo': ['Visit the Tokyo Tower', 'Explore Shibuya Crossing', 'Visit Senso-ji Temple'],
        'Bali': ['Relax on the beaches of Kuta', 'Visit the Ubud Monkey Forest', 'Explore the Tegallalang Rice Terraces'],
        'New York': ['Visit Central Park', 'Explore Times Square', 'See the Statue of Liberty'],
        'Rome': ['Visit the Colosseum', 'Explore Vatican City', 'Throw a coin into the Trevi Fountain'],
        'London': ['Visit the British Museum', 'Explore the Tower of London', 'Watch a West End musical'],
        'Dubai': ['Visit the Burj Khalifa', 'Shop at the Dubai Mall', 'Take a desert safari'],
        'Sydney': ['Visit the Sydney Opera House', 'Relax at Bondi Beach', 'Climb the Sydney Harbour Bridge'],
        'Cairo': ['Visit the Pyramids of Giza', 'Explore the Egyptian Museum', 'Take a Nile River cruise'],
        'Rio de Janeiro': ['Visit Christ the Redeemer', 'Relax on Copacabana Beach', 'Explore Tijuca Forest'],
        'Amsterdam': ['Visit the Anne Frank House', 'Explore the Van Gogh Museum', 'Take a canal cruise'],
        'Barcelona': ['Visit La Sagrada Familia', 'Stroll through Park Güell', 'Enjoy tapas in the Gothic Quarter'],
        'Santorini': ['Watch the sunset in Oia', 'Explore the ancient ruins of Akrotiri', 'Relax on the beaches of Kamari'],
        'Bangkok': ['Visit the Grand Palace', 'Explore the Chatuchak Weekend Market', 'Take a boat ride through the canals'],
        'Buenos Aires': ['Attend a tango show', 'Visit San Telmo', 'Explore Recoleta Cemetery'],
        'Lisbon': ['Ride Tram 28', 'Visit Belém Tower', 'Explore Alfama district'],
        'Hong Kong': ['Visit Victoria Peak', 'Explore Mong Kok', 'Take a ferry ride on Victoria Harbour'],
        'Machu Picchu': ['Hike the Inca Trail', 'Explore the Sacred Valley', 'Visit the Sun Gate for panoramic views'],
    }

    if place in activities:
        suggested_activities = activities[place]
        print(f"Here are some activities you can do in {place}:")
        for activity in suggested_activities:
            print(f"- {activity}")
    else:
        print(f"Sorry, we don't have specific activities to recommend for '{place}' at the moment.")

    weather_conditions = ['sunny', 'cloudy', 'rainy', 'stormy']
    weather_forecast = random.choice(weather_conditions)
    print(f"The weather forecast for {place} is {weather_forecast} today.")

    while True:
        continue_chat = input('Would like to explore another destination or get more information ? (yes/no): ').strip().lower()
        if continue_chat == 'yes':
            chat_bot()
            break
        elif continue_chat == 'no':
            print('Thank you for chatting! Have a great day!')
            break
        else:
            print('Please answer with "yes" or "no"')
    
robo = chat_bot()

