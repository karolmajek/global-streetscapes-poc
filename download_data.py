from huggingface_hub import snapshot_download

dataset_name = "NUS-UAL/global-streetscapes"
print(snapshot_download(repo_id=dataset_name, repo_type="dataset"))
