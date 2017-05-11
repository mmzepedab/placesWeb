from django import forms
from models import Place, Category
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, Div
from django.core.urlresolvers import reverse_lazy
from django.forms.widgets import Input
from django.utils.safestring import mark_safe


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]


class GoogleMapWidget(Input):
    """
    Widget to display a Google Map on a page with the ability to move a marker
    around and fetch coordinates.
    """
    class Media:
        js = (
            'http://maps.google.com/maps/api/js?sensor=true&key=AIzaSyCmz7oHEd5LqSGdal0vtfWUOkxn9GSUKt4',
            'places/js/googlemap_location.js',
        )

    def render(self, name, value, attrs=None):
        """
        Attribute extras:
            width: width of the Google Map in pixels or percent. Must be the full string.
            height: height of the Google Map in pixels or percent. Must be the full string.
            markerMovedCallback: incase we don't want to populate the two default fields, let them specify their own callback.
            center: (lat, lng) coordinates in tuple format. If not provided, will auto-detect location if available.
            geolocate: Boolean. Default = True, If False, will not do any geolocation. Should be set to False if you provide a center() attribute
                    you do not want potentially over-ridden.
        """

        # Defaults, can be overriden by any same-key passed through `attrs`
        final_attrs = self.build_attrs(attrs)

        context = {
            'width': '600px',
            'height': '300px',
            'markerMovedCallback': 'null',
            'lat': 'null',
            'lng': 'null',
            'geolocate': 'true',
        }
        context.update(final_attrs)

        if 'center' in final_attrs:
            context['lat'], context['lng'] = final_attrs['center']

        html = u'''
        <input type='text' style='width: 400px;' id='map_search_text' /> <input type='button' id='map_search' value='Search' />
        </br>
        </br>
        <div id="map_canvas" style='width: %(width)s; height: %(height)s;'></div>
        <div id="map_message">Marker has been placed near the coordinates of your current location. Please adjust it to match the Places location.</div>
        <script type="text/javascript">
            //<![CDATA[
            var call_google_map = function(jQuery) {
                google_map_location.init({
                    'jQuery': jQuery,
                    markerMovedCallback: %(markerMovedCallback)s,
                    lat: %(lat)s,
                    lng: %(lng)s,
                    geolocate: %(geolocate)s
                });
                // Add some event handlers for our search box.
                jQuery("#map_search").click(function() {
                    google_map_location.codeAddress(jQuery("#map_search_text"));
                });
                jQuery("#map_search_text").keypress(function(e) {
                    if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
                        google_map_location.codeAddress(jQuery(this));
                        return false;
                    }
                });
            }
            // Do a simple check to see if we're using this widget in the admin.
            if (typeof django != 'undefined') {
                (function($) {
                    call_google_map($);
                })(django.jQuery);
            } else {
                call_google_map($);
            }
            //]]>
        </script>
        ''' % context

        return mark_safe(html)


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        exclude = ['user']


    address = forms.CharField(
        widget=forms.Textarea,
        label="Address",
        max_length=250,
        required=True,
    )

    decription = forms.CharField(
        label="Description",
        max_length=80,
        required=False,
    )

    search = forms.CharField(
        widget=GoogleMapWidget,
        required=False
    )


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-placeForm'
        self.helper.form_method = 'post'  # this line sets your form's method to post
        self.helper.form_action = reverse_lazy('create_place')  # this line sets the form action
        self.helper.layout = Layout(
            Fieldset(
                'Fill all fields to create a new place',
                Div(
                    Div(Field('name', onkeyup="showAlert()"), css_class='col-md-6', ),
                    Div('place_type_id', css_class='col-md-6', ),
                    css_class='row',
                ),
                HTML("""<p>We use notes to get better, <strong>please help us {{ request.user.username }}</strong></p>"""),
                'description',
                Div(
                    Div(Field('phone_number', onkeyup="showAlert()"), css_class='col-md-6', ),
                    Div('email', css_class='col-md-6', ),
                    css_class='row',
                ),
                Field('address', rows="4", cols="50", type="text"),
                'search',
                Field('latitude', readonly=True),
                Field('longitude', readonly=True),
                'image',
                'image_thumbnail',
                'image_cover',
            ),
            ButtonHolder(
                Submit('submit', 'Create', css_class='button white')
            )
        )
        super(PlaceForm, self).__init__(*args, **kwargs)
