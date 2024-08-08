import pandas as pd
import yaml


def compress_uri(uri):
    """
    Compress URIs from the OBO Foundry
    """
    return uri.replace('http://purl.obolibrary.org/obo/UBERON_', 'UBERON:')


# Read the CSV file
input_file = 'tests/ref-organ-relations.csv'
df = pd.read_csv(input_file)
# Change column names
df.columns = ['user_olabel', 'user_slabel', 'o', 's', 'olabel', 'slabel']
df.dropna(subset=['s', 'o'], inplace=True)
df['s'] = df['s'].apply(compress_uri)
df['o'] = df['o'].apply(compress_uri)

data = []
# Group by 'ref_organ_part' and write each group to a separate CSV file
for ref_organ, group in df.groupby('user_olabel'):
    name_file = ref_organ.split('#')[1]
    # output_file = f'{name_file}.csv'
    group.to_csv(f"tests/{name_file}-ref-organ.csv", index=False)
    data.append(
        {
            'name': name_file,
            'version': 'v2.1',
            'filename': f"tests/{name_file}-ref-organ.csv",
        }
    )

# Write the dictionary to a YAML file
output_file = 'output.yaml'
with open(output_file, 'w', encoding='utf-8') as file:
    data = {'data': data}
    yaml.dump(data, file, default_flow_style=False)
