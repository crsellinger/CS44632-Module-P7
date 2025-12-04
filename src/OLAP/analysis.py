import pathlib
import sys

import matplotlib.pyplot as plt
import pandas as pd

# Ensure project root is in sys.path for local imports (now 3 parents are needed)
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from utils_logger import logger

# Global constants for paths and key directories

THIS_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent
DW_DIR: pathlib.Path = THIS_DIR  # src/analytics_project/OLAP/
PACKAGE_DIR: pathlib.Path = DW_DIR.parent  # src/analytics_project/
SRC_DIR: pathlib.Path = PACKAGE_DIR.parent  # src/
PROJECT_ROOT_DIR: pathlib.Path = SRC_DIR.parent / "CS44632-Module-P7"  # project_root/

# Data directories
DATA_DIR: pathlib.Path = PROJECT_ROOT_DIR / "data"
WAREHOUSE_DIR: pathlib.Path = DATA_DIR / "warehouse"

# Warehouse database location (SQLite)
DB_PATH: pathlib.Path = WAREHOUSE_DIR / "smart_sales.db"

# OLAP output directory
OLAP_OUTPUT_DIR: pathlib.Path = DATA_DIR / "olap_cubing_outputs"

# CUBED File path
CUBED_FILE: pathlib.Path = OLAP_OUTPUT_DIR / "multidimensional_olap_cube.csv"

# Results output directory
RESULTS_OUTPUT_DIR: pathlib.Path = DATA_DIR / "results"

# Recommended - log paths and key directories for debugging

logger.info(f"THIS_DIR:            {THIS_DIR}")
logger.info(f"DW_DIR:              {DW_DIR}")
logger.info(f"PACKAGE_DIR:         {PACKAGE_DIR}")
logger.info(f"SRC_DIR:             {SRC_DIR}")
logger.info(f"PROJECT_ROOT_DIR:    {PROJECT_ROOT_DIR}")

logger.info(f"DATA_DIR:            {DATA_DIR}")
logger.info(f"WAREHOUSE_DIR:       {WAREHOUSE_DIR}")
logger.info(f"DB_PATH:             {DB_PATH}")
logger.info(f"OLAP_OUTPUT_DIR:     {OLAP_OUTPUT_DIR}")

# Create output directory for results if it doesn't exist
RESULTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def visualize(
    cube_df: pd.DataFrame,
    colx: str = None,
    coly: str = None,
    title: str = "Title",
    x: str = "xlabel",
    y: str = "ylabel",
    result: str = "results",
) -> None:
    try:
        # Plot the stacked bar chart
        fig = cube_df.plot(
            x=colx, y=coly, kind="bar", stacked=True, figsize=(12, 8), colormap="tab10"
        )

        plt.title(title, fontsize=16)
        plt.xlabel(x, fontsize=12)
        plt.ylabel(y, fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="$%.0f", label_type="center")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{result}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error creating visual: {e}")
        raise


def visualize_top_cust_by_region(top_cust_by_region: pd.DataFrame) -> None:
    try:
        region_colors = {
            "North": "#1f77b4",
            "South": "#ff7f0e",
            "East": "#2ca02c",
            "West": "#d62728",
            "Central": "#4abd77",
            "South-West": "#F1CF11",
        }

        # Plot the stacked bar chart
        fig = top_cust_by_region.plot(
            x="name",
            y="TotalSales",
            kind="bar",
            stacked=True,
            figsize=(12, 8),
            color=top_cust_by_region["region"].map(region_colors),
        )

        legend_handles = []
        for region, color in region_colors.items():
            # Create a colored square for the legend
            handle = plt.Rectangle((0, 0), 1, 1, color=color)
            legend_handles.append(handle)

        plt.legend(legend_handles, region_colors.keys(), title="Region")

        plt.title("Top Customers per Region", fontsize=16)
        plt.xlabel("Customer", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="$%.0f")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{"top_customers_per_region"}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error creating visual: {e}")
        raise


def visualize_revenue_by_region(revenue_by_region: pd.DataFrame) -> None:
    try:
        # Plot the stacked bar chart
        fig = revenue_by_region.plot(
            x="region", y="TotalSales", kind="bar", stacked=True, figsize=(12, 8)
        )

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="$%.0f")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{"revenue_by_region"}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error visualizing revenue by region: {e}")
        raise


def visualize_top_categories(top_cat: pd.DataFrame) -> None:
    try:
        region_colors = {
            "North": "#1f77b4",
            "South": "#ff7f0e",
            "East": "#2ca02c",
            "West": "#d62728",
            "Central": "#4abd77",
            "South-West": "#F1CF11",
        }

        # Plot the stacked bar chart
        fig = top_cat.plot(
            x="category",
            y="TotalSales",
            kind="bar",
            stacked=True,
            figsize=(12, 8),
            color=top_cat["region"].map(region_colors),
        )

        legend_handles = []
        for region, color in region_colors.items():
            # Create a colored square for the legend
            handle = plt.Rectangle((0, 0), 1, 1, color=color)
            legend_handles.append(handle)

        plt.legend(legend_handles, region_colors.keys(), title="Region")

        plt.title("Top Category per Region", fontsize=16)
        plt.xlabel("Category", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="$%.0f")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{"top_categories_by_region"}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error creating visual: {e}")
        raise

