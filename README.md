# Ecocaasitech Algorithms


## AGENT SALARY

Problem Statement :
To deduce the salary of an Agent, monthly.
Suggestions/Assumptions :
- For an Agent to make 200, 000 XAF of a salary a month, he/she must earn 170, 000
XAF of bonus i.e atleast 20 pickups transactions a day, for 1 month.
- Base Salary :
Min : 15, 000 XAF
Max : 30, 000 XAF
- Shifts :
- 5 : 00am - 12 : 00pm (Morning shift)
- 12 : 00pm - 7 : 00pm (Afternoon shift)
- Payment for any shift is 500 XAF, for Residence
- Payment for any shift is “above 500 XAF” for Commercial. We have 300
XAF for a wheelbarrow.
- CASE 1 :
Booking For Residence (per day) :
- Each Booking = 50 XAF
- 5 Pickup = 1, 000 XAF BONUS
- 10 Pickup = 5000 XAF BONUS ( = 150 000 XAF for 30 days + 30 000
XAF)
- Bonus for being on time for a shift + for bookings in that shift : 350
XAF
Maximum salary : 10 pickups every days + base salary of 2 shifts a day = 180 000 + 20 000
= 200 000 XAF
Booking For Commercial (per day) :
- 1 Pickup = 100 XAF
- 3 Pickup = 1000 XAF
- 5 Pickup = 6500 XAF BONUS or 6666.66 (= 195 000 XAF for 30 days
+ 30 000 XAF)
- Bonus for being on time for a shift + for bookings in that shift : 350
XAF
Maximum salary : 5 pickups every days + base salary of 2 shifts a day = 195 000 + 30 000 +
20 000 = 245 000 XAF
Inputs :
- Agents
- Month
Outputs :
- Salary for that month
Algorithm :
- Step 1 : Start
- Step 2 : Get all the booking done by the agent
- Step 3 : Get all the booking done by the agent for the month
- Step 4 : From the list of booking, sort out the residence and the commercial bookings
- Step 5 : From the list of residence,
- Result1 = length/20
- Remainder1 = length % 20
- IF Remainder1 ≠ 0,
Result2 = Remainder1 / 10
Remainder2 = Remainder1 % 10
IF Remainder2 ≠ 0,
Result3 = Remainder2 / 5
Remainder3 = Remainder % 5
- Step 6 : Total_Bonus
= (𝐵𝑜𝑛𝑢𝑠 𝑜𝑓 20) × 𝑅𝑒𝑠𝑢𝑙𝑡1 + (𝐵𝑜𝑛𝑢𝑠 𝑜𝑓 10) × 𝑅𝑒𝑠𝑢𝑙𝑡2 + (𝐵𝑜𝑛𝑢𝑠 𝑜𝑓 5) × 𝑅𝑒𝑠𝑢𝑙𝑡3 +
(𝑅𝑒𝑚𝑎𝑖𝑛𝑑𝑒𝑟3) × 50
- Step 7 : Get all shifts done by Agent
- Step 8 : Total_Salary = (𝑇𝑜𝑡𝑎𝑙 𝑠ℎ𝑖𝑓𝑡 𝑑𝑜𝑛𝑒 𝑏𝑦 𝑎𝑔𝑒𝑛𝑡) × 500 + (Total_Bonus)
- Step 9 : Return Total_Salary
Note : Step 5 is a method


# PRICE DETERMINATION ALGORITHM (FOR MVP)

### Problem Statement

An algorithm that evaluates a price based on volume for a pickup or a pickup &
cleaning package.
Analysis

* Assumptions
- All prices below the price determined should be rejected

* Requirements
Calculate Volume
Inputs
- Size (bucket-10L, trash bag-27L, wheelbarrow-80L)
- Quantity
Outputs
- Volume = ((size/1000) * quantity) cubic metres
Calculate Price
Inputs
- Volume
- Package
Outputs
- Price = (Volume * 0.05) XAF
IF Package == “pickup”:
Return Price
Else:
Return 1.2 * Price
Bid
Inputs
- Biding price
- Price

Output

- Status (rejected-0 or approved-1)
IF biding < price
THEN Status = rejected
Display “Price too low.”
ELSE
Status = Approved
Display Price

* Algorithm
Inputs
- Package (Pickup and Cleaning & Pickup)
- Trash quantity
- Volume
- Biding price

* Outputs
- Price determined and send to Admin
Step 1: Start
Step 2: Select a package(pickup / cleaning & pickup)
Step 3: Select a trash size
Step 4: Select the trash quantity
Step 5: If trash quantity > 1
Step 6: Calculate volume
Step 7: Assign the calculated price to a variable Price_1
Step 8: Else if trash quantity == 1
Step 9: Calculate volume by dividing the size by 1000
Step 10: Assign the calculated price with the pickup as package to a variable price
Step 11: Else Display “Set a trash quantity of at least one”
Step 12: Bid

* Pseudocode
Inputs
- Package (Pickup & Cleaning and Pickup)
- Trash quantity
- Volume
- Biding price

* Outputs
- Price determined and sent to Admin
Select a package(pickup / cleaning & pickup)
Select a trash size
Select the trash quantity
IF trash quantity > 1
Calculate Volume (size, quantity)
Price_1 = Calculate Price (volume, package)
Else if trash quantity == 1:
Volume = size / 1000
Price = Calculate Price (volume, “pickup” )
Else:
Display “Set a trash quantity of at least one”
Bid(biding price, Price, minimum percentage)


# ECOPOINTS ALGORITHM Earn

* Problem Statement
Convert what a user spend to his number of points
Analysis

* Assumptions
As an owner uses their points it decreases on the dashboard but your points are
accumulated somewhere to make you move from one level to another.
Inputs
- Price
- Total ecopoints
Output
- Number of points

* Requirements
Convert
Input
- Price
Output
- Number of ecopoint
Algorithm
Step 1: Start
Step 2: Get price from user’s transaction
Step 3: Convert price to number of points
Step 4: Round the number of points to the nearest whole number
Step 5: Add number of points to the total Ecopoints
Step 6: Check your level

* Pseudocode
Redeem
Problem Statement
Convert the number of points to the rewards of the owner.
Analysis
Assumptions
An owner can not redeem part of his Ecopoints but can redeem n* base of a
service for Ecopoints.

* Requirements
Input
● Number of points
● Services to redeem
Output
● Reward
● Level
Algorithm
Step 1: Start
Step 2: Get the number of points
Step 3: Select the service to be redeem ( voice, data, or Electricity )
Step 4: Redeem n * base of service value of the service based on your level (**)
Step 5: Decrease the number of points by n base from the dashboard