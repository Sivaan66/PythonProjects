# PythonProjects
This repository contains all the small projects that i made through my Python learnig process. This shows my up untill knowledge about python.
Here are all coding i went through during my learning :  
## Rock Paper Cissor
- A rock paper cissor game where user need to choose r,p,c from a list then bot will choose randomly from the list. If bot and user choice matches then the computer will show a tie and both will get 1 point each.  
- if user = r and bot = p then bot wins where user will get 0 pint, bot will get 1 point and so on.
```py

## Web Scrapping
Used python to scrape data from a website that contained info of some indian companies about their name, industry type, revenue, profits, assets etc.  
Codes used -  
- imported beautifulsoup() to scrape the data.
- imported requests() to get the access to the page and interact with my VS Code.
- Also imported panda to make table in .csv format.  
- 🔗 [Check the Code](./WebScraping.py)  
- 🔗 [Check the Table](./companies.csv)
- Website I worked on : [Click here](https://en.wikipedia.org/wiki/List_of_largest_companies_in_India)
## Automatic File Sorting -
Automatically sort the file to specified folder according to the file type.  

- Imported OS and Shutil()  
- Specified the path.  
- Made three folders uisng os.makedirs()  
- Took three types of files as reference - ".jpg", ".pdf", ".csv"  
- Then created three folders named - "image", "pdf", "sql"  
- Then i used shutil.move(scr,dst) to move those files to their specified folders.  
🔗 [Check the Code](./AutomaticFileSorting.py)
## Treasure Hunt Path -
A coding problem where you calculate the final position on a grid map after a series of movement instructions (U-up, D-down, L-left, R-right).  
  
- The starting point is at (0, 0), and the task is to follow the instructions to determine the final coordinates.  
- Each time the movement will be for only one unit in the map.
- If i say RRLDUR, means the coordinates will be at (2,0) = (x,y).  
🔗 [Check the Code](./TreasureHunt.py)
## Pin Validation -
A problem about checking if any number of given PIN is divisible by 4. If divisible, output "open", else "locked".  

  
- Asked the user to enetr any Four digit number of pin.
- If entered PIN is not 4 digits it wont accept and will ask for the PIN again. 
- If the pin is divisible by 4, it will show open.  
- If it's not, it will show Locked and again ask for a pin.  
🔗 [Check the Code](./PinValidation.py)
## USD to INR Converter
A programme to convert given USD value to INR.  

- Enter the USD value
- Using the relation between USD and INR it gives the value in INR
- 🔗 [Check the Code](./USDtoINR.py)
