import os
import shutil

base_dir = r"c:\Users\Suhas\Downloads\Smart Bridge\Flood_Prediction_Project"
flask_file = os.path.join(base_dir, "Flask")
training_file = os.path.join(base_dir, "Training")
app_file = os.path.join(base_dir, "app.py")
nb_file = os.path.join(base_dir, "floods.ipynb")

flask_dir = os.path.join(base_dir, "Flask")
training_dir = os.path.join(base_dir, "Training")

# Rename files back if they exist as files
if os.path.isfile(flask_file):
    print(f"Renaming {flask_file} to {app_file}")
    try:
        os.rename(flask_file, app_file)
    except Exception as e:
        print(f"Error renaming Flask: {e}")

if os.path.isfile(training_file):
    print(f"Renaming {training_file} to {nb_file}")
    try:
        os.rename(training_file, nb_file)
    except Exception as e:
        print(f"Error renaming Training: {e}")

# Create directories
for d in [flask_dir, training_dir]:
    if not os.path.exists(d):
        print(f"Creating directory {d}")
        os.makedirs(d)

# Move files to Flask
flask_files = ["app.py", "floods.save", "transform.save", "templates", "static", "model.pkl", "test_app.py", "response.html"]
for f in flask_files:
    src = os.path.join(base_dir, f)
    dst = os.path.join(flask_dir, f)
    if os.path.exists(src):
        print(f"Moving {src} to {dst}")
        try:
            shutil.move(src, dst)
        except Exception as e:
            print(f"Error moving {f}: {e}")

# Move files to Training
training_files = ["floods.ipynb", "train_model.py", "inspect_data.py", "check_columns.py"]
for f in training_files:
    src = os.path.join(base_dir, f)
    dst = os.path.join(training_dir, f)
    if os.path.exists(src):
        print(f"Moving {src} to {dst}")
        try:
            shutil.move(src, dst)
        except Exception as e:
            print(f"Error moving {f}: {e}")
            
# Remove data dir if empty/exists (dataset already moved to Dataset folder manually or by previous command)
data_dir = os.path.join(base_dir, "data")
if os.path.exists(data_dir):
    try:
        shutil.rmtree(data_dir)
        print("Removed data directory")
    except:
        pass

print("Done.")
