import os
import json

def save_memory(new_memory,path):
    full_path = os.path.join(path)
    try:
        with open(full_path, 'a', encoding='utf-8') as f:
                json_str = json.dumps(new_memory, ensure_ascii=False)
                f.write(json_str + '\n')
            
        print(f"Save at: {path}")
    except Exception as e:
        print(f"failed because: {e}")

def load_memory(path):
    new_memory = []
    new_memory.append({
        "role": "system", 
        "content": "你叫 Carrot。以下是关于用户的重要记忆："
    })
    full_path = os.path.join(path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    memory_item = json.loads(line)
                    if memory_item["is_important"] == True:
                        new_memory[0]["content"] += f"\n- {memory_item['fact']}"
                    
    except FileNotFoundError:
        print("未检测到记忆")
        
    return new_memory