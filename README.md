# python_challenge
Here's my submission for Challange_3. All code is my own.

PyBank
This code runs through each row of data in the budget_data csv file. Using a for loop, we count the number of months and add the row's net profit/loss value (Column B, or position 1 in the code) and add these to the respective counters, which calculate the totals for each (using += shorthand). Within the loop, we also perform calculations to obtain the difference between the next row's profit value and the current row's one to obtain the monthly change in profit/losses. These calculations and the dates for each row are stored in lists called net_change_list and date_list, which will will allow us to store this values in list format for further analysis - i.e. computing the average change and the greatest increase and decrease in profit/loss, and then using the index function, locate the corresponding date at the same position (i.e., row number) as the max/min values we extracted. We end up by printing these results using a def function that combines the text and variables using f strings and exports the results in the analysis text file. The real challenge here was understanding how to "extract and store" the first row values (shown in the code by doing a "next()" function on the first row as well - variable "first_row") in separate counters and telling python to read the csv starting from row 3 (i.e., after skipping the header and first row of values). I used class materials and asked questions to AI on how we could do this. This is done so that we can compute the net changes in profit/loss appropriately - it allows us to substract "static" row 1 values to obtain the first monthly change in profit/loss (the initial "previous_net") before these are updated by the reader as it loops through the list. As we do this calculation, we append the result (net_change_value) to the net_change_list. Note I also watched some videos to learn how to print data into the .txt file in individual rows/lines using \n.

PyPoll
I used AI to help along the way, particularly to assist on how to use the "If Not" function to tell the loop to perform the task of adding the candidate name to the dictionary prior to adding votes to the candidate. I also used it to better understand whether two lists or a dictionary was the appropropriate object(s) to use to hold the candidate votes. 

I connected with classmates to better understand how to print results into the .txt file in the manner it was asked for in the exercise - piecemeal (total votes, candidate totals and percentages and winner summary). I realized that, in order to print each candidate's totals, this portion had to be done within the For loop "candidate in candidate_votes". I also investigated the usefulness of loading indicators and how it worked in this context. 

Explanation:
    This code works by reading each row of data within the csv file election_data. Skipping over the first row (i.e., headers), the code reads through each line to add a vote to the total_votes counter and collect the candidate's name. Once the name is collected, the code checks if the candidate exists within the dictionary before adding a vote to their rolling counter within the dictionary (i.e., to the corresponding key:value pair). Like we learned in class, the short form "+=" substitutes the need to use = candidate_votes (candidate) + 1 to increase/update the counter. Once they votes are tallied, a function computes the results (total votes per candidate and % of total votes obtained). We then update the winner_count and winner name variable in every iteration so that, in the end, this variable takes the total votes of the winning candidate and the name. The "def" function the helps combine the variable results obtained in the previous step, with text, and then print these. The second def function does the same for the winning candidate values/name. Both t.
