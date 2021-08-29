# Election_Analysis
## Overview of Election Analysis
The purpose of this election audit analysis was to understand how to use Python/ Visual Studio Code in order to read a Microsoft Excel file and create a text file contaning an analysis of the data. In this case, the data contained in the excel file were votes for congressional candidates from different counties, and the ned result was to create a text file that contained the breakdown of votes and percentage of votes for each candidate and for each county, while also calculating which county andcandidate had the most votes, as shown in Figure 6. The code used to analyze the data contained different for loops and if statements, as well as reading and printing mechanisms, as Shown in Figures 1 - 4, which allowed the code to be a bridge between the excel sheet and the final text product, as shown in Figure 5.

### Figure 1.
![Module 3 Code 1](https://user-images.githubusercontent.com/88119309/131264851-1109257b-5251-4d4f-b3ba-51568033f394.PNG)

### Figure 2.
![Module 3 Code 2](https://user-images.githubusercontent.com/88119309/131264855-e5d9f15b-297c-41ad-9da0-b0ddbb338274.PNG)

### Figure 3.
![Module 3 Code 3](https://user-images.githubusercontent.com/88119309/131264858-05d794ee-d044-4287-98fa-e46646a615c2.PNG)

### Figure 4. 
![Module 3 Code 4](https://user-images.githubusercontent.com/88119309/131264861-25efa9bf-494d-447c-8097-5a8ff7900207.PNG)


### Figure 5. (What the code will produce)
![Module 3 Delivarable 1](https://user-images.githubusercontent.com/88119309/131263670-6fc25918-856c-4250-b6df-69e608b3f51b.PNG)

### Figure 6. (The end product text file [Notepad])
![Module 3 Delivarable 2](https://user-images.githubusercontent.com/88119309/131263671-6139121b-4283-47bd-890e-ff8cd90aebee.PNG)

## Election-Audit Results
* There were a total of 369,711 votes in this congressional election
* The breakdown for the votes by county was:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
* The county with the most votes was Denver
* The breakdown for each candidate was:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* The winner of the Election was Diana Degette, who recieved 73.8% of the votes (272,892 votes)
## Election-Audit Summary
The script used for this election can be used for any election given the proper perameters when analyzing the data. If future elections also wish to calcualte by district, state, and/ or neighborhood, the more values must be created the break down the data even further. If only the vote totals and winner are needed, then the script will become shorter as less values are needed. An example of where the script would be smaller would be an election for mayor, which would only consist of one county and would just require the percentage of votes for each candidates. An example of where the script would need more values could be for a presidential election, where votes could be analyzed by state, county, and total amount.
