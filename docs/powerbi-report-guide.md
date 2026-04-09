# Power BI Report Guide: Top Performers

## Report Pages

### Page 1 – Executive Dashboard (Overview)

#### 🎯 Objectives

* Quickly identify tokens with **high overall engagement**
* Evaluate **engagement quality**
* Provide a comprehensive stakeholder snapshot

#### Visual 1: Top Tokens by Engagement

* **Visual**: Table
* **Source**: vw_ExecutiveDashboard
* **Columns**:

  * CurrencySymbol
  * CurrencyName
  * TotalEngagements
  * AvgEngagementScore
  * TotalLikes
  * TotalComments
  * TotalRetweets
* **Sort**: TotalEngagements (Descending)
* **Conditional Formatting**:

  * AvgEngagementScore: Green → High, Red → Low

#### Visual 2: Engagement Volume

* **Visual**: Clustered Bar Chart
* **Axis (Y)**: CurrencySymbol
* **Values (X)**: TotalEngagements
* **Filter**: Top N (by TotalEngagements)

#### Visual 3: Executive KPIs

* **Visual**: Cards

  * Sum of TotalEngagements
  * Avg of AvgEngagementScore
  * Count of CurrencySymbol

---

### Page 2 – Time Series Analysis

#### 🎯 Objectives

* Track interaction trends over time
* Detect unusual spikes/trends

#### Visual 1: Engagement Over Time

* **Visual**: Line Chart
* **X-axis**: FullDate
* **Y-axis**: TotalEngagements
* **Tooltip**:

  * TotalPosts
  * ActiveCurrencies
  * AvgEngagementScore

#### Visual 2: Social Activity Volume

* **Visual**: Area Chart
* **X-axis**: FullDate
* **Y-axis**: TotalPosts

#### Visual 3: Engagement Composition

* **Visual**: Stacked Column Chart
* **X-axis**: FullDate
* **Values**:

  * TotalLikes
  * TotalComments
  * TotalRetweets

---

### Page 3 – Platform Analysis

#### 🎯 Objectives

* Compare Twitter vs Reddit
* Compare engagement volume and quality

#### Visual 1: Engagement by Platform

* **Visual**: Table
* **Source**: vw_SocialAnalytics
* **Columns**:

  * PlatformName
  * TotalEngagements
  * TotalLikes
  * TotalRetweets
  * AvgEngagementScore
  * LastEngagement

#### Visual 2: Platform Comparison

* **Visual**: Clustered Bar Chart
* **Axis**: PlatformName
* **Values**: TotalEngagements

#### Visual 3: Engagement Quality

* **Visual**: Column Chart
* **Axis**: PlatformName
* **Values**: AvgEngagementScore

---

### Page 4 – Currency Deep Dive

#### 🎯 Objectives

* Detailed analysis of each token
* Over time & platform

#### Visual 1: Currency Selector

* **Visual**: Slicer
* **Field**: DimCurrency[Symbol]

#### Visual 2: Engagement Trend

* **Visual**: Line Chart
* **X-axis**: FullDate
* **Y-axis**: TotalEngagements

#### Visual 3: Platform Split

* **Visual**: Donut Chart
* **Legend**: PlatformName
* **Values**: TotalEngagements

---

## 7. Report-level Features

### 7.1 Date Range Slicer (MANDATORY)

* Field: DimDate[FullDate]
* Type: Between
* Sync: All pages

### 7.2 Top N Parameter (RECOMMENDED)

* Name: Top N Count
* Use in Top N filters

### 7.3 Drill-through (RECOMMENDED)

* From: Executive Dashboard
* To: Currency Deep Dive
* Field: CurrencySymbol

### 7.4 Bookmarks (OPTIONS)

* Top Engagement
* High Quality Engagement
* Platform Comparison

---

## 8. Formatting Guidelines

* Theme: Executive / Corporate
* Font: Segoe UI
* AvgEngagementScore: Green → Red
* TotalEngagements: Light color scale
