How to prepare data for the analysis: Handling Amendments

(1.) First sort by FilerName

(2.) Then sort by DocType

(3.) ...


|Year|Cycle|Amended|Amount||FilerName|
| ------ | ------ | ------ | ------ | ------ | ------ |
|2011|2|N|N|0|Friends of Jannie L. Blackwell|
|2011|2|Y|N|0|Friends of Jannie L. Blackwell|
|2011|2|N|N|0|Friends of Jeff Dence|
|2011|2|N|N|0|Friends of Jeff Hornstein|
|2011|2|N|N|0|Friends of Jewell Williams|


(i.) Locate the row that has a value of "Y" for amended and remove all prior instances with an amended value of "N".

(ii.) ....

			
|Year|Cycle|Amended|Amount||FilerName|
| ------ | ------ | ------ | ------ | ------ | ------ |
|2011|2|Y|N|0|Friends of Jannie L. Blackwell|
|2011|2|N|N|0|Friends of Jeff Dence|
|2011|2|N|N|0|Friends of Jeff Hornstein|
|2011|2|N|N|0|Friends of Jewell Williams|


