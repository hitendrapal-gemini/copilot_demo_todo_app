## Module: Few-Shot Prompting – Guiding Copilot with Examples

**Target Audience:** Software Developers using GitHub Copilot (with a focus on FastAPI and Jinja2 for e-commerce applications)

**Module Duration:** Approximately 45-60 minutes

-----

### Module Introduction: Few-Shot Prompting – When Zero-Shot Isn't Enough

In our journey to master GitHub Copilot, we've covered the 4S Principle for clear communication and explored Zero-Shot Prompting for quick, context-driven code generation. However, there are times when Copilot's general knowledge or the surrounding code isn't enough to produce the exact output you need. This is where **Few-Shot Prompting** comes in.

Few-shot prompting involves providing GitHub Copilot with **one or more examples of the desired input-output pattern directly within your prompt**. By showing Copilot "how it's done," you explicitly guide its generation, leading to highly specific and tailored code, even for complex or unique requirements.

**Why Few-Shot Prompting for GitHub Copilot in FastAPI/Jinja2?**

While Copilot is smart, it doesn't read your mind or perfectly infer your project's unique conventions. Few-shot prompting helps you:

  * **Enforce Custom Conventions:** Ensure generated code adheres to your team's specific naming, formatting, or architectural patterns (e.g., custom error response formats, specific logging patterns).
  * **Handle Complex Logic:** Guide Copilot through intricate data transformations or business logic that might be too nuanced for a zero-shot approach.
  * **Generate Boilerplate for Specific Libraries/Patterns:** If you're using a less common library or a very particular way of interacting with a common one, examples can be invaluable.
  * **Overcome Ambiguity:** When a zero-shot prompt produces generic or incorrect results, a few-shot example provides the necessary clarity.

-----

### Core Concept: Learning from Examples

The essence of few-shot prompting is to turn your prompt into a mini "training set" for Copilot. You demonstrate the desired behavior with concrete input-output pairs, allowing the model to learn the underlying pattern and apply it to a new, unseen input (your actual request).

**Structure of a Few-Shot Prompt:**

A few-shot prompt typically follows this structure:

```
# Example 1:
# Input: [Description of input 1]
# Output: [Desired code/text output 1]

# Example 2:
# Input: [Description of input 2]
# Output: [Desired code/text output 2]

# Your actual request:
# Input: [Description of your current input]
# Output: [Copilot generates this based on examples]
```

Or, more commonly in code:

```python
# Function to convert temperature from Celsius to Fahrenheit.
# Example:
# celsius_to_fahrenheit(0) -> 32.0
# celsius_to_fahrenheit(100) -> 212.0
def celsius_to_fahrenheit(celsius: float) -> float:
    # Copilot will complete this based on examples
```

**Strengths of Few-Shot Prompting:**

  * **High Precision:** Excellent for getting very specific outputs.
  * **Customization:** Allows for fine-tuning Copilot's behavior to match your exact needs.
  * **Reduced Iteration:** Can save time by getting closer to the desired code on the first try.

**Weaknesses/Limitations of Few-Shot Prompting:**

  * **Prompt Length:** Examples add to the prompt's length, potentially hitting context window limits for very long or many examples.
  * **Example Quality:** Bad or inconsistent examples will lead to bad output. Examples must be clear and representative.
  * **Overfitting:** Copilot might "overfit" to the examples, struggling to generalize if your new request deviates too much.
  * **Still Needs Context:** While examples are powerful, the surrounding code context (from the 4S "Surround" principle) remains crucial for optimal results.

-----

### Applying Few-Shot Prompting in FastAPI/Jinja2 E-commerce Apps

Let's see how few-shot prompting works with real-world examples in our e-commerce context. We'll continue using the same project structure and baseline files.

**Recall the Project Setup:**

```
ecommerce_app/
├── main.py
├── models.py
├── services.py
└── templates/
    ├── base.html
    ├── product_card.html
    └── category_page.html
    └── index.html
```

**(Assume `main.py`, `models.py`, `services.py` have the baseline setup from previous modules.)**

-----

**Example 1: Generating a Custom Product SKU Generator**

