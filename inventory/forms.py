from cProfile import label
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem, SpecificItem, Room, Status
from django import forms
from django.contrib.auth.models import Group
from crispy_forms.layout import Layout, Fieldset, Div, ButtonHolder, Submit
from django import forms




class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = [
            'name', 'quantity', 'category', 'supplier', 'serial', 'local',
            'image', 'groups',
            'requirement_las_vegas', 'propose_spare_las_vegas',
            'requirement_abu_dhabi', 'propose_spare_abu_dhabi',
            'requirement_monaco', 'propose_spare_monaco',
            'requirement_suzuka', 'propose_spare_suzuka',
            'c1_requirement_las_vegas', 'c1_propose_spare_las_vegas',
            'c2_requirement_abu_dhabi', 'c2_propose_spare_abu_dhabi',
            'c4_requirement_monaco', 'c4_propose_spare_monaco',
            'c3_requirement_suzuka', 'c3_propose_spare_suzuka',
            'it_room_requirements', 'it_room_propose_spare',
            'it_room_storage_requirement', 'it_room_storage_propose_spare',
            'storage_1_requirement', 'storage_1_propose_spare',
            'admin_hr_requirement', 'admin_hr_propose_spare',
            'hallway_requirement', 'hallway_propose_spare',
            'commentator_pantry_requirement', 'commentator_pantry_propose_spare',
            'requirement_ph_studio', 'propose_spare_ph_studio',
            'requirement_3d_dept', 'propose_spare_3d_dept',
            'requirement_plinko', 'propose_spare_plinko',
            'requirement_seven_floor', 'propose_spare_seven_floor',
            'requirement_mini_pitx', 'propose_spare_mini_pitx',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Update label for 'groups'
        if 'groups' in self.fields:
            self.fields['groups'].label = "Assigned TO:"

        # Group fields by category
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # General Information Section
            Fieldset(
                "General Information",
                'name', 'quantity', 'category', 'supplier',
                'serial', 'local', 'model','groups', 'image',
            ),
            # Requirements Section
            Fieldset(
                "Requirements",
                Div(
                    'requirement_las_vegas',
                    'requirement_abu_dhabi',
                    'requirement_monaco',
                    'requirement_suzuka',
                    'requirement_ph_studio',
                    'requirement_3d_dept',
                    'requirement_mini_pitx',
                    'requirement_seven_floor',
                    'requirement_plinko',
                    css_class="requirements-container"
                ),
            ),
            # Proposed Spares Section
            Fieldset(
                "Proposed Spares",
                Div(
                    'propose_spare_las_vegas',
                    'propose_spare_abu_dhabi',
                    'propose_spare_monaco',
                    'propose_spare_suzuka',
                    'propose_spare_ph_studio',
                    'propose_spare_3d_dept',
                    'propose_spare_mini_pitx',
                    'propose_spare_seven_floor',
                    'propose_spare_plinko',
                    css_class="propose-spares-container"
                ),
            ),
            # Submit Button
            ButtonHolder(
                Submit('submit', 'Save Item', css_class='btn-primary')
            )
        )

        # Make fields readonly if the user is not a superuser
        if self.user and not self.user.is_superuser:
            self._set_field_readonly('requirement_las_vegas')
            self._set_field_readonly('propose_spare_las_vegas')
            self._set_field_readonly('requirement_abu_dhabi')
            self._set_field_readonly('propose_spare_abu_dhabi')
            self._set_field_readonly('requirement_monaco')
            self._set_field_readonly('propose_spare_monaco')
            self._set_field_readonly('requirement_suzuka')
            self._set_field_readonly('propose_spare_suzuka')
            self._set_field_readonly('requirement_ph_studio')
            self._set_field_readonly('propose_spare_ph_studio')
            self._set_field_readonly('requirement_mini_pitx')
            self._set_field_readonly('propose_spare_mini_pitx')
            self._set_field_readonly('requirement_plinko')
            self._set_field_readonly('propose_spare_plinko')
            self._set_field_readonly('requirement_3d_dept')
            self._set_field_readonly('propose_spare_3d_dept')
            self._set_field_readonly('requirement_seven_floor')
            self._set_field_readonly('propose_spare_seven_floor')


    def _set_field_readonly(self, field_name):
        field = self.fields.get(field_name)
        if field:
            field.widget.attrs['readonly'] = True
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' locked-field'

class InventoryItemSearchForm(forms.Form):
		query = forms.CharField(max_length=200, required=False, label="Search Inventory Items")


class InventoryFullItemSearchForm(forms.Form):
		query1 = forms.CharField(max_length=200, required=False, label="Search Inventory Items")



class SpecificItemStatusForm(forms.ModelForm):
    class Meta:
        model = SpecificItem
        fields = ['status', 'label','room','serial','model','details']  # Make sure 'label' is included

    # Optionally, you can add custom validation or widgets here
    label = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    room = forms.ModelChoiceField(
        queryset=Room.objects.all(),
        required=False,  # Allow no room selection
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    serial = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    status = forms.ChoiceField(
        choices=SpecificItem.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    model = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    details = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        room = cleaned_data.get('room')
        label = cleaned_data.get('label')

        # Validation: Require room selection if status is 'inUse'
        if status == 'inUse' and not room:
            raise forms.ValidationError({
                'room': "You must select a room when the status is 'inUse'."
            })

        # Validation: Ensure no room selection for disallowed statuses, excluding 'backup/Stock'
        disallowed_statuses = ['broken', 'resell']  # Exclude 'backup/Stock'
        if status in disallowed_statuses and room:
            raise forms.ValidationError({
                'room': f"Room selection is not allowed when the status is '{status}'."
            })

        # Validation: Ensure the label is provided
        if not label:
            raise forms.ValidationError({
                'label': "Label must be filled out."
            })

        return cleaned_data





from django import forms
from .models import Obstacle

class ObstacleForm(forms.ModelForm):
    class Meta:
        model = Obstacle
        fields = ['studio', 'file', 'image','details']  # Add 'image' field here
        widgets = {
            'details': forms.Textarea(attrs={
                'placeholder': 'OBSTACLES DETAILS',
                'rows': 1,
                'class': 'form-control'
            }),
        }
