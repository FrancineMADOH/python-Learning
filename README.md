# Caasi-Learnings
This repository tracks all the learnings related to caasitech learnings

ASSIGN AN AGENT 

Problem Statement

Assign agent(s) for a request.

Assumptions
The baseline of every agent is a truck or tricycle

Questions
Are we still considering categories?

Requirements

Inputs 
A request (location, volume)
List of all available agents

Outputs
Agent(s)

Algorithm

Step 1 : Start
Step 2 : if volume < 160 litres:
        Automatic request : find the closest available agent

Step 3 : Else, Send a list of available agents and their distances (increasing order)


Find the closest available agent

Get the location of the request
For all the agents, create a list of available agents 
Get the location of the agents available
Calculate the distances between the request and all the agent’s location
Select the smallest distance 
Display the agent selected



Available agent
Requirements

Input 
An agent (date, shifts, available)
Agent_shift is a map {“monday”: [“morning”, “afternoon”]}

Output 
Available

Algorithm

Step 1 : Start
Step 2 : Get the current Date and Time
Step 3 : For an agent, check if day == current_date.day and current_date.time in shift and available == true,   output true else output false.
