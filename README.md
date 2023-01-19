# Leader&Follower analysis and popularity index

Project carried out as part of the "Big data and Smart data analytics" course at LUISS University.

*Authors*: [Cosimo Poccianti](https://github.com/cosimopoccianti), [Olimpia Sannucci](https://github.com/olimpiasannucci), [Carlo Ardito](https://github.com/CarloArdito95?tab=repositories), [Miro Confalone](https://github.com/mirocon)

![alt text](https://github.com/cosimopoccianti/Leader-Follower-analysis-and-popularity-index/blob/main/logo/python_logo.png)

This project was realised in cooperation with the consulting company Alkemy, which provided anonymised datasets of a real business case and project goals. The project concerns an analysis on behalf of an e-commerce, to understand whether dynamic pricing trends are present in the market in which it operates, and which market leaders and followers set the price. In addition, it is required to construct a popularity index for the products sold by the e-commerce. The data analysed cover 2021 only.

### 1. Leader&Follower Analysis:
The analysis made use of statistical techniques to identify dynamic pricing and market leaders and followers. More specifically, a VAR model and a Granger Causality model were used, the former to identify dynamic pricing, the latter to identify leaders and followers. The analysis was divided into quarters: January-March, April-June, July-September, October-December, plus a specific and different analysis for the month of November.

### 2. Popularity index:
Seven different indices were created to reflect different aspects and characteristics of the products, so that the ranking of the most popular products can be customised to each specific decision-making need. The result of the analysis is a barchart that can be personalised, thanks to the plotly library, which was realised via a dashboard, accessible at this link: [colab dashboard](https://colab.research.google.com/drive/1Zd9R6JGV3MT3QRVpjsX1GxJNmWK1JeVG?usp=sharing)


