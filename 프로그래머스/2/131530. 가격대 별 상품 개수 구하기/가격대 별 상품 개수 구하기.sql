select
    10000*truncate(p.PRICE/10000, 0) as PRICE_GROUP,
    count(PRICE) as PRODUCTS
from
    PRODUCT as p
group by
    PRICE_GROUP
order by
    PRICE_GROUP asc;