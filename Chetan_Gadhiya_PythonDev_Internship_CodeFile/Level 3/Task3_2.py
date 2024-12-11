import pandas as pd
import plotly.express as px

# i have used dataset from kaggle.
def load_dataset(file_path):
    
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}\n")
        return None

def visualization_generation(data):
    
    print("Choose a visualization type:")
    print("1. Scatter Plot")
    print("2. Bar Plot")
    print("3. Line Plot")
    print("4. Histogram")
    
    choice = int(input("Enter the number corresponding to your choice: "))
    columns = list(data.columns)
    
    print("\nAvailable columns:")
    for idx, column in enumerate(columns, 1):
        print(f"{idx}. {column}")
    
    try:
        x_col = columns[int(input("Select the column for X-axis (number): ")) - 1]
        y_col = None
        if choice in [1, 2, 3]:
            y_col = columns[int(input("Select the column for Y-axis (number): ")) - 1]
        
        if choice == 1:
            fig = px.scatter(data, x=x_col, y=y_col, title="Scatter Plot")
        elif choice == 2:
            fig = px.bar(data, x=x_col, y=y_col, title="Bar Plot")
        elif choice == 3:
            fig = px.line(data, x=x_col, y=y_col, title="Line Plot")
        elif choice == 4:
            fig = px.histogram(data, x=x_col, title="Histogram")
        else:
            print("Wrong choice!")
            return
        
        fig.show()#shows the plot
    except Exception as e:
        print(f"Error generating visualization: {e}")
        
    

def main():
    print("Welcome to the Data Visualization Tool!")
    file_path = input("Enter the path to the dataset (CSV file): ")
    data = load_dataset(file_path)
    
    if data is not None:
        print("\nDataset Loaded Successfully!")
        print(data.head())#shows some of the top dataset values
        visualization_generation(data)
    else:
        print("Unable to load dataset. Please check the file path / file name.")

if __name__ == "__main__":
    main()
