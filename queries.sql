-- Looking into how productive overall congress over time, by looking at how many bills are passed per day over time
-- Interesting because I am curious to see if there are any trends of how productive congress is. More detailed analysis would be necessary to see
-- why congress is more or less productive at certain times.
select count(*) as count, latest_action_date from mlabs-incubator.skills_gong.bills group by latest_action_date order by latest_action_date desc;


-- Overall, how many days pass between an update to a bill vs the latest action taken?
-- If there were many days between updates and actions, it could be a sign that the bill is not being worked on
-- It looks like most of the bills are updated within a week of an action being taken, which is a good sign that the bill is being worked on
SELECT count(*) as count, DATE_DIFF(update_date, latest_action_date, DAY) as days_diff from mlabs-incubator.skills_gong.bills group by days_diff order by count desc;

-- How many bills get sent to committee vs not?
-- If I had more time I would use regex to pull out the names of the committees and see 
-- which ones are the busiest. 
with committees as (
select *, 
    case  
    when lower(latest_action_text) like '%committee%' then TRUE
    else FALSE
end as is_committee
 from mlabs-incubator.skills_gong.bills
)
select count(*), is_committee from committees group by is_committee
