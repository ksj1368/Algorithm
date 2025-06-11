with MOST_REV_CNT as (
    select
        MEMBER_ID,
        count(REVIEW_ID) as REV_CNT,
        RANK() OVER (ORDER BY count(REVIEW_ID) DESC) as RNK
    from
        REST_REVIEW 
    group by
        MEMBER_ID
),
MOST_REV_USER as (
    select
        mp.MEMBER_ID,
        mp.MEMBER_NAME
    from
        MEMBER_PROFILE as mp
    inner join (
        select
            MEMBER_ID,
            REV_CNT
        from 
            MOST_REV_CNT
        where 
            RNK = 1
    ) as mrc on mp.MEMBER_ID = mrc.MEMBER_ID
)

select
    mru.MEMBER_NAME,
    rr.REVIEW_TEXT,
    date_format(rr.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from
    MOST_REV_USER as mru
join REST_REVIEW as rr on mru.MEMBER_ID = rr.MEMBER_ID
order by
    REVIEW_DATE asc,
    REVIEW_TEXT asc;