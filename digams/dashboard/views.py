from django.shortcuts import render
from .forms import AMRDashboardForm
import pandas as pd
import plotly.express as px

# Define the species categories
eskapee_spp = ["Acinetobacter", "Pseudomonas", "Enterobacter", "Staphylococcus", "Helicobacter"]
who_priority_spp = ["Escherichia", "Klebsiella", "Staphylococcus", "Enterococcus", "Pseudomonas"]


# Load your data from all three CSV files
data1 = pd.read_csv('digams/2024_05_28 atlas_antibiotics.csv', low_memory=False)
data2 = pd.read_csv('digams/eskapee.csv', low_memory=False)  # Replace with your file name
data3 = pd.read_csv('digams/who_priority.csv', low_memory=False)  # Replace with your file name

# Combine the data
data = pd.concat([data1, data2, data3], ignore_index=True)

# Convert relevant columns to numeric to avoid type errors
data['Amoxycillin clavulanate'] = pd.to_numeric(data['Amoxycillin clavulanate'], errors='coerce')
data['Amoxycillin clavulanate_I'] = pd.to_numeric(data['Amoxycillin clavulanate_I'], errors='coerce')

# Calculate the Resistance Fraction
data['Resistance Fraction'] = data['Amoxycillin clavulanate'] / (data['Amoxycillin clavulanate'] + data['Amoxycillin clavulanate_I'])

# Handle any NaN values in the Resistance Fraction (optional)
data['Resistance Fraction'] = data['Resistance Fraction'].fillna(0)

def amr_dashboard(request):
    form = AMRDashboardForm(request.POST or None)
    filtered_data = data.copy()

    if form.is_valid():
        selected_year = form.cleaned_data.get('selected_year')
        selected_drug = form.cleaned_data.get('selected_drug')
        selected_country = form.cleaned_data.get('selected_country')
        selected_region = form.cleaned_data.get('selected_region')
        selected_microbe = form.cleaned_data.get('selected_microbe')
        selected_color_theme = form.cleaned_data.get('selected_color_theme')

        if selected_year:
            filtered_data = filtered_data[filtered_data['Year'] == int(selected_year)]
        if selected_country and selected_country != 'All':
            filtered_data = filtered_data[filtered_data['Country'] == selected_country]
        if selected_region and selected_region != 'All':
            filtered_data = filtered_data[filtered_data['Region'] == selected_region]
        if selected_microbe:
            if selected_microbe == 'ESKAPEE':
                filtered_data = filtered_data[filtered_data['Species'].isin(eskapee_spp)]
            elif selected_microbe == 'WHO PRIORITY PATHOGENS':
                filtered_data = filtered_data[filtered_data['Species'].isin(who_priority_spp)]

        # Generate visualizations based on filtered data
        fig = px.line(filtered_data, x='Year', y='Resistance Fraction', color='Species', title='Resistance Trends')
        line_chart = fig.to_html(full_html=False)

        bar_fig = px.bar(filtered_data, x='Species', y='Amoxycillin clavulanate', color='Species', title='Amoxycillin clavulanate')
        bar_chart = bar_fig.to_html(full_html=False)

    else:
        line_chart = None
        bar_chart = None

    context = {
        'form': form,
        'line_chart': line_chart,
        'bar_chart': bar_chart,
    }

    return render(request, 'amr_dashboard.html', context)