def visualize_top_products(top_product: pd.DataFrame) -> None:
    try:
        region_colors = {
            "North": "#1f77b4",
            "South": "#ff7f0e",
            "East": "#2ca02c",
            "West": "#d62728",
            "Central": "#4abd77",
            "South-West": "#F1CF11",
        }

        # Plot the stacked bar chart
        fig = top_product.plot(
            x="product_name",
            y="TotalSales",
            kind="bar",
            stacked=True,
            figsize=(12, 8),
            color=top_product["region"].map(region_colors),
        )

        legend_handles = []
        for region, color in region_colors.items():
            # Create a colored square for the legend
            handle = plt.Rectangle((0, 0), 1, 1, color=color)
            legend_handles.append(handle)

        plt.legend(legend_handles, region_colors.keys(), title="Region")

        plt.title("Top Products per Region", fontsize=16)
        plt.xlabel("Products", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="$%.0f")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{"top_products_by_region"}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error creating visual: {e}")
        raise

def visualize_preferred_paymnt(pref: pd.DataFrame) -> None:
    try:
        region_colors = {
            "North": "#1f77b4",
            "South": "#ff7f0e",
            "East": "#2ca02c",
            "West": "#d62728",
            "Central": "#4abd77",
            "South-West": "#F1CF11",
        }

        # Plot the stacked bar chart
        fig = pref.plot(
            x="paymnt_type",
            y="paymnt_type_count",
            kind="bar",
            stacked=True,
            figsize=(12, 8),
            color=pref["region"].map(region_colors),
        )

        legend_handles = []
        for region, color in region_colors.items():
            # Create a colored square for the legend
            handle = plt.Rectangle((0, 0), 1, 1, color=color)
            legend_handles.append(handle)

        plt.legend(legend_handles, region_colors.keys(), title="Region")

        plt.title("Preferred Payment Method", fontsize=16)
        plt.xlabel("Payment Type", fontsize=12)
        plt.ylabel("Count", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Add labels to bars
        for p in fig.containers:
            fig.bar_label(p, fmt="%.0f")

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath(f"{"preferred_payment"}.png")
        plt.savefig(output_path)
        logger.info(f"Bar chart saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error creating visual: {e}")
        raise

def main():
    logger.info("Starting analysis...")

    # Load precomputed cube
    try:
        cube = pd.read_csv(CUBED_FILE)
        logger.info(f"OLAP cube data successfully loaded from {CUBED_FILE}.")
    except Exception as e:
        logger.error(f"Error loading OLAP cube data: {e}")
        raise

    # print(cube.head())

    # Analyze top 5 customers by summing sale amount
    try:
        grouped = (
            cube.groupby(["customer_id", "name", "region"])["sale_amount_sum"]
            .sum()
            .reset_index()
        )
        grouped.rename(columns={"sale_amount_sum": "TotalSales"}, inplace=True)
        # print(grouped.head())
        top_customers = grouped.sort_values("TotalSales", ascending=False)
        logger.info("Top customers identified.")
        # print(top_customers.head(5))
    except Exception as e:
        logger.error(f"Error getting top customers: {e}")
        raise

    # Group top 5 customers by Region (rank ascending)
    try:
        top_cust_by_region = (
            top_customers.assign(
                rank=lambda df: df.groupby("region")["TotalSales"].rank(
                    "dense", ascending=False
                )
            )
            .query("rank <= 3")
            .sort_values("region", ascending=True)
        )
        logger.info("Top customers per region ranked in ascending order complete.")
    except Exception as e:
        logger.error(f"Error getting top customers per region: {e}")
        raise

    # print(top_cust_by_region.head(30))

    # Sale Amount by Region
    revenue_by_region = (
        top_cust_by_region.groupby(["region"])["TotalSales"].sum().reset_index()
    )
    # print(revenue_by_region.head())

    # Group by product category by region
    product_cat_grouped = (
        cube.groupby(["region", "category"])["sale_amount_sum"].sum().reset_index()
    )
    product_cat_grouped.rename(columns={"sale_amount_sum": "TotalSales"}, inplace=True)
    product_cat_grouped = (
        product_cat_grouped.assign(
            rank=lambda df: df.groupby("region")["TotalSales"].rank(
                "dense", ascending=False
            )
        )
        .query("rank <= 1")
        .sort_values("rank", ascending=True)
    )
    # print(product_cat_grouped.head(30))

    # Group by product ID
    product_id_grouped = (
        cube.groupby(["region", "product_id", "product_name"])["sale_amount_sum"]
        .sum()
        .reset_index()
    )
    product_id_grouped.rename(columns={"sale_amount_sum": "TotalSales"}, inplace=True)
    product_id_grouped = (
        product_id_grouped.assign(
            rank=lambda df: df.groupby("region")["TotalSales"].rank(
                "dense", ascending=False
            )
        )
        .query("rank <= 1")
        .sort_values("rank", ascending=True)
    )
    # print(product_id_grouped.head())

    # Analyze preferred payment and contact method
    pref_payment = (
        cube.groupby(["region","paymnt_type"])
        .size()
        .reset_index()
        .rename(columns={0: 'paymnt_type_count'})
    )
    # print(pref_payment.head())

    # ------------ Visuals ---------------------#
    visualize(
        top_customers.head(5),
        "name",
        "TotalSales",
        "Top Customers Overall",
        "Customer",
        "Total Sales (USD)",
        "top_customers",
    )

    visualize_top_cust_by_region(top_cust_by_region)

    visualize_revenue_by_region(revenue_by_region)

    visualize_top_categories(product_cat_grouped)

    visualize_top_products(product_id_grouped)

    visualize_preferred_paymnt(pref_payment)


if __name__ == "__main__":
    main()
