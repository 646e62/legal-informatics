# Create file folders for each year within a range
# Move this function to an OS tools file
def create_file_folders(start_year, end_year):
    for year in range(start_year, end_year+1):
        os.makedirs(f"./{year}", exist_ok=True)
