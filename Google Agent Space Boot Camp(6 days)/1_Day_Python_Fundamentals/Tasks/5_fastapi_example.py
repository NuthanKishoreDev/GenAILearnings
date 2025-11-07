from fastapi import FastAPI, HTTPException
from flask import json
from Utilities.logger_config import setup_logger
import dotenv, os

logger = setup_logger()

# Initialize FastAPI app
app = FastAPI()

# # ✅ Set up logging configuration
# log_path = Path(r"C:\GCP\GenAILearnings\Google Agent Space Boot Camp(6 days)\1_Day_Python_Fundamentals\data\logs")
# log_path.mkdir(parents=True, exist_ok=True)  # Create folder if not exists

# logging.basicConfig(
#     filename=log_path / "fastapi_logger.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# logger = logging.getLogger(__name__)

# ✅ Define endpoints
@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Hello, FastAPI is running!"}



def get_product_data():
    dotenv.load_dotenv()
    products_path = os.getenv("data_folder_path")+r"\products.json"
    logger.info(f"Reading products from: {products_path}")
    # For demonstration, returning static data
    try:
        with open(products_path) as f:
            reader = json.load(f)
            data = list(reader)
    except Exception as e:
        logger.error(f"Error reading products JSON: {e}")
        data = []
    return {"products": data}


@app.get("/products")
def get_products():
    logger.info("Products endpoint accessed")
    logger.info(f"available products: {get_product_data()} ")
    return {"products": get_product_data()}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    logger.info(f"🔹 Request received for product ID: {product_id}")

    # Fetch all products
    products = get_product_data()["products"]
    logger.info(f"Total products available: {len(products)}")

    # Compare integers instead of string IDs
    product = next((p for p in products if int(p["ProductID"]) == product_id), None)

    if product:
        logger.info(f"✅ Product found: {product}")
        return product
    else:
        logger.warning(f"⚠️ Product ID {product_id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "OK"}

@app.get("/catalogs")
def get_unique_catalogs():
    logger.info("🔹 Request received for unique catalogs list")

    # Fetch all products
    products = get_product_data()["products"]

    # Extract unique catalogs using a set comprehension
    unique_catalogs = sorted({p["Catalog"] for p in products})
    if not unique_catalogs:
        logger.info(f"✅ Found {len(unique_catalogs)} unique catalogs: {unique_catalogs}")
    else:
        logger.warning("⚠️ No unique catalogs found.")

    # Return as a structured JSON response
    return {"catalogs": unique_catalogs}


# 💡 Run the FastAPI app using:
# uvicorn 5_fastapi_example:app --reload
# Access the API at http://localhost:8000
