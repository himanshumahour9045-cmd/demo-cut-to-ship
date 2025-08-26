import pandas as pd
import streamlit as st
from tabulate import tabulate

data_cut_to_ship = {
    "Month" : ["Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Apr 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","Jun 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025","May 2025"],
    "Unit" : ["B-12A","B-12A","B-12A","B-43,44","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-12A","B-12A","B-12A","B-43,44","B-43,44","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-43,44","B-12A","B-43,44","B-12A","B-12A","B-12A","B-43,44","B-12A","B-12A","B-12A","B-43,44","B-12A","B-12A","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-12A","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-12A","B-12A","B-12A","B-43,44","B-12A","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-43,44","B-12A","B-43,44","B-12A","B-43,44","B-12A","B-43,44","B-43,44","B-12A","B-43,44","B-12A","B-43,44","B-43,44","B-43,44","B-43,44","B-12A"],
    "Buyer" : ["Next","Next","The Very Group","Angel And Rocket","The Very Group","The Very Group","The Very Group","The Very Group","The Very Group","The Very Group","The Very Group","Babyshop","The Very Group","The Very Group","The Very Group","Angel And Rocket","Mango","The Very Group","Pull Bear","Mango","Morrisonss","Mango","Babyshop","Li & Fung","Li & Fung","Mango","Morrisonss","Target","Target","Target","Target","Target","Morrisonss","The Very Group","Matalan","Matalan","Pull Bear","Li & Fung","Li & Fung","Li & Fung","Li & Fung","Target","Target","Target","Target","Target","Next","Mango","Target","Next","Target","Next","Scalpers","Next","The Very Group","Next","Next","Scalpers","The Very Group","Scalpers","Scalpers","The Very Group","The Very Group","Scalpers","The Very Group","The Very Group","The Very Group","Angel And Rocket","Next","Scalpers","Target","Matalan","Matalan","Target","Target","Target","Target","Matalan","Target","Matalan","Target","Next","Next","Next","Angel And Rocket","Next","Morrisonss","The Very Group","The Very Group","The Very Group","The Very Group","Angel And Rocket","Angel And Rocket","Angel And Rocket","Angel And Rocket","The Very Group","The Very Group","The Very Group","Angel And Rocket","Babyshop","Pull Bear","Morrisonss","Morrisonss","Target","Morrisonss","Pull Bear","Pull Bear","Morrisonss","Target","Target","Target","Next"],
    "Style" : ["AA8187  R-2","AA8187  R-2","BLS-23 HA","AR-8507","MA25CS-80","BLS-55 HA","TG-3703","TG-3636","TG-3636","TG-3636","TG-3707","I16-B12-06-616","TG-3709","TG-3716","TG-3716","AR-0039","PUMPA BLOUSE","ABW-234","V-3541","ARENA","041058","GRANADA","I66-12-06-041","LL-107","LL-107","BILAMA RPT-1","41264","318425-02","318425-03","318425-01","3550316753-01","3550316753-01","041053","TG-3575","LTS25GFD17","LTS25GFD17","V-3541","LL-107","LL-107","LL-107","LL-107","325320-01","322474-01","318593-03","318593-01","318593-04","F-77376","GARNI","318593-02","F-69757","322282","F-22908","SC SOPHIE BLOUSE GIRLS","AH-6871","WW-KH410","F77863","F-69756","SCLEO DRESS","ABW-824","LOUISE  EMB","MARGOT  BLOUSE","TG-4014","TG-3975","DENIM EMB","MG-2977","TG-3973","TG-3835","AR-3533 R-1","W43038","EMB LACE","318138-1","LTW25GCD01","LTW25GCR-01","318138-1","3550316753-03","322441","322441","LTW25GCD02","323326-01","LTW25GO01","323562-01","AH-6870","F-35451","AH-1284","AR-0089","F-46798","41819","ABW-284","EGHKIN02A","ABW-269","ABW-266","AR-0063","AR-0065","AR-0047","AR0062","ABW-268","EGMK02B","OG-2752","AR-0103","I66-11-03-35","V3650-COLOUR 11","41518-EMB TOP-R1","41518","3550316894-01","41819","V-3650","V-3650","41819","3550316868-01","3550316868-01","3550316753-03","W-22777"],
    "Product" : ["Pinny","Bodysuit","Emb Top","Emb Dress","Emb Dress","Dress","Dress","Emb Top","Short","Emb Bloomar","Dress","Skirt","Dress","Tee Shirt","Bloomer","Emb Dress","Pumpa Blouse","Smoking Dress","White Dress","Dress","Stripe Seashell Dress","Dress","Skirt","Sleep Set Celestial Print Shirt","Sleep Set Celestial Print Short","Print Dress","Emb Short","Dress Pink","Dress Pink Peach","Dress Cream","Cream Leopard Ruffle Dress","Cream Leopard Legging","Woven Aztec Playsuit","Emb Dress","Dungaree","DUNGREE","Black Dress","Sleep Set Pebble Print Shirt","Sleep Set Pebble Print Short","Sleep Set Leopard Print Shirt","Sleep Set Leopard Print Short","Silver Sequin Dress","Multi Tiered Tulle Pink Dress","Dark Pink Ruffle Tulle Dress","Cream Ruffle Tulle Dress","Blue Ruffle Tulle Dress","Black Dress","Dress","Light Pink Ruffle Tulle Dress","Animal Dress","White Dress","Dress","Sophie Blouse","Dress","Dress","Dress","Yellow Dress","Scleo Dress","Blouse","Louise Emb Dress","Margot Blouse","Dress","Top","Denim Emb Blouse","Dress","Emb Dress","Top","Dress","Dress","Emb Lace Blouse","Brown Short Slvand Sleeveless Top","Floral Cord Dress With Tight","Printed Cord Romper And Tightd","Cream Short Slvand Sleeveless Top","Light Pink Ditsy Ruffle Dress","Vintage Floral Dress","Vintage Floral Short","Cord Pinny","Skirt","Mesh Dress Pink","Chambray Dress","Dress Blue","Dress","Emb Dress White","Add Wark Dress","Dress","Pinny","Top","Embroidered Wide Leg Trouser","Emb Skirt","Top","Print Dress","Dress","Top","Top","Emb Top","Top","Emb Dress","Top","Dress","Dress","Emb Top","Floral Moven Set Pant","Top","Bodysuit","Dress","Dress","Bodysuit","Navy Blue Top","Navy Blue dress","Light Pink Ditsy Dress","Dress"],
    "Order Qty" : [5259,5259,500,355,500,500,800,800,800,800,800,929,800,952,952,1001,1530,800,1791,2347,3146,3056,2268,3648,3648,8028,3667,4580,4543,4580,5050,5050,8616,800,7501,7501,13036,18784,18784,21464,21464,16871,11251,11109,10266,8988,5090,3570,7743,9663,8512,5894,512,1500,800,536,1074,510,400,515,512,800,800,562,800,800,900,1259,1050,612,3998,6601,5500,5497,6057,6055,6055,6591,6697,8537,7602,1805,2755,8621,508,1071,4980,301,400,400,402,337,446,570,760,402,452,800,467,1228,2631,3087,3298,3535,4980,5886,5886,4978,6057,6057,6057,7363],
    "Cutting Qty" : [2042,5080,484,362,510,516,816,816,816,816,818,948,820,974,974,1023,1562,833,1839,2399,3212,3124,2344,3725,3725,8108,3750,4673,4638,4681,5154,5154,8730,924,7656,7656,13303,19173,19173,21895,21895,10621,7198,8173,7736,7344,3885,2904,7275,9269,8338,5792,435,1455,786,530,1069,509,412,532,530,818,822,586,824,824,925,1289,1084,648,4085,6709,5609,5612,6183,6183,6183,6728,6864,8707,7774,1678,2689,8581,473,1040,4979,305,408,408,411,348,458,582,776,422,472,822,491,1264,2686,3152,3368,3606,5099,6006,6007,5099,6181,6181,6185,7505],
    "Shipped Qty" : [1828,1828,455,336,483,500,790,784,784,784,795,902,800,945,945,942,1538,395,1782,2317,3080,3057,2198,3648,3648,7977,3659,4536,4538,4506,5012,5012,8422,785,7504,7504,13018,18784,18784,21464,21464,9900,5700,6396,6086,5404,3696,2816,4804,8797,4512,5604,415,1407,781,503,1025,488,389,515,512,780,776,562,800,800,900,1221,791,612,4016,6604,5500,4007,6012,5012,5012,6627,4500,8571,3000,1636,2596,8217,423,985,4896,284,380,402,392,324,442,544,724,402,438,790,440,1193,2608,3086,3291,3504,3351,5739,5738,1545,6012,6012,6012,7344],
    "Remarks" : ["Running","Running","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Running","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Running","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Running","Running","Running","Running","Running","Complete","Complete","Running","Complete","Running","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Running","Complete","Complete","Complete","Complete","Running","Complete","Running","Running","Complete","Running","Complete","Running","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Complete","Running","Complete","Complete","Running","Complete","Complete","Complete","Complete"]


}

