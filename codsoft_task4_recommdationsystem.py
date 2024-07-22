
                # Product Recommendation System

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv('Amazon-Products.csv')

# Preprocess data by combining relevant features into a single string
df['combined_features'] = df['main_category'] + ' ' + df['sub_category'] + ' ' + df['name']

# Convert text data to feature vectors using TF-IDF vectorization
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# Initialize the Nearest Neighbors model
nn_model = NearestNeighbors(metric='cosine', algorithm='brute')
nn_model.fit(feature_matrix)

# Function to get recommendations using Nearest Neighbors
def get_recommendations(df, nn_model, selected_idx, n_recommendations=5):
    # Reshape the query vector
    query_vector = feature_matrix[selected_idx].reshape(1, -1)
    
    # Find the nearest neighbors
    distances, indices = nn_model.kneighbors(query_vector, n_neighbors=n_recommendations + 1)
    
    # Get the indices of the recommended products
    product_indices = indices.flatten()[1:]  # Exclude the first one (itself)
    
    return df.iloc[product_indices]

# Streamlit app interface
st.title("Product Recommendation System")

# Create a dropdown menu to select a main category
main_category = st.selectbox('Select a main category:', df['main_category'].unique())

# Filter the dataframe based on the selected main category
filtered_df_main = df[df['main_category'] == main_category]

# Create a dropdown menu to select a sub category from the filtered main category
sub_category = st.selectbox('Select a sub category:', filtered_df_main['sub_category'].unique())

# Further filter the dataframe based on the selected sub category
filtered_df_sub = filtered_df_main[filtered_df_main['sub_category'] == sub_category]

# If the filtered dataframe is not empty, select a random product for recommendation
if not filtered_df_sub.empty:
    selected_product_idx = filtered_df_sub.index[0]  # Choose the first product in the filtered dataframe
    product_name = filtered_df_sub.loc[selected_product_idx, 'name']

    # Display recommendations when the button is clicked
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(df, nn_model, selected_product_idx)
        st.write(f"Selected product: **{product_name}**")
        st.write("Recommended products:")
        
        # Display recommended products in rows of 3
        cols_per_row = 3
        num_products = len(recommendations)
        num_rows = (num_products + cols_per_row - 1) // cols_per_row
        
        for row in range(num_rows):
            cols = st.columns(cols_per_row)
            for col_idx in range(cols_per_row):
                product_idx = row * cols_per_row + col_idx
                if product_idx < num_products:
                    with cols[col_idx]:
                        row_data = recommendations.iloc[product_idx]
                        st.markdown(f"<div style='margin-bottom: 20px;'>", unsafe_allow_html=True)
                        st.write(f"**{row_data['name']}**")
                        st.image(row_data['image'], width=150)
                        st.write(f"Price: {row_data['discount_price']} (Actual: {row_data['actual_price']})")
                        st.write(f"Ratings: {row_data['ratings']} ({row_data['no_of_ratings']} ratings)")
                        st.write(f"[View Product]({row_data['link']})")
                        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.write("No products found for the selected category.")
