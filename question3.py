import os
import json

def generate_large_json(input_folder, output_file, languages_of_interest):
    # Create a list to store translations from English to other languages for the train set
    translations = []

    # Loop through JSONL files in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jsonl"):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    data = json.loads(line)
                    language = data.get('locale')
                    set_type = data.get('partition')

                    # Filter for languages of interest and train set
                    if language == 'en-US' and set_type == 'train':
                        translation_item = {
                            'id': data['id'],
                            'utt': data['utt'],
                            'translations': {}  # Initialize translations dictionary
                        }

                        # Extract translations for each language of interest
                        for target_language in languages_of_interest:
                            if target_language != 'en-US':
                                # Check if translations key exists and the target language is present
                                if 'translations' in data and target_language in data['translations']:
                                    translation_item['translations'][target_language] = data['translations'][target_language]
                                else:
                                    # Handle the case where translation is not available
                                    translation_item['translations'][target_language] = None

                        translations.append(translation_item)

    # Write the translations to a large JSON file with pretty printing
    with open(output_file, 'w', encoding='utf-8') as large_json_file:
        json.dump(translations, large_json_file, ensure_ascii=False, indent=2)

    print(f'Large JSON file {output_file} created.')

# Example usage:
input_folder = r'C:\Users\cobai\PycharmProjects\pythonProject5\1.1\data'
output_file = 'output2/en_to_xx_large.json'
languages_of_interest = ['en-US', 'sw-KE', 'de-DE']
generate_large_json(input_folder, output_file, languages_of_interest)
