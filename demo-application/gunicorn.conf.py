import os

from opentelemetry.instrumentation.django import DjangoInstrumentor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    if 'APPLICATIONINSIGHTS_CONNECTION_STRING' in os.environ:
        tracer = TracerProvider(resource=Resource({SERVICE_NAME: "Django"}))
        tracer.add_span_processor(BatchSpanProcessor(
            AzureMonitorTraceExporter.from_connection_string(
                os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')
            )
        ))
        DjangoInstrumentor().instrument(tracer_provider = tracer)
