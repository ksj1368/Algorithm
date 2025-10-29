with TOTAL_JULY as (
    select
        FLAVOR,
        sum(TOTAL_ORDER) as TOTAL_ORDER
    from    
        JULY
    group by
        FLAVOR
    
),
UNION_ORDER as (
    select 
        FLAVOR,
        TOTAL_ORDER
    from
        TOTAL_JULY
    union all
    select 
        FLAVOR,
        TOTAL_ORDER
    from
        FIRST_HALF 
)

select
    FLAVOR
from
    UNION_ORDER
group by
    FLAVOR
order by
    sum(TOTAL_ORDER) desc
limit 3;