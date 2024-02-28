from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, LargeBinary, SmallInteger, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class USState(Base):
    __tablename__ = "us_states"

    state_id = Column(Integer, primary_key=True)
    state_name = Column(String(100))
    state_abbr = Column(String(2))
    state_region = Column(String(50))


class Region(Base):
    __tablename__ = "region"

    region_id = Column(Integer, primary_key=True)
    region_description = Column(String)

    territories = relationship("Territory", back_populates="region")


class Territory(Base):
    __tablename__ = "territories"

    territory_id = Column(String(20), primary_key=True, nullable=False)
    territory_description = Column(String(60), nullable=False)
    region_id = Column(SmallInteger, ForeignKey("region.region_id"), nullable=False)


class Shipper(Base):
    __tablename__ = 'shippers'

    shipper_id = Column(SmallInteger, primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    phone = Column(String(24))

    orders = relationship("Order", back_populates="shipper")


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    description = Column(Text)
    picture = Column(LargeBinary)

    products = relationship("Product", back_populates="category")


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(SmallInteger, primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))
    homepage = Column(Text)

    products = relationship("Product", back_populates="supplier")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(SmallInteger, primary_key=True, nullable=False)
    product_name = Column(String(40), nullable=False)
    quantity_per_unit = Column(String(20))
    unit_price = Column(Float)
    units_in_stock = Column(SmallInteger)
    units_on_order = Column(SmallInteger)
    reorder_level = Column(SmallInteger)
    discontinued = Column(Integer, nullable=False)

    category_id = Column(SmallInteger, ForeignKey("categories.category_id"))
    supplier_id = Column(SmallInteger, ForeignKey("suppliers.supplier_id"))

    orders_details = relationship("OrderDetail", back_populates="product")


class OrderDetail(Base):
    __tablename__ = 'order_details'

    unit_price = Column(Float, nullable=False)
    quantity = Column(SmallInteger, nullable=False)
    discount = Column(Float, nullable=False)

    order_id = Column(SmallInteger, ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    product_id = Column(SmallInteger, ForeignKey('products.product_id'), primary_key=True, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(SmallInteger, primary_key=True, nullable=False)
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    freight = Column(Float)
    ship_name = Column(String(40))
    ship_address = Column(String(60))
    ship_city = Column(String(15))
    ship_region = Column(String(15))
    ship_postal_code = Column(String(10))
    ship_country = Column(String(15))

    ship_via = Column(SmallInteger, ForeignKey('shippers.shipper_id'))
    customer_id = Column(String(5), ForeignKey('customers.customer_id'))
    employee_id = Column(SmallInteger, ForeignKey('employees.employee_id'))

    orders_details = relationship("OrderDetail", back_populates="order")


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    title = Column(String(100))
    birth_date = Column(String(10))
    hire_date = Column(String(10))
    address = Column(String(100))
    city = Column(String(50))
    region = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(50))
    home_phone = Column(String(20))
    extension = Column(String(10))
    photo = Column(LargeBinary)
    notes = Column(Text)
    photo_path = Column(String(255))

    reports_to = Column(SmallInteger, ForeignKey("employees.employee_id"))

    employees = relationship("Employee", back_populates="manager")
    manager = relationship("Employee", back_populates="employees")
    orders = relationship("Order", back_populates="employee")


class EmployeeTerritories(Base):
    __tablename__ = 'employee_territories'

    employee_id = Column(SmallInteger, ForeignKey('employees.employee_id'), primary_key=True, nullable=False)
    territory_id = Column(String(20), ForeignKey('territories.territory_id'), primary_key=True, nullable=False)


class CustomerCustomerDemo(Base):
    __tablename__ = 'customer_customer_demo'

    customer_id = Column(String(5), ForeignKey('customers.customer_id'), primary_key=True, nullable=False)
    customer_type_id = Column(String(5), ForeignKey('customer_demographics.customer_type_id'), primary_key=True, nullable=False)


class CustomerDemographics(Base):
    __tablename__ = 'customer_demographics'

    customer_type_id = Column(String(5), primary_key=True, nullable=False)
    customer_desc = Column(Text)


class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(String(5), primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))

    orders = relationship("Order", back_populates="customer")