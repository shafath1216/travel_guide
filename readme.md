Travel Bangladesh

A dynamic web application built with Django and Tailwind CSS that serves as a travel guide for cities in Bangladesh. Users can explore top attractions, hotels, restaurants, and travel packages for each city. All content is fully managed through the Django admin panel.

Dynamic Features

Home Page:
The home page dynamically displays all cities available in the database. Each city is shown with a link that takes visitors to its detailed city page.

City Pages:
Each city page is dynamically generated based on the database content and includes:

Top Attractions: Images, descriptions, and entry fees.

Hotels: Address, phone number, and website if available.

Restaurants: Address and contact information.

Google Map: Interactive map showing the city location.

User Reviews: Logged-in users can post reviews about the city, which display the review text along with the username and timestamp. Visitors can read all reviews without logging in.

Packages Page:
A dedicated page listing travel packages for different cities. Each package includes:

Package name

Description

Price

Duration in days

Associated city

All content updates automatically when new entries are added or modified in the Django admin panel—no changes to the HTML templates are required.