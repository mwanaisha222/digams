from django import forms

class AMRDashboardForm(forms.Form):
    # Define choices for each field based on the data available
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2000, 2025)]  # Example year range
    DRUG_CHOICES = [
        ('Carbapenem', 'Carbapenem'),
        ('Fluoroquinolone', 'Fluoroquinolone'),
        ('Cephalosporin', 'Cephalosporin'),
        ('Penicillin', 'Penicillin'),
        ('Vancomycin', 'Vancomycin'),
        ('Ampicillin', 'Ampicillin'),
        ('Clarithromycin', 'Clarithromycin')
    ]
    COUNTRY_CHOICES = [('All', 'All')]  # Populate dynamically from your data
    REGION_CHOICES = [('All', 'All')]  # Populate dynamically from your data
    MICROBE_CHOICES = [
        ('ESKAPEE', 'ESKAPEE'),
        ('WHO PRIORITY PATHOGENS', 'WHO PRIORITY PATHOGENS')
    ]

    selected_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    selected_drug = forms.ChoiceField(choices=DRUG_CHOICES, required=False)
    selected_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)
    selected_region = forms.ChoiceField(choices=REGION_CHOICES, required=False)
    selected_microbe = forms.ChoiceField(choices=MICROBE_CHOICES, required=False)
    selected_color_theme = forms.ChoiceField(choices=[
        ('blues', 'Blues'),
        ('cividis', 'Cividis'),
        ('greens', 'Greens'),
        ('inferno', 'Inferno'),
        ('magma', 'Magma'),
        ('plasma', 'Plasma'),
        ('reds', 'Reds'),
        ('rainbow', 'Rainbow'),
        ('turbo', 'Turbo'),
        ('viridis', 'Viridis')
    ], required=False)
