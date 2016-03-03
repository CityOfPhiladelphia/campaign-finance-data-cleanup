# Year to Date Reports (2006 - 2015)

**Campaign Finance Reports Documentation**

**Last updated 2.22.16**


**_Overall Goals:_**

* The creation of visualizations that allow members of the public to immediately consume the meaning of this data and reduce the likelihood of misinterpretation if they were just downloading the data, which has certain nuances that need to be taken into account during analysis.

* Make queries simple and reliable so end-users can easily produce their own visualizations.


**_Key Attributes_**

The table below provides an example of the dataset’s attributes (i.e. key columns and the information contained within). 

|FilerName|Year|Cycle|Amount|Description|Amended|SubDate|FiledBy|
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|Friends of Sharon Williams Losier|2015|3|5000|E-Day|N|6/17/2015|2|
|Friends of Sharon Williams Losier|2015|3|1000|GOTV|N|6/17/2015|2|
|Friends of Sharon Williams Losier|2015|3|100|Donation|N|6/17/2015|2|
|Friends of Kevin Boyle|2015|3|25|Parking Expense|N|6/17/2015|2|
|Friends of Kevin Boyle|2015|3|400.99|Phone|N|6/17/2015|2|
|Friends of Kevin Boyle|2015|3|32.39|Phone|N|6/17/2015|2|


**_Extraction Process Used:_**