# Convert Data into Pandas DataFram
df = pd.DataFrame(data_cut_to_ship)

# print Table with row and column by using tabulate
print(tabulate(df, headers="keys", tablefmt="grid"))

# Operations
Month_Count = df["Month"].value_counts()                                    # Month Count
Month_Wise_Ship_Qty = df.groupby("Month")["Shipped Qty"].sum()              # Month wise Shipment Qty
Unit_Count = df["Unit"].value_counts()                                      # Unit Count
Unit_wise_Ship_Qty = df.groupby("Unit")["Shipped Qty"].sum()                # Unit wise Shipment Qty
Buyer_Count = df["Buyer"].value_counts()                                    # Buyer Count
Buyer_Wise_Order_Qty = df.groupby("Buyer")["Order Qty"].sum()               # Buyer wise Order Qty
Buyer_Wise_Ship_Qty = df.groupby("Buyer")["Shipped Qty"].sum()              # Buyer wise Shipment Qty
Total_Order_Qty = df["Order Qty"].sum()                                     # Order Qty Sum
Total_Cutting_Qty = df["Cutting Qty"].sum()                                 # Cutting Qty Sum
Total_Shipped_Qty = df["Shipped Qty"].sum()                                 # Shipment Qty Sum
cut_to_ship_ratio = round((Total_Shipped_Qty/Total_Cutting_Qty*100),2)      # Cut to ship Ratio (%)
Order_to_Ship_ratio = round((Total_Shipped_Qty/Total_Order_Qty*100),2)      # Order to ship Ratio(%)
unit_wise_order_qty = df.groupby("Unit")["Order Qty"].sum()
unit_wise_cut_qty = df.groupby("Unit")["Cutting Qty"].sum()
unit_wise_ship_qty = df.groupby("Unit")["Shipped Qty"].sum()
order_to_cut_unit_wise = round((unit_wise_ship_qty/unit_wise_cut_qty*100),2)
cut_to_ship_unit_wise = round((unit_wise_ship_qty/unit_wise_cut_qty*100),2)



