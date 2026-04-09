-- 1
Total Engagement (Filtered)

Total Engagement (Filtered) = 
CALCULATE(
    SUM(vw_exec_timeseries[TotalEngagements])
)

-- 2
Avg Engagement Score

Avg Engagement Score = 
AVERAGE(vw_ExecutiveDashboard[AvgEngagementScore])

-- 3
Total Likes

Total Likes = 
SUM(vw_ExecutiveDashboard[TotalLikes])

-- 4
Total Comments

Total Comments = 
SUM(vw_ExecutiveDashboard[TotalComments])

-- 5
Total Retweets

Total Retweets = 
SUM(vw_ExecutiveDashboard[TotalRetweets])

-- 6
Engagement Rank

Engagement Rank = 
RANKX(
    ALLSELECTED(DimCurrency[Symbol]),
    [Total Engagements],
    ,
    DESC,
    DENSE
)

-- 7
Selected Engagement

Selected Engagement = 
[Total Engagements]

-- 8
Engagement 7D Avg

Engagement 7D Avg = 
CALCULATE(
    [Total Engagements],
    DATESINPERIOD(
        DimDate[FullDate],
        MAX(DimDate[FullDate]),
        -7,
        DAY
    )
)

-- 9
Engagement 30D Avg

Engagement 30D Avg = 
CALCULATE(
    [Total Engagements],
    DATESINPERIOD(
        DimDate[FullDate],
        MAX(DimDate[FullDate]),
        -30,
        DAY
    )
)

-- 10
Last Activity

Last Activity = 
MAXX(
    vw_SocialAnalytics,
    vw_SocialAnalytics[LastEngagement]
)