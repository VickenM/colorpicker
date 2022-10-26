from setuptools import setup, find_packages

setup(
    name = 'colorpicker',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'colorpicker=colorpicker.color_picker_widget:main'
        ]
    },
    install_requires=[
        'PySide6==6.4.0',
        'PySide6-Addons==6.4.0',
        'PySide6-Essentials==6.4.0',
        'shiboken6==6.4.0'
    ]
)


