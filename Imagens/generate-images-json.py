import os
import json

def generate_images_json(base_path):
    images_data = {}
    
    # Percorre todas as pastas no diretório
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        
        # Verifica se é uma pasta
        if os.path.isdir(folder_path):
            images_list = []
            
            # Lista todos os arquivos de imagem da pasta
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    images_list.append(filename)
            
            # Ordena a lista alfabeticamente
            images_list.sort()
            images_data[folder_name] = images_list
    
    return images_data

# Caminho para sua pasta local (ajuste conforme necessário)
local_path = r"C:\Users\Sweet\Downloads\GitHub\site-images\Imagens"

# Gera o JSON
images_json = generate_images_json(local_path)

# Salva o arquivo JSON
with open('images-index.json', 'w', encoding='utf-8') as f:
    json.dump(images_json, f, indent=2, ensure_ascii=False)

print(f"JSON gerado com {len(images_json)} pastas")
for folder, images in images_json.items():
    print(f"  {folder}: {len(images)} imagens")