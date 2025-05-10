from google.colab import files
uploaded = files.upload()

# Assuming file is named 'heart_failure_clinical_records_dataset.csv'
import io
df = pd.read_csv(io.BytesIO(uploaded['heart_failure_clinical_records_dataset.csv']))