**Scenario:** You need a function to generate unique product SKUs following a very specific internal format (e.g., `[CATEGORY_PREFIX]-[PRODUCT_ID]-[RANDOM_SUFFIX]`). A zero-shot might just give a UUID or simple concatenation.

**Bad Few-Shot Prompt:**

```python
# Bad Few-Shot Prompt:
# Generate SKU.
# Example:
# input: "Electronics", 123
# output: "ELEC-123-XYZ"
def generate_sku(category_name: str, product_id: int) -> str:
    # Copilot prompt starts here
```

**What might go wrong here?**
The example is too simplistic. "XYZ" is not random. It doesn't specify how `category_name` maps to `CATEGORY_PREFIX`.

**Good Few-Shot Prompt (leveraging comments and specific examples):**

*(In `services.py`)*

```python
# Good Few-Shot Prompt:
import uuid

# Function to generate a unique SKU for a product based on category and product ID.
# Format: [CATEGORY_CODE]-[PRODUCT_ID]-[SHORT_UUID]
# Category codes: Electronics -> ELEC, Books -> BOOK, Home & Kitchen -> HOME
#
# Example 1:
# Input: category_name="Electronics", product_id=101
# Expected Output: "ELEC-101-..." (where ... is a short UUID)
#
# Example 2:
# Input: category_name="Books", product_id=205
# Expected Output: "BOOK-205-..."
def generate_product_sku(category_name: str, product_id: int) -> str:
    # Copilot prompt starts here
```

**Explanation:**

  * **Few-Shot:** Provides two clear input-output examples, demonstrating the desired SKU format and category code mapping.
  * **Effectiveness:** The examples explicitly show the transformation logic, guiding Copilot to implement the category code mapping and the random suffix. The comments reinforce the pattern.

**Thought-Provoking Question:** If your SKU generation logic was even more complex (e.g., including color codes, size codes), how would you extend this few-shot prompt to ensure Copilot captures all the nuances? What are the limits of how many examples you can provide?

-----

**Example 2: Custom FastAPI Error Response Format**

**Scenario:** Your e-commerce API needs to return errors in a standardized JSON format, e.g., `{"error_code": "PRODUCT_NOT_FOUND", "message": "Product with ID X not found."}`. FastAPI's default `HTTPException` might not match this.

**Bad Few-Shot Prompt:**

```python
# Bad Few-Shot Prompt (in main.py):
# Handle errors like this: {"code": "ERR", "msg": "Something bad happened"}
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    # Copilot prompt starts here
```

**What might go wrong here?**
The example is too generic and doesn't map to `HTTPException` details (status code, detail message).

**Good Few-Shot Prompt (leveraging `HTTPException` context):**

*(In `main.py`, after `app = FastAPI()` and imports)*

```python
# Good Few-Shot Prompt:
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

# Custom exception handler for HTTPExceptions to return a standardized JSON error response.
#
# Example 1:
# Input: HTTPException(status_code=404, detail="Product not found")
# Expected Output (JSON): {"error_code": "NOT_FOUND", "message": "Product not found"}
#
# Example 2:
# Input: HTTPException(status_code=400, detail="Invalid quantity")
# Expected Output (JSON): {"error_code": "BAD_REQUEST", "message": "Invalid quantity"}
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    # Copilot prompt starts here
```

**Explanation:**

  * **Few-Shot:** Provides two examples mapping `HTTPException` details to a custom JSON structure, including how `status_code` translates to `error_code` strings.
  * **Effectiveness:** Copilot learns the mapping logic and the desired JSON keys, allowing it to generate the `JSONResponse` with the correct content.

**Thought-Provoking Question:** How would you modify this few-shot prompt if you also wanted to include a `timestamp` in the error response, formatted in a specific way (e.g., ISO 8601)?

-----

**Example 3: Jinja2 Macro for a Product Display Grid Item**

**Scenario:** You want a highly specific HTML structure for each product in a grid, including a placeholder image, name, price, and an "Add to Cart" button, all within a Jinja2 macro for reusability.

**Bad Few-Shot Prompt:**

```html
{# Bad Few-Shot Prompt (in templates/macros.html): #}
{% macro product_item(product) %}
    {# Show product #}
{% endmacro %}
```

