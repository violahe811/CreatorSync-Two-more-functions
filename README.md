# CreatorSync-Two-more-functions week13
# CreatorSync
## Overview
CreatorSync is a web application designed to connect content creators with brands and marketing campaigns. The platform allows creators to browse available campaigns, apply to opportunities, manage their applications, and maintain a professional creator profile. Brands can showcase campaigns and discover potential creators for collaboration.

The project was built using Django, HTML, CSS, JavaScript, Bootstrap, and SQLite.

---

## Features

### User Authentication

* User registration
* User login and logout
* Secure authentication using Django's built-in authentication system

### Campaign Management

* View all available campaigns
* View detailed information for each campaign
* Apply to campaigns directly from the platform

### Creator Profiles

* Create and edit creator profiles
* Store Instagram username
* Store TikTok username
* Track follower count

### Application Tracking

* View submitted campaign applications
* Track application status
* Access campaign information from the dashboard

### Advanced JavaScript Interactivity

* Real-time campaign search
* Instant filtering without page refresh
* Dynamic DOM manipulation using JavaScript event listeners

### Data Visualization

* Dashboard statistics cards
* Total Applications count
* Total Campaigns count
* Total Creators count
* Interactive bar chart using Chart.js

---

## Technologies Used

### Backend

* Python
* Django 4.2

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Database

* SQLite

### Libraries

* Chart.js

---

## Project Structure

```text
creatorsync/
│
├── models.py
├── views.py
├── urls.py
├── admin.py
│
├── templates/
│   └── creatorsync/
│       ├── index.html
│       ├── campaigns.html
│       ├── campaign_detail.html
│       ├── dashboard.html
│       ├── profile.html
│       ├── edit_profile.html
│       ├── applications.html
│       ├── creators.html
│       ├── login.html
│       └── register.html
│
├── static/
│   └── creatorsync/
│       ├── styles.css
│       └── script.js
│
└── migrations/
```

---

## Enhancements Implemented

### Enhancement 1: Advanced JavaScript Search

A real-time search feature was added to the Campaigns page. Users can type into the search box and campaigns are filtered instantly without reloading the page. This feature improves usability and provides a smoother browsing experience.

### Enhancement 2: Data Visualization Dashboard

A statistics dashboard was implemented using Chart.js. Users can view visual summaries of platform activity, including:

* Total Applications
* Total Campaigns
* Total Creators

The chart provides a quick overview of platform data and improves information accessibility.

---

## Future Improvements

* Brand account management
* Campaign creation by brands
* Messaging system between creators and brands
* Email notifications
* Campaign analytics
* Creator performance metrics

---

## Author

Viola

Capstone Project – Introduction to Web Development
