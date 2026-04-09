USE noodles_dw;

-- ============================================
-- View: Executive Dashboard
-- ============================================

DROP VIEW IF EXISTS vw_ExecutiveDashboard;

CREATE VIEW vw_ExecutiveDashboard AS
SELECT 
    d.Symbol AS CurrencySymbol,

    SUM(f.Likes + f.Comments) AS TotalEngagements,
    SUM(f.Likes) AS TotalLikes,
    SUM(f.Comments) AS TotalComments,

    AVG(f.EngagementScore) AS AvgEngagementScore,

    CASE 
        WHEN SUM(f.Likes + f.Comments) > 1000 THEN 'High'
        WHEN SUM(f.Likes + f.Comments) > 100 THEN 'Medium'
        ELSE 'Low'
    END AS EngagementLevel

FROM FactSocialEngagement f
JOIN DimCurrency d 
    ON f.CurrencyKey = d.CurrencyKey

GROUP BY d.Symbol;


-- ============================================
-- View: Time Series
-- ============================================

DROP VIEW IF EXISTS vw_TimeSeries;

CREATE VIEW vw_TimeSeries AS
SELECT 
    dd.FullDate,
    dd.Year,
    dd.Month,
    dd.MonthName,

    SUM(f.Likes) AS TotalLikes,
    SUM(f.Comments) AS TotalComments,

    (SUM(f.Likes) + SUM(f.Comments)) AS TotalEngagements,

    AVG(f.EngagementScore) AS AvgEngagementScore

FROM FactSocialEngagement f
JOIN DimDate dd 
    ON f.DateKey = dd.DateKey

GROUP BY dd.FullDate, dd.Year, dd.Month, dd.MonthName
ORDER BY dd.FullDate;


-- ============================================
-- View: Social Analytics
-- ============================================

DROP VIEW IF EXISTS vw_SocialAnalytics;

CREATE VIEW vw_SocialAnalytics AS
SELECT 
    dc.Symbol,
    dp.PlatformName,

    SUM(f.Likes + f.Comments) AS TotalEngagements,
    SUM(f.Likes) AS TotalLikes,
    SUM(f.Comments) AS TotalComments,

    AVG(f.EngagementScore) AS AvgEngagementScore

FROM FactSocialEngagement f
JOIN DimCurrency dc 
    ON f.CurrencyKey = dc.CurrencyKey
JOIN DimPlatform dp 
    ON f.PlatformKey = dp.PlatformKey

GROUP BY dc.Symbol, dp.PlatformName;