**What might go wrong here?**
Copilot might generate a very basic display, missing specific classes, image handling, or the button.

**Good Few-Shot Prompt (leveraging HTML structure and `product` object context):**

*(In `templates/macros.html`)*

```html
{# Good Few-Shot Prompt: #}
{# Define a Jinja2 macro to render a single product item in a grid format. #}
{# It takes a `product` object with `name`, `price`, `image_url`, and `id`. #}
{#
Example Usage:
{% from 'macros.html' import product_card %}
{{ product_card(product) }}

Example Output (simplified):
<div class="col-md-4">
    <div class="card">
        <img src="/static/product_image.png" alt="Product Name">
        <div class="card-body">
            <h5>Product Name</h5>
            <p>$123.45</p>
            <a href="/products/123" class="btn">View</a>
            <form action="/add-to-cart" method="post"><button type="submit">Add</button></form>
        </div>
    </div>
</div>
#}
{% macro product_card(product) %}
    {# Copilot prompt starts here #}
{% endmacro %}
```

**Explanation:**

  * **Few-Shot:** The extensive comment block acts as a few-shot example, illustrating the desired HTML structure, classes, and how `product` attributes should be used.
  * **Effectiveness:** Copilot can parse the "Example Output" to understand the exact HTML elements, attributes, and text formatting, including the `url_for` pattern for links and form structure for "Add to Cart."

**Thought-Provoking Question:** If you wanted to add a "stock status" (e.g., "In Stock", "Low Stock", "Out of Stock") to this product card based on `product.stock`, how would you modify the few-shot prompt to guide Copilot for this conditional rendering?

-----

**Example 4: Complex Data Transformation for Analytics Dashboard**

**Scenario:** You have a raw list of historical `Order` objects and need to transform them into a summary suitable for a daily sales chart (e.g., `{"date": "YYYY-MM-DD", "total_sales": X.XX, "total_orders": Y}`).

**Bad Few-Shot Prompt:**

```python
# Bad Few-Shot Prompt (in services.py):
# Summarize orders by day.
# Example:
# input: [order1, order2]
# output: [{"date": "...", "sales": ...}]
def get_daily_sales_summary(orders: List[Order]) -> List[Dict]:
    # Copilot prompt starts here
```

**What might go wrong here?**
The example is too abstract. It doesn't show the structure of `order1`, nor how `total_sales` and `total_orders` are derived.

**Good Few-Shot Prompt (leveraging `Order` model and specific output structure):**

*(In `services.py`, assuming `Order` model is imported)*

```python
# Good Few-Shot Prompt:
from models import Order
from typing import List, Dict
from datetime import datetime, date
from collections import defaultdict

# Function to aggregate historical orders into daily sales summaries.
#
# Example 1:
# Input: [
#     Order(order_id="o1", user_id=1, items=[], total_amount=100.0, order_date=datetime(2023, 1, 1, 10, 0, 0), status="Completed"),
#     Order(order_id="o2", user_id=2, items=[], total_amount=50.0, order_date=datetime(2023, 1, 1, 14, 0, 0), status="Completed"),
#     Order(order_id="o3", user_id=1, items=[], total_amount=200.0, order_date=datetime(2023, 1, 2, 9, 0, 0), status="Completed"),
# ]
# Expected Output: [
#     {"date": "2023-01-01", "total_sales": 150.0, "total_orders": 2},
#     {"date": "2023-01-02", "total_sales": 200.0, "total_orders": 1},
# ]
def get_daily_sales_summary(orders: List[Order]) -> List[Dict]:
    # Copilot prompt starts here
```

**Explanation:**

  * **Few-Shot:** Provides a concrete example of `Order` objects as input and the exact desired aggregated output format.
  * **Effectiveness:** Copilot can infer the need for grouping by date, summing `total_amount`, and counting orders, using `datetime` and `defaultdict` for efficient processing.

**Thought-Provoking Question:** What if you also wanted to include the number of unique customers per day in the summary? How would you add that to the few-shot example?

-----

**Example 5: Custom FastAPI Dependency for Role-Based Access Control**

**Scenario:** You need a FastAPI dependency that checks if the authenticated user has a specific role (e.g., "admin") before allowing access to a route.

