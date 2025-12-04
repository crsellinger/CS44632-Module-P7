# Module P7: Custom BI Project

#### Section 1. The Business Goal

To find the most high value customers, and target a marketing strategy toward them by analyzing their region, their top products, and their preferred payment method using their preferred contact method in the customer table.

#### Section 2. Data Source

The database file stored in the warehouse.

Columns required:

Descriptive:
1. Region
2. paymnt_type
3. product_name
4. category

Numeric:
1. sale_amount

#### Section 3. Tools Used

Python

#### Section 4. Workflow & Logic

1. Join customer and sale tables on customer_id.
2. Join new table with product on product_id.
3. Aggregate sum of sale_amount by customer_id on new cube.
4. Group customer_id by region.
5. Calculate sale_amount.
6. Slice product category by region
7. Slice product_id by region
8. Calculate ~~percentages~~ counts of preferred payment method

#### Section 5. Results (narrative + visualizations)

Top Customers: The top 5 customers all spend $20,000 or more.

Top Customers per Region: The Central and West region top customers spend about the same while top customers in the other regions have a high standard deviation (one customer that spends thousands more than the next leading customer).

Revenue by Region: The North and East regions make the most revenue.

Top Categories by Region: The Home category makes the most revenue in 4 out of 6 regions.

Top Products by Region: The top products are Electronics-Letter and Office-Cultural, which are in the Electronics and Home categories, respectively.

Preferred Payment Method: The preferred payment method in all regions, except the West, is Cash.

#### Section 6. Suggested Business Action

The customers come from the North, East, South, and Southwest and their favorite categories to buy in are Home. The Central region needs a heavier marketing strategy with a campaign towards cash spending to boost sales. 

#### Section 7. Challenges

Lots of Key Errors, but thats just me either forgetting the name of a column or omitting the column that I needed entirely before trying to access it. Overall, went well.

#### Section 8. Ethical Considerations

Data from sales transactions are dated on a single day. This data set does not take historical trends into account. Thus, data may be skewed for this day following each region and customer.
