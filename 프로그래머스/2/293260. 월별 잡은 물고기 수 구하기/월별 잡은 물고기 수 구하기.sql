select
    count(ID) as FISH_COUNT,
    convert(date_format(TIME, "%m"), unsigned)as MONTH
from
    FISH_INFO    
group by
    MONTH
order by
    MONTH asc;