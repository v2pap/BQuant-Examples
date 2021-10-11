from collections import deque, OrderedDict
from ipywidgets import BoundedFloatText, BoundedIntText, Button, Dropdown, FloatText, HBox, HTML, Label, Layout, RadioButtons, Text, Textarea, ToggleButton, VBox
import pandas as pd

from bqwidgets import DataGrid
from bqwidgets import DatePicker





# Buttons

class ComputeButton(Button):
    
    def __init__(self, width=110, button_style='success', description="COMPUTE", tooltip="Compute Allocations", *args, **kwargs):
        '''
        Summary:
            Standard, big Compute button from Button.
        Args:
            width (int): The width of the compute button.
            button_style (Enum): The style of the button. 'success' (default), 'info', 'warning', 'danger' or ''
            description (str): The string displayed on the button.
            tooltip (str): The string displayed when hovering on the button.
        '''
        layout = kwargs.pop('layout', Layout(width='{w}px'.format(w=str(width))))
        super().__init__(layout=layout, description=description, tooltip=tooltip, button_style=button_style, *args, **kwargs)
        on_click = kwargs.get('on_click', None)
        if on_click is not None:
            self.on_click(on_click)


# Selection of Parameter

class DropdownAndLabel(VBox):
    
    def __init__(self, options, label, width, init_value=None):
        '''
        Summary:
            A Dropdown with a label on top.
        Args:
            options (dict): The dict of options available in the dropdown mapped by names (keys) and values.
            label (str): The label on top of the dropdown.
            width (int): The width of the dropdown and the label.
            value (obj): The initial value.
        '''
        self.label = Label(value=label, layout=Layout(width='{w}px'.format(w=width)))
        if init_value is None:
            self.dd = Dropdown(options=options, layout=Layout(width='{w}px'.format(w=width)))
        else:
            self.dd = Dropdown(options=options, value=init_value, layout=Layout(width='{w}px'.format(w=width)))
        super().__init__(children=[self.label, self.dd], layout=Layout(margin='0 0 10px 0'))
    
    @property
    def value(self):
        ''' Returns the value selected from the dropdown.'''
        try:
            return self.dd.options.get(self.key)
        except AttributeError:
            return self.key
    
    @property
    def key(self):
        ''' Returns the key selected from the dropdown.'''
        return self.dd.label
    




class TextBoxAndLabel(VBox):
    
    def __init__(self, label, width, init_value='INDU Index'):
        '''
        Summary:
            A text box with a label on top.
        Args:
            label (str): the label on top of the text box.
            width (int): the width of the text box and the label.
            init_value (str): the initial value in the text box.
        '''
        self.label = Label(value=label, layout=Layout(width='{w}px'.format(w=width)))
        self.text = Text(value=init_value, layout=Layout(width='{w}px'.format(w=width)))
        super().__init__(children=[self.label, self.text], layout=Layout(margin='0 0 10px 0'))
        
    @property
    def value(self):
        ''' Returns the value selected from the slider.'''
        return self.text.value
    

class TextAreaAndLabel(VBox):
    
    def __init__(self, label, width, height, init_value='MXWO Index'):
        '''
        Summary:
            A text box with a label on top.
        Args:
            label (str): the label on top of the text box.
            width (int): the width of the text box and the label.
            init_value (str): the initial value in the text box.
        '''
        self.label = Label(value=label, layout=Layout(width='{w}px'.format(w=width)))
        self.textarea = Textarea(value=init_value, layout=Layout(width='{w}px'.format(w=width), height='{h}px'.format(h=height)))
        super().__init__(children=[self.label, self.textarea], layout=Layout(margin='0 0 10px 0'))
        
    @property
    def value(self):
        ''' Returns the value selected from the slider.'''
        return self.textarea.value.split(sep='\n', maxsplit=10)
    

class DatePickerAndLabel(VBox):
    
    def __init__(self, label, width, init_value=None):
        '''
        Summary:
            A DatePicker with a label on top.
        Args:
            label (str): the label on top of the dropdown.
            width (int): the width of the date picker and the label.
            init_value (str): the initial value.
        '''
        self.label = Label(value=label, layout=Layout(width='{w}px'.format(w=width)))
        if init_value is None:
            init_value = str(pd.datetime.today().date())
        self.dp = DatePicker(value=init_value, date_format='%Y-%m-%d', layout=Layout(width='{w}px'.format(w=width)))
        super().__init__(children=[self.label, self.dp], layout=Layout(margin='0 0 10px 0'))
        
    @property
    def value(self):
        ''' Returns the value selected from the dropdown.'''
        return self.dp.value
    


    

# Title

class AppTitle(HTML):
    
    def __init__(self, title, description=None, *args, **kwargs):
        ''' Standard title and description from HTML.'''
        value = '<h2 style="color: lightgrey; font-weight: bold;">{text}</h2>'.format(text=title)
        if description is not None:
            description = '<h4 style="color: lightgrey">{text}</h4>'.format(text=description)
            value = "".join([value, description])
        super().__init__(value=value, *args, **kwargs)
        self.layout.margin = '0px 0px 15px 0px'

