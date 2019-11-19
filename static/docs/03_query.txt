-- Create a database
CREATE DATABASE project2


-- Create a schema cps
CREATE SCHEMA cps
    AUTHORIZATION postgres;


-- Create a new table
CREATE TABLE october (
  hrmonth INT,
  hryear4 INT,
  pwsswgt BIGINT,
  prtage INT,
  pemlr INT, 
  peeduca INT,
  gestfips character varying
);


-- Query employed & unemployed population by education degrees in each State with pemlr in (X, Y) and peeduca=Z
-- (X, Y) = (1, 2)  employed
-- (X, Y) = (3, 4)  unemployed
-- Z = 43  Bachelor's degree
-- Z = 44  Master's degree
-- Z = 46  Doctorate degree
select 
gestfips as snum,
case 
when gestfips='1' then 'AL'
when gestfips='2' then 'AK'
when gestfips='4' then 'AZ'
when gestfips='5' then 'AR'
when gestfips='6' then 'CA'
when gestfips='8' then 'CO'
when gestfips='9' then 'CT'
when gestfips='10' then 'DE'
when gestfips='11' then 'DC'
when gestfips='12' then 'FL'
when gestfips='13' then 'GA'
when gestfips='15' then 'HI'
when gestfips='16' then 'ID'
when gestfips='17' then 'IL'
when gestfips='18' then 'IN'
when gestfips='19' then 'IA'
when gestfips='20' then 'KS'
when gestfips='21' then 'KY'
when gestfips='22' then 'LA'
when gestfips='23' then 'ME'
when gestfips='24' then 'MD'
when gestfips='25' then 'MA'
when gestfips='26' then 'MI'
when gestfips='27' then 'MN'
when gestfips='28' then 'MS'
when gestfips='29' then 'MO'
when gestfips='30' then 'MT'
when gestfips='31' then 'NE'
when gestfips='32' then 'NV'
when gestfips='33' then 'NH'
when gestfips='34' then 'NJ'
when gestfips='35' then 'NM'
when gestfips='36' then 'NY'
when gestfips='37' then 'NC'
when gestfips='38' then 'ND'
when gestfips='39' then 'OH'
when gestfips='40' then 'OK'
when gestfips='41' then 'OR'
when gestfips='42' then 'PA'
when gestfips='44' then 'RI'
when gestfips='45' then 'SC'
when gestfips='46' then 'SD'
when gestfips='47' then 'TN'
when gestfips='48' then 'TX'
when gestfips='49' then 'UT'
when gestfips='50' then 'VT'
when gestfips='51' then 'VA'
when gestfips='53' then 'WA'
when gestfips='54' then 'WV'
when gestfips='55' then 'WI'
when gestfips='56' then 'WY'
else gestfips
end as state, 
(sum(pwsswgt)/10000)::int as unemployed 
from october 
where  
pemlr in (X, Y) and
peeduca = Z 
group by gestfips order by snum;


-- Query employed & unemployment population by ages in Missouri & Kansas pemlr in (X, Y)
-- (X, Y) = (1, 2)  employed
-- (X, Y) = (3, 4)  unemployed
-- Z = 20  Kansas
-- Z= 29  Mossouri
select 
prtage as age, 
(sum(pwsswgt)/10000)::int as unemployed 
from october 
where pemlr in (X, Y) and 
gestfips = 'Z' 
group by prtage;

