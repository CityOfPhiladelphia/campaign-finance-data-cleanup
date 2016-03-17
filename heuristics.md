## How to prepare data for analysis: Handling Amendments

(1.) Sort by FilerName

(2.) Sort by DocType

(3.) Sort by EntityName

(4.) Sort by Date

(5.) Sort by SubDate



|FilerName|Year|EntityName|Date|Amount|Amended|SubDate||
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|Friends of X|2011|Committee to Elect Tony Payton Jr.|2/23/2011|500|N|5/4/2011|2|
|Friends of X|2011|Committee to Elect Tony Payton Jr.|4/27/2011|1000|Y|5/6/2011|2|
|Candidate Y|2011|Contributor Z|3/9/2011|100|N|4/3/2011|1|
|Candidate Y|2011|Contributor Z|3/10/2011|150|N|4/4/2011|1|
|Candidate Y|2011|Contributor Z|3/7/2011|175.16|Y|4/5/2011|1|




(i.) Locate the row that has a value of "Y" for amended and remove all prior instances with an amended value of "N".


![alt text](https://github.com/CityOfPhiladelphia/campaign-finance-data-cleanup/blob/master/out2.gif "Logo Title Text 1")







(ii.) ....

|FilerName|Year|EntityName|Date|Amount|Amended|SubDate||
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|Friends of X|2011|Committee to Elect Tony Payton Jr.|4/27/2011|1000|Y|5/6/2011|2|
|Candidate Y|2011|Contributor Z|3/7/2011|175.16|Y|4/5/2011|1|

			



