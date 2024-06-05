import pymongo
import pandas as pd

# Replace with your MongoDB connection details (if applicable)
client = pymongo.MongoClient(f"mongodb+srv://memeslordak:dHWukrLt2ZcBCMR0@cluster0.9cm0c6m.mongodb.net/")
  # Default host and port
db = client["student_Data"]  # Your database name

# Collection name (replace with the actual collection you want to access)
collection_name = "student_info"

# Connect to the collection
collection = db[collection_name]

# Create an empty list to store the documents
data = []

# Fetch documents from the collection
for document in collection.find():
    # Remove the "_id" field if you don't need it in the CSV/DataFrame
    if "_id" in document:
        del document["_id"]
    data.append(document)

# Create a pandas DataFrame from the list of documents
df = pd.DataFrame(data)
print(df.head())
# Convert the DataFrame to a CSV file (optional)
df.to_csv("raw_data.csv", index=False)  # Save to 'jost_data.csv'

print("Data successfully converted to pandas DataFrame and (optionally) CSV file.")
