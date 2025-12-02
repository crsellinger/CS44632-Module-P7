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
5. Calculate sale_amount by region.
6. Slice by product category
7. Slice by product_id
8. Calculate percentages of preferred payment method

#### Section 5. Results (narrative + visualizations)



#### Section 6. Suggested Business Action



#### Section 7. Challenges



#### Section 8. Ethical Considerations


