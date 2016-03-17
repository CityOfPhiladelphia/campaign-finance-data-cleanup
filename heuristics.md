How to prepare data for analysis: Handling Amendments

(1.) Sort by FilerName

(2.) Sort by DocType

(3.) Sort by EntityName

(4.) Sort by Date

(5.) Sort by SubDate


|Year|Cycle|Amended|Amount||FilerName|
| ------ | ------ | ------ | ------ | ------ | ------ |
|2011|2|N|N|0|Friends of Jannie L. Blackwell|
|2011|2|Y|N|0|Friends of Jannie L. Blackwell|
|2011|2|N|N|0|Friends of Jeff Dence|
|2011|2|N|N|0|Friends of Jeff Hornstein|
|2011|2|N|N|0|Friends of Jewell Williams|


(i.) Locate the row that has a value of "Y" for amended and remove all prior instances with an amended value of "N".


![alt text](https://github.com/CityOfPhiladelphia/campaign-finance-data-cleanup/blob/master/out2.gif "Logo Title Text 1")







(ii.) ....

			
|Year|Cycle|Amended|Amount||FilerName|
| ------ | ------ | ------ | ------ | ------ | ------ |
|2011|2|Y|N|0|Friends of Jannie L. Blackwell|
|2011|2|N|N|0|Friends of Jeff Dence|
|2011|2|N|N|0|Friends of Jeff Hornstein|
|2011|2|N|N|0|Friends of Jewell Williams|


