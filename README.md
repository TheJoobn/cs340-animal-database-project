# Animal Rescue Dashboard

**CS-340: Client/Server Development**

A Python and MongoDB application that provides an interactive dashboard for exploring Austin Animal Center data and identifying animals that match specific rescue-training criteria.

The project combines a reusable MongoDB CRUD layer with an interactive Dash interface containing database-driven filtering, a sortable data table, data visualization, and geographic mapping.

## Technologies

- Python
- MongoDB
- PyMongo
- Dash
- JupyterDash
- Pandas
- Plotly
- Dash Leaflet
- Jupyter Notebook

## Project Overview

The application was developed around a client scenario for Grazioso Salvare, an organization that identifies shelter dogs as candidates for different types of rescue training.

The dashboard allows animal records to be filtered according to characteristics associated with:

- Water Rescue
- Mountain or Wilderness Rescue
- Disaster or Individual Tracking

The selected rescue category is translated into a MongoDB query using criteria such as breed, age, and sex.

## MongoDB CRUD Module

The `AnimalShelter` class provides a reusable interface between Python and the MongoDB animal collection.

It implements the four primary CRUD operations:

- **Create** — Insert a new animal document
- **Read** — Retrieve documents matching a MongoDB query
- **Update** — Modify documents matching a query
- **Delete** — Remove documents matching a query

The dashboard uses this database layer rather than placing MongoDB access logic directly throughout the interface code.

## Dashboard Features

### Rescue-Type Filtering

Users can filter the dataset by rescue-training category.

Each category generates a MongoDB query based on the breed, age, and sex characteristics required for that type of rescue work.

A reset option restores the complete dataset.

### Interactive Data Table

The dashboard displays animal records in a Dash DataTable with:

- Sorting
- Case-insensitive filtering
- Row selection
- Column selection
- Pagination
- Selected-row and selected-column highlighting

### Outcome Visualization

A Plotly chart displays the distribution of animal outcome types for the currently filtered dataset.

Because the chart is generated from the filtered records, it updates as the selected rescue category changes.

### Geographic Map

Selecting an animal updates an interactive map using the latitude and longitude stored in the dataset.

The map places a marker at the animal's location and displays identifying information such as the animal's name and breed.

## Application Structure

The project separates database functionality from dashboard functionality.

### `animal_shelter.py`

Contains the `AnimalShelter` class responsible for communicating with MongoDB and performing CRUD operations.

### `animal_rescue_database_v2.0.ipynb`

Contains the interactive dashboard, including:

- Database queries
- Rescue-category filters
- Dash layout
- Data table
- Plotly visualization
- Geographic map
- Dashboard callbacks

## Client-Server Design

The application follows a client/server approach in which MongoDB provides persistent animal records while the Python application queries and presents that information through an interactive dashboard.

The CRUD module creates a reusable abstraction around database access, allowing queries to be passed into methods without duplicating MongoDB connection logic throughout the application.

The dashboard then uses those query results to update the table, visualization, and map.

## Skills Demonstrated

- Python
- MongoDB
- PyMongo
- CRUD Operations
- Database Queries
- Client-Server Architecture
- Dashboard Development
- Data Filtering
- Data Visualization
- Interactive UI Callbacks
- Pandas Data Manipulation
- Geographic Data Visualization

## Course Context

This project was completed for **CS-340: Client/Server Development** at Southern New Hampshire University.

The course project focused on connecting a Python application to MongoDB, creating reusable CRUD functionality, and using database results to build an interactive dashboard for a client scenario.
