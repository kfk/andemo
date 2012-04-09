Intro
-----
This is a demo analytics project using flask and jquery. The idea is to use ajax calls to populate data widgets (tables, plots, reports, etc.). Flot is used for plotting. 


Why
---
Data analytics in many business environments is done wrong. It takes too much effort to make simple reports and handle medium sized datasets. It takes too much effort to follow different versions of the same report in order to use the most updated data. It takes to much efforts to manually update periodic reports. It takes too much effort to use a data warehouse system or share point system that cannot be accessed programmatically through apis.

Finally, most of the solutions out there are too expensive and do not provide a useful api. That is why this demos will focus on ajax. Every source of data, external or internal (internal meaning feeded with companies data: financials, sales data, etc.), should be available through a simple url and should provide valid json through a get request. This will give people chance to use data *outside* the reporting system. For example, users may use a certain data source to update an excel report with VBA.

Open issues
----
Lots of them. If somebody wants to help (any type of help/feedback very welcomed), a big hairy issue to solve is outputting PDFs from html reports. Flot is using canvas, those are not very well supported in ie, so there are some things to play with there.