**Bad Few-Shot Prompt:**

```python
# Bad Few-Shot Prompt (in main.py or dependencies.py):
# Check admin role.
# Example:
# user_role="admin" -> True
# user_role="customer" -> False
def admin_required(user_role: str):
    # Copilot prompt starts here
```

**What might go wrong here?**
It's too simplistic. It doesn't show how it integrates with FastAPI's `Depends`, `HTTPException`, or how `user_role` is obtained (e.g., from a JWT token).

**Good Few-Shot Prompt (leveraging FastAPI `Depends` and `HTTPException` context):**

*(In `main.py` or a new `dependencies.py` file, assuming a dummy `get_current_user` dependency exists)*

```python
# Good Few-Shot Prompt:
from fastapi import Depends, HTTPException, status
from typing import Callable, Annotated

# Assume this dependency exists to get the current user (e.g., from JWT token)
# In a real app, this would decode a token and return a User object/dict
def get_current_user() -> Dict:
    # Dummy user for demonstration
    return {"id": 1, "email": "admin@example.com", "roles": ["admin", "customer"]}

# Create a FastAPI dependency that checks if the current user has the 'admin' role.
# If the user does not have the 'admin' role, raise an HTTPException with status 403 Forbidden.
#
# Example 1 (Usage):
# @app.get("/admin-only", dependencies=[Depends(admin_required)])
# async def admin_route(): pass
#
# Example 2 (Behavior for admin user):
# Input: user = {"id": 1, "email": "admin@example.com", "roles": ["admin"]}
# Output: No exception raised, function proceeds.
#
# Example 3 (Behavior for non-admin user):
# Input: user = {"id": 2, "email": "user@example.com", "roles": ["customer"]}
# Output: HTTPException(status_code=403, detail="Not authorized") is raised.
def admin_required(current_user: Annotated[dict, Depends(get_current_user)]):
    # Copilot prompt starts here
```

