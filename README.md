# python-challenge
# Task 1: PyBank
In this Challenge, a Python script is used to analyze the financial records of a company, with the given financial dataset that is composed of two columns: "Date" and "Profit/Losses".

  # Requirements
  A Python script that analyzes the records to calculate each of the following values and print the analysis to the terminal as well as export a text file with the results:
  
  1. The total number of months included in the dataset.
  2. The net total amount of "Profit/Losses" over the entire period.
  3. The changes in "Profit/Losses" over the entire period, and then the average of those changes.
  4. The greatest increase in profits (date and amount) over the entire period.
  5. The greatest decrease in profits (date and amount) over the entire period.
  
  # Step 1: Set lists, variables, and path for input and output file
  1. The Lists to store data used are: `date = []`; `profit_losses = []`; `greatest_decrease` set to "", 0; `greatest_increase` set to "", 0; and `change_value_list` = [].
  2. The variables used are: `previous_value` set to 0 and `change_in_value` set to 0.
  3. Variable for input file: `budget_csv` and for output file: `bankanalysis_csv`.
  
  # Step 2: Open the input CSV 
  1. Open the CSV using the UTF-8 encoding.
  2. Store the header row.
  
  # Step 3: Calculate and print the results on to the terminal
  1. Calculate and print the total months using the `len` function.
  2. Calculate and print the total value of Profits/Losses.
  3. Read through each row of data after the header to:
     a. Calculate the average change in value between each consecutive months over the entire period.
     b. Check for the greatest increase in value (date and amount) over the entire period.
     c. Check for the greatest decrease in value (date and amount) over the entire period.
  4. Calculate and print the Average Change using the average change in value between each consecutive months over the entire period that is calculated for each row, using the `mean` function that is imported         from the package `numpy`.
  5. Print the greatest increase and decrease in profits.

  ![Bankanalysis_terminal](https://github.com/Pooja14n/python-challenge/assets/144713762/fb2b907d-922e-4a9f-970f-ed170e22f28b)
  
  # Step 4: Open the output CSV
  1. Print output in the `bankanalysis` File.
  
  ![Bankanalysis_outputfile](https://github.com/Pooja14n/python-challenge/assets/144713762/0fc345cc-b432-4a3d-9f91-9d16728d48b4)


# Task 2: PyPoll
In this Challenge, a Python script is used to help a small, rural town modernize its vote-counting process, with the given set of poll dataset that is composed of three columns: "Voter ID", "County", and "Candidate".

  # Requirements
  A Python script that analyzes the votes and calculates each of the following values:

  1. The total number of votes cast. 
  2. A complete list of candidates who received votes.   
  3. The percentage of votes each candidate won.
  4. The total number of votes each candidate won.
  5. The winner of the election based on popular vote.

  # Step 1: Set lists, dictionary, variables, and path for input and output file
  1. The List to store names of the candidates is: `candidate_name` = []; and dictionary to store the number of votes for the candidates is: `candidate_votes` = {}.
  2. The variables used are: `votes_count` set to 0; `winner_count` set to 0; and `winner_cand` set to "".
  3. Variable for input file: `election_csv` and for output file: `pollanalysis_csv`.

  # Step 2: Open the input CSV 
  1. Open the CSV using the UTF-8 encoding.
  2. Store the header row.
  
  # Step 3: Calculate the results, open the Output CSV, and print the results
  1. Calculate the overall votes for all the candidates within a `for` loop and print the results outside the loop, on to the terminal.
  2. Within the first `for` loop, run an `if` statement to find names of all the canadidates and add it to the list `candidate_name` and outside the if statement, add the votes for each of the candidates.
  3. Open the output file and print the result for the overall votes, in the `pollanalysis` File.
  4. Run another `for` loop outside the first `for` loop, to calculate the percent of votes for each of the candidate names based on their votes; and print the result on to the terminal as well as the output           file.
  5. Within the second `for` loop, find the winner using an `if` statement; and print the result on to the terminal as well as the output file.

  ![Pollanalysis_terminal](https://github.com/Pooja14n/python-challenge/assets/144713762/9ae9f8a7-ace1-4b3a-9a0c-dbedc05bf930)


  ![Pollanalysis_outputfile](https://github.com/Pooja14n/python-challenge/assets/144713762/c453f2a0-c306-4b70-bae5-fef3edbf898c)



# References:
Referred to various class activity exercises, Python Documentation, Stack Overflow, and support from BCS Learning Assistant.

# Files submitted including this README File:
1. Folder for each task: PyBank and PyPoll.
2. In each folder that was created, the following were added:
   a. A new file called `main.py`, which is the main script to run for each analysis.
   b. A Resources folder that contains the CSV files were used; the path to which are in the script.
       i. PyBank: `budget_data.csv`; path: r"PyBank\Resources\budget_data.csv"
       ii. PyPoll: `election_data.csv`; path: r"PyPoll\Resources\election_data.csv"
   c. An analysis folder that contains text file that has the results from the analysis; the path to which are in the script.
       i. PyBank: `bankanalysis.csv`; path: r"PyBank\Analysis\bankanalysis.csv"
       ii. PyPoll: `pollanalysis.csv`; path: r"PyPoll\Analysis\pollanalysis.csv"