# Print Data
print("_____Describe Shipment Data_____")
print(tabulate(df.describe(), headers="keys", tablefmt="grid"))

# print("Unit wise Shipped Count :", Unit_Count)
# print("Unit wise Ship Qty :", Unit_wise_Ship_Qty)
# print("Month Count :",Month_Count)
# print("Month wise Ship Qty :", Month_Wise_Ship_Qty)
# print("Total Shipped Qty", Total_Shipped_Qty)
# print("Buyer Name :", Buyer_Count)
# print("Buyer wise Order Qty :",Buyer_Wise_Order_Qty)
# print("Buyer wise Ship Qty :", Buyer_Wise_Ship_Qty)
# print("Total Order Qty :",Total_Order_Qty)
# print("Total Cutting Qty", Total_Cutting_Qty)
# print("Total Shipped Qty", Total_Shipped_Qty)
# print("Cut to Ship Ratio :", (f"{cut_to_ship_ratio}%"))
# print("Order to Ship :",f"{Order_to_Ship_ratio}%")
# print("Unit wise Order Qty :",unit_wise_order_qty)
# print("Unit wise Cut Qty :",unit_wise_cut_qty)
# print("Unit wise Shipped Qty :",unit_wise_ship_qty)
# print("Unit wise Order to Ship(%) :",(f"{order_to_cut_unit_wise}%"))
# print("Unit wise Cut to Ship(%) :",(f"{cut_to_ship_unit_wise}%"))

