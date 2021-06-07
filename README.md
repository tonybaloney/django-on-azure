# PyCon 2021 Workshop Notes

Resources for my Django on Azure workshop at PyCon US 2021

A copy of [the slides](slides.pdf) is available in this repository.

## Sections

### Azure Architecture

#### Links

- [Tutorial: Deploy a Django web app with PostgreSQL in Azure App Service](https://docs.microsoft.com/azure/app-service/tutorial-python-postgresql-app?WT.mc_id=python-00000-anthonyshaw)

### Azure Web Apps

[App Service Pricing](https://azure.microsoft.com/en-au/pricing/details/app-service/linux/?WT.mc_id=python-00000-anthonyshaw)

#### App Service Components

- [Web Apps](https://docs.microsoft.com/en-us/azure/app-service/?WT.mc_id=python-00000-anthonyshaw)
- [App Service Plans](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans?WT.mc_id=python-00000-anthonyshaw)
- [Continuous Deployment with App Service](https://tonybaloney.github.io/posts/django-on-azure-beyond-hello-world.html#testing)
- [Using LocustIO to load test Django](https://tonybaloney.github.io/posts/django-on-azure-beyond-hello-world.html#performance)
- [Django Template Caching](https://docs.djangoproject.com/en/3.2/topics/cache/)
- [Scale up an App in Azure](https://docs.microsoft.com/en-us/azure/app-service/manage-scale-up?WT.mc_id=python-00000-anthonyshaw)

#### Configuring ASGI workers

1. Add the following `startup.sh` script

```console
gunicorn --workers 8 --threads 4 --timeout 60 --access-logfile '-' --error-logfile '-' --bind=0.0.0.0:8000 -k uvicorn.workers.UvicornWorker --chdir=/home/site/wwwroot your_django_app.asgi
```

2. Make sure you add `uvicorn` to the `requirements.txt` file
3. Pick the right number of workers and threads for the instance size
4. To enable this startup command, you need to set the startup command to startup.sh in Settings -> Configuration -> General Settings -> Startup command. After making these changes, the application will restart

### Databases

#### Overview of DBaaS offerings

- [Azure Database for PostgreSQL](https://docs.microsoft.com/en-au/azure/postgresql/?WT.mc_id=python-00000-anthonyshaw)
- [Azure SQL](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?WT.mc_id=python-00000-anthonyshaw)
- [Azure Database for MySQL](https://docs.microsoft.com/en-us/azure/mysql/?WT.mc_id=python-00000-anthonyshaw)
- [Azure Database for MariaDB](https://docs.microsoft.com/en-us/azure/mariadb/?WT.mc_id=python-00000-anthonyshaw)
- [Django support for Microsoft SQL Server](https://github.com/microsoft/mssql-django?WT.mc_id=python-00000-anthonyshaw)
- [Azure Database for Postgres Pricing](https://docs.microsoft.com/en-us/azure/app-service/?WT.mc_id=python-00000-anthonyshaw)

#### Types of Postgres Deployment on Azure

- [Flexible Server Overview](https://docs.microsoft.com/en-au/azure/postgresql/flexible-server/overview?WT.mc_id=python-00000-anthonyshaw)
- [Single Server Overview](https://docs.microsoft.com/en-us/azure/postgresql/overview?WT.mc_id=python-00000-anthonyshaw)
- [Hyperscale (Citus) Server](https://docs.microsoft.com/en-au/azure/postgresql/hyperscale-overview?WT.mc_id=python-00000-anthonyshaw)
- [Azure Arc enabled Postgres](https://docs.microsoft.com/en-us/azure/azure-arc/data/what-is-azure-arc-enabled-postgres-hyperscale?WT.mc_id=python-00000-anthonyshaw)

#### Other Useful Links

- [Performance optimizations for Postgres on Azure](https://www.citusdata.com/blog/2020/05/20/postgres-tips-for-django-and-python/)

### Content Delivery

- [Static Files and CDN example](https://tonybaloney.github.io/posts/django-on-azure-beyond-hello-world.html#storage)
- [Azure CDN Pricing](https://azure.microsoft.com/pricing/details/cdn/?WT.mc_id=python-0000-anthonyshaw)

### Monitoring and Insights

- [OpenCensus extension for Django](https://pypi.org/project/opencensus-ext-django/)
- [OpenCensus extension for Azure](https://pypi.org/project/opencensus-ext-azure/)

### Deployment and DevOps

- [Azure Pipelines Examples](https://tonybaloney.github.io/posts/django-on-azure-beyond-hello-world.html#testing)

### Extra Components

- [Writing an Azure Function for Python](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?WT.mc_id=python-00000-anthonyshaw)
- [SendGrid on the Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/SendGrid.SendGrid?WT.mc_id=python-0000-anthonyshaw)

