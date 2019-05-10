# Week 1 Assignment - Karl Tomecek - SWDV 660 1W 19/SU1

The deliverable for this week was to learn how to install and use a packaging suite in order to create an executable that would run on a Windows platform.  The focus was not on the application itself and as such the only requirement was for it to use two external packages.

## Files


| Filename      | Description                       |
| ------------- |:---------------------------------:|
| beers.py      | Source code                       |
| README.md     | This README document              |
| drinkbeer.exe | Standalone executable file        |
| drinkbeer.spec| Pyinstaller script process details|
| Pipfile       | Package requirements              |
| Pipfile.Lock  | Package versions                  |

## Installation

Use the [pyinstaller](http://www.pyinstaller.org/) to create the installion.

```bash
pyinstaller -y -F -n drinkbeer beers.py
```

## Usage

```python
Copy the **drinkbeer.exe** file to the desired directory.

At the command prompt type:

*drinkbeer*
```

## Packages
| Package       | Description                       |
| ------------- |:---------------------------------:|
| datetime      | Date and Time functions           |
| random_name   | Generates random silly names      |


### Date
May 10th 2019