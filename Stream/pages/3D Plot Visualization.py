import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    st.title("3D Plot of Age, Rating, and Positive Feedback")
    
    data = pd.read_csv("ecommerce_dataset.csv")

    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()

    x_column = st.selectbox("Select column for X-axis", numerical_columns)
    y_column = st.selectbox("Select column for Y-axis", numerical_columns)
    z_column = st.selectbox("Select column for Z-axis", numerical_columns)

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(data[x_column], data[y_column], data[z_column], c='blue', marker='o')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_zlabel(z_column)
    ax.set_title('Relationship between {}, {}, and {}'.format(x_column, y_column, z_column))

    st.write("3D Plot:")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
