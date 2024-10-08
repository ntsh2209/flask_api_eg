import os
import pandas as pd
import yaml

def get_file_list(location, file_format):
    """Return a list of files in the specified location with the given format."""
    if not os.path.isdir(location):
        raise FileNotFoundError(f"Location not found: {location}")
    
    # Return files with the specific format (.csv or .txt)
    files = [f for f in os.listdir(location) if f.endswith(f".{file_format}")]
    return files

def process_file(file_path):
    """Load the file into a DataFrame and return column names and data types."""
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.txt'):
        df = pd.read_table(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
    
    # Get column names and data types
    column_info = {}
    for col in df.columns:
        column_info[col] = str(df[col].dtype)
    
    return column_info

def generate_yaml(location, file_format, output_yaml):
    """Process all files in the location and generate a YAML file with column names and data types."""
    files = get_file_list(location, file_format)
    
    all_files_info = {}
    
    for file_name in files:
        file_path = os.path.join(location, file_name)
        try:
            column_info = process_file(file_path)
            all_files_info[file_name] = column_info
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")
    
    # Save the information to a YAML file
    with open(output_yaml, 'w') as yaml_file:
        yaml.dump(all_files_info, yaml_file, default_flow_style=False)
    
    print(f"YAML file generated: {output_yaml}")

if __name__ == "__main__":
    location = input("Enter the location of the files: ")
    file_format = input("Enter the file format (csv or txt): ")
    output_yaml = input("Enter the output YAML file name (e.g., output.yaml): ")
    
    generate_yaml(location, file_format, output_yaml)
