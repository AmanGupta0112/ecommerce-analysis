import csv
import io
import pandas as pd
from django.http import HttpResponse
from django.db.models import Sum, F
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_data(request):
    if "file" not in request.FILES:
        return Response(
            {"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST
        )

    file = request.FILES["file"]

    try:
        df = pd.read_csv(io.BytesIO(file.read()))
    except Exception as e:
        return Response(
            {"error": f"Error reading file: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    for _, row in df.iterrows():
        Product.objects.create(
            product_id=row["product_id"],
            product_name=row["product_name"],
            category=row["category"],
            price=row["price"],
            quantity_sold=row["quantity_sold"],
            rating=row["rating"],
            review_count=row["review_count"],
        )

    return Response(
        {"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def clean_data(request):
    products = Product.objects.all()
    df = pd.DataFrame(list(products.values()))

    # Handle missing values
    df["price"] = df["price"].fillna(df["price"].median())
    df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].median())

    # Calculate average rating by category
    category_avg_rating = df.groupby("category")["rating"].mean()
    df["rating"] = df.apply(
        lambda row: (
            category_avg_rating[row["category"]]
            if pd.isna(row["rating"])
            else row["rating"]
        ),
        axis=1,
    )

    # Ensure numeric values
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Update the database
    for index, row in df.iterrows():
        Product.objects.filter(id=row["id"]).update(
            price=row["price"], quantity_sold=row["quantity_sold"], rating=row["rating"]
        )

    return Response({"message": "Data cleaned successfully"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def generate_summary_report(request):
    summary = (
        Product.objects.values("category")
        .annotate(
            total_revenue=Sum(F("price") * F("quantity_sold")),
        )
        .order_by("-total_revenue")
    )

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="summary_report.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ["category", "total_revenue", "top_product", "top_product_quantity_sold"]
    )

    for category in summary:
        top_product = (
            Product.objects.filter(category=category["category"])
            .order_by("-quantity_sold")
            .first()
        )
        writer.writerow(
            [
                category["category"],
                category["total_revenue"],
                top_product.product_name,
                top_product.quantity_sold,
            ]
        )

    return response
