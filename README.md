# CSE351 Library

This package contains common classes and helper methods for the CSE 351 course.

## Installation Instructions

Python and pip must be installed on your system already. Make sure Python has been added to your system path. If running one of these commands `python --version` or `python3 --version` or `py --version` does not return a Python version do not continue until you have correctly installed Python. Note that the returned Python version should be at least 3.11 or greater.

**Windows**

1.  Open a command prompt.
2.  Install the package using `python -m pip`:
    
    `python -m pip install git+https://github.com/byui-cse/cse351-py-package.git`
    
    If you have Python 3 installed as the default, you might use:
    
    `python3 -m pip install git+https://github.com/byui-cse/cse351-py-package.git`
    
    If you have Python installed and added to PATH as `py`, you can also use:
    
    `py -m pip install git+https://github.com/byui-cse/cse351-py-package.git`

**MacOS**

1.  Open a terminal.
2.  Install the package using `python -m pip`:
    
    `python -m pip install git+https://github.com/byui-cse/cse351-py-package.git`
    
    If you have Python 3 installed as the default, you might use:
    
    `python3 -m pip install git+https://github.com/byui-cse/cse351-py-package.git`
    

**Linux**

1.  Open a terminal.
2.  Install the package using `python -m pip`:
    
    `python -m pip install git+https://github.com/byui-cse/cse351-py-package.git`
    
    If you have Python 3 installed as the default, you might use:
    
    `python3 -m pip install git+https://github.com/byui-cse/cse351-py-package.git`

## Usage

You can import this package into your assignments by adding the following with your import statements:

`from cse351 import *`

## Overview

This utility package provides a set of convenient tools for data analysis and visualization. It offers the following key features:

1. **Setting Script Working Directory:**
   - Easily set the current working directory using the `set_working_directory` function.

2. **Logging Utility:**
   - The `Log` class facilitates efficient logging, providing both console output (stdout) and log file recording. Users can conveniently manage log messages, warnings, errors, and timing information. The logger supports customization options such as log file naming, formatting, and verbosity.

3. **JSON File Handling:**
   - Use the `load_json_file` function to effortlessly load and parse JSON files. This function enhances the convenience of working with JSON data, supporting seamless integration into data processing workflows.

4. **Matplotlib Plotting Support:**
   - The `Plots` class simplifies the creation of line and bar plots using `matplotlib`. It offers a straightforward interface for users to generate visually appealing plots with customizable titles, labels, and saving options.

This utility is designed to be easily installable using the Python package manager, pip. Installing this package will auto install the following dependencies:

- **matplotlib:** For creating high-quality plots and visualizations.
- **numpy:** A powerful library for numerical operations.
- **pillow:** An imaging library for opening, manipulating, and saving various image file formats.
- **requests:** A versatile library for making HTTP requests.
- **opencv-python:** A computer vision library for image and video processing.

## Authors
- Luc Comeau
- [Hunter Wilhelm](https://github.com/hunterwilhelm)
- Christopher Keers

## License
MIT License

---

## Functions

### `set_working_directory(file_path)`
Sets the current working directory to the specified folder.

**Parameters:**
- `file_path` (str): The path to the folder to use as the working directory.

### `print_dict(dict, title='', indent=2)`
Displays a dictionary in a structured format.

**Parameters:**
- `dict` (dict): The dictionary to pretty print.
- `title` [str]: A title line to print before the dictionary if desired.
- `indent` [int]: How much to indent each succeeding level of the dictionary; default 2.

### `load_json_file(filename)`
Attempts to load and parse a JSON file.

**Parameters:**
- `filename` (str): The path including filename of the JSON file to attempt to open.

**Returns:**
- `dict`: The parsed JSON or an empty dictionary.

---

## `Log` Class

### Parameters
- `filename_log` [str]: Name of the log file; default is [timestamp].log.
- `linefmt` [str]: Logger format; default `%(message)s`.
- `show_levels` [bool]: Set to True to record levels when necessary; default False.
- `include_time` [bool]: Set to False to exclude timestamps; default True.
- `append_mode` [bool]: Set to True to append to previous log; default False (overwrite).

### Methods

#### `start_timer(message='')`
Starts (restarts) the timer.

**Parameters:**
- `message` [str]: Optional message to print as you restart the timer.

#### `step_timer(message='')`
Gets the current timer value.

**Parameters:**
- `message` [str]: Optional message to print as you restart the timer.

**Returns:**
- `float`: Current timer value.

#### `stop_timer(message='')`
Stops the timer and reports the elapsed time.

**Parameters:**
- `message` [str]: Optional message to print as you restart the timer.

**Returns:**
- `float`: Elapsed time.

#### `get_time()`
Gets the current timer value.

**Returns:**
- `float`: Current timer value.

#### `write_blank_line()`
Writes a blank line to the log file.

#### `write(message='')`
Writes an info message to the log file.

**Parameters:**
- `message` (str): Message to be written to the log file.

#### `write_warning(message='')`
Writes a warning message to the log file.

**Parameters:**
- `message` (str): Warning message to be written to the log file.

#### `write_error(message='')`
Writes an error message to the log file.

**Parameters:**
- `message` (str): Error message to be written to the log file.

---

## `Plots` Class

### Parameters
- `title` (str): Title for the plot graph.

### Methods

#### `line(xdata, ydata, desc='', title='', x_label='', y_label='', show_plot=True, filename='')`
Creates a line plot.

**Parameters:**
- `xdata`: X-axis data.
- `ydata`: Y-axis data.
- `desc` [str]: Description of the plot.
- `title` [str]: Title of the plot.
- `x_label` [str]: Label for the X-axis.
- `y_label` [str]: Label for the Y-axis.
- `show_plot` [bool]: Whether to display the plot.
- `filename` [str]: Filename to save the plot.

---

#### `bar(xdata, ydata, desc='', title='', x_label='', y_label='', show_plot=True, filename='')`
Creates a bar plot.

**Parameters:**
- `xdata`: X-axis data.
- `ydata`: Y-axis data.
- `desc` [str]: Description of the plot.
- `title` [str]: Title of the plot.
- `x_label` [str]: Label for the X-axis.
- `y_label` [str]: Label for the Y-axis.
- `show_plot` [bool]: Whether to display the plot.
- `filename` [str]: Filename to save the plot.
