# Sort and Limit Pets

In this activity, you will revisit the data from PetSitly Marketing and practice writing queries while using the sort and limit methods with PyMongo.

## Instructions

* Open [sort_and_limit_pets.ipynb](Unsolved/sort_and_limit_pets.ipynb) and run the first few blocks of code to connect to the database and store the `customer_list` collection as a variable.

* Create a query that finds customers who have pets **in** the list, `["cat", "dog"]`, then sorts in descending order by `2021_Total_Spend`, and limits the results to the first 5. Pretty print the results.

* Create a query that finds customers who spent less than $500 in 2021, then sorts in ascending order by `Customer_Last`, and limits the results to the first 5. Pretty print the results.

* Pretty print the results of a query that:

    * Finds customers who spent less than $500 **and** had more than 20 visits in 2021.

    * Removes the `Address` and `Email` fields from the results.

    * Sorts in ascending order by `2021_Visits`, then `2021_Total_Spend`.

    * Limits the results to the first 8.

## Reference

Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
