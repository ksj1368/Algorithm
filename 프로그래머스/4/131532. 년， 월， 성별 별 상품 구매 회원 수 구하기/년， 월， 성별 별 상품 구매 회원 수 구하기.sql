with USER_GENDER as (
    select
        USER_ID,
        GENDER
    from
        USER_INFO
    where
        GENDER is not null
)

select
    year(os.SALES_DATE) as YEAR, 
    month(os.SALES_DATE) as MONTH,
    ug.GENDER as GENDER,
    count(distinct(os.USER_ID)) as USERS
from
    ONLINE_SALE as os
join USER_GENDER as ug on os.USER_ID = ug.USER_ID
group by
    YEAR, 
    MONTH,
    GENDER
order by
    YEAR asc, 
    MONTH asc,
    GENDER asc;