
SELECT * FROM JA15.rd_data5;

# Row_number given based on where condition: seats available given in asc order between row_num 500 and 1000
SELECT ROW_NUMBER() OVER (order by Seats_Available ASC) "ROW_NUMBER", Seats_Available, Route_name,ID,Bus_name,Bus_type FROM JA15.rd_data5;

SELECT* FROM ( 
SELECT ROW_NUMBER() OVER (order by Seats_Available ASC) "ROW_NUM", Seats_Available, Route_name,ID,Bus_name,Bus_type FROM JA15.rd_data5
) As T2
WHERE ROW_NUM BETWEEN 10 AND 1000
;

# Route name in Asc order , row_num b/w 500 and 1000
SELECT* FROM ( 
SELECT ROW_NUMBER() OVER (order by Route_name ASC) "ROW_NUM", Seats_Available, Route_name,ID,Bus_name FROM JA15.rd_data5
) As T2

WHERE ROW_NUM BETWEEN 500 AND 1000
;

# Rank given based on Ratings desc order
SELECT RANK() OVER (ORDER BY Ratings DESC) "COL_RANK", Seats_Available,Ratings,Bus_type,Price,Bus_name
FROM JA15.rd_data5;

# Having function
# less than 50 rank based on ratings
SELECT COL_RANK, COUNT(COL_RANK) FROM (
SELECT RANK() OVER (ORDER BY Ratings DESC) "COL_RANK", Seats_Available,Ratings,Bus_type
FROM JA15.rd_data5
) AS T2

GROUP BY COL_RANK
HAVING COUNT(COL_RANK) < 50;

