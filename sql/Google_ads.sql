-- SELECT 
-- SUM(f.impressions) as total_impressions,
-- Sum(f.clicks) as total_clicks,
-- SUM(f.cost)as total_cost,
-- SUM(f.conversions) as total_conversions,
-- SUM(f.revenue) as total_revenue

-- FROM `marketing-analytica-project.marketing_analytics.fact_ads_performance` f
-- JOIN `marketing-analytica-project.marketing_analytics.dim_platform` p
-- ON f.platform_id = p.platform_id

-- WHERE p.platform = 'Google Ads'

-- -- calculating using aggregated sum adn defining kpis to measure the efficiency and cost of campaigns

-- SELECT 
-- SAFE_DIVIDE(SUM(f.clicks),SUM(f.impressions)) as CTR,
-- SAFE_DIVIDE(SUM(f.cost),SUM(f.clicks)) AS CPC, 
-- SAFE_DIVIDE(SUM(f.cost),SUM(f.conversions))AS CPA,
-- SAFE_DIVIDE(SUM(f.revenue),SUM(f.cost)) AS ROAS

-- from `marketing-analytica-project.marketing_analytics.fact_ads_performance` f
-- JOIN `marketing-analytica-project.marketing_analytics.dim_platform` p
-- ON f.platform_id = p.platform_id

-- WHERE p.platform = 'Google Ads'

-- breaking google ads by campaign type and calculating kpis
SELECT c.campaign_type,
SAFE_DIVIDE(SUM(f.clicks),SUM(f.impressions)) as CTR,
SAFE_DIVIDE(SUM(f.cost),SUM(f.clicks)) AS CPC, 
SAFE_DIVIDE(SUM(f.cost),SUM(f.conversions))AS CPA,
SAFE_DIVIDE(SUM(f.revenue),SUM(f.cost)) AS ROAS
from `marketing-analytica-project.marketing_analytics.fact_ads_performance` f
JOIN `marketing-analytica-project.marketing_analytics.dim_platform` p
ON f.platform_id = p.platform_id
JOIN `marketing-analytica-project.marketing_analytics.dim_campaign` c
on f.campaign_id=c.campaign_id

where p.platform = 'Google Ads'
group by c.campaign_type