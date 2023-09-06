-- 코드를 입력하세요
with sub as (
SELECT car_id, car_type, daily_fee, timestampdiff(day, start_date, end_date)+1 as period, history_id, (
case
    when timestampdiff(day, start_date, end_date)+1 < 7
    then null
    when timestampdiff(day, start_date, end_date)+1 < 30
    then '7일 이상'
    when timestampdiff(day, start_date, end_date)+1 < 90
    then '30일 이상'
    when 90 <= timestampdiff(day, start_date, end_date)+1
    then '90일 이상'
end) as day_diff
from CAR_RENTAL_COMPANY_CAR natural join CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_type = '트럭')

select history_id, 
    round(daily_fee * period * 
            (100 - ifnull(p.discount_rate, 0)) / 100) as fee
from sub as s left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p 
    on s.day_diff = p.duration_type
    and s.car_type = p.car_type
order by fee desc, history_id desc

# select *
# from sub as s left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p 
#     on s.day_diff = p.duration_type
#     and s.car_type = p.car_type