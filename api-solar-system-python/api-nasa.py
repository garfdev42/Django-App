import requests

def get_comet_data(comet_id):
    try:
        url = f"http://api.nasa.gov/neo/rest/v1/neo/{comet_id}?api_key=fx0IXZKycwcqJ8eA5LVty0zitW9Fcopo53oAVC7T"
        response = requests.get(url)
        response.raise_for_status()

        comet_data = response.json()

        # Extracting name, estimated diameter, absolute magnitude, and orbital data
        name = comet_data.get('name', 'Unknown')
        diameter_km_min = comet_data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_min', 'Unknown')
        diameter_km_max = comet_data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max', 'Unknown')
        diameter_ft_min = comet_data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_min', 'Unknown')
        diameter_ft_max = comet_data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_max', 'Unknown')
        absolute_magnitude_h = comet_data.get('absolute_magnitude_h', 'Unknown')
        orbital_data = comet_data.get('orbital_data', {})

        print("Name:", name)
        print("Estimated Diameter (km): Min:", diameter_km_min, "Max:", diameter_km_max)
        print("Estimated Diameter (ft): Min:", diameter_ft_min, "Max:", diameter_ft_max)
        print("Absolute Magnitude (H):", absolute_magnitude_h)
        print("Orbital Data:")
        print("   Semi-major axis (AU):", orbital_data.get('semi_major_axis', 'Unknown'))
        print("   Eccentricity:", orbital_data.get('eccentricity', 'Unknown'))
        print("   Inclination (degrees):", orbital_data.get('inclination', 'Unknown'))
        print("   Perihelion distance (AU):", orbital_data.get('perihelion_distance', 'Unknown'))
        print("   Aphelion distance (AU):", orbital_data.get('aphelion_distance', 'Unknown'))

    except requests.exceptions.RequestException as e:
        print("API Error:", e)


get_comet_data(3726712)