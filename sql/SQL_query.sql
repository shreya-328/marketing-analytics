--data sanity check
--Is data loaded correctly? are totals matching expectations? is revenue null behaving properly?

SELECT 
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(cost) AS total_cost,
    SUM(conversions) AS total_conversions,
    SUM(revenue) AS total_revenue
FROM `marketing-analytica-project.marketing_analytics.fact_ads_performance`;


-- calculating overall performance efficiency
SELECT 
    SAFE_DIVIDE(SUM(clicks), SUM(impressions)) AS CTR,
    SAFE_DIVIDE(SUM(cost), SUM(clicks)) AS CPC,
    SAFE_DIVIDE(SUM(cost), SUM(conversions)) AS CPA,
    SAFE_DIVIDE(SUM(revenue), SUM(cost)) AS ROAS
FROM `marketing-analytica-project.marketing_analytics.fact_ads_performance`;

-- platform wise performance
SELECT
    p.platform,
    
    SUM(f.impressions) AS total_impressions,
    SUM(f.clicks) AS total_clicks,
    SUM(f.cost) AS total_cost,
    SUM(f.conversions) AS total_conversions,
    SUM(f.revenue) AS total_revenue,

    SAFE_DIVIDE(SUM(f.clicks), SUM(f.impressions)) AS CTR,
    SAFE_DIVIDE(SUM(f.cost), SUM(f.clicks)) AS CPC,
    SAFE_DIVIDE(SUM(f.cost), SUM(f.conversions)) AS CPA,
    SAFE_DIVIDE(SUM(f.revenue), SUM(f.cost)) AS ROAS

FROM `marketing-analytica-project.marketing_analytics.fact_ads_performance` f
JOIN `marketing-analytica-project.marketing_analytics.dim_platform` p
ON f.platform_id = p.platform_id

GROUP BY p.platform
ORDER BY ROAS DESC;

