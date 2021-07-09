-- Capital Gain/Loss

-- SQL Schema
-- Table: Stocks

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | stock_name    | varchar |
-- | operation     | enum    |
-- | operation_day | int     |
-- | price         | int     |
-- +---------------+---------+
-- (stock_name, operation_day) is the primary key for this table.
-- The operation column is an ENUM of type ('Sell', 'Buy')
-- Each row of this table indicates that the stock which has stock_name had an
-- operation on the day operation_day with the price.
-- It is guaranteed that each 'Sell' operation for a stock has a corresponding
-- 'Buy' operation in a previous day.
 
-- Write an SQL query to report the Capital gain/loss for each stock.

-- The capital gain/loss of a stock is total gain or loss after buying and
-- selling the stock one or many times.

SELECT
    stock_name,
    SUM(IF(operation = 'Buy', -price, price)) as capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name