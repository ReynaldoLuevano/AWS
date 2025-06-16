CREATE EXTERNAL TABLE IF NOT EXISTS `default`.`demo` (
  `record_number` int,
  `first_name` string,
  `last_name` string,
  `transaction_date` date,
  `card_number` bigint,
  `card_expire` string,
  `card_type` string,
  `card_sec_code` int,
  `transaction_amount` decimal(7,2)
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://arquitecto122experis/ingesta122/'
TBLPROPERTIES ("skip.header.line.count"="1");