# Data Wrangling Cookbook

1. [Read a CSV file](01_read-csv/) — Load a comma-separated file into a DataFrame.
2. [Read an Excel file](02_read-excel/) — Load an Excel worksheet into a DataFrame.
3. [Read JSON](03_read-json/) — Load records-oriented JSON into a DataFrame.
4. [Read Parquet](04_read-parquet/) — Load columnar Parquet data into a DataFrame.
5. [Write a CSV file](05_write-csv/) — Persist a DataFrame back out to CSV.
6. [Write Parquet](06_write-parquet/) — Persist a DataFrame to Parquet.
7. [Select columns](07_select-columns/) — Project a subset of columns.
8. [Filter rows](08_filter-rows/) — Row selection with a boolean condition.
9. [Rename columns](09_rename-columns/) — Change one or more column names.
10. [Sort rows](10_sort-values/) — Order rows by one or more columns.
11. [Drop duplicates](11_drop-duplicates/) — Remove repeated rows.
12. [Fill missing values](12_handle-missing-fillna/) — Replace NaN/null with a default.
13. [Drop rows with missing values](13_handle-missing-dropna/) — Discard rows that contain NaN/null.
14. [Change column dtypes](14_type-conversion/) — Cast columns to the right type.
15. [Add a calculated column](15_add-column/) — Create a new column from existing ones.
16. [Conditional column (if/else)](16_conditional-column/) — Populate a column based on a rule.
17. [Replace values](17_replace-values/) — Swap specific values for others.
18. [String operations](18_string-operations/) — Common vectorized string methods.
19. [Extract text with regex](19_regex-extract/) — Pull a pattern out of a string column.
20. [Parse datetime strings](20_datetime-parse/) — Turn strings into a real datetime dtype.
21. [Extract date parts](21_datetime-components/) — Pull year / month / day / weekday from a datetime.
22. [GroupBy aggregate](22_groupby-aggregate/) — Summarize rows within groups.
23. [GroupBy multiple aggregations](23_groupby-multiple-agg/) — Multiple metrics per group in one pass.
24. [Pivot table](24_pivot-table/) — Reshape long to wide with an aggregation.
25. [Melt / unpivot](25_melt-unpivot/) — Wide to long: turn columns into rows.
26. [Cross-tabulation](26_crosstab/) — Frequency table of two categorical variables.
27. [Inner join](27_merge-inner-join/) — Keep only matching rows from both sides.
28. [Left join](28_merge-left-join/) — Keep all rows from the left, fill missing right side with null.
29. [Outer / full join](29_merge-outer-join/) — Keep rows from either side.
30. [Concatenate rows](30_concat-rows/) — Stack two DataFrames vertically.
31. [Concatenate columns](31_concat-columns/) — Bind two frames side by side (aligned on row index).
32. [As-of join (time-based)](32_merge-asof/) — Match each row to the most recent matching key in another frame.
33. [Apply a Python function](33_apply-function/) — Row-wise or column-wise custom logic.
34. [Value counts](34_value-counts/) — Frequency of each distinct value.
35. [Summary statistics](35_describe-stats/) — Count / mean / std / quantiles across numeric columns.
36. [Correlation matrix](36_correlation/) — Pairwise correlation of numeric columns.
37. [Rolling window](37_rolling-window/) — Moving average / rolling aggregate.
38. [Cumulative sum](38_cumulative-sum/) — Running total.
39. [Rank values](39_rank/) — Assign ranks (dense / ordinal).
40. [Bin values into categories](40_bin-cut/) — Discretize a continuous column into buckets.
41. [One-hot encode](41_one-hot-encode/) — Turn a categorical column into indicator columns.
42. [Outlier detection (IQR)](42_outlier-iqr/) — Flag rows outside 1.5 * IQR of a numeric column.
43. [Random sample rows](43_sample-rows/) — Take a reproducible random subset.
44. [Explode list column](44_explode-lists/) — Turn each list element into its own row.
45. [SQL-like query()](45_query-sql-like/) — Filter rows via a string expression.
46. [Window functions over partitions](46_window-functions/) — Row number / rank within each group.
47. [Resample a time series](47_resample-timeseries/) — Roll up daily data to weekly totals.
48. [Read many CSVs (glob)](48_read-multiple-csvs/) — Load and concatenate a folder of CSV shards.
49. [Chained transformation pipeline](49_chained-pipeline/) — Method-chain a filter -> derive -> group -> sort in one flow.
50. [Polars lazy evaluation](50_polars-lazy/) — Build a query graph with scan_csv() and let polars optimize.
51. [Read a CSV and inspect its schema](51_read-csv/) — Load a small sales extract and select the first three rows for inspection.
52. [Select and rename columns](52_select-rename/) — Keep the fields needed by a downstream report and give them readable names.
53. [Filter rows using multiple conditions](53_filter-rows/) — Find East-region orders containing at least three units.
54. [Sort and retrieve the top N rows](54_sort-top-n/) — Find the three largest orders by unit count with a stable tie-breaker.
55. [Fill missing numeric and categorical values](55_missing-values/) — Fill missing ages with the observed median and missing cities with a label.
56. [Keep the latest record per key](56_deduplicate/) — Resolve duplicate customer records by retaining the most recent update.
57. [Trim whitespace and normalize text](57_clean-strings/) — Standardize names and email addresses before matching records.
58. [Convert messy numeric strings](58_numeric-conversion/) — Remove currency formatting and convert invalid amounts to missing values.
59. [Parse dates and handle invalid input](59_parse-dates/) — Parse ISO date strings while retaining rows with malformed dates.
60. [Calculate derived numeric columns](60_derived-columns/) — Calculate line revenue and a tax-inclusive total for each order.
61. [Assign labels with conditional logic](61_conditional-labels/) — Classify scores as high, medium, or low using ordered thresholds.
62. [Map codes to readable categories](62_map-categories/) — Translate known status codes and label unmapped values explicitly.
63. [Clip values to a permitted range](63_clip-values/) — Bound percentage values between zero and one hundred.
64. [Replace sentinel values with missing values](64_sentinel-values/) — Treat -999 as an unavailable sensor reading before calculating an average.
65. [Flag records that violate data rules](65_flag-invalid-rows/) — Mark rows whose age or email fails a simple quality rule.
66. [Aggregate totals and averages by group](66_group-aggregation/) — Build a region-level summary of units and order sizes.
67. [Group by multiple dimensions](67_multi-column-grouping/) — Summarize units sold for each region and product combination.
68. [Count unique values within each group](68_distinct-counts/) — Count distinct customers served by each region.
69. [Build a frequency and percentage table](69_frequency-table/) — Count ticket priorities and their share of all tickets.
70. [Calculate a weighted average](70_weighted-average/) — Calculate each product’s average selling price weighted by units sold.
71. [Compare each row with its group average](71_group-transform/) — Attach team averages to employee rows and calculate the difference.
72. [Rank values within groups](72_rank-within-groups/) — Rank employee scores within teams, giving tied scores the same dense rank.
73. [Calculate running totals by group](73_cumulative-totals/) — Track cumulative quantities by customer in order-date order.
74. [Calculate a rolling moving average](74_rolling-average/) — Smooth daily sales with a trailing three-observation average.
75. [Compare a row with the previous row](75_lag-and-difference/) — Add previous-day sales and the absolute change.
76. [Calculate percentage changes safely](76_percentage-change/) — Calculate day-to-day growth while handling a zero previous value.
77. [Extract calendar features](77_date-components/) — Derive year, month, and an ISO weekday number from order dates.
78. [Aggregate daily records into months](78_monthly-summary/) — Build a monthly units report using month-start labels.
79. [Filter a half-open date interval](79_date-range-filter/) — Select January records using an inclusive start and exclusive end.
80. [Fill missing dates in a daily series](80_fill-calendar-gaps/) — Build a complete calendar and fill absent daily sales with zero.
81. [Convert UTC timestamps to local time](81_timezone-conversion/) — Convert event times to New York while preserving the original instant.
82. [Pivot long data into a summary table](82_pivot-table/) — Create one row per region and one units column per product.
83. [Unpivot wide data into tidy rows](83_unpivot/) — Turn monthly sales columns into month and sales fields.
84. [Expand delimited values into rows](84_explode-lists/) — Create one row per article tag from pipe-separated tags.
85. [Split a compound field into columns](85_split-columns/) — Separate a location field into city and state using its last delimiter.
86. [Append files and retain source lineage](86_concatenate-files/) — Combine two monthly extracts and keep the source filename on each row.
87. [Join matching records from two tables](87_inner-join/) — Enrich orders with customer names and keep only matched customers.
88. [Keep all left-side rows when joining](88_left-join/) — Retain all orders and flag those without a customer lookup match.
89. [Find rows with no matching lookup key](89_anti-join/) — Find orders referring to customers absent from the customer table.
90. [Join on a composite key](90_multi-key-join/) — Attach a regional product price and compute order revenue.
91. [Match the most recent earlier observation](91_asof-join/) — Attach the latest available quote to each trade without using future quotes.
92. [Bucket numeric values into intervals](92_bin-numeric-values/) — Assign ages to minor, adult, and senior categories with matching boundaries.
93. [Standardize a numeric feature with z-scores](93_zscore-standardization/) — Center scores at zero and scale by the population standard deviation.
94. [Scale a numeric feature to the unit interval](94_min-max-scaling/) — Rescale observed scores so the minimum is zero and maximum is one.
95. [Flag outliers using the interquartile range](95_iqr-outliers/) — Flag unusually large or small values using the 1.5×IQR rule.
96. [Measure correlation between two columns](96_correlation/) — Calculate Pearson correlation after removing incomplete pairs.
97. [Search text with case-insensitive patterns](97_text-search/) — Find support tickets mentioning a refund or a return.
98. [Extract structured values from text](98_regex-extraction/) — Extract an order ID and a dollar amount from semi-structured messages.
99. [Calculate each row’s share of a group total](99_share-of-group-total/) — Calculate each order’s percentage contribution to regional revenue.
100. [Process a CSV with chunks or a lazy query](100_chunked-and-lazy-pipeline/) — Filter orders with at least two units and aggregate revenue by region using pandas chunks or a Polars lazy plan.
101. [Choose the first available value](101_coalesce-columns/) — Combine primary and backup contact columns by taking the first nonmissing value in each row.
102. [Carry observations forward within groups](102_forward-fill-by-group/) — Fill missing sensor readings from the latest earlier reading for the same sensor.
103. [Interpolate gaps between observations](103_linear-interpolation/) — Estimate missing readings between known values in an evenly spaced time series.
104. [Keep records whose keys exist in another table](104_semi-join/) — Select orders from eligible customers without adding lookup columns or multiplying rows.
105. [Build a complete category grid](105_complete-category-grid/) — Create every store/product combination and fill unobserved sales combinations with zero.
106. [Select the top N rows per group](106_top-n-per-group/) — Keep the two best-selling products in each region with a deterministic tie-breaker.
107. [Filter groups using an aggregate threshold](107_filter-groups-by-total/) — Keep all transactions for customers whose total spending reaches a specified threshold.
108. [Reconcile two dataset snapshots](108_reconcile-snapshots/) — Compare product prices across snapshots and label added, removed, changed, and unchanged records.
109. [Assign sessions to user events](109_sessionize-events/) — Start a new session whenever a user’s consecutive events are more than 30 minutes apart.
110. [Count consecutive value streaks](110_consecutive-value-streaks/) — Number runs of repeated statuses and count each row’s position within its run.
111. [Flatten nested JSON records](111_flatten-nested-json/) — Expand nested customer details into ordinary columns while preserving one row per order.
112. [Parse multiple known date formats](112_parse-multiple-date-formats/) — Combine explicit parsers for ISO and US-style dates while leaving invalid values missing.
113. [Summarize distributions with group percentiles](113_group-percentiles/) — Calculate median and 90th-percentile response times for each service using linear interpolation.
114. [Calculate elapsed time and flag overdue work](114_elapsed-time-and-sla/) — Measure ticket resolution time in hours and flag completed tickets exceeding a 24-hour target.
115. [Calculate monthly cohort retention](115_monthly-cohort-retention/) — Group customers by first observed activity month and measure the share active in later months.