**Explanation:**

  * **Few-Shot:** Provides examples of both usage (how it's applied as a dependency) and behavior (what happens for admin vs. non-admin users), including the expected `HTTPException`.
  * **Effectiveness:** Copilot understands the `Depends` mechanism, how to access `current_user` from the dependency chain, and how to raise the correct `HTTPException` for unauthorized access.

**Thought-Provoking Question:** How would you adapt this few-shot prompt to create a more generic `role_required` dependency that takes a list of required roles as an argument?

-----

### Limitations of Few-Shot Prompting

While few-shot prompting is powerful, it's not a silver bullet:

  * **Context Window Pressure:** Each example adds to the prompt's length. For very complex tasks requiring many examples, you might hit the context window limit, forcing you to be selective or concise with your examples.
  * **Overfitting to Examples:** Copilot might sometimes adhere *too strictly* to the provided examples, struggling to generalize if your new input deviates slightly from the pattern shown in the examples.
  * **Example Quality is Key:** The effectiveness of few-shot prompting is entirely dependent on the quality, clarity, and representativeness of your examples. Poor examples will lead to poor output.
  * **Still Needs Surrounding Context:** Even with examples, Copilot still heavily relies on the surrounding code (imports, variable definitions, function signatures) to correctly integrate the generated code.
  * **Not for Debugging:** Few-shot prompting is for *generating* code based on a pattern, not for *debugging* existing code.

**When to use Few-Shot:**

  * When zero-shot is too generic or incorrect.
  * For custom formatting, naming, or architectural patterns.
  * Complex data transformations with specific input/output structures.
  * Generating code for specific library usage that isn't immediately obvious.

-----

### Ready-to-Use Code Snippets for Practice (FastAPI & Jinja2 Few-Shot)

Use the `my_ecommerce_app` structure and `main.py` baseline from the previous modules.

**Scenario 1: Custom Product Link Generator**

**Task:** Create a helper function that generates a product URL in a specific format like `/item/P-[PRODUCT_ID]`.

```python
# In `services.py`:
from typing import Dict

# Function to generate a custom product URL.
# Example 1:
# Input: product_id=101
# Expected Output: "/item/P-101"
#
# Example 2:
# Input: product_id=205
# Expected Output: "/item/P-205"
def generate_product_url(product_id: int) -> str:
    # Copilot prompt starts here
```

-----

**Scenario 2: Jinja2 Filter for Truncating Product Descriptions**

**Task:** Create a custom Jinja2 filter that truncates a string to a maximum length and appends "..." if truncated.

```python
# In `main.py`, where you set up Jinja2Templates (e.g., after `templates = Jinja2Templates(...)`):
from jinja2 import Environment, FileSystemLoader

# Register a custom Jinja2 filter to truncate text.
# Example 1:
# Input: "This is a long description.", max_length=10
# Expected Output: "This is a..."
#
# Example 2:
# Input: "Short text.", max_length=20
# Expected Output: "Short text."
def truncate_filter(s: str, max_length: int) -> str:
    # Copilot prompt starts here for the filter logic
    pass

# After defining the filter, register it with Jinja2 environment:
# templates.env.filters["truncate"] = truncate_filter

# Then, in a template (e.g., `product_card.html`):
{# <p>{{ product.description | truncate(50) }}</p> #}
```

-----

**Scenario 3: FastAPI Endpoint for Bulk Product Price Update (Specific Input Schema)**

**Task:** Create a FastAPI `PUT` endpoint to update prices for multiple products. The input should be a list of dictionaries, each with `product_id` and `new_price`.

```python
# In `models.py`:
from pydantic import BaseModel
from typing import List

class ProductPriceUpdate(BaseModel):
    product_id: int
    new_price: float

# In `main.py`, below other product routes:
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List

# Assume `products_db` is a mutable list of `Product` objects for this example.

# Create a FastAPI PUT endpoint `/api/products/bulk-update-prices`.
# It should accept a list of `ProductPriceUpdate` models in the request body.
# For each update, find the product in `products_db` by `product_id` and update its `price`.
# If a product is not found, skip it but log a warning (or return an error).
# Return a JSON response with a success message and the count of updated products.
#
# Example Request Body:
# [
#   {"product_id": 1, "new_price": 1250.00},
#   {"product_id": 2, "new_price": 95.00}
# ]
#
# Example Response:
# {"message": "Prices updated successfully", "updated_count": 2}
@app.put("/api/products/bulk-update-prices")
async def bulk_update_product_prices(updates: List[ProductPriceUpdate]):
    # Copilot prompt starts here
```

-----

### Deep Dive and References

For those who want to explore few-shot prompting and its broader context:

  * **Prompt Engineering Guide (Few-Shot):** [https://www.promptingguide.ai/techniques/fewshot](https://www.promptingguide.ai/techniques/fewshot) - A dedicated section on few-shot prompting.
  * **FastAPI Request Body with Pydantic:** [https://fastapi.tiangolo.com/tutorial/body/](https://fastapi.tiangolo.com/tutorial/body/) - Understanding how FastAPI handles request bodies with Pydantic models.
  * **Jinja2 Custom Filters:** [https://jinja.palletsprojects.com/en/3.1.x/api/\#custom-filters](https://www.google.com/search?q=https://jinja.palletsprojects.com/en/3.1.x/api/%23custom-filters) - How to extend Jinja2 with your own Python functions.

-----

### Conclusion and Next Steps

You've now mastered Few-Shot Prompting, adding a crucial tool to your GitHub Copilot arsenal for FastAPI and Jinja2 development. By providing concrete examples, you can precisely guide Copilot to generate code that adheres to your specific conventions, handles complex logic, and integrates seamlessly into your e-commerce application.

**Key Takeaways for Few-Shot:**

  * **Show, Don't Just Tell:** Examples are powerful for conveying subtle patterns.
  * **Precision and Customization:** Ideal for unique requirements or enforcing strict styles.
  * **Mind the Context Window:** Balance the number and detail of examples with overall prompt length.
  * **Quality Over Quantity:** A few well-chosen examples are better than many ambiguous ones.

Continue practicing few-shot prompts in your FastAPI projects. Identify scenarios where zero-shot falls short and experiment with providing targeted examples. This will empower you to leverage Copilot for an even wider range of development tasks, making you a more efficient and effective developer.