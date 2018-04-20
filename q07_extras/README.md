# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?

The task is to find the number of more **extras** bowled in the second innings, compared to first.

## Write the function `extras_runs` that :

* Extracts the information of key `extras` present in the 1st innings and stores it in a list.
* Extracts the information of key `extras` present in the 2st innings and stores it in another list.
* Calculates the difference of extras and between 1st and 2nd innings and store it in a variable `difference`.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| data | dict | compulsory |  | data loaded from the yaml file |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| variable difference | int |Extra ball bowled |

_Hint: Find the total count of extras bowled in the first innings, and the total count of extras bowled in the second innings. Subtract them._
