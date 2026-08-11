
import streamlit as st
import requests

st.title("___Super Kart UI__") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area =  st.number_input("Product Allocated Area") 
Product_MRP = st.number_input("Product MRP")
Store_Size = st.number_input("Store Size")
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket", "Grocery Store"])
Product_Id_char = st.selectbox("Product Id char", ["A", "B", "C", "D", "E"])
Store_Age_Years = st.number_input("Store Age Years")
Product_Type_Category = st.selectbox("Product Type Category", ["Dairy", "Bakery", "Meat", "Fruits", "Vegetables", "Others"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    response = requests.post("https://gl-super-kart-service.app.github.dev/v1/predict", json=product_data)    
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")
