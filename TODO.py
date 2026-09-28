# TODO LIST

## TODAY:
    # TODO: learn Dagster

        # TODO: Dagster University:
        # TODO: Dagster Essentials: lessons on assets, resources, schedules, partitions, sensors.
            # TODO: Dagster & dbt.
            # TODO: Dagster & ETL: covers APIs, backfilling from APIs, dlt basics, and Dagster with dlt. 
        # TODO: Docs: Dagster & dbt. If you are just getting started, the docs recommend the new dbt component, so follow that path. Also read the Asset checks and Freshness pages. 
        # TODO: Videos:
            # TODO: Unlocking the Power of Dagster and dbt (short)
            # TODO: Modern data stack: automating dlt and dbt pipeline with Dagster
            # TODO: Building a Data Pipeline with Dagster, dbt, and BigQuery, which is very close to your stack
            # TODO: Reference repo: dagster-io/quickstart-dbt

    # TODO: Player count data
        # TODO: Scaffold the project with uv and create-dagster, and make a registry/games.csv of about 200 app IDs.
        # TODO: Build one asset that fetches current players for all games and writes a JSON file per hour to data/landing/. Add an hourly schedule, then leave dagster dev running overnight with sleep disabled.










# ## LEARNING

# ### dbt

# Quickstart for dbt Core using DuckDB. You already know DuckDB, so this is the fastest on-ramp.
# Video: dbt + DuckDB: Complete Beginner Tutorial
# dbt Fundamentals (free on learn.getdbt.com). Take the models, sources, tests, and docs modules and skip deployment.
# Kimball: Building a Kimball dimensional model with dbt, plus the Kimball Group's "Dimensional Modeling Techniques" page. Read the section on the three fact table types; it's the backbone of your data model.

# ### dlt

# The REST API tutorial in the dlt docs (about 30 min, loads into DuckDB). Then swap the destination to BigQuery.
# REST client and paginators and the advanced REST API source page. Read the cursor paginator section carefully.

# ### BigQuery and Terraform

# The BigQuery sandbox docs (cloud.google.com/bigquery/docs/sandbox). Read the limits section before anything else.
# The BigQuery docs on partitioned and clustered tables, and on dry-run queries.
# HashiCorp's "Get started – Google Cloud" tutorial: install, build, variables, and outputs only. Read the VM parts but don't apply them. Also skim the google_bigquery_dataset resource page on the Terraform registry.
# The free DataTalksClub Data Engineering Zoomcamp has good videos for this stack. Module 1 covers Terraform + GCP, Module 3 covers BigQuery partitioning and clustering, and Module 4 covers dbt. Just watch those videos.

# ### MCP

# Anthropic Academy's free Introduction to Model Context Protocol. It covers building servers with the Python SDK, the three primitives (tools, resources, prompts), and the MCP Inspector, and comes with a certificate for LinkedIn. 
# pasqualepillitteri
# Video: Build Your Own MCP Server in Python (FastMCP Tutorial)
# Docs: modelcontextprotocol.io (the build-a-server quickstart) and gofastmcp.com.

# ### Steam API

# The Steamworks "User Reviews – Get List" page (partner.steamgames.com/doc/store/getreviews)
# steamapi.xpaw.me, the best community reference for the Web API