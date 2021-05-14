# pycon-django-workshop

Resources for my Django on Azure workshop at PyCon US 2021

A copy of [the slides](slides.pdf) is available in this repository.

## Sections

### Azure Architecture

**Links:**

- [Tutorial: Deploy a Django web app with PostgreSQL in Azure App Service](https://docs.microsoft.com/azure/app-service/tutorial-python-postgresql-app?WT.mc_id=python-00000-anthonyshaw)


### Azure Web Apps

[App Service Pricing](https://azure.microsoft.com/en-au/pricing/details/app-service/linux/?WT.mc_id=python-00000-anthonyshaw)

#### App Service Components

- [Web Apps](https://docs.microsoft.com/en-us/azure/app-service/)
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

**Links**

- [Azure Database for Postgres]
- [Azure SQL]
- [Azure Database for MySQL/MariaDB]
- [Django support for Microsoft SQL Server]
- [Azure Database for Postgres Tiers]
- [Postgres Flexible Server Tiers]
- [Performance optimizations for Postgres on Azure]
- [Hyperscale (Citus) Server]
- [Azure Arc enabled Postgres]

### Content Delivery


### Monitoring and Insights


### Deployment and DevOps


### Extra Components


### Conclusion