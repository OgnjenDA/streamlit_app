import streamlit as st
from joblib import load
import pandas as pd

# Load your trained model (make sure the path is correct)
regressor = load('xgb_regressor_model.joblib')


# Define a function to get user input
def user_input_features():
    dwelling_type = st.sidebar.selectbox('Dwelling Type', 
                          ('Detached', 'Semi-detached', 'Mid-terrace', 'End-terrace',
                          'Flat – purpose built', 'Flat – converted'))
    adult_occupants = st.sidebar.number_input('Adult OccupantsNo.', min_value=0)
    child_occupants = st.sidebar.number_input('Child OccupantsNo.', min_value=0)
    region = st.sidebar.selectbox('Region', 
                          ('North East', 'Yorkshire and The Humber', 'North West', 'East Midlands', 
                           'West Midlands', 'South West', 'East of England', 'South East', 
                           'London', 'Western Scotland', 'Eastern Scotland', 'Northern Scotland'))
    external_wall_construction = st.sidebar.selectbox('External Wall Construction', 
                                              ('Stone: granite or whin (as built)', 'Stone: sandstone (as built)', 
                                               'Solid brick (as built)', 'Stone/solid brick (external insulation)', 
                                               'Stone/solid brick (internal insulation)', 'Cob (as built)', 
                                               'Cob (external insulation)', 'Cob (internal insulation)', 
                                               'Cavity (as built)', 'Filled cavity / Cavity with insulation (internal/external)', 
                                               'Timber frame', 'System build (as built)', 
                                               'System build (external insulation)', 'System build (internal insulation)', 
                                               'Metal Frame', '0 Not Applicable'))
    semi_exposed_wall_construction = st.sidebar.selectbox('Semi Exposed Wall Construction', 
                                              ('Stone: granite or whin (as built)', 'Stone: sandstone (as built)', 
                                               'Solid brick (as built)', 'Stone/solid brick (external insulation)', 
                                               'Stone/solid brick (internal insulation)', 'Cob (as built)', 
                                               'Cob (external insulation)', 'Cob (internal insulation)', 
                                               'Cavity (as built)', 'Filled cavity / Cavity with insulation (internal/external)', 
                                               'Timber frame', 'System build (as built)', 
                                               'System build (external insulation)', 'System build (internal insulation)', 
                                               'Metal Frame', '0 Not Applicable'))
    roof_construction = st.sidebar.selectbox('Roof Construction', 
                                    ('Pitched, slates or tiles', 'Thatched roof', 
                                    'Flat roof', '0 (not applicable)'))

    loft_insulation = st.sidebar.selectbox('Loft Insulation', 
                                   ('0 (no insulation)', '25 (mm)', '50 (mm)', 
                                    '75 (mm)', '100 (mm)', '125 (mm)', 
                                    '150 (mm)', '200 (mm)', '250 (mm)', 
                                    '300 (mm)', '>300 (mm)'))
    dhw_system = st.sidebar.selectbox('DHW System', 
                              ('Gas standard', 'Gas - combi (storage)', 
                               'Gas - combi (instantaneous)', 'Gas back boiler', 
                               'Oil standard', 'Solid boiler (house coal/anthracite)', 
                               'Biomass boiler', 'Electric boiler', 
                               'Other electric', 'Community heating without CHP', 
                               'Community heating with CHP'))

    dhw_boiler_with_central_heating = st.sidebar.selectbox('DHW Boiler with Central Heating', 
                                                   ('Yes', 'No'))

    dhw_electric_system = st.sidebar.selectbox('DHW Electric System', 
                                       ('Single Immersion', 'Dual Immersion', 
                                        'Other electric', 'Not applicable'))

    dhw_cylinder_insulation = st.sidebar.selectbox('DHW Cylinder Insulation', 
                                           ('No cylinder', 'Loose jacket', 
                                            'Factory spray foam', 'Cylinder not insulated'))
    
    solar_dhw_in_cylinder = st.sidebar.selectbox('Solar DHW in Cylinder', 
                                         ('No', 'Yes', 'No Solar DHW'))
    
    solar_dhw_storage = st.sidebar.number_input('Solar DHW Storagelitre', min_value=0)
    main_heating_system = st.sidebar.selectbox('Main Heating System', 
                                       ('Gas standard', 'Gas - combi', 'Gas back boiler', 'Oil standard', 
                                        'Solid boiler (house coal/anthracite)', 'Electric boiler', 'Electric storage', 
                                        'Electric room heater', 'Warm air - gas fired', 'Warm air - electric', 
                                        'Community heating without CHP', 'Community heating with CHP', 
                                        'Biomass boiler', 'Ground source heat pump', 'Air source heat pump'))

    main_heating_electric_tariff = st.sidebar.selectbox('Main Heating Electric Tariff', 
                                                ('Off-peak tariff (Economy 7)', 'Off-peak tariff (Economy 10)', 
                                                 '24-hour heating tariff', 'Standard tariff', '0 (not applicable)'))

    main_heating_flue_type = st.sidebar.selectbox('Main Heating - Flue Type', 
                                          ('Open', 'Balanced', 'Fan'))
    main_heating_oil_pump_location = st.sidebar.selectbox('Main Heating - Oil Boiler Pump Location', 
                                                  ('Inside dwelling', 'Outside dwelling', 'Not Applicable'))

    main_heating_heat_emitter = st.sidebar.selectbox('Heat Emitter', 
                                ('Not applicable', 'Radiators', 'Underfloor', 'Electric or storage panel'))

    main_heating_control_programmer = st.sidebar.selectbox('Heating Control - Programmer', 
                                              ('Programmer: no', 'Programmer: yes'))

    low_energy_lighting = st.sidebar.slider('Low Energy Lighting%', 0, 100, 50)
    total_floor_area = st.sidebar.number_input('Total Floor Aream2', min_value=0)
    age_of_property = st.sidebar.selectbox('Age of Property',
                                           ('Before 1900', '1983 - 1990', '1930 - 1949', '1967 - 1975',
                                            '2003 - 2007', '1950 - 1966', '1976 - 1982', '1991 - 1995',
                                            '1900 - 1929', '1996 - 2002'))

    # Convert categorical inputs to corresponding numerical values
    dwelling_type_dict = {'Detached': 1, 
                          'Semi-detached': 2, 
                          'Mid-terrace': 3, 
                          'End-terrace': 4, 
                          'Flat – purpose built': 5, 
                          'Flat – converted': 6
                          }
    dwelling_type_value = dwelling_type_dict[dwelling_type]


    region_dict = {'North East': 1, 'Yorkshire and The Humber': 2, 'North West': 3, 'East Midlands': 4, 
                   'West Midlands': 5, 'South West': 6, 'East of England': 7, 'South East': 8, 
                   'London': 9, 'Western Scotland': 10, 'Eastern Scotland': 11, 'Northern Scotland': 12}
    region_value = region_dict[region]
    
    age_of_property_dict = {'Before 1900':1, '1983 - 1990':7, '1930 - 1949':3, '1967 - 1975':5,
       '2003 - 2007':10, '1950 - 1966':4, '1976 - 1982':6, '1991 - 1995':8,
       '1900 - 1929':2, '1996 - 2002':9}
    
    age_of_property_value = age_of_property_dict[age_of_property]
    
    external_wall_construction_dict = {
        'Stone: granite or whin (as built)': 1, 'Stone: sandstone (as built)': 2, 
        'Solid brick (as built)': 3, 'Stone/solid brick (external insulation)': 4, 
        'Stone/solid brick (internal insulation)': 5, 'Cob (as built)': 6, 
        'Cob (external insulation)': 7, 'Cob (internal insulation)': 8, 
        'Cavity (as built)': 9, 'Filled cavity / Cavity with insulation (internal/external)': 10, 
        'Timber frame': 11, 'System build (as built)': 12, 
        'System build (external insulation)': 13, 'System build (internal insulation)': 14, 
        'Metal Frame': 15, '0': 16
    }
    external_wall_construction_value = external_wall_construction_dict[external_wall_construction]

        # Convert categorical inputs to corresponding numerical values
    roof_construction_dict = {
        'Pitched, slates or tiles': 1, 'Thatched roof': 2, 
        'Flat roof': 3, '0 (not applicable)': 4
    }
    roof_construction_value = roof_construction_dict[roof_construction]

    loft_insulation_dict = {
        '0 (no insulation)': 1, '25 (mm)': 2, '50 (mm)': 3, 
        '75 (mm)': 4, '100 (mm)': 5, '125 (mm)': 6, 
        '150 (mm)': 7, '200 (mm)': 8, '250 (mm)': 9, 
        '300 (mm)': 10, '>300 (mm)': 11
    }
    loft_insulation_value = loft_insulation_dict[loft_insulation]
    
    dhw_system_dict = {
        'Gas standard': 1, 'Gas - combi (storage)': 2, 
        'Gas - combi (instantaneous)': 3, 'Gas back boiler': 4, 
        'Oil standard': 5, 'Solid boiler (house coal/anthracite)': 6, 
        'Biomass boiler': 7, 'Electric boiler': 8, 
        'Other electric': 9, 'Community heating without CHP': 10, 
        'Community heating with CHP': 11
    }
    dhw_system_value = dhw_system_dict[dhw_system]

    # Convert categorical input to corresponding numerical values
    dhw_boiler_with_central_heating_dict = {'Yes': 1, 'No': 2}
    dhw_boiler_with_central_heating_value = dhw_boiler_with_central_heating_dict[dhw_boiler_with_central_heating]

    dhw_electric_system_dict = {'Single Immersion': 1, 'Dual Immersion': 2, 
                                'Other electric': 3, 'Not applicable': 4}
    dhw_electric_system_value = dhw_electric_system_dict[dhw_electric_system]

    dhw_cylinder_insulation_dict = {'No cylinder': 1, 'Loose jacket': 2, 
                                    'Factory spray foam': 3, 'Cylinder not insulated': 4}
    dhw_cylinder_insulation_value = dhw_cylinder_insulation_dict[dhw_cylinder_insulation]

    solar_dhw_in_cylinder_dict = {'No': 1, 'Yes': 2, 'No Solar DHW': 3}
    solar_dhw_in_cylinder_value = solar_dhw_in_cylinder_dict[solar_dhw_in_cylinder]
    
    main_heating_system_dict = {
        'Gas standard': 1, 'Gas - combi': 2, 'Gas back boiler': 3, 'Oil standard': 4, 
        'Solid boiler (house coal/anthracite)': 5, 'Electric boiler': 6, 'Electric storage': 7, 
        'Electric room heater': 8, 'Warm air - gas fired': 9, 'Warm air - electric': 10, 
        'Community heating without CHP': 11, 'Community heating with CHP': 12, 
        'Biomass boiler': 13, 'Ground source heat pump': 14, 'Air source heat pump': 15
    }
    main_heating_system_value = main_heating_system_dict[main_heating_system]

    main_heating_electric_tariff_dict = {
        'Off-peak tariff (Economy 7)': 1, 'Off-peak tariff (Economy 10)': 2, 
        '24-hour heating tariff': 3, 'Standard tariff': 4, '0 (not applicable)': 5
    }
    main_heating_electric_tariff_value = main_heating_electric_tariff_dict[main_heating_electric_tariff]

    main_heating_flue_type_dict = {
        'Open': 1, 'Balanced': 2, 'Fan': 3
    }
    main_heating_flue_type_value = main_heating_flue_type_dict[main_heating_flue_type]

        # Convert categorical input to corresponding numerical values
    main_heating_oil_pump_location_dict = {
        'Inside dwelling': 1, 'Outside dwelling': 2, 'Not Applicable': 3
    }
    main_heating_oil_pump_location_value = main_heating_oil_pump_location_dict[main_heating_oil_pump_location]

    main_heating_heat_emitter_dict = {
        'Not applicable': 1,
        'Radiators': 2,
        'Underfloor': 3,
        'Electric or storage panel': 4
    }
  
    main_heating_heat_emitter_value = main_heating_heat_emitter_dict[main_heating_heat_emitter]

    # Dropdown for Heating Control - Programmer
    main_heating_control_programmer_dict = {
        'Programmer: no': 1,
        'Programmer: yes': 2
    }
    main_heating_control_programmer_value = main_heating_control_programmer_dict[main_heating_control_programmer]


    data = {
        'Dwelling Type[1-7]': dwelling_type_value,
        'Adult OccupantsNo.': adult_occupants,
        'Child OccupantsNo.': child_occupants,
        'Region[1-12]': region_value,
        'External Wall Construction[1-16]': external_wall_construction_value,
        'Semi-exposed Wall Construction[1-16]': external_wall_construction_value,
        'Roof Construction[1-4]': roof_construction_value,
        'Loft Insulation[1-12]': loft_insulation_value,
        'DHW System[1-11]': dhw_system_value,
        'DHW Boiler with Central Heating[1/2]': dhw_boiler_with_central_heating_value,
        'DHW Electric System Type[1-4]': dhw_electric_system_value,
        'Cylinder Insulation Type[1-4]': dhw_cylinder_insulation_value,
        'Solar DHW in Cylinder[1-3]': solar_dhw_in_cylinder_value,
        'Solar DHW Storagelitre': solar_dhw_storage,
        'Main Heating System[1-15]': main_heating_system_value,
        'Main Heating - Electric Tariff[1-5]': main_heating_electric_tariff_value,
        'Main Heating - Heater Flue[1-3]': main_heating_flue_type_value,
        'Main Heating - Oil Pump Location[1-3]': main_heating_oil_pump_location_value,
        'Main Heating - Heat Emitter[1-4]': main_heating_heat_emitter_value,
        'Main Heating Control - Programmer[1/2]': main_heating_control_programmer_value,
        'Low Energy Lighting%': low_energy_lighting,
        'Total Floor Aream2': total_floor_area,
        'Age of Property': age_of_property_value
    }
    return pd.DataFrame(data, index=[0])

# Main app
st.write("# Energy Consumption Prediction App")

# Get user input
input_df = user_input_features()

# Predict and display the output
if st.button('Predict'):
    prediction = regressor.predict(input_df)
    st.write("## Prediction Result:")
    st.write(f"Predicted Total (£/year): {prediction[0]:.2f}")
    
    
    
    