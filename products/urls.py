from django.urls import path
from .views import (
    upload_data,
    clean_data,
    generate_summary_report,
)

urlpatterns = [
    path("upload-data/", upload_data, name="upload_data"),
    path("clean-data/", clean_data, name="clean_data"),
    path("summary-report/", generate_summary_report, name="summary_report"),
]
