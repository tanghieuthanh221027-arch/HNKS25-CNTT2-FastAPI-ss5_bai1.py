# code đã sửa
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
app = FastAPI()
products = [
    {
        "id": 1,
        "code": "SP001",
        "name": "Laptop Dell",
        "price": 15000000,
        "stock": 10
    },
    {
        "id": 2,
        "code": "SP002",
        "name": "Mouse Logitech",
        "price": 350000,
        "stock": 50
    }
]

class ProductCreate(BaseModel):
    code: str
    name: str
    price: float
    stock: int

@app.post("/products")
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "code": product.code,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }
    
    for pr in products:
        if pr['code'] == product.code:
            raise HTTPException(
                status_code=409,
                detail= "Mã code sản phẩm đã tồn tại"
            )

    products.append(new_product)
    raise HTTPException(
        status_code=201,
        detail= "Create product successfully"
    )

# 2 test case : 
# 1. Mở swagger UI để test : thử nhập mã SP001 -> vẫn báo thêm thành công -> lỗi
# cần sửa lại : thêm điều kiện -> duyệt vòng lặp xét nếu trùng thì raise lỗi HTTPException 409 (lỗi conflig)
# 2. Xem ở terminal của vscode -> khi thêm thành công báo status_code = 200 -> không đúng yêu cầu đầu bài -> khiến người dùng không biết đã tạo mới thành công chưa
# cần sửa lại : Dùng HTTPException thay đổi status_code = 201 (Created) để báo rằng sản phẩm đã được tạo mới thành công