# # Style wise Summary Cut to Ship
# print("Style wise Summary Cut to Ship")
# style_analysis = df.groupby(["Month","Unit","Style", "Product"])[["Order Qty", "Cutting Qty", "Shipped Qty"]].sum()
# # add 2 row for calculate cut and ship ratio
# style_analysis["Order_to_Ship_ratio"] = ((style_analysis["Shipped Qty"]/style_analysis["Order Qty"])*100).round(2).astype(str) + " %"
# style_analysis["Cut_to_Ship_Ratio"] = ((style_analysis["Shipped Qty"]/style_analysis["Cutting Qty"])*100).round(2).astype(str) + " %"
# print("Summary of Cut to Ship for the month Apr-25 to Jun-25\n",style_analysis.to_string())


# Web App Deployment

st.markdown("## **Cut to Ship Analysis :cityscape:**")
st.markdown("Month - Apr to Jun 25")

months = df["Month"].unique()
selected_month = st.selectbox("Select Month", sorted(months))

# Filtered Data
month_data = df[df["Month"] == selected_month]

# Summary Metrics (Month-wise)
Total_Order_Qty = month_data["Order Qty"].sum()
Total_Cutting_Qty = month_data["Cutting Qty"].sum()
Total_Shipped_Qty = month_data["Shipped Qty"].sum()

cut_to_ship_ratio = round((Total_Shipped_Qty / Total_Cutting_Qty * 100), 2) if Total_Cutting_Qty > 0 else 0
Order_to_Ship_ratio = round((Total_Shipped_Qty / Total_Order_Qty * 100), 2) if Total_Order_Qty > 0 else 0

st.metric("Total Order Qty :house:", f"{Total_Order_Qty:,}")
st.metric("Total Cutting Qty :scissors:", f"{Total_Cutting_Qty:,}")
st.metric("Total Shipped Qty :ship:", f"{Total_Shipped_Qty:,}")
st.metric("Cut to Ship Ratio 🛒 :+1:", f"{cut_to_ship_ratio}%")
st.metric("Order to Ship Ratio 🛒 :+1:", f"{Order_to_Ship_ratio}%")

# Buyer Wise Shipment Analysis
st.subheader("🛒 Buyer Wise Shipment (Month-wise)")

month_analysis = month_data.groupby("Month")["Shipped Qty"].sum().reset_index()
buyer_analysis = month_data.groupby("Buyer")["Shipped Qty"].sum().reset_index()
style_analysis = month_data.groupby("Style")["Shipped Qty"].sum().reset_index()

st.dataframe(month_analysis)
st.dataframe(buyer_analysis)
st.dataframe(style_analysis)

st.bar_chart(buyer_analysis.set_index("Buyer")["Shipped Qty"])
st.bar_chart(style_analysis.set_index("Style")["Shipped Qty"])

