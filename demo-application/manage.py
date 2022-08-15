#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from opentelemetry.instrumentation.django import DjangoInstrumentor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    os.environ.setdefault('WEBSITE_HOSTNAME', 'localhost')
    try:
        tracer = TracerProvider(resource=Resource({SERVICE_NAME: "FastAPI"}))

        tracer.add_span_processor(BatchSpanProcessor(
            AzureMonitorTraceExporter.from_connection_string(
                os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')
            )
        ))
        DjangoInstrumentor().instrument(tracer_provider = tracer)
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
