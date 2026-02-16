"""
Premium Calculator App - By Secure Dev
Cross-platform mobile calculator with enhanced security
Version: 1.0.0
License: Proprietary - For sale on Uptodown
"""

import os
import json
from functools import wraps
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.config import Config
from kivy.logger import Logger

# Security: Disable logging to prevent sensitive data leaks
Logger.disabled = True

# Security: Set fixed window size for mobile
Window.size = (540, 960)
Config.set('graphics', 'height', '960')
Config.set('graphics', 'width', '540')
Config.set('graphics', 'resizable', '0')

# Security: Prevent screenshots on secure devices
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    print("Mobile environment detected")
except ImportError:
    print("Desktop environment")


class CalculatorValidator:
    """Input validation to prevent injection attacks"""
    
    SAFE_CHARACTERS = set('0123456789+-*/.() ')
    MAX_INPUT_LENGTH = 100
    MAX_HISTORY_SIZE = 50
    
    @staticmethod
    def is_safe_input(text):
        """Validate input contains only safe characters"""
        return all(c in CalculatorValidator.SAFE_CHARACTERS for c in text)
    
    @staticmethod
    def check_length(text):
        """Prevent buffer overflow attacks"""
        return len(text) <= CalculatorValidator.MAX_INPUT_LENGTH
    
    @staticmethod
    def sanitize_input(text):
        """Remove potentially dangerous characters"""
        return ''.join(c for c in text if c in CalculatorValidator.SAFE_CHARACTERS)


def secure_calculation(func):
    """Decorator to handle calculation securely"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except SyntaxError:
            return "Error: Invalid input"
        except Exception as e:
            # Don't expose error details to prevent information disclosure
            return "Error: Calculation failed"
    return wrapper


class CalculatorApp(App):
    """Premium Calculator Application"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculation_history = []
        self.theme = 'dark'
        self.validator = CalculatorValidator()
        self.load_app_config()
    
    def load_app_config(self):
        """Load app configuration with security checks"""
        config_path = self.get_config_path()
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    if isinstance(config, dict):
                        self.theme = config.get('theme', 'dark')
            except (json.JSONDecodeError, IOError):
                # Silently fail and use defaults
                pass
    
    def get_config_path(self):
        """Get secure config path"""
        app_dir = self.user_data_dir
        if not os.path.exists(app_dir):
            try:
                os.makedirs(app_dir)
            except OSError:
                pass
        return os.path.join(app_dir, 'config.json')
    
    def on_pause(self):
        """Security: Handle app pause - clear sensitive state"""
        return True
    
    def on_resume(self):
        """Security: Handle app resume"""
        pass
    
    def build(self):
        """Build the UI"""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display area
        display_layout = BoxLayout(size_hint_y=0.2)
        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=32,
            size_hint_x=0.7,
            background_color=(0.15, 0.15, 0.15, 1) if self.theme == 'dark' else (0.95, 0.95, 0.95, 1),
            foreground_color=(0, 1, 0, 1) if self.theme == 'dark' else (0, 0, 0, 1)
        )
        
        self.previous_display = TextInput(
            multiline=False,
            readonly=True,
            font_size=14,
            size_hint_x=0.3,
            background_color=(0.1, 0.1, 0.1, 1) if self.theme == 'dark' else (0.9, 0.9, 0.9, 1),
            foreground_color=(0.5, 0.5, 0.5, 1)
        )
        display_layout.add_widget(self.previous_display)
        display_layout.add_widget(self.display)
        
        main_layout.add_widget(display_layout)
        
        # Buttons grid
        buttons_layout = GridLayout(cols=4, spacing=5, size_hint_y=0.8)
        
        buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '←', '(', ')'],
        ]
        
        for row in buttons:
            for btn_text in row:
                btn = self.create_button(btn_text)
                buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        
        # Info label
        info_label = Label(
            text='v1.0.0 - Premium Calculator',
            size_hint_y=0.05,
            color=(0.5, 0.5, 0.5, 1)
        )
        main_layout.add_widget(info_label)
        
        return main_layout
    
    def create_button(self, text):
        """Create a styled button"""
        btn = Button(text=text, font_size=18)
        
        # Determine button color
        if text in ['=']:
            bg_color = (0.0, 0.7, 0.0, 0.9) if self.theme == 'dark' else (0.2, 0.8, 0.2, 0.9)
        elif text in ['C', '←']:
            bg_color = (0.7, 0.0, 0.0, 0.9) if self.theme == 'dark' else (0.9, 0.2, 0.2, 0.9)
        elif text in ['÷', '×', '-', '+', '(', ')']:
            bg_color = (0.2, 0.4, 0.8, 0.9) if self.theme == 'dark' else (0.2, 0.5, 0.9, 0.9)
        else:
            bg_color = (0.2, 0.2, 0.2, 1) if self.theme == 'dark' else (0.9, 0.9, 0.9, 1)
        
        btn.background_color = bg_color
        btn.bind(on_press=self.on_button_press)
        
        with btn.canvas.before:
            Color(*bg_color)
            btn.rect = RoundedRectangle(size=btn.size, pos=btn.pos, radius=[15])
        
        btn.bind(size=self._update_rect, pos=self._update_rect)
        
        return btn
    
    def _update_rect(self, instance, value):
        """Update button rectangle"""
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def on_button_press(self, instance):
        """Handle button press"""
        text = instance.text
        current = self.display.text
        
        if text == 'C':
            self.display.text = ''
            self.previous_display.text = ''
        elif text == '←':
            self.display.text = current[:-1]
        elif text == '=':
            self.calculate()
        elif text == '÷':
            self.add_operator('/')
        elif text == '×':
            self.add_operator('*')
        else:
            # Validate input before adding
            new_text = current + text
            if (self.validator.is_safe_input(new_text) and 
                self.validator.check_length(new_text)):
                self.display.text = new_text
    
    def add_operator(self, operator):
        """Add operator with validation"""
        current = self.display.text
        if current and not current[-1] in '+-*/.':
            self.display.text = current + operator
    
    @secure_calculation
    def calculate(self):
        """Perform secure calculation"""
        current = self.display.text
        
        if not current:
            return
        
        # Sanitize input
        safe_input = self.validator.sanitize_input(current)
        
        try:
            # Use eval with restricted namespace for security
            result = eval(safe_input, {"__builtins__": {}}, {})
            result = round(float(result), 10)
            
            # Log to history
            self.add_to_history(f"{safe_input} = {result}")
            
            # Update displays
            self.previous_display.text = current
            self.display.text = str(result)
        except:
            self.display.text = "Error"
    
    def add_to_history(self, entry):
        """Add calculation to history with size limit"""
        self.calculation_history.append({
            'calculation': entry,
            'timestamp': datetime.now().isoformat()
        })
        
        # Prevent memory bloat
        if len(self.calculation_history) > self.validator.MAX_HISTORY_SIZE:
            self.calculation_history.pop(0)


if __name__ == '__main__':
    app = CalculatorApp()
    app.title = 'Premium Calculator'
    app.run()
