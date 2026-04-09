1. Overview

The Executive Dashboard delivers a management-level view of social media performance across tokens and platforms.

It enables stakeholders to:

Monitor token engagement performance
Analyze engagement trends over time
Compare platform effectiveness (Twitter vs Reddit)
Evaluate engagement quality using Avg Engagement Score
🔧 Architecture Principles

The dashboard is built on optimized warehouse views to ensure:

⚡ High query performance
📈 Scalability for growing datasets
📊 Consistency for executive reporting

2. Key Features
📌 Executive KPIs
Total Engagements
Average Engagement Score
Total Likes / Comments / Retweets
Active Tokens
📈 Time-Based Analysis
Engagement trends (Daily / Monthly)
Spike and anomaly detection
🔄 Platform Comparison
Twitter vs Reddit performance
Volume vs Quality comparison
🎯 Interactive Filtering
Global Date filtering
Token-level filtering
🔍 Drill-through Capability
Token → Deep dive analysis page
🧭 Bookmark Navigation
Switch between curated analytical views
⚡ Performance Optimized
Uses pre-aggregated views (no raw fact tables)

3. Report Pages
3.1 Executive Dashboard

Purpose:
Provides a high-level snapshot of top-performing tokens.

Primary Data Source:

vw_ExecutiveDashboard

Key Visuals:

KPI Cards (Engagement, Score, Likes, Comments, Retweets)
Top Tokens by Engagement (Table)
Engagement Quality Indicators

Usage:

Sort by Total Engagements
Apply Top N filter for focus
Identify high-performing tokens quickly

3.2 Time Series Analysis

Purpose:
Analyze how engagement evolves over time.

Data Sources:

vw_TimeSeries
DimDate

Key Visuals:

Line Chart → Engagement Trend
Area Chart → Total Posts
Stacked Columns → Likes / Comments / Retweets

Usage:

Use Date Slicer to zoom into periods
Identify spikes, drops, and seasonality patterns

3.3 Platform Analysis

Purpose:
Compare engagement performance across platforms.

Data Source:

vw_SocialAnalytics

Key Visuals:

Engagement by Platform (Table)
Total Engagements by Platform (Donut/Bar)
Avg Engagement Score by Platform

Usage:

Compare volume vs quality
Identify which platform drives better engagement

3.4 Currency Deep Dive (Drill-through Page)

Purpose:
Provide detailed analysis for a selected token.

Key Visuals:

Engagement trend over time
Platform-wise engagement breakdown
Likes / Comments / Retweets distribution

Usage:

Access via drill-through from Executive Dashboard
Analyze token-level performance in depth

4. How to Use the Dashboard
4.1 Date Range Filtering (Global Control)
Slicer: DimDate[FullDate]
Applies to: Entire report

Use Cases:

Monthly / quarterly comparison
Short-term trend analysis
Event-based investigation

4.2 Token Filtering

Options:

Click token in table/chart
Use slicer: DimCurrency[Symbol]

Behavior:

Filters all visuals on the page
Enables focused analysis on a single token

4.3 Drill-through (Controlled Navigation)
Right-click token
Select → Drill through → Currency Deep Dive

Best Practice:

Enabled only on Executive Dashboard
Used for detailed investigation

4.4 Bookmarks (View Switching)

Available views:

Overview → General performance
Top Engagement → High-performing tokens
Platform Comparison → Platform insights

Usage:

Click buttons to switch between analytical perspectives
Improves storytelling flow

5. Key Metrics Explained
Metric	Description
TotalEngagements	Combined interactions (Likes + Comments + Retweets + weights)
AvgEngagementScore	Quality of engagement (normalized metric)
TotalLikes	        Total number of likes
TotalComments    	Total number of comments
TotalRetweets   	Total number of shares
TotalPosts	        Number of posts
ActiveCurrencies	Count of active tokens

6. Refresh & Performance
Component	Details
Refresh Schedule	Daily – 06:00 AM
Data Source	MySQL via Gateway
Refresh Time	< 5 minutes
Load Time	< 3 seconds (Import Mode)

7. Troubleshooting
❌ No Data Displayed
Check Date Slicer range
Verify filters are not overly restrictive
⚠️ Slow Performance
Reduce date range
Avoid multiple high-cardinality filters
🔄 Refresh Failure
Check Gateway status
Validate MySQL credentials
Confirm source availability

8. Governance Rules (Critical)
🔒 Visual Interaction Rules
Token selection → Filters entire page
Platform selection → Filters related visuals
Date slicer → Affects entire report
Drill-through → Enabled only from Executive Dashboard

9. Contact
For data or dashboard issues:

Data Team – Noodles