* We used a combination of [bash shell scripts](https://github.com/pixels2predicates/CFR/tree/master/extract) and [python](https://github.com/pixels2predicates/CFR/blob/master/extract/recYTD.py) to recursively download from the ftp site.

* The Python script is used to grab the year to date files.

* There are two bash scripts: one is used to grab 4 files (contrib.txt, receipt.txt, debt.txt, and expense.txt) in each of the directories. The second is used to account for the formatting of filer.txt that cannot be obtained via the logic of the first script.


**_Research Questions:_**

*Below are potential research questions that visualizations could help answer for the Board of Ethics as well as those questions that the Board receives most often from the public.*

1. *For any particular candidate, how much did he/she raise? How much did they spend? And how much unpaid debts this year?*

2. *Who are the largest contributors?*
        
      (i.) by total amount spent

      (ii.) by total number of donations,

      (iii.) by type of filer (i.e. unions, individuals, PACs, etc.) 

3. *Measuring campaign finance reports by geographic region?*


**_Use Cases:_**

To help spur ideas, we provide examples below of the types of ways that this dataset could be used.

* DOWNLOADABLE: End-users will be able to download the data to conduct his/her own analyses to answer inquiries concerning who filed (filer), when something was filed (cycle, year, SubDate) and for how much (amount). Location is among our attributes (Entity Name Address1, etc. al.), so we can include location of contributor transactions as well. Stakeholders most likely interested in this include journalists, oppositional research groups, academics, advocates dedicated to Campaign Finance and the Board of Ethics in conducting investigations and analysing trends.


* APPLICATIONS: The data can power applications that enable a user to query a database and return the data they are interested in. Even though this application already [exists](https://phila-records.com/campaign-finance/web/), questions remain of whether it is user-friendly and could be improved. If so, how?

* VISUALIZATIONS: To broaden the audience of this data, we aim to collaborate on creating visualizations. 

    * A possible visualization could be a graph of contributions, expenditures, and unpaid debt of a candidate committee, or other political committee, by reporting cycle, election cycle, or year. Timelines of multiple committees could be compared in relation to each other.

    * The Board of Ethics has had discussions with the Chief Integrity Office about. joining this data with the Lobbying data and other datasets. However, these datasets were never designed to go together, so it’s questionable how to align them for analysis (i.e. lobbying data is quarterly and does not have a date and Campaign Finance has 7 reporting cycles with dates).

Ultimately we want to present the data in a visually informative way, but the risk of misrepresenting the data is high. Below, we list the tools we have at our disposal to visualize this data.

   	
   * [Socrata- dataLens?](https://support.socrata.com/hc/en-us/articles/204798848-Getting-Started-with-Data-Lens) ([out-of-the-box](https://www.dropbox.com/s/ia9iy5u1dq2coim/Screenshot%202016-01-27%2015.08.41.png?dl=0): the applications of the [filters produce illogical information](https://www.dropbox.com/s/f8hivoinw6srwkp/Screenshot%202016-01-27%2015.10.07.png?dl=0))

   * [Vizwit](https://github.com/timwis/vizwit)?

   * [R](https://www.r-project.org/other-docs.html)?

   * [Python](http://pandas.pydata.org/)?


**_Challenges:_**

A. Generally speaking, the dataset is massive, inconsistent, and difficult to interpret. The following describes the challenges to producing meaningful and relatively accurate analyses.

1. DUPLICATE FIELDS: The database includes all amended reports in addition to the original submissions. Therefore multiple duplicate entries can be found for many transactions in the system. In addition, 24-Hour reports are transactions which are included in Cycle 3 or Cycle 6 reports after an election. They can be analysed on their own; but are also duplicative of some of the transactions in the Cycle 3 or 6 report. During analysis some of the fields need to be redacted so that amendments are taken into consideration. It’s not clear how to write the logic that will handle this task so that we avoid duplicating monetary values and compromising the integrity of the dataset. Is this something which can be done through written logic, or must it be done by hand?

2. CHANGING CONTRIBUTION LIMITS: These limits complicate analyses in three ways:

  1. Every 4 years, the contribution limits are adjusted upward to account for inflation; so, in an analysis of maximum contributions  or in comparing contributions over time, you should only compare to the maximum limit imposed during that  timeframe. 

  2. Additionally, if a candidate spends over $250k of their own money, the contribution limits at that time double for every candidate in that race only. 

  3. Finally, when a candidate is no longer a candidate after an election, from the time he/she are no longer a candidate until the end of that calendar year he/she can receive another maximum contribution from someone who already contributed to him/her to pay off campaign debt. (i.e. one candidate received 3 max contributions from a filer, once because it was okay to do so, the second time because a competitor had used $250k of his/her own money, and then a third time because he/she lost the campaign. Could create an API that information.

C. NO STANDARDIZATION OF DATA: When a filer completes a campaign finance report, there are no standard options for fields in the report - filers write in the data. This means that the same contributor might be listed in different ways (i.e. ‘Local 98’ is the same as ‘IBW98’); the dates may be different because the PAC reports the date he/she wrote the check, and the candidate reports the date it was received. The only fields that are generally consistent are the amount contributed and to whom.

D. DATA MISINTERPRETATION CONCERNS: This is a high-value dataset that press and oppositional researchers may use - inaccurate analysis due to data quality issues could misinform the public or lead to lawsuits against candidates.

E. AUTOMATION:This dataset is updated on a regular basis, so maintaining it would (ideally) make use of automation. While keeping the dataset updated with a ETL workflow is possible (it may even be the easy part), maintaining the integrity of the data must also be a part of this procedure.

F. VISUALIZATIONS:Visualizations would be a great asset for the end-user only if the data is not telling a misleading story. Perhaps chopping up large portions of the dataset into manageable subsets that we are confident will make an honest visualization is the best approach. How to accomplish this is less clear.


**_Next Steps:_**

* **Remove duplicates:** The most important next step is to find a way to remove the duplicate values so that we can make use of the values attribute in a way that does not distort the numbers. This still has not been resolved.

* **Engage partners:** An effort to expand the project to include others within and outside of OIT would be beneficial.

* **Brainstorm visualizations:** Taking some time in the lab and trying to collaborate on the best way to visualize the data, (no matter how small the subset may be) would be a good exercise to engage in. Ultimately, it would help up us identify some of the problems that are preventing us from portraying the data in a logical way. It may also get the public more interested in the dataset if we have a visualization to share that we feel confident in.

* Share at [Democracy Hackathon](https://codeforphilly.org/blog/apps_for_philly_democracy--hackathon-2016) from March 18 - 20.


**Resources:**

* [Board of Ethics - Campaign Finance:](http://www.phila.gov/ethicsboard/campaignfinance/Pages/default.aspx): This site contains information regarding campaign finance laws, gives instructions on how to file electronically, and provides the ability to search the campaign finance database.

* [Department of Records:](http://www.phila.gov/records/campaignfinance/CampaignFinance.html) General information about campaign finance records from the department of records.

* [Original ](https://github.com/CityOfPhiladelphia/phl-campaign-finance-data)[metadata](https://github.com/CityOfPhiladelphia/phl-campaign-finance-data) for Campaign Finance Reports on GitHub

* [Metadata:](http://metadata.phila.gov/#home/datasetdetails/5543867c20583086178c4f5f/)[for campaign finance reports in Benny](https://docs.google.com/document/d/1V3PREesTtowwclW3oDNphrGxiIMHrbx6VLiYDtbJPD4/edit): The City of Philadelphia's online metadata catalog entry for the campaign finance records dataset.

* [Open Data Philly](https://www.opendataphilly.org/dataset/campaign-finance-records) The resources page on ODP contains a direct link to the ftp site.

* [VizWit](https://github.com/timwis/vizwit) - An interactive data visualization tool. VizWit uses a [JSON config file](https://gist.github.com/601224472a5d53cbb908) to generate interactive charts that cross-filter one another. It currently supports data hosted in a Socrata Open Data portal, which includes cities such as [Philadelphia](http://opendataphilly.org/), [Chicago](https://data.cityofchicago.org/), [San Francisco](https://data.sfgov.org/) and many others. However, interactions with Socrata have been [abstracted](https://github.com/timwis/vizwit/blob/master/src/scripts/collections/socrata.js) to allow for [other data providers](https://github.com/timwis/vizwit/wiki/Adding-a-provider) to be written.

* [CampaignFinancePHL](https://github.com/CfABrigadePhiladelphia/CampaignFinancePHL) - A project to improve access to/report on/organize Philadelphia's public campaign finance data.

